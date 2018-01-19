import requests
from flask import json

vendor = 'cisco'
platform = 'NCS-5500'
URL = 'http://yangcatalog.org:8008/api/config/catalog/vendors/vendor/cisco/platforms/platform/{}'.format(platform)
HEADERS = 'application/vnd.yang.data+json'


def remove_implementation():
    requests.delete('http://yangcatalog.org:8008/api/config/catalog/modules/module/{},{},{}/implementations/implementation/{},{},{},{}'
                    .format(mod['name'], mod['revision'], mod['organization'], vendor, platform, version_name, flavor_name),
                            auth=('admin', 'Y@ng_adm1n->(paSS)'))


if __name__ == '__main__':
    response = requests.get('{}?deep'.format(URL),
                            auth=('admin', 'Y@ng_adm1n->(paSS)'),
                            headers={'Accept': HEADERS,
                                     'Content-type': HEADERS})
    vendor_info = json.loads(response.content)['yang-catalog:platform']
    modified_modules = []
    vendor_info = vendor_info['software-versions']['software-version']
    for version in vendor_info:
        version_name = version['name']
        for flavor in version['software-flavors']['software-flavor']:
            flavor_name = flavor['name']
            for mod in flavor['modules']['module']:
                remove_implementation()