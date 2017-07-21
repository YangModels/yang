import argparse
import base64
import datetime
import errno
import glob
import json
import os
import urllib2
# Make a http request on path with json_data
from collections import OrderedDict


def http_request(path, method, json_data, credentials):
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(path, data=json_data)
        request.add_header('Content-Type', 'application/vnd.yang.data+json')
        request.add_header('Accept', 'application/vnd.yang.data+json')
        base64string = base64.b64encode('%s:%s' % (credentials[0], credentials[1]))
        request.add_header("Authorization", "Basic %s" % base64string)
        request.get_method = lambda: method
        return opener.open(request)
    except:
        print('Could not send request with body ' + json_data + ' and path ' + path)
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This serves to save or load all information in yangcatalog.org to json in'
                    ' case the server will go down and we would lose all the information we'
                    ' have got. We have two options in here. Saving makes a GET request to '
                    'file with name that would be set as a argument or it will be set to '
                    'a current time and date. Load will read the file and make a PUT request '
                    'to write all data to yangcatalog.org.')
    parser.add_argument('--port', default=8008, type=int,
                        help='Set port where the confd is started. Default -> 8008')
    parser.add_argument('--ip', default='127.0.0.1', type=str,
                        help='Set ip address where the confd is started. Default -> 127.0.0.1')
    parser.add_argument('--credentials', help='Set authorization parameters username password respectively.'
                                              ' Default parameters are admin admin', nargs=2, default=['admin', 'admin']
                        , type=str)
    parser.add_argument('--name_save', default=str(datetime.datetime.utcnow()).split('.')[0].replace(' ', '_') + '-UTC',
                        type=str, help='Set name of the file to save. Default name is date and time in UTC')
    parser.add_argument('--name_load', type=str,
                        help='Set name of the file to load. Default will take a last saved file')
    parser.add_argument('--type', default='save', type=str, choices=['save', 'load'],
                        help='Set weather you want to save a file or load a file. Default is save')
    parser.add_argument('--protocol', type=str, default='http', help='Whether confd-6.4 runs on http or https.'
                                                                     ' Default is set to http')

    args = parser.parse_args()
    prefix = args.protocol + '://{}:{}'.format(args.ip, args.port)
    if 'save' is args.type:
        try:
            os.makedirs('./cache/')
        except OSError as e:
            # be happy if someone already created the path
            if e.errno != errno.EEXIST:
                raise
        file_save = open('./cache/' + args.name_save + '.json', 'w')
        file_save.write(http_request(prefix + '/api/config/catalog?deep', 'GET', None, args.credentials).read())
        file_save.close()
    else:
        if args.name_load:
            file_load = args.name_load
        else:
            list_of_files = glob.glob('./cache/*')
            latest_file = max(list_of_files, key=os.path.getctime)
            file_load = open(latest_file, 'rw')
        body = json.load(file_load, object_pairs_hook=OrderedDict)
        http_request(prefix + '/api/config/catalog', 'PUT', json.dumps(body), args.credentials)
        file_load.close()
