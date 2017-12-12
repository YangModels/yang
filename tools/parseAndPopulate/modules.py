import json
import os
import re
import subprocess
import sys
import unicodedata
from subprocess import PIPE

import requests
from click.exceptions import FileError

import tools.statistics.statistics as stats
from tools.utility import log, yangParser
from tools.utility.util import find_first_file, get_curr_dir

IETF_RFC_MAP = {
    "iana-crypt-hash@2014-08-06.yang": "NETMOD",
    "iana-if-type@2014-05-08.yang": "NETMOD",
    "ietf-complex-types@2011-03-15.yang": "N/A",
    "ietf-inet-types@2010-09-24.yang": "NETMOD",
    "ietf-inet-types@2013-07-15.yang": "NETMOD",
    "ietf-interfaces@2014-05-08.yang": "NETMOD",
    "ietf-ip@2014-06-16.yang": "NETMOD",
    "ietf-ipfix-psamp@2012-09-05.yang": "IPFIX",
    "ietf-ipv4-unicast-routing@2016-11-04.yang": "NETMOD",
    "ietf-ipv6-router-advertisements@2016-11-04.yang": "NETMOD",
    "ietf-ipv6-unicast-routing@2016-11-04.yang": "NETMOD",
    "ietf-key-chain@2017-06-15.yang": "RTGWG",
    "ietf-l3vpn-svc@2017-01-27.yang": "L3SM",
    "ietf-lmap-common@2017-08-08.yang": "LMAP",
    "ietf-lmap-control@2017-08-08.yang": "LMAP",
    "ietf-lmap-report@2017-08-08.yang": "LMAP",
    "ietf-netconf-acm@2012-02-22.yang": "NETCONF",
    "ietf-netconf-monitoring@2010-10-04.yang": "NETCONF",
    "ietf-netconf-notifications@2012-02-06.yang": "NETCONF",
    "ietf-netconf-partial-lock@2009-10-19.yang": "NETCONF",
    "ietf-netconf-time@2016-01-26.yang": "N/A",
    "ietf-netconf-with-defaults@2011-06-01.yang": "NETCONF",
    "ietf-netconf@2011-06-01.yang": "NETCONF",
    "ietf-restconf-monitoring@2017-01-26.yang": "NETCONF",
    "ietf-restconf@2017-01-26.yang": "NETCONF",
    "ietf-routing@2016-11-04.yang": "NETMOD",
    "ietf-snmp-common@2014-12-10.yang": "NETMOD",
    "ietf-snmp-community@2014-12-10.yang": "NETMOD",
    "ietf-snmp-engine@2014-12-10.yang": "NETMOD",
    "ietf-snmp-notification@2014-12-10.yang": "NETMOD",
    "ietf-snmp-proxy@2014-12-10.yang": "NETMOD",
    "ietf-snmp-ssh@2014-12-10.yang": "NETMOD",
    "ietf-snmp-target@2014-12-10.yang": "NETMOD",
    "ietf-snmp-tls@2014-12-10.yang": "NETMOD",
    "ietf-snmp-tsm@2014-12-10.yang": "NETMOD",
    "ietf-snmp-usm@2014-12-10.yang": "NETMOD",
    "ietf-snmp-vacm@2014-12-10.yang": "NETMOD",
    "ietf-snmp@2014-12-10.yang": "NETMOD",
    "ietf-system@2014-08-06.yang": "NETMOD",
    "ietf-template@2010-05-18.yang": "NETMOD",
    "ietf-x509-cert-to-name@2014-12-10.yang": "NETMOD",
    "ietf-yang-library@2016-06-21.yang": "NETCONF",
    "ietf-yang-metadata@2016-08-05.yang": "NETMOD",
    "ietf-yang-patch@2017-02-22.yang": "NETCONF",
    "ietf-yang-smiv2@2012-06-22.yang": "NETMOD",
    "ietf-yang-types@2010-09-24.yang": "NETMOD",
    "ietf-yang-types@2013-07-15.yang": "NETMOD"
}

NS_MAP = {
    "http://cisco.com/ns/yang/": "cisco",
    "http://www.huawei.com/netconf": "huawei",
    "http://openconfig.net/yang/": "openconfig",
    "http://tail-f.com/": "tail-f"
}

github = 'https://github.com/'
github_raw = 'https://raw.githubusercontent.com/'
MISSING_ELEMENT = 'missing element'

LOGGER = log.get_logger('modules')


