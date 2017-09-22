import ConfigParser
import argparse
import base64
import datetime
import errno
import json
import os
import shutil
import subprocess
import sys
import urllib2
from Crypto.Hash import SHA, HMAC
from urllib2 import URLError

import pika

import tools.utility.log as log

LOGGER = log.get_logger('receiver')


# Make a http request on path with json_data
def http_request(path, method, json_data, http_credentials, header, indexing=None, return_code=False):
    """Create HTTP request
        Arguments:
            :param indexing: (str) Whether there need to be added a X-YC-Signature.
                This is because of the verification with indexing script
            :param header: (str) to set Content-type and Accept headers to this variable
            :param http_credentials: (list) Basic authorization credentials - username, password
                respectively
            :param json_data: (dict) Body of the payload send via request 
            :param method: (str) Request method.
            :param path : (str) Path of the request.
            :return a response from the request.
    """
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(path, data=json_data)
        request.add_header('Content-Type', header)
        request.add_header('Accept', header)
        if indexing:
            request.add_header('X-YC-Signature', 'sha1={}'.format(indexing))
        base64string = base64.b64encode('%s:%s' % (http_credentials[0], http_credentials[1]))
        request.add_header("Authorization", "Basic %s" % base64string)
        request.get_method = lambda: method
        return opener.open(request)
    except urllib2.HTTPError as e:
        LOGGER.debug('Could not send request with body ' + repr(json_data) + ' and path ' + path)
        if return_code:
            return e
        else:
            raise e
    except URLError as e:
        raise e


