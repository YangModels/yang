import json
import tools.utility.log as lo
import requests

LOGGER = lo.get_logger('missing-element')
URL = 'http://localhost:8009/api/config/catalog/modules'
HEADERS = 'application/vnd.yang.data+json'
API_URL = 'http://localhost:5000/search/name/'
DELETE_URL = 'http://yangcatalog.org:8008/api/config/catalog/vendors/vendor/{}/platforms/platform/{}/software-versions/software-version/{}/software-flavors/software-flavor/{}/modules/module/{},{},{}'


def schema_does_not_exist():
    org = mod['organization']
    if org == 'independent':
        if mod.get('schema') is None:
            LOGGER.info('removing {} {}'.format(mod['name'], mod['revision']))
            if mod.get('implementations'):
                imp = mod['implementations']['implementation']
                for im in imp:
                    r = requests.delete(
                        DELETE_URL.format(im['vendor'], im['platform'],
                                          im['software-version'],
                                          im['software-flavor'],
                                          mod['name'], mod['revision'],
                                          'missing element'),
                        auth=('admin', 'admin'),
                        headers={'Accept': HEADERS,
                                 'Content-type': HEADERS})
                    pass
            r = requests.delete('{}/module/{},{},{}'.format(URL, mod['name'],
                                                            mod['revision'],
                                                            'independent'
                                                            ),
                                auth=('admin', 'admin'),
                                headers={'Accept': HEADERS,
                                         'Content-type': HEADERS})
            removed_independent.add(mod['name'] + '@' + mod['revision'])


def check_module_missing_element():
    name = mod['name']
    res = requests.get('{}{}'.format(API_URL, name), auth=('admin', 'admin'))
    mods = json.loads(res.content)['yang-catalog:modules']['module']

    for m in mods:
        found = True
        if m['organization'] == 'missing element':
            found = False
            for m2 in mods:
                if (m2['organization'] != 'missing element' and
                            m2['revision'] == m['revision']):
                    if m.get('implementations'):
                        imp = m['implementations']['implementation']
                        for im in imp:
                            r = requests.delete(
                                DELETE_URL.format(im['vendor'], im['platform'],
                                                  im['software-version'],
                                                  im['software-flavor'],
                                                  m['name'], m['revision'],
                                                  m['organization']),
                                auth=('admin', 'admin'),
                                headers={'Accept': HEADERS,
                                         'Content-type': HEADERS})
                            pass
                    LOGGER.info('removing {} {}'.format(name, m['revision']))
                    r = requests.delete('{}/module/{},{},{}'.format(URL, name,
                                                                    m[
                                                                        'revision'],
                                                                    'missing element'
                                                                    ),
                                        auth=('admin', 'admin'),
                                        headers={'Accept': HEADERS,
                                                 'Content-type': HEADERS})
                    found = True
                    redundant_missing.add(name + '@' + m['revision'])
                    break
            if not found:
                body = m
                body['organization'] = 'independent'
                requests.patch('{}/module'.format(URL),
                               data=json.dumps({'module': body}),
                               auth=('admin', 'admin'),
                               headers={'Accept': HEADERS,
                                        'Content-type': HEADERS})
                LOGGER.info('removing {} {}'.format(name, m['revision']))
                r = requests.delete('{}/module/{},{},{}'.format(URL, name,
                                                          m['revision'],
                                                          'missing element'
                                                          ),
                                auth=('admin', 'admin'),
                                headers={'Accept': HEADERS,
                                         'Content-type': HEADERS})
                changed_to_independent.add(name + '@' + m['revision'])


if __name__ == '__main__':
    response = requests.get('{}?deep'.format(URL),
                            auth=('admin', 'admin'),
                            headers={'Accept': HEADERS,
                                     'Content-type': HEADERS})
    modules = json.loads(response.content)['yang-catalog:modules']['module']
    changed_to_independent = set()
    redundant_missing = set()
    removed_independent = set()
    for mod in modules:
        schema_does_not_exist()
    message = json.dumps({'redundant': list(redundant_missing),
                          'changed_to_independent': list(changed_to_independent),
                          'removed_independent': list(removed_independent)},
                         indent=4)
    LOGGER.info(message)

