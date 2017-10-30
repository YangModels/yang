import ConfigParser
import argparse
import errno
import fnmatch
import json
import os
import shutil
import subprocess
import unicodedata
from datetime import datetime

import requests

import tools.utility.log as log
from tools.api.receiver import send_to_indexing
from tools.utility.util import get_curr_dir

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
    parser.add_argument('--save-file-dir', default='/home/miroslav/results/',
                        type=str, help='Directory where the file will be saved')
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
    prefix = '{}://{}:{}'.format(args.protocol, args.ip, args.port)
    LOGGER.info('Calling runcapabilities script')
    if args.api:
        if args.sdo:
            with open("log_api_sdo.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--api", "--sdo", "--dir",
                             args.dir, "--json-dir", direc, "--result-html-dir", args.result_html_dir,
                             '--save-file-dir', args.save_file_dir]
                subprocess.check_call(arguments, stderr=f)
        else:
            with open("log_api.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--api", "--dir", args.dir,
                             "--json-dir", direc, "--result-html-dir", args.result_html_dir,
                             '--save-file-dir', args.save_file_dir]
                subprocess.check_call(arguments, stderr=f)
    else:
        if args.sdo:
            with open("log_sdo.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--sdo", "--dir", args.dir,
                             "--json-dir", direc, "--result-html-dir", args.result_html_dir,
                             '--save-file-dir', args.save_file_dir]
                subprocess.check_call(arguments, stderr=f)
        else:
            with open("log_no_sdo_api.txt", "wr") as f:
                arguments = ["python", "../parseAndPopulate/runCapabilities.py", "--dir", args.dir, "--json-dir", direc,
                             "--result-html-dir", args.result_html_dir,
                             '--save-file-dir', args.save_file_dir]
                subprocess.check_call(arguments, stderr=f)

    LOGGER.info('Populating yang catalog with data. Starting to add modules')

    with open('../parseAndPopulate/{}/prepare.json'.format(direc)) as data_file:
        read = data_file.read()
        modules_json = json.loads(read)['module']
        mod = len(modules_json) % 1000
        for x in range(0, len(modules_json) / 1000):
            json_modules_data = json.dumps({
                'modules':
                    {
                        'module': modules_json[x*1000: (x*1000)+1000]
                    }
            })

            if '{"module": []}' not in read:
                url = prefix + '/api/config/catalog/modules/'
                response = requests.patch(url, json_modules_data,
                                          auth=(args.credentials[0],
                                                args.credentials[1]),
                                          headers={
                                              'Accept': 'application/vnd.yang.data+json',
                                              'Content-type': 'application/vnd.yang.data+json'})
                if response.status_code < 200 or response.status_code > 299:
                    LOGGER.error('Request with body on path {} failed with {}'
                                 .format(json_modules_data, url,
                                        response.content))
    rest = (len(modules_json) / 1000) * 1000
    json_modules_data = json.dumps({
        'modules':
            {
                'module': modules_json[rest: rest + mod]
            }
    })
    url = prefix + '/api/config/catalog/modules/'
    response = requests.patch(url, json_modules_data,
                              auth=(args.credentials[0],
                                    args.credentials[1]),
                              headers={
                                  'Accept': 'application/vnd.yang.data+json',
                                  'Content-type': 'application/vnd.yang.data+json'})
    if response.status_code < 200 or response.status_code > 299:
        LOGGER.error('Request with body on path {} failed with {}'
                     .format(json_modules_data, url,
                             response.content))
    #files = []
    ## Find all parsed json files
    #for filename in find_files('../parseAndPopulate/' + direc, 'normal*.json'):
    #    with open(filename) as data_file:
    #        files.append(json.load(data_file))

    # In each json
    LOGGER.info('Starting to add vendors')
    if os.path.exists('../parseAndPopulate/{}/normal.json'):
        with open('../parseAndPopulate/{}/normal.json'.format(direc)) as data:
            vendors = json.loads(data.read())['vendors']['vendor']

            mod = len(vendors) % 1000
            for x in range(0, len(vendors) / 1000):
                json_implementations_data = json.dumps({
                    'vendors':
                        {
                            'vendor': vendors[x * 1000: (x * 1000) + 1000]
                        }
                })
                # Prepare json_data for put request - this request will prepare list vendors
                # to populate it with protocols and modules
                #json_implementations_data = json.dumps(data)
                # Make a PATCH request to create a root for each file
                url = prefix + '/api/config/catalog/vendors/'
                response = requests.patch(url, json_implementations_data,
                                          auth=(args.credentials[0],
                                                args.credentials[1]),
                                          headers={
                                              'Accept': 'application/vnd.yang.data+json',
                                              'Content-type': 'application/vnd.yang.data+json'})
                if response.status_code < 200 or response.status_code > 299:
                    LOGGER.error('Request with body on path {} failed with {}'.
                                 format(json_implementations_data, url,
                                        response.content))
            rest = (len(vendors) / 1000) * 1000
            json_implementations_data = json.dumps({
                'vendors':
                    {
                        'vendor': vendors[rest: rest + mod]
                    }
            })
            url = prefix + '/api/config/catalog/vendors/'
            response = requests.patch(url, json_implementations_data,
                                      auth=(args.credentials[0],
                                            args.credentials[1]),
                                      headers={
                                          'Accept': 'application/vnd.yang.data+json',
                                          'Content-type': 'application/vnd.yang.data+json'})
            if response.status_code < 200 or response.status_code > 299:
                LOGGER.error('Request with body on path {} failed with {}'
                             .format(json_implementations_data, url,
                                     response.content))
    if not args.api:
        #do_indexing = True
        #if 'ietf-extracted-YANG-modules' in args.dir:
        #    try:
        #        os.makedirs('./old')
        #    except OSError:
        #        # Be happy if deleted
        #        pass
        #    try:
        #        with open('./old/prepare.json', 'r') as f:
        #            old = f.read()
        #    except:
        #        old = ''
        #    with open('../parseAndPopulate/' + direc + '/prepare.json', 'r') as f:
        #        new = f.read()
        #    if old != new:
        #        do_indexing = True
        #    shutil.copy('../parseAndPopulate/' + direc + '/prepare.json', './old/.')
        if args.notify_indexing:# and do_indexing:
            LOGGER.info('Sending files for indexing')
            send_to_indexing('../parseAndPopulate/' + direc + '/prepare.json', args.credentials, args.ip, args.api_port,
                             args.api_protocol, from_api=False, set_key=key, force_indexing=args.force_indexing)
        LOGGER.info('Removing temporary json data and cache data')

        try:
            shutil.rmtree('../api/cache')
        except OSError:
            # Be happy if deleted
            pass
        LOGGER.info('Sending request to reload cache')
        url = (args.api_protocol + '://' + args.api_ip + ':' +
               repr(args.api_port) + '/load-cache')
        response = requests.post(url, None,
                                 auth=(args.credentials[0],
                                        args.credentials[1]),
                                 headers={
                                     'Accept': 'application/vnd.yang.data+json',
                                     'Content-type': 'application/vnd.yang.data+json'})
        if response.status_code != 201:
            LOGGER.warning('Could not send a load-cache request')

        with open('../parseAndPopulate/' + direc + '/prepare.json', 'r') as f:
            all_modules = json.load(f)

        new_modules = []
        for module in all_modules['module']:
            LOGGER.info('Searching semver for {}'.format(module['name']))
            url = '{}://{}:{}/search/name/{}'.format(args.api_protocol, args.api_ip, args.api_port, module['name'])
            response = requests.get(url, auth=(args.credentials[0], args.credentials[1]),
                                    headers={'Accept': 'application/json'})
            if response.status_code == 404:
                module['derived-semantic-version'] = '1.0.0'
                new_modules.append(module)
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
                    new_modules.append(module)
                    continue
                modules = sorted(modules, key=lambda k: k['date'])
                if modules[-1]['date'] == date and semver_exist:
                    if modules[-1]['compilation'] != 'passed':
                        versions = modules[-2]['semver'].split('.')
                        ver = int(versions[0])
                        ver += 1
                        upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                        module['derived-semantic-version'] = upgraded_version
                        new_modules.append(module)
                    else:
                        if modules[-2]['compilation'] != 'passed':
                            versions = modules[-2]['semver'].split('.')
                            ver = int(versions[0])
                            ver += 1
                            upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                            module['derived-semantic-version'] = upgraded_version
                            new_modules.append(module)
                            continue
                        #if (modules[-2]['schema'] is None or
                        #        modules[-1]['schema']):
                        #    LOGGER.warning('Schema is missing {} or {}'.
                        #                   format(modules[-2]['schema'],
                        #                          modules[-1]['schema']))
                        #    continue
                        else:
                            schema2 = '{}{}@{}.yang'.format(args.save_file_dir,
                                                            modules[-2]['name'],
                                                            modules[-2]['revision'])
                            schema1 = '{}{}@{}.yang'.format(args.save_file_dir,
                                                            modules[-1]['name'],
                                                            modules[-1]['revision'])
                            #if (schema1.status_code == 404 or
                            #    schema2.status_code == 404):
                            #    LOGGER.warning('Schema not found {} or {}'.
                            #                   format(modules[-2]['schema'],
                            #                          modules[-1]['schema']))
                            #    continue
                        #to_write_before = '{}/{}@{}.yang'.format(direc,
                        #                                modules[-2]['name'],
                        #                                modules[-2]['revision'])
                        #to_write = '{}/{}@{}.yang'.format(direc,
                        #                                       modules[-1][
                        #                                           'name'],
                        #                                       modules[-1][
                        #                                           'revision'])
                        #with open(to_write_before, 'w') as f:
                        #    f.write(schema2)
                        #with open(to_write, 'w+') as f:
                        #    f.write(schema1.content)
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
                                new_modules.append(module)
                                continue
                            else:
                                versions = modules[-2]['semver'].split('.')
                                ver = int(versions[1])
                                ver += 1
                                upgraded_version = '{}.{}.{}'.format(versions[0],
                                                                     ver, 0)
                                module[
                                    'derived-semantic-version'] = upgraded_version
                                new_modules.append(module)
                                continue
                        else:
                            versions = modules[-2]['semver'].split('.')
                            ver = int(versions[0])
                            ver += 1
                            upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                            module[
                                'derived-semantic-version'] = upgraded_version
                            new_modules.append(module)
                            continue
                else:
                    mod = {}
                    mod['name'] = modules[0]['name']
                    mod['revision'] = modules[0]['revision']
                    mod['organization'] = modules[0]['organization']
                    modules[0]['semver'] = '1.0.0'
                    response = requests.get(
                        '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(args.protocol, args.ip, args.port,
                            mod['name'], mod['revision'], mod['organization']),
                        auth=('admin', 'admin'), headers={'Accept': 'application/vnd.yang.data+json'})
                    response = json.loads(response.content)['yang-catalog:module']
                    response['derived-semantic-version'] = '1.0.0'
                    new_modules.append(response)

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
                                    args.protocol, args.ip, args.port,
                                    mod['name'], mod['revision'],
                                    mod['organization']),
                                auth=('admin', 'admin'), headers={
                                    'Accept': 'application/vnd.yang.data+json'})
                            response = json.loads(response.content)[
                                'yang-catalog:module']
                            response['derived-semantic-version'] = upgraded_version
                            new_modules.append(response)
                        else:
                            if modules[x - 1]['compilation'] != 'passed':
                                versions = modules[x - 1]['semver'].split('.')
                                ver = int(versions[0])
                                ver += 1
                                upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                                modules[x]['semver'] = upgraded_version
                                response = requests.get(
                                    '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                        args.protocol, args.ip, args.port,
                                        mod['name'], mod['revision'],
                                        mod['organization']),
                                    auth=('admin', 'admin'), headers={
                                        'Accept': 'application/vnd.yang.data+json'})
                                response = json.loads(response.content)[
                                    'yang-catalog:module']
                                response[
                                    'derived-semantic-version'] = upgraded_version
                                new_modules.append(response)
                                continue
                            #if (modules[x]['schema'] is None or
                            #        modules[x-1]['schema']):
                            #    break
                            #if (modules[x]['schema'] is None or
                            #        modules[x-1]['schema']):
                            #    LOGGER.warning('Schema is missing {} or {}'.
                            #                   format(modules[x]['schema'],
                            #                          modules[x-1]['schema']))
                            #    continue
                            else:
                                schema2 = '{}{}@{}.yang'.format(
                                    args.save_file_dir,
                                    modules[x]['name'],
                                    modules[x]['revision'])
                                schema1 = '{}{}@{}.yang'.format(
                                    args.save_file_dir,
                                    modules[x - 1]['name'],
                                    modules[x - 1]['revision'])
                                #if (schema1.status_code == 404 or
                                #            schema2.status_code == 404):
                                #    LOGGER.warning('Schema not found {} or {}'.
                                #                   format(modules[-2]['schema'],
                                #                          modules[-1][
                                #                              'schema']))
                                #    continue
                            #to_write = '{}/{}@{}.yang'.format(direc,
                            #                                modules[x]['name'],
                            #                                modules[x]['revision'])
                            #to_write_before = '{}/{}@{}.yang'.format(direc,
                            #                                       modules[x - 1][
                            #                                           'name'],
                            #                                       modules[x - 1][
                            #                                           'revision'])
                            #with open(to_write, 'w+') as f:
                            #    f.write(schema2.content)
                            #with open(to_write_before, 'w+') as f:
                            #    f.write(schema1.content)
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
                                            args.protocol, args.ip, args.port,
                                            mod['name'], mod['revision'],
                                            mod['organization']),
                                        auth=('admin', 'admin'), headers={
                                            'Accept': 'application/vnd.yang.data+json'})
                                    response = json.loads(response.content)[
                                        'yang-catalog:module']
                                    response[
                                        'derived-semantic-version'] = upgraded_version
                                    new_modules.append(response)
                                else:
                                    versions = modules[x - 1]['semver'].split('.')
                                    ver = int(versions[1])
                                    ver += 1
                                    upgraded_version = '{}.{}.{}'.format(
                                        versions[0], ver, 0)
                                    modules[x]['semver'] = upgraded_version
                                    response = requests.get(
                                        '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                            args.protocol, args.ip, args.port,
                                            mod['name'], mod['revision'],
                                            mod['organization']),
                                        auth=('admin', 'admin'), headers={
                                            'Accept': 'application/vnd.yang.data+json'})
                                    response = json.loads(response.content)[
                                        'yang-catalog:module']
                                    response[
                                        'derived-semantic-version'] = upgraded_version
                                    new_modules.append(response)
                            else:
                                versions = modules[x - 1]['semver'].split('.')
                                ver = int(versions[0])
                                ver += 1
                                upgraded_version = '{}.{}.{}'.format(ver, 0, 0)
                                modules[x]['semver'] = upgraded_version
                                response = requests.get(
                                    '{}://{}:{}/api/config/catalog/modules/module/{},{},{}'.format(
                                        args.protocol, args.ip, args.port,
                                        mod['name'], mod['revision'],
                                        mod['organization']),
                                    auth=('admin', 'admin'), headers={
                                        'Accept': 'application/vnd.yang.data+json'})
                                response = json.loads(response.content)[
                                    'yang-catalog:module']
                                response[
                                    'derived-semantic-version'] = upgraded_version
                                new_modules.append(response)

        for mod in all_modules['module']:
            name = mod['name']
            revision = mod['revision']
            new_dependencies = mod['dependencies']
            for new_dep in new_dependencies:
                if new_dep.get('revision'):
                    search = {'name': new_dep['name'], 'revision': new_dep['revision']}
                else:
                    search = {'name': new_dep['name']}
                response = requests.post(
                    args.api_protocol + '://' + args.api_ip + ':' + repr(
                        args.api_port) + '/search-filter', auth=(args.credentials[0], args.credentials[1]),
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
                            new_modules.append(m)

            response = requests.post(args.api_protocol + '://' + args.api_ip + ':' + repr(args.api_port) + '/search-filter',
                                     auth=(
                                     args.credentials[0], args.credentials[1]),
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
                    new_modules.append(mod)
        mod = len(new_modules) % 250
        for x in range(0, len(new_modules) / 250):
            json_modules_data = json.dumps({'modules': {'module': new_modules[x*250: (x*250)+250]}})
            if '{"module": []}' not in json_modules_data:
                url = prefix + '/api/config/catalog/modules/'
                response = requests.patch(url, json_modules_data,
                                          auth=(args.credentials[0],
                                                args.credentials[1]),
                                          headers={
                                              'Accept': 'application/vnd.yang.data+json',
                                              'Content-type': 'application/vnd.yang.data+json'})
                if response.status_code < 200 or response.status_code > 299:
                    LOGGER.error('Request with body on path {} failed with {}'.
                                 format(json_modules_data, url,
                                        response.content))
        rest = (len(new_modules) / 250) * 250
        json_modules_data = json.dumps(
            {'modules': {'module': new_modules[rest: rest + mod]}})
        if '{"module": []}' not in json_modules_data:
            url = prefix + '/api/config/catalog/modules/'
            response = requests.patch(url, json_modules_data,
                                      auth=(args.credentials[0],
                                            args.credentials[1]),
                                      headers={
                                          'Accept': 'application/vnd.yang.data+json',
                                          'Content-type': 'application/vnd.yang.data+json'})
            if response.status_code < 200 or response.status_code > 299:
                LOGGER.error('Request with body on path {} failed with {}'.
                             format(json_modules_data, url,
                                    response.content))
        try:
            shutil.rmtree('../api/cache')
        except OSError:
            # Be happy if deleted
            pass
        url = (args.api_protocol + '://' + args.api_ip + ':' +
               repr(args.api_port) + '/load-cache')
        response = requests.post(url, None,
                                 auth=(args.credentials[0],
                                       args.credentials[1]))
        if response.status_code != 201:
            LOGGER.warning('Could not send a load-cache request')
        shutil.rmtree('../parseAndPopulate/' + direc)