def process_sdo(arguments):
    """Processes SDOs. Calls populate script which calls script to parse all the modules
    on the given path which is one of the params. Populate script will also send the
    request to populate confd on given ip and port. It will also copy all the modules to 
    parent directory of this project /api/sdo. It will also call indexing script to
    update searching.
            Arguments:
                :param arguments: (list) list of arguments sent from api sender
                :return (__response_type) one of the response types which is either
                    'Failed' or 'Finished successfully' 
    """
    LOGGER.debug('Processing sdo')
    tree_created = True if arguments[-4] == 'True' else False
    api_port = arguments[-1]
    api_protocol = arguments[-2]
    arguments = arguments[:-4]
    direc = '/'.join(arguments[6].split('/')[0:3])
    arguments.append("--result-html-dir")
    arguments.append(result_dir)

    with open("log.txt", "wr") as f:
        try:
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            shutil.rmtree(direc)
            LOGGER.error('Server error: {}'.format(e))
            return __response_type[0] + '#split#Server error while parsing or populating data'

    try:
        os.makedirs('../../api/sdo/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return __response_type[0] + '#split#Server error - could not create directory'

    if tree_created:
        subprocess.call(["cp", "-r", direc + "/temp/.", "../../api/sdo/"])
        if notify_indexing:
            send_to_indexing(direc + '/prepare.json', [arguments[11], arguments[12]], arguments[9], api_port,
                             api_protocol, True)
        shutil.rmtree(direc)
    return __response_type[1]


def create_signature(secret_key, string):
    """ Create the signed message from api_key and string_to_sign
            Arguments:
                :param string: (str) String that needs to be signed
                :param secret_key: Secret key that the string will be signed with
                :return A string of 2* `digest_size` bytes. It contains only
                    hexadecimal ASCII digits.
    """
    string_to_sign = string.encode('utf-8')
    hmac = HMAC.new(secret_key, string_to_sign, SHA)
    return hmac.hexdigest()


def send_to_indexing(modules_to_index, credentials, confd_api_ip, api_port, api_protocol, sdo_type=False, delete=False,
                     from_api=True, set_key=None, force_indexing=True):
    """ Sends the POST request which will activate indexing script for modules which will
    help to speed up process of searching. It will create a json body of all the modules
    containing module name and path where the module can be found if we are adding new
    modules. Other situation can be if we need to delete module. In this case we are sending
    list of modules that need to be deleted.
            Arguments:
                :param modules_to_index: (json file) prepare.json file generated while parsing
                    all the modules. This file is used to iterate through all the modules.
                :param credentials: (list) Basic authorization credentials - username, password
                    respectively.
                :param confd_api_ip: (str) Confd and api ip address. It should be the same.
                :param api_port: (int) Port to API.
                :param api_protocol: (str) protocol of API.
                :param sdo_type: (bool) Whether or not it is sdo that needs to be sent.
                :param delete: (bool) Whether or not we are deleting module.
                :param from_api: (bool) Whether or not api sent the request to index.
                :param set_key: (str) String containing key to confirm that it is receiver that sends data. This is
                    is verified before indexing takes place.
                :param force_indexing: (bool) Whether or not we should force indexing even if module exists in cache.
    """
    LOGGER.debug('Sending data for indexing')
    if delete:
        body_to_send = json.dumps({'modules-to-delete': modules_to_index})
    else:
        with open(modules_to_index, 'r') as f:
            sdos_json = json.load(f)
        post_body = {}
        if from_api:
            if sdo_type:
                prefix = 'api/sdo/'
            else:
                prefix = 'api/vendor/'

            for module in sdos_json['module']:
                response = http_request('{}://{}:{}/search/modules/{},{},{}'.format(api_protocol, confd_api_ip,
                                                                                    api_port, module['name'],
                                                                                    module['revision'],
                                                                                    module['organization']), 'GET',
                                        '',
                                        credentials, 'application/vnd.yang.data+json', return_code=True)
                code = response.code
                if force_indexing or (code != 200 and code != 201 and code != 204):
                    if module.get('schema'):
                        path = prefix + module['schema'].split('githubusercontent.com/')[1]
                        path = os.path.abspath('../../' + path)
                    else:
                        path = 'module does not exist'
                    post_body[module['name'] + '@' + module['revision'] + '/' + module['organization']] = path
        else:
            for module in sdos_json['module']:
                response = http_request('{}://{}:{}/search/modules/{},{},{}'.format(api_protocol, confd_api_ip,
                                                                                    api_port, module['name'],
                                                                                    module['revision'],
                                                                                    module['organization']), 'GET', '',
                                        credentials, 'application/vnd.yang.data+json', return_code=True)
                code = response.code
                if force_indexing or (code != 200 and code != 201 and code != 204):
                    if module.get('schema'):
                        path = module['schema'].split('master')[1]
                        path = os.path.abspath('../../' + path)
                    else:
                        path = 'module does not exist'
                    post_body[module['name'] + '@' + module['revision'] + '/' + module['organization']] = path
        body_to_send = json.dumps({'modules-to-index': post_body})

    try:
        set_key = key
    except NameError:
        pass
    LOGGER.info('Sending data for indexing with body {}'.format(body_to_send))
    try:
        http_request('https://' + confd_api_ip + '/yang-search/metadata-update.php', 'POST', body_to_send,
                     credentials, 'application/json', indexing=create_signature(set_key, body_to_send))
    except urllib2.HTTPError as e:
        LOGGER.error('could not send data for indexing. Reason: {}'.format(e.msg))
    except URLError as e:
        LOGGER.error('could not send data for indexing. Reason: {}'.format(repr(e.message)))


def process_vendor(arguments):
    """Processes vendors. Calls populate script which calls script to parse all the modules
    that are contained in the given hello message xml file or in ietf-yang-module xml file
    which is one of the params. Populate script will also send the request to populate confd
    on given ip and port. It will also copy all the modules to parent directory of this
    project /api/sdo. It will also call indexing script to update searching.
            Arguments:
                :param arguments: (list) list of arguments sent from api sender
                :return (__response_type) one of the response types which is either
                    'Failed' or 'Finished successfully' 
    """
    LOGGER.debug('Processing vendor')
    tree_created = True if arguments[-5] == 'True' else False
    integrity_file_location = arguments[-4]
    api_port = arguments[-1]
    api_protocol = arguments[-2]

    arguments = arguments[:-5]
    direc = '/'.join(arguments[5].split('/')[0:3])
    arguments.append("--result-html-dir")
    arguments.append(result_dir)

    with open("log.txt", "wr") as f:
        try:
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            shutil.rmtree(direc)
            LOGGER.error('Server error: {}'.format(e))
            return __response_type[0] + '#split#Server error while parsing or populating data'
    try:
        os.makedirs('../../api/vendor/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            LOGGER.error('Server error: {}'.format(e))
            return __response_type[0] + '#split#Server error - could not create directory'

    subprocess.call(["cp", "-r", direc + "/temp/.", "../../api/vendor/"])

    if tree_created:
        if notify_indexing:
            send_to_indexing(direc + '/prepare.json', [arguments[9], arguments[10]], arguments[8], api_port,
                             api_protocol)
        shutil.rmtree(direc)

    integrity_file_name = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%m:%S.%f")[:-3] + 'Z'

    if integrity_file_location != './':
        shutil.move('./integrity.html', integrity_file_location + 'integrity' + integrity_file_name + '.html')
    return __response_type[1]


def process_vendor_deletion(arguments, api_protocol, api_port):
    """Deletes vendors. It calls the delete request to confd to delete all the module
    in vendor branch of the yang-catalog.yang module on given path. If the module was
    added by vendor and it doesn't contain any other implementations it will delete the 
    whole module in modules branch of the yang-catalog.yang module. It will also call
    indexing script to update searching.
            Arguments:
                :param api_port: (int) Port where the API runs
                :param api_protocol: (str) Whether API runs on http or https
                :param arguments: (list) list of arguments sent from api sender
                :return (__response_type) one of the response types which is either
                    'Failed' or 'Finished successfully' 
    """
    vendor, platform, software_version, software_flavor = arguments[0:4]
    protocol, confd_ip, confdPort = arguments[4:7]
    credentials = arguments[7:9]
    path_to_delete = arguments[9]

    response = 'work'
    try:
        with open('./cache/catalog.json', 'r') as catalog:
            vendors_data = json.load(catalog)['yang-catalog:catalog']['vendors']
    except IOError:
        LOGGER.warning('Cache file does not exist')
        # Try to create a cache if not created yet and load data again
        response = make_cache(credentials, response, protocol, confd_ip, confdPort, api_protocol, api_port)
        if response != 'work':
            return response
        else:
            try:
                with open('./cache/catalog.json', 'r') as catalog:
                    vendors_data = json.load(catalog)['yang-catalog:catalog']['vendors']
            except:
                LOGGER.error('Unexpected error: {}'.format(sys.exc_info()[0]))
                return __response_type[0] + '#split#' + sys.exc_info()[0]

    modules = set()
    modules_that_succeeded = []
    iterate_in_depth(vendors_data, modules)

    try:
        http_request(path_to_delete, 'DELETE', None, credentials, 'application/vnd.yang.data+json')
    except:
        e = sys.exc_info()[0]
        LOGGER.error('Couldn\'t delete vendor on path {}. Error: '.format(path_to_delete, e))
        return __response_type[0] + '#split#' + repr(e)

    for mod in modules:
        try:
            path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/modules/module/' \
                   + mod
            modules_data = json.loads(http_request(path + '?deep', 'GET', '', credentials,
                                                   'application/vnd.yang.data+json').read())
            implementations = modules_data['yang-catalog:module']['implementations']['implementation']
            count_of_implementations = len(implementations)
            count_deleted = 0
            for imp in implementations:
                if vendor and vendor != imp['vendor']:
                    continue
                if platform and platform != imp['platform']:
                    continue
                if software_flavor and software_flavor != imp['software-flavor']:
                    continue
                if software_version and software_version != imp['software-version']:
                    continue
                imp_key = imp['vendor'] + ',' + imp['platform'] + ',' + imp['software-version'] \
                          + ',' + imp['software-flavor']
                try:
                    http_request(path + '/implementations/implementation/' + imp_key,
                                 'DELETE', None, credentials, 'application/vnd.yang.data+json')
                except:
                    # In case that only some modules were deleted, send only those for indexing
                    if len(modules_that_succeeded) > 0:
                        if notify_indexing:
                            send_to_indexing(modules_that_succeeded, credentials, confd_ip, arguments[-1],
                                             arguments[-2], delete=True)
                    e = sys.exc_info()[0]
                    LOGGER.error('Couldn\'t delete implementation of module on path {} because of error: {}'
                                 .format(path + '/implementations/implementation/' + imp_key, e))
                    # return make_response(jsonify({'error': e.msg}), 500)
                count_deleted += 1
            modules_that_succeeded.append(mod)
            if count_deleted == count_of_implementations:
                try:
                    http_request(path, 'DELETE', None, credentials, 'application/vnd.yang.data+json')
                except:
                    # In case that only some modules were deleted, send only those for indexing
                    if len(modules_that_succeeded) > 0:
                        if notify_indexing:
                            send_to_indexing(modules_that_succeeded, credentials, confd_ip, arguments[-1],
                                             arguments[-2], delete=True)
                    e = sys.exc_info()[0]
                    LOGGER.error('Could not delete module on path {} because of error: {}'.format(path, e))
                    # return make_response(jsonify({'error': e.msg}), 500)
        except:
            LOGGER.error('Yang file {} doesn\'t exist although it should exist'.format(mod))
            # return make_response(jsonify({'error': 'Server error'}), 500)
        if notify_indexing:
            send_to_indexing(modules, credentials, confd_ip, arguments[-1], arguments[-2], delete=True)
        return __response_type[1]


def iterate_in_depth(value, modules):
    """Iterates through the branch to get to the level with modules
            Arguments:
                :param value: (dict) data through which we will need to iterate
                :param modules: (set) set that will contain all the modules that
                 need to be deleted
    """
    for key, val in value.iteritems():
        if key == 'protocols':
            continue
        if isinstance(val, list):
            for v in val:
                iterate_in_depth(v, modules)
        if isinstance(val, dict):
            if key == 'modules':
                for mod in val['module']:
                    name = mod['name']
                    revision = mod['revision']
                    organization = mod['organization']
                    modules.add(name + ',' + revision + ',' + organization)
            else:
                iterate_in_depth(val, modules)


def make_cache(credentials, response, protocol, confd_ip, confd_port, api_protocol, api_port):
    """After we delete or add modules we need to reload all the modules to the file
    for qucker search. This module is then loaded to the memory.
            Arguments:
                :param api_port: (int) Port where the API runs
                :param api_protocol: (str) Whether API runs on http or https
                :param confd_port: (int) Port where the confd runs
                :param confd_ip: (str) Ip address where the confd runs
                :param protocol: (str) Whether confd runs on http or https
                :param response: (str) Contains string 'work' which will be sent back if 
                    everything went through fine
                :param credentials: (list) Basic authorization credentials - username, password
                    respectively
                :return 'work' if everything went through fine otherwise send back the reason why
                    it failed.
    """
    try:
        try:
            os.makedirs('./cache')
        except OSError as e:
            # be happy if someone already created the path
            if e.errno != errno.EEXIST:
                return __response_type[0] + '#split#Server error - could not create directory'

        path = protocol + '://' + confd_ip + ':' + confd_port + '/api/config/catalog?deep'
        with open('./cache/catalog.json', "w") as cache_file:
            cache_file.write(http_request(path, 'GET', '', credentials, 'application/vnd.yang.data+json').read())
    except:
        e = sys.exc_info()[0]
        LOGGER.error('Could not load json to cache. Error: {}'.format(e))
        return __response_type[0] + '#split#Server error - downloading cache'
    path = api_protocol + '://' + confd_ip + ':' + api_port + '/load-cache'
    try:
        http_request(path, 'POST', '', credentials, 'application/vnd.yang.data+json').read()
    except:
        e = sys.exc_info()[0]
        LOGGER.error('Could not load json to memory-cache. Error: {}'.format(e))
        return __response_type[0] + '#split#Server error - loading to memory'
    return response


def process_module_deletion(arguments):
    """Deletes module. It calls the delete request to confd to delete module on given path.
    This will delete whole module in modules branch of the yang-catalog.yang module.
    It will also call indexing script to update searching.
                Arguments:
                    :param arguments: (list) list of arguments sent from api sender
                    :return (__response_type) one of the response types which is either
                        'Failed' or 'Finished successfully' 
    """
    credentials = arguments[3:5]
    path_to_delete = arguments[5]
    confd_ip = arguments[1]
    try:
        http_request(path_to_delete, 'DELETE', None, credentials, 'application/vnd.yang.data+json')
    except:
        e = sys.exc_info()[0]
        LOGGER.error('Couldn\'t delete module on path {}. Error : {}'.format(path_to_delete, e))
        return __response_type[0] + '#split#' + repr(e)
    name, revision, organization = path_to_delete.split('/')[-1].split(',')
    if notify_indexing:
        send_to_indexing(['{}@{}/{}'.format(name, revision, organization)], credentials, confd_ip, arguments[-1],
                         arguments[-2], delete=True)
    return __response_type[1]


def on_request(ch, method, props, body):
    """Function called when something was sent from API sender. This function will process
    all the requests that would take too long to process for API. When the processing is 
    done we will sent back the result of the request which can be either 'Failed' or
    'Finished successfully' with corespondent correlation id. If the request 'Failed'
    it will sent back also a reason why it failed.
            Arguments:
                :param body: (str) String of arguments that need to be processed separated
                by '#'.
        """
    LOGGER.info('Received request with body {}'.format(body))
    arguments = body.split('#')

    if arguments[-3] == 'DELETE':
        if 'http' in arguments[0]:
            response = process_module_deletion(arguments)
            credentials = arguments[3:5]
            protocol, confd_ip, confd_port = arguments[0:3]
            api_protocol, api_port = arguments[-2:]
        else:
            api_protocol, api_port = arguments[-2:]
            response = process_vendor_deletion(arguments, api_protocol, api_port)
            credentials = arguments[7:9]
            protocol, confd_ip, confd_port = arguments[4:7]

    elif '--sdo' in arguments[2]:
        response = process_sdo(arguments)
        credentials = arguments[11:13]
        confd_ip = arguments[9]
        confd_port = arguments[4]
        protocol = arguments[-3]
        api_protocol, api_port = arguments[-2:]
    else:
        response = process_vendor(arguments)
        credentials = arguments[10:12]
        confd_ip = arguments[8]
        confd_port = arguments[3]
        protocol = arguments[-3]
        api_protocol, api_port = arguments[-2:]

    if response.split('#split#')[0] == __response_type[1]:
        response = make_cache(credentials, response, protocol, confd_ip, confd_port, api_protocol, api_port)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-path', type=str, default='../utility/config.ini',
                        help='Set path to config file')
    LOGGER.info('Starting receiver')
    args = parser.parse_args()
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    global key
    key = config.get('Receiver-Section', 'key')
    global notify_indexing
    notify_indexing = config.get('Receiver-Section', 'notify-index')
    global result_dir
    result_dir = config.get('Receiver-Section', 'result-html-dir')
    if notify_indexing == 'True':
        notify_indexing = True
    else:
        notify_indexing = False
    __response_type = ['Failed', 'Finished successfully']
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='module_queue')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='module_queue')

    LOGGER.info('Awaiting RPC request')
    channel.start_consuming()
