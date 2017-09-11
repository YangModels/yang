import ConfigParser
import argparse
import base64
import errno
import fnmatch
import json
import os
import shutil
import subprocess
import unicodedata
import urllib2

import tools.utility.log as log
from tools.api.receiver import send_to_indexing

LOGGER = log.get_logger('populate')


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


# Unicode to string
def unicode_normalize(variable):
    return unicodedata.normalize('NFKD', variable).encode('ascii', 'ignore')


# Make a http request on path with json_data
def http_request(path, method, json_data, credentials):
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(path, data=json_data)
        request.add_header('Content-Type', 'application/vnd.yang.data+json')
        request.add_header('Accept', 'application/vnd.yang.data+json')
        base64string = base64.b64encode('%s:%s' % (credentials[0], credentials[1]))
        request.add_header("Authorization", "Basic %s" % base64string)
        request.get_method = lambda: method
        opener.open(request)
    except:
        LOGGER.error('Could not send request with body {} and path {}'.format(json_data, path))
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse hello messages and yang files to json dictionary. These"
                                                 " dictionaries are used for populating a yangcatalog. This script runs"
                                                 " first a runCapabilities.py script to create a Json files which are "
                                                 "used to populate database.")
    parser.add_argument('--port', default=8008, type=int,
                        help='Set port where the confd is started. Default -> 8008')
    parser.add_argument('--ip', default='127.0.0.1', type=str,
                        help='Set ip address where the confd is started. Default -> 127.0.0.1')
    parser.add_argument('--api-port', default=8443, type=int,
                        help='Set port where the api is started. Default -> 8443')
    parser.add_argument('--api-ip', default='127.0.0.1', type=str,
                        help='Set ip address where the api is started. Default -> 127.0.0.1')
    parser.add_argument('--credentials', help='Set authorization parameters username password respectively.'
                                              ' Default parameters are admin admin', nargs=2, default=['admin', 'admin']
                        , type=str)
    parser.add_argument('--dir', default='../../vendor', type=str,
                        help='Set dir where to look for hello message xml files.Default -> ../../vendor')
    parser.add_argument('--api', action='store_true', default=False, help='If we are doing apis')
    parser.add_argument('--sdo', action='store_true', default=False, help='If we are sneding SDOs only')
    parser.add_argument('--notify-indexing', action='store_true', default=False, help='Weather to send files for'
                                                                                      ' indexing')
    parser.add_argument('--protocol', type=str, default='http', help='Whether confd-6.4 runs on http or https.'
                                                                     ' Default is set to http')
    parser.add_argument('--api-protocol', type=str, default='https', help='Whether api runs on http or https.'
                                                                          ' Default is set to http')
    parser.add_argument('--result-html-dir', default='/home/miroslav/results/', type=str,
                        help='Set dir where to write html result files. Default -> /home/miroslav/results/')
    parser.add_argument('--config-path', type=str, default='../utility/config.ini',
                        help='Set path to config file')
    parser.add_argument('--force-indexing', action='store_true', default=False, help='Force to index files')
    args = parser.parse_args()
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    key = config.get('Receiver-Section', 'key')
    LOGGER.info('Starting the populate script')
    if args.api:
        direc = '/'.join(args.dir.split('/')[0:3])
    else:
        direc = 0
        while True:
            try:
                os.makedirs('../parseAndPopulate/' + repr(direc))
                break
            except OSError as e:
                direc += 1
                if e.errno != errno.EEXIST:
                    raise
        direc = repr(direc)
    prefix = args.protocol + '://{}:{}'.format(args.ip, args.port)
    LOGGER.info('Calling runcapabilities script')
    if args.api:
        if args.sdo:
            with open("log_api_sdo.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--api", "--sdo", "--dir",
                             args.dir, "--json-dir", direc, "--result-html-dir", args.result_html_dir]
                subprocess.check_call(arguments, stderr=f)
        else:
            with open("log_api.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--api", "--dir", args.dir,
                             "--json-dir", direc, "--result-html-dir", args.result_html_dir]
                subprocess.check_call(arguments, stderr=f)
    else:
        if args.sdo:
            with open("log_sdo.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--sdo", "--dir", args.dir,
                             "--json-dir", direc, "--result-html-dir", args.result_html_dir]
                subprocess.check_call(arguments, stderr=f)
        else:
            with open("log_no_sdo_api.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--dir", args.dir, "--json-dir", direc,
                             "--result-html-dir", args.result_html_dir]
                subprocess.check_call(arguments, stderr=f)

    LOGGER.info('Populating yang catalog with data. Starting to add modules')
    for filename_prepare in find_files('../parseAndPopulate/' + direc, 'prepare.json'):
        with open(filename_prepare) as data_file:
            read = data_file.read()
            json_modules_data = json.dumps({
                'modules': json.loads(read)
            })

            if '{"module": []}' not in read:
                http_request(prefix + '/api/config/catalog/modules/', 'PATCH',
                             json_modules_data, args.credentials)

    files = []
    # Find all parsed json files
    for filename in find_files('../parseAndPopulate/' + direc, 'normal*.json'):
        with open(filename) as data_file:
            files.append(json.load(data_file))

    # In each json
    LOGGER.info('Starting to add vendors')
    for data in files:
        # Prepare json_data for put request - this request will prepare list vendors
        # to populate it with protocols and modules
        json_implementations_data = json.dumps(data)
        # Make a PUT request to create a root for each file
        http_request(prefix + '/api/config/catalog/vendors/', 'PATCH', json_implementations_data,
                     args.credentials)

    if not args.api:
        do_indexing = True
        if 'ietf-extracted-YANG-modules' in args.dir:
            try:
                os.makedirs('./old')
            except OSError:
                # Be happy if deleted
                pass
            try:
                with open('./old/prepare.json', 'r') as f:
                    old = f.read()
            except:
                old = ''
            with open('../parseAndPopulate/' + direc + '/prepare.json', 'r') as f:
                new = f.read()
            if old != new:
                do_indexing = True
            shutil.copy('../parseAndPopulate/' + direc + '/prepare.json', './old/.')
        if args.notify_indexing and do_indexing:
            LOGGER.info('Sending files for indexing')
            send_to_indexing('../parseAndPopulate/' + direc + '/prepare.json', args.credentials, args.ip, args.api_port,
                             args.api_protocol, from_api=False, set_key=key, force_indexing=args.force_indexing)
        LOGGER.info('Removing temporary json data and cache data')
        shutil.rmtree('../parseAndPopulate/' + direc)
        try:
            shutil.rmtree('../api/cache')
        except OSError:
            # Be happy if deleted
            pass
        try:
            LOGGER.info('Sending request to reload cache')
            http_request(args.api_protocol + '://' + args.api_ip + ':' + repr(args.api_port) + '/load-cache', 'POST', None,
                         args.credentials)
        except:
            LOGGER.warning('Could not send a load-cache request')