class Modules:
    def __init__(self, path, html_result_dir, jsons, temp_dir, is_vendor=False,
                 is_yang_lib=False, data=None, is_vendor_imp_inc=False,
                 run_integrity=False):
        self.run_integrity = run_integrity
        self.__temp_dir = temp_dir
        self.__missing_submodules = []
        self.__missing_modules = []
        self.__missing_namespace = None
        self.__missing_revision = None
        self.is_yang_lib = is_yang_lib
        self.html_result_dir = html_result_dir
        self.jsons = jsons
        self.__is_vendor = is_vendor
        self.revision = '*'
        self.__path = path
        self.features = []
        self.deviations = []

        if is_vendor:
            if is_yang_lib:
                self.deviations = data['deviations']
                self.features = data['features']
                self.revision = data['revision']
                if self.revision is None:
                    self.revision = '*'
                self.__path = self.__find_file(data['name'], self.revision)
            else:
                self.features = self.\
                    __resolve_deviations_and_features('features=', data)
                self.deviations = \
                    self.__resolve_deviations_and_features('deviations=', data)

                if 'revision' in data:
                    revision_and_more = data.split('revision=')[1]
                    revision = revision_and_more.split('&')[0]
                    self.revision = revision

                self.__path = self.__find_file(data.split('&')[0], self.revision)
        else:
            self.__path = path

        if is_vendor_imp_inc:
            self.__is_vendor = True
        if self.__path:
            self.name = None
            self.organization = None
            self.ietf_wg = None
            self.namespace = None
            self.schema = None
            self.generated_from = None
            self.maturity_level = None
            self.document_name = None
            self.author_email = None
            self.reference = None
            self.tree = None
            self.expired = None
            self.expiration_date = None
            self.module_classification = None
            self.compilation_status = None
            self.compilation_result = {}
            self.prefix = None
            self.yang_version = None
            self.description = None
            self.contact = None
            self.belongs_to = None
            self.submodule = []
            self.dependencies = []
            self.module_type = None
            self.tree_type = None
            self.semver = None
            self.derived_semver = None
            self.implementation = []
            self.imports = []
            self.json_submodules = json.dumps([])
            self.__parsed_yang = yangParser.parse(os.path.abspath(self.__path))
            if self.__parsed_yang is None:
                pass
                # TODO file has wrong format. probably end with CODE END
        else:
            raise FileError(path.split('&')[0], 'File not found')
            # TODO file does not exist

    def __resolve_deviations_and_features(self, search_for, data):
        my_list = []
        if search_for in data:
            devs_or_features = data.split(search_for)[1]
            devs_or_features = devs_or_features.split('&')[0]
            my_list = devs_or_features.split(',')
        return my_list

    def parse_all(self, name, keys, schema, to, api_sdo_json=None):
        def get_json(js):
            if js:
                return js
            else:
                return u'missing element'

        if api_sdo_json:
            author_email = api_sdo_json.get('author-email')
            maturity_level = api_sdo_json.get('maturity-level')
            reference = api_sdo_json.get('reference')
            document_name = api_sdo_json.get('document-name')
            generated_from = api_sdo_json.get('generated-from')
            organization = unicodedata.normalize('NFKD', get_json(
                api_sdo_json.get('organization'))).encode('ascii', 'ignore')
            module_classification = api_sdo_json.get('module-classification')
        else:
            author_email = None
            reference = None
            maturity_level = None
            generated_from = None
            organization = None
            module_classification = None
            document_name = None
        self.__resolve_name(name)
        self.__resolve_revision()
        self.__resolve_module_type()
        self.__resolve_belongs_to()
        self.__resolve_namespace()
        self.__resolve_organization(organization)
        key = '{}@{}/{}'.format(self.name, self.revision, self.organization)
        if key in keys:
            self.__resolve_schema(schema)
            self.__resolve_submodule()
            self.__resolve_imports()
            return
        self.__resolve_schema(schema)
        self.__resolve_submodule()
        self.__resolve_imports()
        if not self.run_integrity:
            self.__save_file(to)
            self.__resolve_generated_from(generated_from)
            self.__resolve_compilation_status_and_result()
            self.__resolve_yang_version()
            self.__resolve_prefix()
            self.__resolve_contact()
            self.__resolve_description()
            self.__resolve_document_name_and_reference(document_name, reference)
            self.__resolve_tree()
            self.__resolve_expiration()
            self.__resolve_module_classification(module_classification)
            self.__resolve_working_group()
            self.__resolve_author_email(author_email)
            self.__resolve_maturity_level(maturity_level)
            self.__resolve_semver()
            self.__resolve_tree_type()

    def __resolve_tree(self):
        if self.module_type == 'module':
            self.tree = 'services/tree/{}@{}.yang'.format(self.name,
                                                          self.revision)

    def __resolve_expiration(self):
        if self.reference and 'datatracker.ietf.org' in self.reference:
            ref = self.reference.split('/')[-1]
            url = ('https://datatracker.ietf.org/api/v1/doc/document/'
                   + ref + '/?format=json')
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.content)
                if '/api/v1/doc/state/2/' in data['states']:
                    self.expired = True
                    self.expiration_date = data['expires']

    def __save_file(self, to):
        file_with_path = '{}{}@{}.yang'.format(to, self.name, self.revision)
        if not os.path.exists(file_with_path):
            with open(self.__path, 'r') as f:
                with open(file_with_path, 'w') as f2:
                    f2.write(f.read())

    def __resolve_semver(self):
        yang_file = open(self.__path)
        for line in yang_file:
            if re.search('oc-ext:openconfig-version .*;', line):
                self.semver = re.findall('\d.\d.\d', line).pop()
        yang_file.close()

    def __resolve_imports(self):
        try:
            self.imports = self.__parsed_yang.search('import')
            if len(self.imports) == 0:
                return

            for chunk in self.imports:
                dependency = self.Dependencies()
                dependency.name = chunk.arg
                if len(chunk.search('revision-date')) > 0:
                    dependency.revision = chunk.search('revision-date')[0].arg
                if dependency.revision:
                    yang_file = self.__find_file(dependency.name,
                                                 dependency.revision)
                else:
                    yang_file = self.__find_file(dependency.name)
                if yang_file is None:
                    dependency.schema = None
                else:
                    suffix = os.path.abspath(yang_file).split('/yang/')[1]
                    prefix = self.schema.split('/yang/')[0]
                    dependency.schema = '{}/yang/master/{}'.format(prefix, suffix)
                self.dependencies.append(dependency)
        except:
            return

    def add_vendor_information(self, vendor, platform_data, software_version,
                               os_version, feature_set, os_type,
                               confarmance_type, capability, netconf_version):
        for data in platform_data:
            implementation = self.Implementations()
            implementation.vendor = vendor
            implementation.platform = data['platform']
            implementation.software_version = software_version
            implementation.software_flavor = data['software-flavor']
            implementation.os_version = os_version
            implementation.feature_set = feature_set
            implementation.os_type = os_type
            implementation.feature = self.features
            implementation.capability = capability
            implementation.netconf_version = netconf_version

            if self.is_yang_lib:
                for x in range(0, len(self.deviations['name'])):
                    devs = implementation.Deviations()
                    devs.name = self.deviations['name'][x]
                    devs.revision = self.deviations['revision'][x]
                    implementation.deviations.append(devs)
            else:
                for name in self.deviations:
                    devs = implementation.Deviations()
                    devs.name = name
                    yang_file = self.__find_file(name)
                    if yang_file is None:
                        devs.revision = '1970-01-01'
                    else:
                        try:
                            devs.revision = yangParser.parse(os.path.abspath(yang_file)) \
                                .search('revision')[0].arg
                        except:
                            devs.revision = '1970-01-01'
                    implementation.deviations.append(devs)

            implementation.conformance_type = confarmance_type
            self.implementation.append(implementation)

    def __resolve_name(self, name):
        self.name = name

    def __resolve_revision(self):
        if self.revision == '*':
            try:
                self.revision = self.__parsed_yang.search('revision')[0].arg
            except:
                self.__missing_revision = self.name
                self.revision = '1970-01-01'

    def __resolve_schema(self, schema):
        if schema:
            split_index = '/yang/'
            if '/tmp/' in self.__path:
                split_index = self.__path.split('/')[1]
            if self.__is_vendor:
                suffix = os.path.abspath(self.__path).split(split_index)[1]
                self.schema = schema + suffix
            else:
                self.schema = schema
        else:
            self.schema = None

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
                coresponding_nmda_file = self.__find_file(name_of_module,
                                                          normal_search=False)
                if coresponding_nmda_file:
                    arguments = ["pyang", "-p", get_curr_dir(__file__) + "/../../.", "-f", "tree",
                                 coresponding_nmda_file]
                    pyang = subprocess.Popen(arguments, stdout=PIPE,
                                             stderr=PIPE)
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

                            if leaf not in pyang_list_of_rows[x]:
                                return False
                    return True
                else:
                    return False
            else:
                return False

        def is_split(rows, output):
            #states = set()
            failed = False
            row_num = 0
            if output.split('\n')[0].endswith('-state'):
                return False
            for row in rows:
                if 'x--' in row or 'o--' in row:
                    continue
                if '+--rw config' == row.replace('|', '').strip(
                        ' ') or '+--ro state' == row.replace('|', '')\
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
                            #if ':' in part:
                            #    state = part.split(':')[1].split('-state')[0]
                            #else:
                            #    state = part.split('-state')[0]
                        #else:
                        #    state = \
                        #        row.strip(' ').split('-state')[0].split(' ')[1]
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
                        #states.add(state)

                row_num += 1
            #if failed:
            #    return False
