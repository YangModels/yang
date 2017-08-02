import base64
import datetime
import errno
import json
import tools.utility.log as log
import os
import shutil
import subprocess
import urllib2
from urllib2 import URLError

import pika

LOGGER = log.get_logger('receiver')

# Make a http request on path with json_data
def http_request(path, method, json_data, http_credentials, header):
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(path, data=json_data)
        request.add_header('Content-Type', header)
        request.add_header('Accept', header)
        base64string = base64.b64encode('%s:%s' % (http_credentials[0], http_credentials[1]))
        request.add_header("Authorization", "Basic %s" % base64string)
        request.get_method = lambda: method
        return opener.open(request)
    except urllib2.HTTPError as e:
        if method == 'DELETE':
            return
        print('Could not send request with body ' + repr(json_data) + ' and path ' + path)
        raise e
    except URLError as e:
        raise e


def process_sdo(arguments):
    LOGGER.debug('Processing sdo')
    tree_created = True if arguments[-1] == 'True' else False
    arguments = arguments[:-1]
    direc = arguments[6].split('/')[0]

    with open("log.txt", "wr") as f:
        try:
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            shutil.rmtree('../parseAndPopulate/' + direc)
            return __response_type[0]

    try:
        os.makedirs('../../api/sdo/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return __response_type[0]

    if tree_created:
        subprocess.call(["cp", "-r", '../parseAndPopulate/' + direc + "/temp/.", "../../api/sdo/"])
        send_to_indexing('../parseAndPopulate/' + direc + '/prepare.json',
                         [arguments[11], arguments[12]], arguments[9], True)
        shutil.rmtree('../parseAndPopulate/' + direc)
    return __response_type[1]


def send_to_indexing(file_to_index, credentials, confd_ip, sdo_type=False):
    LOGGER.debug('Sending data for indexing')
    with open(file_to_index, 'r') as f:
        sdos_json = json.load(f)
    post_body = {}
    if sdo_type:
        prefix = 'api/sdo'
    else:
        prefix = 'api/vendor'

    for sdo in sdos_json['module']:
        if sdo.get('schema'):
            path = prefix + sdo['schema'].split('githubusercontent.com/')[1]
        else:
            path = 'module does not exist'
        post_body[sdo['name'] + '@' + sdo['revision']] = path
    body_to_send = json.dumps({'modules-to-index': post_body})
    LOGGER.info('Sending data for indexing with body {}'.format(body_to_send))
    try:
        http_request('https://' + confd_ip + '/yang-search/metadata-update.php', 'POST', body_to_send,
                     credentials, 'application/json')
    except urllib2.HTTPError as e:
        print('could not send data for indexing. Reason: ' + e.msg)
    except URLError as e:
        print('could not send data for indexing. Reason: ' + repr(e.message))


def process_vendor(arguments):
    LOGGER.debug('Processing vendor')
    tree_created = True if arguments[-2] == 'True' else False
    integrity_file_location = arguments[-1]
    arguments = arguments[:-2]
    direc = arguments[5].split('/')[0]

    with open("log.txt", "wr") as f:
        try:
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            shutil.rmtree('../parseAndPopulate/' + direc)
            return __response_type[0]
    try:
        os.makedirs('../../api/vendor/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return __response_type[0]

    subprocess.call(["cp", "-r", "../parseAndPopulate/" + direc + "/temp/.", "../../api/vendor/"])

    if tree_created:
        send_to_indexing('../parseAndPopulate/' + direc + '/prepare.json', [arguments[10], arguments[10]], arguments[8])
        shutil.rmtree('../parseAndPopulate/' + direc)

    integrity_file_name = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%m:%S.%f")[:-3]+'Z'

    if integrity_file_name != './':
        shutil.move('./integrity.html', integrity_file_location + 'integrity' + integrity_file_name + '.html')
    return __response_type[1]


def on_request(ch, method, props, body):
    LOGGER.info('Received request')
    print ('request with body ' + body)
    arguments = body.split('#')

    if '--sdo' in arguments[2]:
        response = process_sdo(arguments)
    else:
        response = process_vendor(arguments)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    LOGGER.debug('Starting receiver')
    __response_type = ['Failed', 'Finished successfully']
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='module_queue')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='module_queue')

    LOGGER.debug('Awaiting RPC request')
    channel.start_consuming()
