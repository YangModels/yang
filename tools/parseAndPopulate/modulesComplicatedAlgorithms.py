import json
import subprocess
from datetime import datetime

import requests

from tools.utility import log
from tools.utility.util import get_curr_dir, find_first_file

LOGGER = log.get_logger('')


class ModulesComplicatedAlgorithms:

    def __init__(self, yangcatalog_api_prefix, credentials, protocol, ip, port,
                 save_file_dir, direc, all_modules):
        if all_modules is None:
            with open('../parseAndPopulate/' + direc + '/prepare.json', 'r') as f:
                self.__all_modules = json.load(f)
        else:
            self.__all_modules = all_modules
        self.__yangcatalog_api_prefix = yangcatalog_api_prefix
        self.__new_modules = []
        self.__credentials = credentials
        self.__protocol = protocol
        self.__ip = ip
        self.__port = port
        self.__save_file_dir = save_file_dir
        self.__path = None
        self.__prefix = '{}://{}:{}'.format(protocol, ip, port)

    def parse(self, tree_type_allowed):
        if tree_type_allowed:
            LOGGER.info("parsing tree types")
            self.__resolve_tree_type()
        LOGGER.info("parsing semantic version")
        self.__parse_semver()
        LOGGER.info("parsing dependents")
        self.__parse_dependents()

    def populate(self):
        mod = len(self.__new_modules) % 250
        for x in range(0, len(self.__new_modules) / 250):
            json_modules_data = json.dumps({'modules': {'module': self.__new_modules[x * 250: (x * 250) + 250]}})
            if '{"module": []}' not in json_modules_data:
                url = self.__prefix + '/api/config/catalog/modules/'
                response = requests.patch(url, json_modules_data,
                                          auth=(self.__credentials[0],
                                                self.__credentials[1]),
                                          headers={
                                              'Accept': 'application/vnd.yang.data+json',
                                              'Content-type': 'application/vnd.yang.data+json'})
                if response.status_code < 200 or response.status_code > 299:
                    LOGGER.error('Request with body on path {} failed with {}'.
                                 format(json_modules_data, url,
                                        response.content))
        rest = (len(self.__new_modules) / 250) * 250
        json_modules_data = json.dumps(
            {'modules': {'module': self.__new_modules[rest: rest + mod]}})
        if '{"module": []}' not in json_modules_data:
            url = self.__prefix + '/api/config/catalog/modules/'
            response = requests.patch(url, json_modules_data,
                                      auth=(self.__credentials[0],
                                            self.__credentials[1]),
                                      headers={
                                          'Accept': 'application/vnd.yang.data+json',
                                          'Content-type': 'application/vnd.yang.data+json'})
            if response.status_code < 200 or response.status_code > 299:
                LOGGER.error('Request with body on path {} failed with {}'.
                             format(json_modules_data, url,
                                    response.content))
        url = (self.__yangcatalog_api_prefix + 'load-cache')
        LOGGER.info('{}'.format(url))
        response = requests.post(url, None,
                                 auth=(self.__credentials[0],
                                       self.__credentials[1]))
        if response.status_code != 201:
            LOGGER.warning('Could not send a load-cache request')

    def __resolve_tree_type(self):
        def is_openconfig(rows, output):
            count_config = output.count('+-- config')
            count_state = output.count('+-- state')
            if count_config != count_state:
                return False
            row_number = 0
            skip = []
            for row in rows:
                if 'x--' in row or 'o--' in row:
                    continue
                if '' == row.strip(' '):
                    break
                if '+--rw' in row and row_number != 0 \
                        and row_number not in skip and '[' not in row and \
                        (len(row.replace('|', '').strip(' ').split(
                            ' ')) != 2 or '(' in row):
                    if '->' in row and 'config' in row.split('->')[
                        1] and '+--rw config' not in rows[row_number - 1]:
                        row_number += 1
                        continue
                    if '+--rw config' not in rows[row_number - 1]:
                        if 'augment' in rows[row_number - 1]:
                            if not rows[row_number - 1].endswith(':config:'):
                                return False
                        else:
                            return False
                    length_before = set([len(row.split('+--')[0])])
                    skip = []
                    for x in range(row_number, len(rows)):
                        if 'x--' in rows[x] or 'o--' in rows[x]:
                            continue
                        if len(rows[x].split('+--')[0]) not in length_before:
                            if (len(rows[x].replace('|', '').strip(' ').split(
                                    ' ')) != 2 and '[' not in rows[x]) \
                                    or '+--:' in rows[x] or '(' in rows[x]:
                                length_before.add(len(rows[x].split('+--')[0]))
                            else:
                                break
                        if '+--ro' in rows[x]:
                            return False
                        duplicate = \
                            rows[x].replace('+--rw', '+--ro').split('+--')[1]
                        if duplicate.replace(' ', '') not in output.replace(' ',
                                                                            ''):
                            return False
                        skip.append(x)
                if '+--ro' in row and row_number != 0 and row_number not in skip and '[' not in row and \
                        (len(row.replace('|', '').strip(' ').split(
                            ' ')) != 2 or '(' in row):
                    if '->' in row and 'state' in row.split('->')[
                        1] and '+--ro state' not in rows[row_number - 1]:
                        row_number += 1
                        continue
                    if '+--ro state' not in rows[row_number - 1]:
                        if 'augment' in rows[row_number - 1]:
                            if not rows[row_number - 1].endswith(':state:'):
                                return False
                        else:
                            return False
                    length_before = len(row.split('+--')[0])
                    skip = []
                    for x in range(row_number, len(rows)):
                        if 'x--' in rows[x] or 'o--' in rows[x]:
                            continue
                        if len(rows[x].split('+--')[0]) < length_before:
                            break
                        if '+--rw' in rows[x]:
                            return False
                        skip.append(x)
                row_number += 1
            return True

        def is_combined(rows, output):
            if output.split('\n')[0].endswith('-state'):
                return False
            next_obsolete_or_deprecated = False
            for row in rows:
                if next_obsolete_or_deprecated:
                    if 'x--' in row or 'o--' in row:
                        next_obsolete_or_deprecated = False
                    else:
                        return False
                if 'x--' in row or 'o--' in row:
                    continue
                if '+--rw config' == row.replace('|', '').strip(
                        ' ') or '+--ro state' == row.replace('|', '').strip(
                    ' '):
                    return False
                if len(row.split('+--')[0]) == 4:
                    if '-state' in row and '+--ro' in row:
                        return False
                if len(row.split('augment')[0]) == 2:
                    part = row.strip(' ').split('/')[1]
                    if '-state' in part:
                        next_obsolete_or_deprecated = True
                    part = row.strip(' ').split('/')[-1]
                    if ':state:' in part or '/state:' in part \
                            or ':config:' in part or '/config:' in part:
                        next_obsolete_or_deprecated = True
            return True

        def is_transational(rows, output):
            if output.split('\n')[0].endswith('-state'):
                if '+--rw' in output:
                    return False
                name_of_module = output.split('\n')[0].split(': ')[1]
                name_of_module = name_of_module.split('-state')[0]
                coresponding_nmda_file = self.__find_file(name_of_module)
                if coresponding_nmda_file:
                    arguments = ["pyang", "-p", get_curr_dir(__file__) + "/../../.", "-f", "tree",
                                 coresponding_nmda_file]
                    pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    stdout, stderr = pyang.communicate()
                    pyang_list_of_rows = stdout.split('\n')[1:]
                    if 'error' in stderr and 'is not found' in stderr:
                        return False
                    elif stdout == '':
                        return False
                    for x in range(0, len(rows)):
                        if 'x--' in rows[x] or 'o--' in rows[x]:
                            continue
                        if rows[x].strip(' ') == '':
                            break
                        if len(rows[x].split('+--')[0]) == 4:
                            if '-state' in rows[x]:
                                return False
                        if len(rows[x].split('augment')[0]) == 2:
                            part = rows[x].strip(' ').split('/')[1]
                            if '-state' in part:
                                return False
                        if '+--ro ' in rows[x]:
                            leaf = \
                                rows[x].split('+--ro ')[1].split(' ')[0].split(
                                    '?')[0]

                            dataExist = False
                            for y in range(0, len(pyang_list_of_rows)):
                                if leaf in pyang_list_of_rows[y]:
                                    dataExist = True
                            if not dataExist:
                                return False
                    return True
                else:
                    return False
            else:
                return False

        def is_split(rows, output):
            failed = False
            row_num = 0
            if output.split('\n')[0].endswith('-state'):
                return False
            for row in rows:
                if 'x--' in row or 'o--' in row:
                    continue
                if '+--rw config' == row.replace('|', '').strip(
                        ' ') or '+--ro state' == row.replace('|', '') \
                        .strip(' '):
                    return False
                if 'augment' in row:
                    part = row.strip(' ').split('/')[-1]
                    if ':state:' in part or '/state:' in part or ':config:' in part or '/config:' in part:
                        return False
            for row in rows:
                if 'x--' in row or 'o--' in row:
                    continue
                if row == '':
                    break
                if (len(row.split('+--')[0]) == 4 and 'augment' not in rows[
                    row_num - 1]) or len(row.split('augment')[0]) == 2:
                    if '-state' in row:
                        if 'augment' in row:
                            part = row.strip(' ').split('/')[1]
                            if '-state' not in part:
                                row_num += 1
                                continue
                        for x in range(row_num + 1, len(rows)):
                            if 'x--' in rows[x] or 'o--' in rows[x]:
                                continue
                            if rows[x].strip(' ') == '' \
                                    or (len(rows[x].split('+--')[
                                                0]) == 4 and 'augment' not in
                                        rows[row_num - 1]) \
                                    or len(row.split('augment')[0]) == 2:
                                break
                            if '+--rw' in rows[x]:
                                failed = True
                                break
                row_num += 1
            if failed:
                return False
            else:
                return True

        x = 0
        for module in self.__all_modules['module']:
            x += 1
            self.__path = '{}{}@{}.yang'.format(self.__save_file_dir,
                                                            module['name'],
                                                            module['revision'])
            LOGGER.info('Searching tree type for {}. {} out of {}'.format(module['name'], x, len(self.__all_modules['module'])))
            LOGGER.debug(
                'Get tree type from tag from module {}'.format(self.__path))
            arguments = ["pyang", "-p", get_curr_dir(__file__) + "/../../.", "-f", "tree", self.__path]
            pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = pyang.communicate()
            if 'error' in stderr and 'is not found' in stderr:
                LOGGER.debug(
                    'Could not use pyang to generate tree because of error {} on module {}'.
                        format(stderr, self.__path))
                module['tree-type'] = 'unclassified'
            elif stdout == '':
                module['tree-type'] = 'not-applicable'
            else:
                pyang_list_of_rows = stdout.split('\n')[1:]
                if 'submodule' == module['module-type']:
                    LOGGER.debug('Module {} is a submodule'.format(self.__path))
                    module['tree-type'] = 'not-applicable'
                elif is_combined(pyang_list_of_rows, stdout):
                    module['tree-type'] = 'nmda-compatible'
                elif is_transational(pyang_list_of_rows, stdout):
                    module['tree-type'] = 'transitional-extra'
                elif is_openconfig(pyang_list_of_rows, stdout):
                    module['tree-type'] = 'openconfig'
                elif is_split(pyang_list_of_rows, stdout):
                    module['tree-type'] = 'split'
                else:
                    module['tree-type'] = 'unclassified'

    def __parse_semver(self):
        z = 0
        for module in self.__all_modules['module']:
            z += 1
            LOGGER.info('Searching semver for {}. {} out of {}'.format(module['name'], z, len(self.__all_modules['module'])))
            url = '{}search/name/{}'.format(self.__yangcatalog_api_prefix, module['name'])
            response = requests.get(url, auth=(self.__credentials[0], self.__credentials[1]),
                                    headers={'Accept': 'application/json'})
            if response.status_code == 404:
                module['derived-semantic-version'] = '1.0.0'
                self.__new_modules.append(module)
            else:
                data = json.loads(response.content)
                rev = module['revision'].split('-')
                date = datetime(int(rev[0]), int(rev[1]), int(rev[2]))
                module_temp = {}
                module_temp['name'] = module['name']
                module_temp['revision'] = module['revision']
                module_temp['organization'] = module['organization']
                module_temp['compilation'] = module['compilation-status']
                module_temp['date'] = date
                module_temp['schema'] = module['schema']
                modules = [module_temp]
                semver_exist = True
                for mod in data['yang-catalog:modules']['module']:
                    module_temp = {}
                    revision = mod['revision']
                    if revision == module['revision']:
                        continue
                    rev = revision.split('-')
                    module_temp['revision'] = revision
                    module_temp['date'] = datetime(int(rev[0]), int(rev[1]), int(rev[2]))
                    module_temp['name'] = mod['name']
                    module_temp['organization'] = mod['organization']
                    module_temp['schema'] = mod.get('schema')
                    module_temp['compilation'] = mod['compilation-status']
                    module_temp['semver'] = mod.get('derived-semantic-version')
                    if module_temp['semver'] is None:
                        semver_exist = False
                    modules.append(module_temp)
                if len(modules) == 1:
                    module['derived-semantic-version'] = '1.0.0'
                    self.__new_modules.append(module)
                    continue
                modules = sorted(modules, key=lambda k: k['date'])
                if modules[-1]['date'] == date and semver_exist:
                    if modules[-1]['compilation'] != 'passed':
                        versions = modules[-2]['semver'].split('.')
                        ver = int(versions[0])
                        ver += 1
                        upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                        module['derived-semantic-version'] = upgraded_version
                        self.__new_modules.append(module)
                    else:
                        if modules[-2]['compilation'] != 'passed':
                            versions = modules[-2]['semver'].split('.')
                            ver = int(versions[0])
                            ver += 1
                            upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                            module['derived-semantic-version'] = upgraded_version
                            self.__new_modules.append(module)
                            continue
                        else:
                            schema2 = '{}{}@{}.yang'.format(self.__save_file_dir,
                                                            modules[-2]['name'],
                                                            modules[-2]['revision'])
                            schema1 = '{}{}@{}.yang'.format(self.__save_file_dir,
                                                            modules[-1]['name'],
                                                            modules[-1]['revision'])
                        arguments = ['pyang', '-P', get_curr_dir(__file__) + '/../../.', '-p', get_curr_dir(__file__) + '/../../.',
                                     schema1, '--check-update-from',
                                     schema2]
                        pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
                        stdout, stderr = pyang.communicate()
                        if stderr == '':
                            arguments = ["pyang", '-p', get_curr_dir(__file__) + '/../../.', "-f", "tree",
                                         schema1]
                            pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
                            stdout, stderr = pyang.communicate()
                            arguments = ["pyang", "-p", get_curr_dir(__file__) + "/../../.", "-f", "tree",
                                         schema2]
                            pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
                            stdout2, stderr = pyang.communicate()
                            if stdout == stdout2:
                                versions = modules[-2]['semver'].split('.')
                                ver = int(versions[2])
                                ver += 1
                                upgraded_version = '{}.{}.{}'.format(versions[0],
                                                                     versions[1],
                                                                     ver)
                                module[
                                    'derived-semantic-version'] = upgraded_version
                                self.__new_modules.append(module)
                                continue
                            else:
                                versions = modules[-2]['semver'].split('.')
                                ver = int(versions[1])
                                ver += 1
                                upgraded_version = '{}.{}.{}'.format(versions[0],
                                                                     ver, 0)
                                module[
                                    'derived-semantic-version'] = upgraded_version
                                self.__new_modules.append(module)
                                continue
                        else:
                            versions = modules[-2]['semver'].split('.')
                            ver = int(versions[0])
                            ver += 1
                            upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                            module[
                                'derived-semantic-version'] = upgraded_version
                            self.__new_modules.append(module)
                            continue
                else:
                    mod = {}
                    mod['name'] = modules[0]['name']
                    mod['revision'] = modules[0]['revision']
                    mod['organization'] = modules[0]['organization']
                    modules[0]['semver'] = '1.0.0'
                    response = requests.get(
                        '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(self.__protocol, self.__ip, self.__port,
                                                                                       mod['name'], mod['revision'], mod['organization']),
                        auth=(self.__credentials[0], self.__credentials[1]), headers={'Accept': 'application/vnd.yang.data+json'})
                    response = json.loads(response.content)['yang-catalog:module']
                    response['derived-semantic-version'] = '1.0.0'
                    self.__new_modules.append(response)

                    for x in range(1, len(modules)):
                        mod = {}
                        mod['name'] = modules[x]['name']
                        mod['revision'] = modules[x]['revision']
                        mod['organization'] = modules[x]['organization']
                        if modules[x]['compilation'] != 'passed':
                            versions = modules[x - 1]['semver'].split('.')
                            ver = int(versions[0])
                            ver += 1
                            upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                            modules[x]['semver'] = upgraded_version
                            response = requests.get(
                                '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                    self.__protocol, self.__ip, self.__port,
                                    mod['name'], mod['revision'],
                                    mod['organization']),
                                auth=(self.__credentials[0], self.__credentials[1]), headers={
                                    'Accept': 'application/vnd.yang.data+json'})
                            response = json.loads(response.content)[
                                'yang-catalog:module']
                            response['derived-semantic-version'] = upgraded_version
                            self.__new_modules.append(response)
                        else:
                            if modules[x - 1]['compilation'] != 'passed':
                                versions = modules[x - 1]['semver'].split('.')
                                ver = int(versions[0])
                                ver += 1
                                upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                                modules[x]['semver'] = upgraded_version
                                response = requests.get(
                                    '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                        self.__protocol, self.__ip, self.__port,
                                        mod['name'], mod['revision'],
                                        mod['organization']),
                                    auth=(
                                        self.__credentials[0], self.__credentials[1]), headers={
                                        'Accept': 'application/vnd.yang.data+json'})
                                response = json.loads(response.content)[
                                    'yang-catalog:module']
                                response[
                                    'derived-semantic-version'] = upgraded_version
                                self.__new_modules.append(response)
                                continue
                            else:
                                schema2 = '{}{}@{}.yang'.format(
                                    self.__save_file_dir,
                                    modules[x]['name'],
                                    modules[x]['revision'])
                                schema1 = '{}{}@{}.yang'.format(
                                    self.__save_file_dir,
                                    modules[x - 1]['name'],
                                    modules[x - 1]['revision'])
                            arguments = ['pyang', '-p', get_curr_dir(__file__) + '/../../.', '-P', get_curr_dir(__file__) + '/../../.',
                                         schema2,
                                         '--check-update-from', schema1]
                            pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
                            stdout, stderr = pyang.communicate()
                            if stderr == '':
                                arguments = ["pyang", '-p', get_curr_dir(__file__) + '/../../.', "-f", "tree",
                                             schema1]
                                pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE)
                                stdout, stderr = pyang.communicate()
                                arguments = ["pyang", '-p', get_curr_dir(__file__) + '/../../.', "-f", "tree",
                                             schema2]
                                pyang = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE)
                                stdout2, stderr = pyang.communicate()
                                if stdout == stdout2:
                                    versions = modules[x - 1]['semver'].split('.')
                                    ver = int(versions[2])
                                    ver += 1
                                    upgraded_version = '{}.{}.{}'.format(
                                        versions[0], versions[1], ver)
                                    modules[x]['semver'] = upgraded_version
                                    response = requests.get(
                                        '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                            self.__protocol, self.__ip, self.__port,
                                            mod['name'], mod['revision'],
                                            mod['organization']),
                                        auth=(self.__credentials[0],
                                              self.__credentials[1]), headers={
                                            'Accept': 'application/vnd.yang.data+json'})
                                    response = json.loads(response.content)[
                                        'yang-catalog:module']
                                    response[
                                        'derived-semantic-version'] = upgraded_version
                                    self.__new_modules.append(response)
                                else:
                                    versions = modules[x - 1]['semver'].split('.')
                                    ver = int(versions[1])
                                    ver += 1
                                    upgraded_version = '{}.{}.{}'.format(
                                        versions[0], ver, 0)
                                    modules[x]['semver'] = upgraded_version
                                    response = requests.get(
                                        '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                            self.__protocol, self.__ip, self.__port,
                                            mod['name'], mod['revision'],
                                            mod['organization']),
                                        auth=(self.__credentials[0],
                                              self.__credentials[1]), headers={
                                            'Accept': 'application/vnd.yang.data+json'})
                                    response = json.loads(response.content)[
                                        'yang-catalog:module']
                                    response[
                                        'derived-semantic-version'] = upgraded_version
                                    self.__new_modules.append(response)
                            else:
                                versions = modules[x - 1]['semver'].split('.')
                                ver = int(versions[0])
                                ver += 1
                                upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                                modules[x]['semver'] = upgraded_version
                                response = requests.get(
                                    '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                        self.__protocol, self.__ip, self.__port,
                                        mod['name'], mod['revision'],
                                        mod['organization']),
                                    auth=(
                                        self.__credentials[0], self.__credentials[1]), headers={
                                        'Accept': 'application/vnd.yang.data+json'})
                                response = json.loads(response.content)[
                                    'yang-catalog:module']
                                response[
                                    'derived-semantic-version'] = upgraded_version
                                self.__new_modules.append(response)

    def __parse_dependents(self):
        x = 0
        for mod in self.__all_modules['module']:
            x += 1
            LOGGER.info('Searching dependents for {}. {} out of {}'.format(mod['name'], x, len(self.__all_modules['module'])))
            name = mod['name']
            revision = mod['revision']
            new_dependencies = mod['dependencies']
            for new_dep in new_dependencies:
                if new_dep.get('revision'):
                    search = {'name': new_dep['name'], 'revision': new_dep['revision']}
                else:
                    search = {'name': new_dep['name']}
                response = requests.post(self.__yangcatalog_api_prefix
                                         + 'search-filter',
                                         auth=(self.__credentials[0], self.__credentials[1]),
                                         json={'input': search})
                if response.status_code == 200:
                    mods = json.loads(response.content)['yang-catalog:modules'][
                        'module']
                    for m in mods:
                        if m.get('dependents') is None:
                            m['dependents'] = []
                        new = {'name': name,
                               'revision': revision,
                               'schema': mod['schema']}
                        if new not in m['dependents']:
                            m['dependents'].append(new)
                            self.__new_modules.append(m)
            response = requests.post(self.__yangcatalog_api_prefix + 'search-filter',
                                     auth=(self.__credentials[0], self.__credentials[1]),
                                     json={'input': {'dependencies': [{'name': name}]}})
            if response.status_code == 200:
                mods = json.loads(response.content)['yang-catalog:modules']['module']
                if mod.get('dependents')is None:
                    mod['dependents'] = []
                for m in mods:
                    passed = False
                    for dependency in m['dependencies']:
                        if dependency['name'] == name:
                            passed = True
                            rev = dependency.get('revision')
                            if rev:
                                passed = False
                                if rev == revision:
                                    passed = True
                    if passed:
                        new = {'name': m['name'],
                               'revision': m['revision'],
                               'schema': m['schema']}
                        if new not in mod['dependents']:
                            mod['dependents'].append(new)
                if len(mod['dependents']) > 0:
                    self.__new_modules.append(mod)

    def __find_file(self, name, revision='*'):
        yang_file = find_first_file('/'.join(self.__path.split('/')[0:-1]),
                                    name + '.yang'
                                    , name + '@' + revision + '.yang')
        if yang_file is None:
            yang_file = find_first_file(get_curr_dir(__file__) + '/../../.', name + '.yang',
                                        name + '@' + revision + '.yang')
        return yang_file