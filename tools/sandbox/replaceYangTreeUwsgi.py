import json

import requests

response = requests.get('http://yangcatalog.org:8008/api/config/catalog/modules?deep',
             auth=('admin', 'admin'),
             headers={'Accept': 'application/vnd.yang.data+json'})
modules = json.loads(response.content)['yang-catalog:modules']['module']
for mod in modules:
    tree = mod.get('yang-tree')
    if tree is None or tree == '':
        continue
    name = mod['name']
    revision = mod['revision']
    organization = mod['organization']
    tree = tree.replace(':8443', '/api')
    requests.patch('http://yangcatalog.org:8008/api/config/catalog/modules/module/{},{},{}/yang-tree'.format(name, revision, organization),
                   data=json.dumps({'yang-tree': tree}), auth=('admin', 'admin'),
                   headers={
                       'Accept': 'application/vnd.yang.data+json',
                       'Content-type': 'application/vnd.yang.data+json'}
                   )

