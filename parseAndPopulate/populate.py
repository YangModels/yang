import fnmatch
import json
import os
import unicodedata
import urllib2
import subprocess
import sys

prefix = 'http://127.0.0.1:8008'


# Recursively look for pattern file in directory
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
def http_request(path, method, json_data):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(path, data=json_data)
    request.add_header('Content-Type', 'application/vnd.yang.data+json')
    request.add_header('Accept', 'application/vnd.yang.data+json')
    request.add_header('Authorization', 'Basic YWRtaW46YWRtaW4=')
    request.get_method = lambda: method
    opener.open(request)


# Parse data and send request
def prepare_data(json_data, path_suffix):
    # Parse platform os feature-set and os-version
    platform = unicode_normalize(data['platform'])
    os_from_yang = unicode_normalize(data['os'])
    feature_set = unicode_normalize(data['feature-set'])
    os_version = unicode_normalize(data['os-version'])
    # Patch HTTP request to make sure that data will be merged and not replaced
    http_request(prefix + '/api/config/catalog/implementations/' + platform + ',' + os_from_yang + ','
                 + feature_set + ',' + os_version + path_suffix, 'PATCH', json_data)


if len(sys.argv) > 1:
    prefix = 'http://' + sys.argv[1] + ':8008'
subprocess.call("python runCapabilities.py", shell=True)
files = []
# Find all parsed json files
for filename in find_files('./', '*.json'):
    with open(filename) as data_file:
        files.append(json.load(data_file))
platform = ''
os_from_yang = ''
feature_set = ''

print("Populating yang catalog with data")
# In each json
for data in files:
    # Parse platform os feature-set and os-version
    platform = unicode_normalize(data['platform'])
    os_from_yang = unicode_normalize(data['os'])
    feature_set = unicode_normalize(data['feature-set'])
    os_version = unicode_normalize(data['os-version'])

    # Prepare json_data for put request - this request will prepare list implementations
    # to populate it with protocols and modules
    json_implementations_data = json.dumps({
        'implementations': [
            {
                'platform': platform,
                'os': os_from_yang,
                'feature-set': feature_set,
                'os-version': os_version
            }]
    })

    # Make a PUT request to create a root for each file
    http_request(prefix + '/api/config/catalog/implementations/' + platform + ',' + os_from_yang + ','
                 + feature_set + ',' + os_version, 'PUT', json_implementations_data)

# In each json
for data in files:
    # Prepare json_data for patch request - this data will populate container protocols of ietf-yang-catalog
    json_protocol_data = json.dumps({
        'protocols': data['protocols'],
    })

    prepare_data(json_protocol_data, '/protocols')

# In each json
for data in files:
    # Prepare json_data for patch request - this data will populate container modules of ietf-yang-catalog
    json_modules_data = json.dumps({
        'modules': data['modules']
    })

    prepare_data(json_modules_data, '/modules')
print("Removing temporary json files")
subprocess.call(['rm', '-rf', './*.json'])
for item in os.listdir('./'):
    if item.endswith(".json"):
        os.remove(item)