#
            #for state in states:
            #    if failed:
            #        return False
            #    row_num = 0
            #    failed = True
            #    for row in rows:
            #        if 'x--' in row or 'o--' in row:
            #            continue
            #        if '+--:' in row or '+--ro' in row:
            #            continue
            #        if row.strip(' ') == '':
            #            failed = True
            #            break
            #        if (len(row.split('+--')[0]) == 4 and 'augment' not in rows[
            #                row_num - 1]) \
            #                or len(row.split('augment')[0]) == 2:
            #            if ('augment' in row and (
            #                                    ':' + state + '/' in row or '/' + state + '/' in row)) \
            #                    or ('augment' in row
            #                        and (
            #                                                    ':' + state + '-config' + '/' in row or '/' + state + '-config' + '/' in row)) \
            #                    or (state + '-config' ==
            #                            row.strip(' ').split(' ')[
            #                                1]) \
            #                    or (state == row.strip(' ').split(' ')[1]):
            #                failed = False
            #                for x in range(row_num + 1, len(rows)):
            #                    if 'x--' in rows[x] or 'o--' in rows[x]:
            #                        continue
            #                    if rows[x].strip(' ') == '' or len(
            #                            rows[x].split('+--')[0]) == 4 \
            #                            or len(row.split('augment')[0]) == 2:
            #                        break
            #                    if '+--ro' in rows[x]:
            #                        failed = True
            #                        break
            #                break
            #        row_num += 1
            if failed:
                return False
            else:
                return True

        LOGGER.debug(
            'Get tree type from tag from module {}'.format(self.__path))
        arguments = ["pyang", "-p", get_curr_dir(__file__) + "/../../.", "-f", "tree", self.__path]
        pyang = subprocess.Popen(arguments, stdout=PIPE, stderr=PIPE)
        stdout, stderr = pyang.communicate()
        if 'error' in stderr and 'is not found' in stderr:
            LOGGER.debug(
                'Could not use pyang to generate tree because of error {} on module {}'.
                    format(stderr, self.__path))
            self.tree_type = 'unclassified'
        elif stdout == '':
            self.tree_type = 'not-applicable'
        else:
            pyang_list_of_rows = stdout.split('\n')[1:]
            if 'submodule' == self.module_type:
                LOGGER.debug('Module {} is a submodule'.format(self.__path))
                self.tree_type = 'not-applicable'
            elif is_combined(pyang_list_of_rows, stdout):
                self.tree_type = 'nmda-compatible'
            elif is_transational(pyang_list_of_rows, stdout):
                self.tree_type = 'transitional-extra'
            elif is_openconfig(pyang_list_of_rows, stdout):
                self.tree_type = 'openconfig'
            elif is_split(pyang_list_of_rows, stdout):
                self.tree_type = 'split'
            else:
                self.tree_type = 'unclassified'

    def __resolve_module_classification(self, module_classification=None):
        if module_classification:
            self.module_classification = module_classification
        else:
            self.module_classification = 'unknown'

    def __resolve_maturity_level(self, maturity_level=None):
        if maturity_level:
            self.maturity_level = maturity_level
        else:
            try:
                maturity_level = \
                    self.jsons.ietf_draft_json[self.name + '.yang'][0].split(
                        '</a>')[
                        0].split('\">')[1].split('-')[1]
                if 'ietf' in maturity_level:
                    self.maturity_level = 'adopted'
                    return
                else:
                    self.maturity_level = 'initial'
                    return
            except KeyError:
                pass
            # try to find in draft with revision
            try:
                maturity_level = \
                    self.jsons.ietf_draft_json[
                        self.name + '@' + self.revision + '.yang'][0].split(
                        '</a>')[0].split('\">')[1].split(
                        '-')[1]
                if 'ietf' in maturity_level:
                    self.maturity_level = 'adopted'
                    return
                else:
                    self.maturity_level = 'initial'
                    return
            except KeyError:
                pass
            # try to find in rfc with revision
            try:
                maturity_level = self.jsons.ietf_rfc_json[
                    self.name + '@' + self.revision + '.yang']
                self.maturity_level = 'ratified'
                return
            except KeyError:
                pass
            try:
                maturity_level = self.jsons.ietf_rfc_json[self.name + '.yang']
                self.maturity_level = 'ratified'
                return
            except KeyError:
                pass
            self.maturity_level = None

    def __resolve_author_email(self, author_email=None):
        if author_email:
            self.author_email = author_email
        else:
            try:
                email = \
                    self.jsons.ietf_draft_json[self.name + '.yang'][1].split(
                        '\">Email')[0].split('mailto:')[1]
                self.author_email = email
                return
            except KeyError:
                pass
            # try to find in draft with revision
            try:
                email = \
                    self.jsons.ietf_draft_json[
                        self.name + '@' + self.revision + '.yang'][1].split(
                        '\">Email')[0].split('mailto:')[1]
                self.author_email = email
                return
            except KeyError:
                pass
            try:
                email = \
                    self.jsons.ietf_draft_example_json[self.name + '.yang'][
                        1].split(
                        '\">Email')[0].split('mailto:')[1]
                self.author_email = email
                return
            except KeyError:
                pass
            # try to find in draft with revision
            try:
                email = \
                    self.jsons.ietf_draft_example_json[
                        self.name + '@' + self.revision + '.yang'][1].split(
                        '\">Email')[0].split('mailto:')[1]
                self.author_email = email
                return
            except KeyError:
                pass
            self.author_email = None

    def __resolve_working_group(self):
        if self.organization == 'ietf':
            try:
                self.ietf_wg = \
                    self.jsons.ietf_draft_json[self.name + '.yang'][0].split(
                        '</a>')[
                        0].split('\">')[1].split('-')[2]
                return
            except KeyError:
                pass
            # try to find in draft with revision
            try:
                self.ietf_wg = \
                    self.jsons.ietf_draft_json[
                        self.name + '@' + self.revision + '.yang'][
                        0].split('</a>')[0].split('\">')[1].split('-')[2]
                return
            except KeyError:
                pass
            # try to find in ietf RFC map with revision
            try:
                self.ietf_wg = IETF_RFC_MAP[self.name + '.yang']
                return
            except KeyError:
                pass
            # try to find in ietf RFC map with revision
            try:
                self.ietf_wg = IETF_RFC_MAP[
                    self.name + '@' + self.revision + '.yang']
                return
            except KeyError:
                pass
            self.ietf_wg = None

    def __resolve_document_name_and_reference(self, document_name=None,
                                              reference=None):
        if document_name:
            self.document_name = document_name
        if reference:
            self.reference = reference

        if document_name is None and reference is None:
            self.document_name, self.reference = \
                self.__parse_document_reference()

    def __resolve_submodule(self):
        try:
            submodules = self.__parsed_yang.search('include')
        except:
            return

        if len(submodules) == 0:
            return

        for chunk in submodules:
            dep = self.Dependencies()
            sub = self.Submodules()
            sub.name = chunk.arg

            if len(chunk.search('revision-date')) > 0:
                sub.revision = chunk.search('revision-date')[0].arg

            if sub.revision:
                yang_file = self.__find_file(sub.name, sub.revision, True)
                dep.revision = sub.revision
            else:
                yang_file = self.__find_file(sub.name, submodule=True)
                try:
                    sub.revision = \
                        yangParser.parse(os.path.abspath(yang_file)).search(
                            'revision')[0].arg
                except:
                    sub.revision = '1970-01-01'
            if yang_file is None:
                LOGGER.error('Module can not be found')
                continue
            path = '/'.join(self.schema.split('/')[0:-1])
            path += '/{}'.format(yang_file.split('/')[-1])
            if yang_file:
                sub.schema = path
            dep.name = sub.name
            dep.schema = sub.schema
            self.dependencies.append(dep)
            self.submodule.append(sub)
        self.json_submodules = json.dumps([{'name': self.submodule[x].name,
                                            'schema': self.submodule[x].schema,
                                            'revision': self.submodule[
                                                x].revision
                                            } for x in
                                           range(0, len(self.submodule))])

    def __resolve_yang_version(self):
        try:
            self.yang_version = self.__parsed_yang.search('yang-version')[0].arg
        except:
            self.yang_version = '1.0'
        if self.yang_version == '1':
            self.yang_version = '1.0'

    def __resolve_generated_from(self, generated_from=None):
        if generated_from:
            self.generated_from = generated_from
        else:
            if ':smi' in self.namespace:
                self.generated_from = 'mib'
            elif 'cisco' in self.name.lower():
                self.generated_from = 'native'
            else:
                self.generated_from = 'not-applicable'

    def __resolve_compilation_status_and_result(self):
        if self.name == 'Cisco-IOS-XE-native':
            pass
        self.compilation_status = self.__parse_status()
        if self.compilation_status != 'passed':
            self.compilation_result = self.__parse_result()
            if (self.compilation_result['pyang'] == ''
                and self.compilation_result['yanglint'] == ''
                and self.compilation_result['confdrc'] == ''
                and self.compilation_result['yumadump'] == ''
                and self.organization == 'cisco'
                and (self.generated_from == 'native'
                     or self.generated_from == 'mib')):
                self.compilation_status = 'passed'
        else:
            self.compilation_result = {'pyang': '', 'pyang_lint': '',
                                       'confdrc': '', 'yumadump': '',
                                       'yanglint': ''}
        self.compilation_result = self.__create_compilation_result_file()

    def __create_compilation_result_file(self):
        if self.compilation_status == 'passed' \
                and self.compilation_result['pyang_lint'] == '':
            return ''
        else:
            result = self.compilation_result
        result['name'] = self.name
        result['revision'] = self.revision
        if self.organization == 'ietf':
            result['switch'] = '--ietf'
        else:
            result['switch'] = '--lint'
        context = {'result': result}
        rendered_html = stats.render(
            '../parseAndPopulate/template/compilationStatusTemplate.html',
            context)
        file_url = '{}@{}_{}.html'.format(self.name, self.revision,
                                          self.organization)
        with open(self.html_result_dir + file_url, 'w+') as f:
            f.write(rendered_html)
        return 'https://yangcatalog.org/results/{}'.format(file_url)

    def __resolve_contact(self):
        try:
            self.contact = self.__parsed_yang.search('contact')[0].arg
        except:
            self.contact = None

    def __resolve_description(self):
        try:
            self.description = self.__parsed_yang.search('description')[0].arg
        except:
            self.description = None

    def __resolve_namespace(self):
        self.namespace = self.__resolve_submodule_case('namespace')
        if self.namespace == MISSING_ELEMENT:
            self.__missing_namespace = self.name + ' : ' +  MISSING_ELEMENT

    def __resolve_belongs_to(self):
        if self.module_type == 'submodule':
            try:
                self.belongs_to = self.__parsed_yang.search('belongs-to')[0].arg
            except:
                self.belongs_to = None

    def __resolve_module_type(self):
        LOGGER.debug('Searching for module type')
        try:
            file_input = open(self.__path, "r")
        except:
            LOGGER.critical(
                'Could not open a file {}. Maybe a path is set wrongly'.format(
                    self.__path))
            sys.exit(10)
        all_lines = file_input.readlines()
        file_input.close()
        commented_out = False
        for each_line in all_lines:
            module_position = each_line.find('module')
            submodule_position = each_line.find('submodule')
            cpos = each_line.find('//')
            if commented_out:
                mcpos = each_line.find('*/')
            else:
                mcpos = each_line.find('/*')
            if mcpos != -1 and cpos > mcpos:
                if commented_out:
                    commented_out = False
                else:
                    commented_out = True
            if submodule_position >= 0 and (
                            submodule_position < cpos or cpos == -1) and not commented_out:
                LOGGER.debug(
                    'Module {} is of type submodule'.format(self.__path))
                self.module_type = 'submodule'
                return
            if module_position >= 0 and (
                            module_position < cpos or cpos == -1) and not commented_out:
                LOGGER.debug('Module {} is of type module'.format(self.__path))
                self.module_type = 'module'
                return
        LOGGER.error('Module {} has wrong format'.format(self.__path))
        self.module_type = None

    def __resolve_organization(self, organization=None):
        if organization:
            self.organization = organization
        else:
            for ns, org in NS_MAP.items():
                if ns in self.namespace:
                    self.organization = org
                    return
            if self.organization is None:
                if 'urn:' in self.namespace:
                    self.organization = \
                        self.namespace.split('urn:')[1].split(':')[0]
                    return
                elif 'cisco' in self.namespace:
                    self.organization = 'cisco'
                    return
            if self.organization is None:
                self.organization = 'independent'

    def __resolve_prefix(self):
        self.prefix = self.__resolve_submodule_case('prefix')

    def __resolve_submodule_case(self, field):
        if self.module_type == 'submodule':
            LOGGER.debug(
                'Getting parent information because file {} is a submodule'.format(
                    self.__path))
            yang_file = self.__find_file(self.belongs_to)
            if yang_file is None:
                return None
            parsed_parent_yang = yangParser.parse(os.path.abspath(yang_file))
            try:
                return parsed_parent_yang.search(field)[0].arg
            except:
                if field == 'prefix':
                    return None
                else:
                    return MISSING_ELEMENT
        else:
            try:
                return self.__parsed_yang.search(field)[0].arg
            except:
                if field == 'prefix':
                    return None
                else:
                    return MISSING_ELEMENT

    def __parse_status(self):
        LOGGER.debug('Parsing status of module {}'.format(self.__path))

        status = self.__get_module_status(self.jsons.ietf_draft_json, 3)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.ietf_rfc_standard_json)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.bbf_json)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.ieee_standard_json)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.ieee_experimental_json)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xr611)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xr612)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xr613)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xr621)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xr622)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xr631)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xe1631)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xe1632)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xe1641)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xe1651)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xe1661)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xe1662)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.xe1671)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703f11)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703f21)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703f22)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703f31)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703i51)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703i61)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703i52)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703i71)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.nx703i72)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.huawei8910)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.mef_experimental_json)
        if status == 'unknown':
            status = self.__get_module_status(self.jsons.openconfig_json)
        return status

    def __get_module_status(self, files_json, index=0):
        # try to find in rfc without revision
        try:
            status = files_json[self.name + '.yang'][index]
            if status == 'PASSED WITH WARNINGS':
                status = 'passed-with-warnings'
            status = status.lower()
            return status
        except:
            pass
        # try to find in draft with revision
        try:
            status = files_json[self.name + '@' + self.revision + '.yang'][
                index]
            if status == 'PASSED WITH WARNINGS':
                status = 'passed-with-warnings'
            status = status.lower()
            return status
        except:
            pass
        return 'unknown'

    def __parse_result(self):
        LOGGER.debug(
            'Parsing compulation status of module {}'.format(self.__path))
        # try to find in draft without revision
        result = {}
        try:
            result['pyang_lint'] = self.jsons.ietf_draft_json[self.name + '.yang'][4]
            result['pyang'] = \
                self.jsons.ietf_draft_json[self.name + '.yang'][
                    5]
            result['confdrc'] = self.jsons.ietf_draft_json[self.name + '.yang'][
                6]
            result['yumadump'] = \
                self.jsons.ietf_draft_json[self.name + '.yang'][7]
            result['yanglint'] = \
                self.jsons.ietf_draft_json[self.name + '.yang'][8]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result['pyang_lint'] = \
                self.jsons.ietf_draft_json[
                    self.name + '@' + self.revision + '.yang'][
                    4]
            result['pyang'] = \
                self.jsons.ietf_draft_json[
                    self.name + '@' + self.revision + '.yang'][
                    5]
            result['confdrc'] = \
                self.jsons.ietf_draft_json[
                    self.name + '@' + self.revision + '.yang'][
                    6]
            result['yumadump'] = \
                self.jsons.ietf_draft_json[
                    self.name + '@' + self.revision + '.yang'][
                    7]
            result['yanglint'] = \
                self.jsons.ietf_draft_json[
                    self.name + '@' + self.revision + '.yang'][
                    8]
            return result
        except KeyError:
            pass
        res = self.__parse_res(self.jsons.bbf_json)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.ieee_standard_json)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.ieee_experimental_json)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703i52)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703i61)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703i51)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703f21)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703f11)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703f22)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703f31)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.nx703i71)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xr621)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xr622)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xr631)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xr613)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xr612)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xr611)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xe1651)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xe1661)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xe1662)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xe1641)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xe1632)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.xe1631)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.huawei8910)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.ietf_rfc_standard_json)
        if res != '':
            return res
        res = self.__parse_res(self.jsons.openconfig_json)
        if res != '':
            return res
        return {'pyang': '', 'pyang_lint': '', 'confdrc': '', 'yumadump': '',
                'yanglint': ''}

    def __parse_res(self, json_file):
        result = {}
        try:
            result['pyang_lint'] = json_file[self.name + '.yang'][1]
            result['pyang'] = json_file[self.name + '.yang'][2]
            result['confdrc'] = json_file[self.name + '.yang'][3]
            result['yumadump'] = json_file[self.name + '.yang'][4]
            result['yanglint'] = json_file[self.name + '.yang'][5]
            return result
        except:
            pass
        # try to find in draft with revision
        try:
            result['pyang_lint'] = \
                json_file[self.name + '@' + self.revision + '.yang'][1]
            result['pyang'] = \
                json_file[self.name + '@' + self.revision + '.yang'][2]
            result['confdrc'] = \
                json_file[self.name + '@' + self.revision + '.yang'][3]
            result['yumadump'] = \
                json_file[self.name + '@' + self.revision + '.yang'][4]
            result['yanglint'] = \
                json_file[self.name + '@' + self.revision + '.yang'][5]
            return result
        except:
            pass
        return ''

    def __parse_document_reference(self):
        LOGGER.debug(
            'Parsing document reference of module {}'.format(self.__path))
        # try to find in draft without revision
        try:
            doc_name = \
                self.jsons.ietf_draft_json[self.name + '.yang'][0].split(
                    '</a>')[
                    0].split(
                    '\">')[1]
            doc_source = \
                self.jsons.ietf_draft_json[self.name + '.yang'][0].split(
                    'a href=\"')[
                    1].split('\">')[0]
            return [doc_name, doc_source]
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            doc_name = \
                self.jsons.ietf_draft_json[
                    self.name + '@' + self.revision + '.yang'][
                    0].split('</a>')[0].split('\">')[1]
            doc_source = \
                self.jsons.ietf_draft_json[
                    self.name + '@' + self.revision + '.yang'][
                    0].split('a href=\"')[1] \
                    .split('\">')[0]
            return [doc_name, doc_source]
        except KeyError:
            pass
            # try to find in rfc with revision
            try:
                doc_name = self.jsons.ietf_rfc_json[
                    self.name + '@' + self.revision + '.yang'].split('</a>')[
                    0].split('\">')[1]
                doc_source = self.jsons.ietf_rfc_json[
                    self.name + '@' + self.revision + '.yang'].split(
                    'a href=\"')[1] \
                    .split('\">')[0]
                return [doc_name, doc_source]
            except KeyError:
                pass
            try:
                doc_name = \
                    self.jsons.ietf_rfc_json[self.name + '.yang'].split('</a>')[
                        0].split(
                        '\">')[1]
                doc_source = \
                    self.jsons.ietf_rfc_json[self.name + '.yang'].split(
                        'a href=\"')[
                        1].split('\">')[0]
                return [doc_name, doc_source]
            except KeyError:
                pass
        return [None, None]

    def __find_file(self, name, revision='*', submodule=False,
                    normal_search=True):
        yang_file = find_first_file('/'.join(self.__path.split('/')[0:-1]),
                                    name + '.yang'
                                    , name + '@' + revision + '.yang')
        if yang_file is None:
            if normal_search:
                if submodule:
                    self.__missing_submodules.append(name)
                else:
                    self.__missing_modules.append(name)
            yang_file = find_first_file(get_curr_dir(__file__) + '/../../.', name + '.yang',
                                        name + '@' + revision + '.yang')
        return yang_file

    class Submodules:
        def __init__(self):
            self.name = None
            self.revision = None
            self.schema = None

    class Dependencies:
        def __init__(self):
            self.name = None
            self.revision = None

    class Implementations:
        def __init__(self):
            self.vendor = None
            self.platform = None
            self.software_version = None
            self.software_flavor = None
            self.os_version = None
            self.feature_set = None
            self.os_type = None
            self.feature = []
            self.deviations = []
            self.conformance_type = None
            self.capability = None
            self.netconf_version = None

        class Deviations:
            def __init__(self):
                self.name = None
                self.revision = None
                self.schema = None

    def resolve_integrity(self, integrity_checker, split, os_version):
        key = '/'.join(split[0:-1])
        key2 = key + '/' + split[-1]
        if self.name not in self.__missing_modules:
            integrity_checker.remove_one(key, self.__path.split('/')[-1])
        integrity_checker.add_submodule(key2, self.__missing_submodules)
        integrity_checker.add_module(key2, self.__missing_modules)
        integrity_checker.add_revision(key2, self.__missing_revision)

        if self.__missing_namespace is None:
            for ns, org in NS_MAP.items():
                if os_version is '1651':
                    if 'urn:' not in self.namespace\
                            and ns not in self.namespace:
                        self.__missing_namespace = self.name + ' : ' + self.namespace
                    else:
                        self.__missing_namespace = None
                        break
                else:
                    if (ns not in self.namespace and 'urn:' not in self.namespace)\
                            or 'urn:cisco' in self.namespace:
                        self.__missing_namespace = self.name + ' : ' + self.namespace
                    else:
                        self.__missing_namespace = None
                        break

        integrity_checker.add_namespace(key2, self.__missing_namespace)
