import argparse
import base64
import fnmatch
import json
import os
import sys
import time
import subprocess
import unicodedata
import urllib2
from collections import OrderedDict


def progress_bar(done, total, time_diff, old_percentage, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * done / float(total)))

    percents = round(100.0 * done / float(total), 4)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    time_percentage = percents - old_percentage
    if time_percentage > 0:
        seconds = int((time_diff / time_percentage) * (100 - percents))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        time_s = "%dh:%02dm:%02ds" % (h, m, s)
    else:
        time_s = "inf"
    sys.stdout.write('[%s] %s%s time remaining %s  ...%s\r' % (bar, percents, '%', time_s, suffix))
    sys.stdout.flush()
    return percents


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
        print 'Could not send request with body ' + json_data + ' and path ' + path
        raise


# Parse data and send request
def prepare_data(json_data, path_suffix, credentials):
    # Parse vendor os feature-set and os-version
    vendor = unicode_normalize(data['vendor'])
    os_from_yang = unicode_normalize(data['os-type'])
    feature_set = unicode_normalize(data['feature-set'])
    os_version = unicode_normalize(data['os-version'])
    platform = unicode_normalize(data['platform'])
    # Patch HTTP request to make sure that data will be merged and not replaced
    http_request(prefix + '/api/config/catalog/vendors/vendor/' + vendor + '/os-types/os-type/' + os_from_yang +
                 '/platforms/platform/' + platform + '/os-versions/os-version/' + os_version +
                 '/feature-sets/feature-set/' + feature_set + path_suffix, 'PATCH', json_data, credentials)


parser = argparse.ArgumentParser(description="Parse hello messages and yang files to json dictionary. These"
                                             " dictionaries are used for populating a yangcatalog. This script runs"
                                             " first a runCapabilities.py script to create a Json files which are used"
                                             " to populate database.o")
parser.add_argument('--port', default=8008, type=int,
                    help='Set port where the confd is started. Default -> 8008')
parser.add_argument('--ip', default='127.0.0.1', type=str,
                    help='Set ip address where the confd is started. Default -> 127.0.0.1')
parser.add_argument('--credentials', help='Set authorization parameters username password respectively.'
                                          ' Default parameters are admin admin', nargs=2, default=['admin', 'admin']
                    , type=str)
args = parser.parse_args()
prefix = 'http://{}:{}'.format(args.ip, args.port)
subprocess.call("python runCapabilities.py", shell=True)
files = []
# Find all parsed json files
for filename in find_files('./', 'normal*.json'):
    with open(filename) as data_file:
        files.append(json.load(data_file))

vendor = ''
os_from_yang = ''
feature_set = ''
platform = ''
os_version = ''

print("Populating yang catalog with data")

# In each json
print("adding vendors")
for data in files:
    # Parse vendor os feature-set and os-version
    vendor = unicode_normalize(data['vendor'])

    # Prepare json_data for put request - this request will prepare list vendors
    # to populate it with protocols and modules
    json_implementations_data = json.dumps({
                'vendor': [{
                    'name': vendor
                }]
    })
    # Make a PUT request to create a root for each file
    http_request(prefix + '/api/config/catalog/vendors/vendor/' + vendor, 'PUT', json_implementations_data,
                 args.credentials)

print("adding os-types")
for data in files:
    vendor = unicode_normalize(data['vendor'])
    os_from_yang = unicode_normalize(data['os-type'])
    json_implementations_data = json.dumps({
            'os-type': [{
                'name': os_from_yang
            }]
    })
    # Make a PUT request to create a root for each file
    http_request(prefix + '/api/config/catalog/vendors/vendor/' + vendor + '/os-types/os-type/' + os_from_yang, 'PUT',
                 json_implementations_data, args.credentials)

print("adding platforms")
for data in files:
    vendor = unicode_normalize(data['vendor'])
    os_from_yang = unicode_normalize(data['os-type'])

    platform = unicode_normalize(data['platform'])
    json_implementations_data = json.dumps({
            'platform': [{
                'name': platform
            }]
    })
    # Make a PUT request to create a root for each file
    http_request(prefix + '/api/config/catalog/vendors/vendor/' + vendor + '/os-types/os-type/' + os_from_yang +
                 '/platforms/platform/' + platform, 'PUT', json_implementations_data, args.credentials)

