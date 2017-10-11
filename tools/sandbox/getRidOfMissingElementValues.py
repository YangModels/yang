import json

import requests

URL = 'http://yangcatalog.org:8008/api/config/catalog/modules'
HEADERS = 'application/vnd.yang.data+json'

MANDATORY_LEAFS = ['name', 'revision', 'organization', 'namespace', 'vendor',
                   'module-classification', 'submodule', 'dependencies',
                   'dependents', 'implementations']


def check_module_missing_element():
    modified_module = False
    for k in mod:
        if k not in MANDATORY_LEAFS:
            if mod[k] == 'missing element':
                mod[k] = None
                modified_module = True
    if modified_module:
        data = json.dumps({
            'module': mod
        })
        url = '{}/module/{},{},{}'.format(URL, mod['name'], mod['revision'],
                                          mod['organization'])
        requests.put(url, data, auth=('admin', 'admin'),
                     headers={'Accept': HEADERS,
                              'Content-type': HEADERS})


if __name__ == '__main__':
    response = requests.get('{}?deep'.format(URL),
                            auth=('admin', 'admin'),
                            headers={'Accept': HEADERS,
                                     'Content-type': HEADERS})
    modules = json.loads(response.content)['yang-catalog:modules']['module']
    modified_modules = []
    for mod in modules:
        check_module_missing_element()
