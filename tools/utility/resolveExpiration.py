import argparse
import json

import requests

import tools.utility.log as log

LOGGER = log.get_logger('ResolveExpiration')


def __resolve_expiration(reference, module, args):
    update = False
    if reference is not None and 'datatracker.ietf.org' in reference:
        ref = reference.split('/')[-1]
        url = ('https://datatracker.ietf.org/api/v1/doc/document/'
               + ref + '/?format=json')
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            if '/api/v1/doc/state/2/' in data['states']:
                expired = module.get('expired')
                if expired is None or not expired:
                    update = True
                    module['expired'] = True
                if module.get('expires') is not None:
                    if module['expires'] != data['expires']:
                        update = True
                        module['expires'] = data['expires']
            else:
                expired = module.get('expired')
                if expired is None or expired:
                    update = True
                    module['expires'] = data['expires']
                    module['expired'] = False
        else:
            if module.get('expired') is None:
                update = True
                module['expired'] = 'not-applicable'
                module['expires'] = None
    elif module.get('expired') is None:
        update = True
        module['expired'] = 'not-applicable'
        module['expires'] = None
    if update:
        url = 'http://yangcatalog.org:8008/api/config/catalog/modules/module/{},{},{}' \
            .format(module['name'], module['revision'],
                    module['organization'])
        body = json.dumps({'yang-catalog:module': {
                'name': module['name'],
                'revision': module['revision'],
                'organization': module['organization'],
                'expires': module.get('expires'),
                'expired': module['expired']
            }
        })
        response = requests.patch(url, body,
                                  auth=(args.credentials[0],
                                        args.credentials[1]),
                                  headers={
                                      'Accept': 'application/vnd.yang.data+json',
                                      'Content-type': 'application/vnd.yang.data+json'}
                                  )
        LOGGER.info('Updating module {}@{} with confd response {} - {}'
                    .format(module['name'], module['revision'],
                            repr(response.status_code), response.content))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--credentials',
                        help='Set authorization parameters username password respectively.'
                             ' Default parameters are admin admin', nargs=2,
                        default=['admin', 'admin'], type=str)
    parser.add_argument('--api-protocol', type=str, default='https',
                        help='Whether api runs on http or https.'
                             ' Default is set to http')
    parser.add_argument('--api-ip', default='yangcatalog.org', type=str,
                        help='Set ip address where the api is started. Default -> yangcatalog.org')

    args = parser.parse_args()
    modules = requests.get('{}://{}/api/search/modules'.format(args.api_protocol,
                                                              args.api_ip),
                           auth=(args.credentials[0], args.credentials[1]))
    modules = json.loads(modules.content)['module']
    for mod in modules:
        ref = mod.get('reference')
        __resolve_expiration(ref, mod, args)
    url = (args.api_protocol + '://' + args.api_ip + '/api/load-cache')
    response = requests.post(url, None, auth=(args.credentials[0],
                                              args.credentials[1]))