print("adding os-versions")
for data in files:
    vendor = unicode_normalize(data['vendor'])
    os_from_yang = unicode_normalize(data['os-type'])
    platform = unicode_normalize(data['platform'])
    os_version = unicode_normalize(data['os-version'])
    json_implementations_data = json.dumps({
            'os-version': [{
                'name': os_version
            }]
    })
    # Make a PUT request to create a root for each file
    http_request(prefix + '/api/config/catalog/vendors/vendor/' + vendor + '/os-types/os-type/' + os_from_yang +
                 '/platforms/platform/' + platform + '/os-versions/os-version/' + os_version, 'PUT',
                 json_implementations_data, args.credentials)
print("adding feature-sets")
for data in files:
    vendor = unicode_normalize(data['vendor'])
    os_from_yang = unicode_normalize(data['os-type'])
    platform = unicode_normalize(data['platform'])
    os_version = unicode_normalize(data['os-version'])
    feature_set = unicode_normalize(data['feature-set'])
    json_implementations_data = json.dumps({
            'feature-set': [{
                'name': feature_set
            }]
    })
    # Make a PUT request to create a root for each file
    http_request(prefix + '/api/config/catalog/vendors/vendor/' + vendor + '/os-types/os-type/' + os_from_yang +
                 '/platforms/platform/' + platform + '/os-versions/os-version/' + os_version +
                 '/feature-sets/feature-set/' + feature_set, 'PUT', json_implementations_data, args.credentials)

# In each json
print("adding protocols")
for data in files:
    # Prepare json_data for patch request - this data will populate container protocols of ietf-yang-catalog
    json_protocol_data = json.dumps({
        'protocols': data['protocols'],
    })

    prepare_data(json_protocol_data, '/protocols', args.credentials)

# In each json
print("adding modules")
for data in files:
    # Prepare json_data for patch request - this data will populate container modules of ietf-yang-catalog
    json_modules_data = json.dumps({
        'modules': data['modules']
    })
    prepare_data(json_modules_data, '/modules', args.credentials)

files_prepare = []
for filename_prepare in find_files('./', 'prepare.json'):
    with open(filename_prepare) as data_file:
        print("adding modules PUT")
        read = data_file.read()
        json_modules_data = json.dumps({
            'modules': json.loads(read)
        })

        http_request(prefix + '/api/config/catalog/modules/', 'PUT',
                     json_modules_data, args.credentials)

length_of_modules = 0
old_percent = 0

for data in files:
    length_of_modules += len(data['modules']['module'])

j = 0
i = 0
# In each json
print("adding modules PATCH")
for data in files:
    j += 1
    for obj in data['modules']['module']:

        start = time.time()
        name = obj['name']
        revision = obj['revision']
        i += 1

        json_modules_data = json.dumps({
            'module': [json.loads('{'
                '"name":"' + obj['name'] + '",'
                '"revision":"' + obj['revision'] + '",'
                '"namespace":"' + obj['namespace'] + '",'
                '"contact":"' + obj['contact'] + '",'
                '"organization":"' + obj['organization'] + '",'
                '"description":"' + obj['description'] + '",'
                '"yang-version":"' + obj['yang-version'] + '",'
                '"prefix":"' + obj['prefix'] + '",'
                '"feature":' + json.dumps(obj['feature']) + ','
                '"deviation":' + json.dumps(obj['deviation']) + ','
                '"reference":"' + obj['reference'] + '",'
                '"conformance-type":"' + obj['conformance-type'] + '",'
                '"submodule":' + json.dumps(obj['submodule'], sort_keys=True) + ','
                '"schema":"' + obj['schema'] + '",'
                '"compilation-status":"' + obj['compilation-status'] + '",'
                '"author-email":"' + obj['author-email'] + '",'
                '"reference":"' + obj['reference'] + '",'
                '"implementations": {'
                    '"implementation":[{'
                        '"vendor": "' + data['vendor'] + '",'
                        '"platform":"' + data['platform'] + '",'
                        '"version": "' + data['os-version'] + '",'
                        '"os-type": "' + data['os-type'] + '",'
                        '"feature-set": "' + data['feature-set'] + '"'
                 '}]}'
            '}', object_pairs_hook=OrderedDict, strict=False)
                       ]
        })

        http_request(prefix + '/api/config/catalog/modules/module/' + name + ',' + revision, 'PATCH',
                     json_modules_data, args.credentials)
        end = time.time()

        old_percent = progress_bar(i, length_of_modules, end - start, old_percent, 'adding modules PATCH ' + repr(j))


print("Removing temporary json files")

for item in os.listdir('./'):
    if item.endswith(".json"):
        os.remove(item)
