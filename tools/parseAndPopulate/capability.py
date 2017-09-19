from __future__ import print_function

import fileinput
import fnmatch
import json
import os
import subprocess
import unicodedata
import urllib2
import xml.etree.ElementTree as ET
from subprocess import PIPE

from numpy.f2py.auxfuncs import throw_error

import tools.utility.log as log
from tools.utility import yangParser

LOGGER = log.get_logger(__name__)

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


# searching for file based on pattern or pattern_with_revision
def find_first_file(directory, pattern, pattern_with_revision):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern_with_revision):
                filename = os.path.join(root, basename)
                return filename
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                return filename


def load_json_from_url(url):
    failed = True
    loaded_json = None
    tries = 10
    while failed:
        try:
            response = urllib2.urlopen(url).read()
            loaded_json = json.loads(response)
            failed = False
        except:
            tries -= 1
            if tries == 0:
                failed = False
            pass
    if tries == 0:
        raise throw_error('Couldn`t open a json file from url: ' + url)
    return loaded_json


def module_or_submodule(input_file):
    LOGGER.debug('Searching for module type')
    if input_file:
        file_input = open(input_file, "r")
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
            if submodule_position >= 0 and (submodule_position < cpos or cpos == -1) and not commented_out:
                LOGGER.debug('Module {} is of type submodule'.format(input_file))
                return 'submodule'
            if module_position >= 0 and (module_position < cpos or cpos == -1) and not commented_out:
                LOGGER.debug('Module {} is of type module'.format(input_file))
                return 'module'
        LOGGER.warning('Module {} has wrong format'.format(input_file))
        return 'wrong file'
    else:
        return None


def create_generated_from(namespace, module_name):
    LOGGER.debug('Get generated from tag from module {}'.format(module_name))
    if ':yang:smiv2:' in namespace:
        return 'mib'
    elif 'Cisco-IOS-XR' in module_name:
        return 'native'
    else:
        return 'not-applicable'


def get_tree_type(yang_file, is_submodule):
    if yang_file:
        LOGGER.debug('Get tree type from tag from module {}'.format(yang_file))
        arguments = ["pyang", "-p", "../../.", "-f", "tree", yang_file]
        pyang = subprocess.Popen(arguments, stdout=PIPE, stderr=PIPE)
        stdout, stderr = pyang.communicate()
        if 'error' in stderr and 'is not found' in stderr:
            LOGGER.debug('Could not use pyang to generate tree because of error {} on module {}'.
                        format(stderr, yang_file))
            return 'unclassified'
        elif stdout == '':
            return 'unclassified'
        else:
            pyang_list_of_rows = stdout.split('\n')[1:]
            if 'submodule' == is_submodule:
                LOGGER.debug('Module {} is a submodule'.format(yang_file))
                return 'not-applicable'
            elif is_combined(pyang_list_of_rows, stdout):
                return 'nmda-compatible'
            elif is_split(pyang_list_of_rows, stdout):
                return 'split'
            elif is_transational(pyang_list_of_rows, stdout):
                return 'transitional-extra'
            elif is_openconfig(pyang_list_of_rows, stdout):
                return 'openconfig'
            else:
                return 'unclassified'
    else:
        return 'unclassified'


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
            if '+--rw' in row and row_number != 0 and row_number not in skip and '[' not in row and \
                    (len(row.replace('|', '').strip(' ').split(' ')) != 2 or '(' in row):
                if '->' in row and 'config' in row.split('->')[1] and '+--rw config' not in rows[row_number - 1]:
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
                        if (len(rows[x].replace('|', '').strip(' ').split(' ')) != 2 and '[' not in rows[x]) \
                                or '+--:' in rows[x] or '(' in rows[x]:
                            length_before.add(len(rows[x].split('+--')[0]))
                        else:
                            break
                    if '+--ro' in rows[x]:
                        return False
                    duplicate = rows[x].replace('+--rw', '+--ro').split('+--')[1]
                    if duplicate.replace(' ', '') not in output.replace(' ', ''):
                        return False
                    skip.append(x)
            if '+--ro' in row and row_number != 0 and row_number not in skip and '[' not in row and \
                    (len(row.replace('|', '').strip(' ').split(' ')) != 2 or '(' in row):
                if '->' in row and 'state' in row.split('->')[1] and '+--ro state' not in rows[row_number - 1]:
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
        if '+--rw config' == row.replace('|', '').strip(' ') or '+--ro state' == row.replace('|', '').strip(' '):
            return False
        if len(row.split('+--')[0]) == 4:
            if '-state' in row and '+--ro' in row:
                return False
        if len(row.split('augment')[0]) == 2:
            part = row.strip(' ').split('/')[1]
            if '-state' in part:
                next_obsolete_or_deprecated = True
            part = row.strip(' ').split('/')[-1]
            if ':state:' in part or '/state:' in part or ':config:' in part or '/config:' in part:
                next_obsolete_or_deprecated = True
    return True


def is_transational(rows, output):
    if output.split('\n')[0].endswith('-state'):
        if '+--rw' in output:
            return False
        name_of_module = output.split('\n')[0].split(': ')[1]
        name_of_module = name_of_module.split('-state')[0]
        coresponding_nmda_file = find_first_file('../../.', name_of_module + '.yang', name_of_module + '@*.yang')
        if coresponding_nmda_file:
            arguments = ["pyang", "-p", "../../.", "-f", "tree", coresponding_nmda_file]
            pyang = subprocess.Popen(arguments, stdout=PIPE, stderr=PIPE)
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
                    leaf = rows[x].split('+--ro ')[1].split(' ')[0].split('?')[0]

                    if leaf not in pyang_list_of_rows[x]:
                        return False
            return True
        else:
            return False
    else:
        return False


def is_split(rows, output):
    states = set()
    failed = False
    row_num = 0
    if output.split('\n')[0].endswith('-state'):
        return False
    for row in rows:
        if 'x--' in row or 'o--' in row:
            continue
        if '+--rw config' == row.replace('|', '').strip(' ') or '+--ro state' == row.replace('|', '').strip(' '):
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
        if (len(row.split('+--')[0]) == 4 and 'augment' not in rows[row_num - 1]) or len(row.split('augment')[0]) == 2:
            if '-state' in row:
                if 'augment' in row:
                    part = row.strip(' ').split('/')[1]
                    if '-state' not in part:
                        row_num += 1
                        continue
                    if ':' in part:
                        state = part.split(':')[1].split('-state')[0]
                    else:
                        state = part.split('-state')[0]
                else:
                    state = row.strip(' ').split('-state')[0].split(' ')[1]
                for x in range(row_num + 1, len(rows)):
                    if 'x--' in rows[x] or 'o--' in rows[x]:
                        continue
                    if rows[x].strip(' ') == '' \
                            or (len(row.split('+--')[0]) == 4 and 'augment' not in rows[row_num - 1])\
                            or len(row.split('augment')[0]) == 2:
                        break
                    if '+--rw' in rows[x]:
                        failed = True
                        break
                states.add(state)

        row_num += 1
    if failed:
        return False

    for state in states:
        if failed:
            return False
        row_num = 0
        failed = True
        for row in rows:
            if 'x--' in row or 'o--' in row:
                continue
            if '+--:' in row:
                continue
            if row.strip(' ') == '':
                failed = True
                break
            if (len(row.split('+--')[0]) == 4 and 'augment' not in rows[row_num - 1])\
                    or len(row.split('augment')[0]) == 2:
                if ('augment' in row and (':' + state + '/' in row or '/' + state + '/' in row)) \
                        or ('augment' in row
                            and (':' + state + '-config' + '/' in row or '/' + state + '-config' + '/' in row)) \
                        or (state + '-config' == row.strip(' ').split(' ')[1]) \
                        or (state == row.strip(' ').split(' ')[1]):
                    failed = False
                    for x in range(row_num + 1, len(rows)):
                        if 'x--' in rows[x] or 'o--' in rows[x]:
                            continue
                        if rows[x].strip(' ') == '' or len(rows[x].split('+--')[0]) == 4\
                                or len(row.split('augment')[0]) == 2:
                            break
                        if '+--ro' in rows[x]:
                            failed = True
                            break
                    break
            row_num += 1
    if failed:
        return False
    else:
        return True


class Capability:
    def __init__(self, hello_message_file, index, prepare, integrity_checker, api, sdo,
                 json_dir):
        LOGGER.debug('Running constructor')
        self.json_dir = json_dir
        self.index = index
        self.prepare = prepare
        self.integrity_checker = integrity_checker
        self.parsed_yang = None
        self.api = api
        self.sdo = sdo
        # Get hello message root
        if 'xml' in hello_message_file:
            try:
                LOGGER.debug('Checking for xml hello message file')
                self.root = ET.parse(hello_message_file).getroot()
            except:
                #try to change & to &amp
                hello_file = fileinput.FileInput(hello_message_file, inplace=True)
                for line in hello_file:
                    print(line.replace('&', '&amp;'), end='')
                hello_file.close()
                LOGGER.warning('Hello message file has & instead of &amp, automatically changing to &amp')
                self.root = ET.parse(hello_message_file).getroot()
        # Split it so we can get vendor, os-type, os-version
        self.split = hello_message_file.split('/')
        self.hello_message_file = hello_message_file

        if self.api and not self.sdo:
            json_file = open(hello_message_file.split('.xml')[0] + '.json')
            impl = json.load(json_file)
            self.initialize(impl)
            json_file.close()

        if not self.api and not self.sdo:
            if os.path.isfile('/'.join(self.split[:-1]) + '/platform-metadata.json'):
                json_file = open('/'.join(self.split[:-1]) + '/platform-metadata.json')
                platforms = json.load(json_file)['platforms']
                for impl in platforms:
                    self.initialize(impl)
                json_file.close()
            else:
                LOGGER.debug('Setting metadata concerning whole directory')
                self.owner = 'YangModels'
                self.repo = 'yang'
                self.path = None
                self.branch = 'master'
                self.feature_set = 'ALL'
                self.software_version = self.split[5]#repr(165) + self.feature_set
                self.vendor = self.split[3]
                # Solve for os-type
                if 'nx' in self.split[4]:
                    self.os = 'NX-OS'
                    self.platform = self.split[6].split('-')[0]
                elif 'xe' in self.split[4]:
                    self.os = 'IOS-XE'
                    self.platform = self.split[6].split('-')[0]
                elif 'xr' in self.split[4]:
                    self.os = 'IOS-XR'
                    self.platform = self.split[6].split('-')[1]
                else:
                    self.os = 'Unknown'
                    self.platform = 'Unknown'
                self.os_version = self.split[5]
                self.software_flavor = 'ALL' #self.os + '|' + self.os_version
            integrity_checker.add_platform('/'.join(self.split[:-2]), self.platform)

        LOGGER.debug('Loading Benoit\'s compilation statuses and results')
        self.ietf_rfc_json = {}
        self.ietf_draft_json = {}
        self.ietf_draft_example_json = {}
        self.bbf_json = {}
        self.ieee_standard_json = {}
        self.ieee_experimental_json = {}
        self.ietf_rfc_standard_json = {}
        self.ietf_rfc_standard_json = load_json_from_url('http://www.claise.be/RFCStandard.json')
        self.ietf_rfc_json = load_json_from_url('http://www.claise.be/IETFYANGRFC.json')
        self.bbf_json = load_json_from_url('http://www.claise.be/BBF.json')
        self.ieee_standard_json = load_json_from_url('http://www.claise.be/IEEEStandard.json')
        self.ieee_experimental_json = load_json_from_url('http://www.claise.be/IEEEExperimental.json')
        self.ietf_draft_json = load_json_from_url('http://www.claise.be/IETFYANGDraft.json')
        self.mef_experimental_json = load_json_from_url('http://www.claise.be/MEFExperimental.json')

        self.xe1631 = ''
        if '1631' in self.split:
            self.xe1631 = load_json_from_url('http://www.claise.be/CiscoXE1631.json')
        self.xe1632 = ''
        if '1633' in self.split:
            self.xe1632 = load_json_from_url('http://www.claise.be/CiscoXE1632.json')
        self.xe1641 = ''
        if '1641' in self.split:
            self.xe1641 = load_json_from_url('http://www.claise.be/CiscoXE1641.json')
        self.xe1651 = ''
        if '1651' in self.split:
            self.xe1651 = load_json_from_url('http://www.claise.be/CiscoXE1651.json')
        self.xe1661 = ''
        if '1661' in self.split:
            self.xe1661 = load_json_from_url('http://www.claise.be/CiscoXE1661.json')

        self.xr611 = ''
        if '611' in self.split:
            self.xr611 = load_json_from_url('http://www.claise.be/CiscoXR611.json')
        self.xr612 = ''
        if '612' in self.split:
            self.xr612 = load_json_from_url('http://www.claise.be/CiscoXR612.json')
        self.xr613 = ''
        if '613' in self.split:
            self.xr613 = load_json_from_url('http://www.claise.be/CiscoXR613.json')
        self.xr621 = ''
        if '621' in self.split:
            self.xr621 = load_json_from_url('http://www.claise.be/CiscoXR621.json')

        self.nx703f11 = ''
        if '7.0-3-F1-1' in self.split:
            self.nx703f11 = load_json_from_url('http://www.claise.be/CiscoNX703F11.json')
        self.nx703f21 = ''
        if '7.0-3-F2-1' in self.split or '7.0-3-F2-2' in self.split:
            self.nx703f21 = load_json_from_url('http://www.claise.be/CiscoNX703F21.json')
        self.nx703i51 = ''
        if '7.0-3-I5-1' in self.split:
            self.nx703i51 = load_json_from_url('http://www.claise.be/CiscoNX703I51.json')
        self.nx703i52 = ''
        if '7.0-3-I5-2' in self.split:
            self.nx703i52 = load_json_from_url('http://www.claise.be/CiscoNX703I52.json')
        self.nx703i61 = ''
        if '7.0-3-I6-1' in self.split:
            self.nx703i61 = load_json_from_url('http://www.claise.be/CiscoNX703I61.json')
        self.huawei8910 = load_json_from_url('http://www.claise.be/NETWORKROUTER8910.json')

    def initialize(self, impl):
        if impl['module-list-file']['path'] in self.hello_message_file:
            LOGGER.info('Parsing a received json file')
            self.feature_set = 'ALL'
            self.os_version = impl['software-version']
            self.software_flavor = impl['software-flavor']
            self.vendor = impl['vendor']
            self.platform = impl['name']
            self.os = impl['os-type']
            self.software_version = impl['software-version']#repr(165) + self.feature_set
            self.owner = impl['module-list-file']['owner']
            self.repo = impl['module-list-file']['repository'].split('.')[0]
            self.path = impl['module-list-file']['path']
            self.branch = impl['module-list-file'].get('branch')
            if not self.branch:
                self.branch = 'master'

    def handle_exception(self, field, object, module_name):
        LOGGER.debug('field {} was not found in module {}'.format(field, module_name))
        # In case of include exception create empty
        if 'include' in field:
            names = []
            revs = []
            incl = {'name': names, 'revision': revs}
            object[module_name] = incl
        # In case of revision exception create dummy revision -> '1970-01-01'
        elif 'revision' in field:
            object[module_name] = '1970-01-01'
            self.integrity_checker.add_revision(self.split, module_name)
        # In case of yang-version exception create version 1.0 because
        # if yang doesn`t contain any version value it is 1.0 by default
        elif 'yang-version' in field:
            object[module_name] = '1.0'
        # In case of namespace exception create dummy exception -> 'urn:dummy'
        elif 'namespace' in field:
            object[module_name] = MISSING_ELEMENT
        # For everything else insert null value
        elif 'import' in field:
            object[module_name] = None
        elif 'feature' in field:
            object[module_name] = MISSING_ELEMENT
        elif 'compilation-status' in field:
            object[module_name] = 'unknown'
        else:
            object[module_name] = MISSING_ELEMENT

    # pyang parsing variables and saving field value
    def find_yang_var(self, object, field, module_name, yang_file):
        LOGGER.debug('Searching for field {} in module {}'.format(field, module_name))
        try:
            # In case it is import, include or feature there might be more than one object
            if 'import' in field or 'include' in field or 'feature' in field:
                # If this yang is not yet found and parsed
                if self.parsed_yang is None:
                    # Find and Parse yang file
                    self.parsed_yang = yangParser.parse(os.path.abspath(yang_file))
                object[module_name] = []
                names = []
                revs = []
                incl = {}

                # Search for the field in yang file
                for chunk in self.parsed_yang.search(field):
                    # If it is included parse it to name and revision
                    if 'include' in field:
                        names.append(chunk.arg)
                        if len(chunk.search('revision-date')) > 0:
                            revs.append(chunk.search('revision-date')[0].arg)
                    # Otherwise add object
                    else:
                        object[module_name].append(chunk.arg)
                if 'include' in field:
                    incl['name'] = names
                    incl['revision'] = revs
                    object[module_name] = incl
            else:
                # If this yang is not yet found and parsed
                if self.parsed_yang is None:
                    # Find and Parse yang file
                    self.parsed_yang = yangParser.parse(os.path.abspath(yang_file))

                # Search for the field and parse first one you find (in case of revision
                # we want just first one which is the newest one)
                yang_variable = self.parsed_yang.search(field)[0].arg
                if yang_variable == '1' and field == 'yang-version':
                    yang_variable = '1.0'

                if isinstance(yang_variable, unicode):
                    object[module_name] = unicodedata.normalize('NFKD', yang_variable).encode('ascii', 'ignore')
                else:
                    object[module_name] = yang_variable

        # In case of exception handle them
        except AttributeError:
            self.handle_exception(field, object, module_name)
        except IndexError:
            self.handle_exception(field, object, module_name)
        except UnicodeDecodeError:
            self.handle_exception(field, object, module_name)

    @staticmethod
    def get_json(js):
        if js:
            return js
        else:
            return u'missing element'

    def parse_and_dump_sdo(self):
        if self.api:
            LOGGER.debug('Parsing sdo files sent via API')
            with open('../parseAndPopulate/' + self.json_dir + '/prepare-sdo.json', 'r') as f:
                sdos_json = json.load(f)
            sdos_list = sdos_json['modules']['module']
            for sdo in sdos_list:
                file_name = unicodedata.normalize('NFKD', sdo['source-file']['path'].split('/')[-1])\
                    .encode('ascii', 'ignore')
                LOGGER.info('Parsing sdo file sent via API{}'.format(file_name))
                self.owner = sdo['source-file']['owner']
                repo_file_path = sdo['source-file']['path']
                self.branch = sdo['source-file'].get('branch')
                if not self.branch:
                    self.branch = 'master'
                self.repo = sdo['source-file']['repository'].split('.')[0]
                root = self.owner + '/' + sdo['source-file']['repository'].split('.')[0] + '/' + self.branch + '/'\
                    + '/'.join(repo_file_path.split('/')[:-1])
                root = self.json_dir + '/temp/'\
                    + unicodedata.normalize('NFKD', root).encode('ascii', 'ignore')
                if not os.path.isfile(root + '/' + file_name):
                    LOGGER.error('File {} sent via API was not downloaded'.format(file_name))
                    continue
                self.parsed_yang = None
                prefix = {}
                yang_version = {}
                contact = {}
                includes = {}
                imports = {}
                description = {}
                revision = {}
                namespace = {}
                features = {}
                belongs_to = {}
                LOGGER.debug('Parsing extractable metadata from file {}'.format(file_name))
                module_submodule = module_or_submodule(root + '/' + file_name)
                tree_type = get_tree_type(root + '/' + file_name, module_submodule)
                if '[1]' in file_name:
                    LOGGER.warning('File {} contains invalid character [1] in file name'.format(file_name))
                    module_submodule = 'wrong file'
                if module_submodule != 'wrong file':
                    conformance_type = None
                    schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' + repo_file_path
                    self.find_yang_var(yang_version, 'yang-version', file_name, root + '/' + file_name)
                    self.find_yang_var(contact, 'contact', file_name, root + '/' + file_name)
                    self.find_yang_var(description, 'description', file_name, root + '/' + file_name)
                    self.find_yang_var(includes, 'include', file_name, root + '/' + file_name)
                    self.find_yang_var(imports, 'import', file_name, root + '/' + file_name)
                    self.find_yang_var(features, 'feature', file_name, root + '/' + file_name)
                    self.find_yang_var(revision, 'revision', file_name, root + '/' + file_name)
                    compilations_status = self.parse_status(file_name, revision[file_name])

                    if compilations_status != 'passed':
                        compilations_result = self.parse_result(file_name, revision[file_name])
                    else:
                        compilations_result = ''
                    LOGGER.debug('Getting non-extractable metadata from file {}'.format(file_name))
                    author_email = unicodedata.normalize('NFKD', self.get_json(sdo.get('author-email')))\
                        .encode('ascii', 'ignore')
                    if author_email == MISSING_ELEMENT:
                        author_email = None
                    working_group = unicodedata.normalize('NFKD', self.get_json(sdo.get('maturity-level')))\
                        .encode('ascii', 'ignore')
                    reference = unicodedata.normalize('NFKD', self.get_json(sdo.get('reference')))\
                        .encode('ascii', 'ignore')
                    document_name = unicodedata.normalize('NFKD', self.get_json(sdo.get('document-name')))\
                        .encode('ascii', 'ignore')
                    generated_from = sdo.get('generated-from')
                    module_classification = sdo.get('module-classification')
                    if module_classification is None:
                        module_classification = 'unknown'
                    if module_submodule == 'submodule':
                        LOGGER.debug('Getting parent information because file {} is a submodule'.format(file_name))

                        self.find_yang_var(belongs_to, 'belongs-to', file_name, root + '/' + file_name)
                        yang_file = find_first_file('/'.join(self.split[0:-1]), belongs_to[file_name] + '.yang'
                                                    , belongs_to[file_name] + '@*.yang')
                        self.parsed_yang = None
                        self.find_yang_var(namespace, 'namespace', file_name, yang_file)
                        self.find_yang_var(prefix, 'prefix', file_name, yang_file)
                        self.parsed_yang = None
                    else:
                        belongs_to[file_name] = None
                        self.find_yang_var(namespace, 'namespace', file_name, root + '/' + file_name)
                        self.find_yang_var(prefix, 'prefix', file_name, root + '/' + file_name)

                    if generated_from is None:
                        generated_from = create_generated_from(namespace.get(file_name), file_name)
                    organization = unicodedata.normalize('NFKD', self.get_json(sdo.get('organization'))) \
                        .encode('ascii', 'ignore')
                    name = file_name.split('.')[0]
                    self.prepare.add_key_sdo(name + '@' + revision.get(file_name) + ',' + organization,
                                             namespace.get(file_name),
                                             conformance_type, reference, prefix.get(file_name),
                                             yang_version.get(file_name), organization,
                                             description.get(file_name), contact.get(file_name), schema,
                                             features.get(file_name),
                                             self.get_submodule_info(includes.get(file_name)['name']),
                                             compilations_status, author_email, working_group, compilations_result,
                                             module_submodule, document_name, generated_from, None, tree_type,
                                             module_classification, belongs_to.get(file_name))

        else:
            LOGGER.debug('Parsing sdo files from directory')
            for root, subdirs, sdos in os.walk('/'.join(self.split)):
                for file_name in sdos:
                    if '.yang' in file_name and ('vendor' not in root or 'odp' not in root):
                        LOGGER.info('Parsing sdo file from directory {}'.format(file_name))
                        self.parsed_yang = None
                        prefix = {}
                        yang_version = {}
                        organization = {}
                        contact = {}
                        includes = {}
                        imports = {}
                        description = {}
                        revision = {}
                        namespace = {}
                        features = {}
                        belongs_to = {}
                        LOGGER.debug('Parsing extractable metadata from file {}'.format(file_name))
                        module_submodule = module_or_submodule(root + '/' + file_name)
                        tree_type = get_tree_type(root + '/' + file_name, module_submodule)
                        if '[1]' in file_name:
                            LOGGER.warning('File {} contains [1] it its file name'.format(file_name))
                            module_submodule = 'wrong file'
                        if module_submodule != 'wrong file':
                            self.owner = 'YangModels'
                            self.repo = 'yang'
                            self.branch = 'master'
                            path = root + '/' + file_name
                            schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' + path.replace('../', '')
                            conformance_type = None

                            self.find_yang_var(yang_version, 'yang-version', file_name, root + '/' + file_name)
                            self.find_yang_var(contact, 'contact', file_name, root + '/' + file_name)
                            self.find_yang_var(description, 'description', file_name, root + '/' + file_name)
                            self.find_yang_var(includes, 'include', file_name, root + '/' + file_name)
                            self.find_yang_var(imports, 'import', file_name, root + '/' + file_name)
                            self.find_yang_var(revision, 'revision', file_name, root + '/' + file_name)
                            self.find_yang_var(features, 'feature', file_name, root + '/' + file_name)

                            compilations_status = self.parse_status(file_name, revision[file_name])
                            if compilations_status != 'passed':
                                compilations_result = self.parse_result(file_name, revision[file_name])
                            else:
                                compilations_result = ''
                            LOGGER.debug('Getting non-extractable metadata from file {}'.format(file_name))
                            author_email = self.parse_email(file_name, revision[file_name])
                            working_group = self.parse_maturityLevel(file_name, revision[file_name])

                            doc_name_reference = self.parse_document_reference(file_name, revision[file_name])
                            reference = doc_name_reference[1]
                            document_name = doc_name_reference[0]

                            if module_submodule == 'submodule':
                                LOGGER.debug(
                                    'Getting parent information because file {} is a submodule'.format(file_name))
                                self.find_yang_var(belongs_to, 'belongs-to', file_name, root + '/' + file_name)
                                yang_file = find_first_file('/'.join(self.split[0:-1]), belongs_to[file_name] + '.yang'
                                                            , belongs_to[file_name] + '@*.yang')
                                self.parsed_yang = None
                                self.find_yang_var(namespace, 'namespace', file_name, yang_file)
                                self.find_yang_var(prefix, 'prefix', file_name, yang_file)
                                self.parsed_yang = None
                            else:
                                belongs_to[file_name] = None
                                self.find_yang_var(namespace, 'namespace', file_name, root + '/' + file_name)
                                self.find_yang_var(prefix, 'prefix', file_name, root + '/' + file_name)
                            generated_from = create_generated_from(namespace.get(file_name), file_name)
                            for ns, org in NS_MAP.items():
                                if ns in namespace[file_name]:
                                    organization[file_name] = org
                            if organization.get(file_name) is None:
                                if 'urn:' in namespace[file_name]:
                                    organization[file_name] = namespace[file_name].split('urn:')[1].split(':')[0]
                                elif 'cisco' in namespace[file_name]:
                                    organization[file_name] = 'cisco'
                            if organization.get(file_name) is None:
                                organization[file_name] = MISSING_ELEMENT
                            if organization.get(file_name) == 'ietf':
                                wg = self.parse_wg(file_name, revision[file_name])
                            else:
                                wg = None
                            name = file_name.split('.')[0]
                            self.prepare.add_key_sdo(name + '@' + revision.get(file_name) +
                                                     ',' + repr(organization.get(file_name)),
                                                     namespace.get(file_name), conformance_type, reference,
                                                     prefix.get(file_name), yang_version.get(file_name),
                                                     organization.get(file_name), description.get(file_name),
                                                     contact.get(file_name), schema, features.get(file_name),
                                                     self.get_submodule_info(includes.get(file_name)['name']),
                                                     compilations_status, author_email, working_group,
                                                     compilations_result, module_submodule, document_name,
                                                     generated_from, wg, tree_type, 'unknown',
                                                     belongs_to.get(file_name))

    # parse capability xml and save to file
    def parse_and_dump_yang_lib(self):
        LOGGER.debug('Starting to parse files from vendor')
        capability = []
        module_names = []
        name_revision = []
        deviations = {}
        features = {}
        revision = {}
        yang_version = {}
        namespace = {}
        prefix = {}
        organization = {}
        contact = {}
        description = {}
        includes = {}
        imports = {}
        conformance_type = {}
        compilations_status = {}
        working_group = {}
        author_email = {}
        netconf_version = ''
        compilations_result = {}
        organization_module = {}
        belongs_to = {}

        # netconf capability parsing
        modules = self.root[0]
        for module in modules:
            if 'module-set-id' in module.tag:
                continue
            LOGGER.debug('Getting capabilities out of yang-library xml message')
            module_name = None
            for mod in module:
                if 'name' in mod.tag:
                    module_name = mod.text
                    module_names.append(module_name)
                    break
            feature_names = []
            LOGGER.info('Starting to parse {}'.format(module_name))
            names = []
            revs = []
            for mod in module:
                if 'revision' in mod.tag:
                    revision[module_name] = mod.text
                elif 'conformance-type' in mod.tag:
                    conformance_type[module_name] = mod.text
                elif 'feature' in mod.tag:
                    feature_names.append(mod.text)
                elif 'deviation' in mod.tag:
                    names.append(mod[0].text)
                    revs.append(mod[1].text)
            features[module_name] = feature_names

            devs = {}

            # Parse deviations of the module
            devs['name'] = names
            devs['revision'] = revs
            if len(devs['name']) == 0:
                deviations[module_name] = None
            else:
                deviations[module_name] = devs

            # Parse revision of the module from capability.xml file
            my_var = revision[module_name]
            if my_var is None:
                my_var = ''
                yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
                                            module_name + '.yang')
                self.find_yang_var(revision, 'revision', module_name, yang_file)
            name_revision.append(module_name + '@' + revision[module_name])
            # Find yang file in the same directory as capability.xml file is
            # so we can parse all needed fields out of it

            yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
                                        module_name + '@' + my_var + '.yang')

            if yang_file is None:
                # In case we didn`t find the module try to look for it in any other directory of this project
                self.integrity_checker.add_module(self.split, module_name)
                yang_file = find_first_file('/'.join(self.split[0:1]), module_name + '.yang',
                                            module_name + '@' + my_var + '.yang')
            if yang_file is not None:
                self.integrity_checker.remove_one(self.split, yang_file)
            self.parsed_yang = None
            namespace_exist = False
            # Parse rest of the fields out of the yang file
            self.find_yang_var(namespace, 'namespace', module_name, yang_file)
            LOGGER.debug('Parsing organization for module {}'.format(module_name))
            for ns, org in NS_MAP.items():
                if self.os_version is '1651':
                    if 'urn:cisco' in namespace[module_name]:
                        if ns in namespace[module_name]:
                            organization_module[module_name] = org
                            namespace_exist = True
                else:
                    if ns in namespace[module_name]:
                        organization_module[module_name] = org
                        namespace_exist = True
            if organization_module.get(module_name) is None:
                if 'urn:' in namespace[module_name]:
                    organization_module[module_name] = namespace[module_name].split('urn:')[1].split(':')[0]
                    namespace_exist = True
                elif 'cisco' in namespace[module_name]:
                    organization_module[module_name] = 'cisco'

            if not namespace_exist:
                if organization_module.get(module_name) is None:
                    organization_module[module_name] = MISSING_ELEMENT
                if namespace[module_name] is None or namespace[module_name] == MISSING_ELEMENT:
                    self.integrity_checker.add_namespace(self.split,
                                                         module_name + ' : missing data')

            module_submodule = module_or_submodule(yang_file)
            LOGGER.debug('Parsing extractable fields')
            self.find_yang_var(prefix, 'prefix', module_name, yang_file)
            self.find_yang_var(yang_version, 'yang-version', module_name, yang_file)
            if 'urn:ietf:' in namespace:
                organization[module_name] = 'ietf'
            else:
                self.find_yang_var(organization, 'organization', module_name, yang_file)
            self.find_yang_var(contact, 'contact', module_name, yang_file)
            self.find_yang_var(description, 'description', module_name, yang_file)
            self.find_yang_var(includes, 'include', module_name, yang_file)
            self.find_yang_var(imports, 'import', module_name, yang_file)
            belongs_to[module_name] = None
            tree_type = get_tree_type(yang_file, module_submodule)
            reference = MISSING_ELEMENT
            document_name = MISSING_ELEMENT
            compilations_status[module_name] = self.parse_status(module_name,
                                                                 revision[module_name])
            if compilations_status[module_name] != 'passed':
                compilations_result[module_name] = self.parse_result(module_name,
                                                                     revision[module_name])
            else:
                compilations_result[module_name] = ''
            author_email[module_name] = self.parse_email(module_name, revision[module_name])
            working_group[module_name] = self.parse_maturityLevel(module_name,
                                                                  revision[module_name])
            if organization_module[module_name] == 'ietf':
                wg = self.parse_wg(module_name, revision[module_name])
            else:
                wg = None

            if yang_file:
                if self.api:
                    schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' + \
                             '/'.join(yang_file.split('/')[2:])
                else:
                    schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' \
                             + '/'.join(yang_file.split('/')[2:])
            else:
                schema = None
            self.prepare.add_key(
                module_name + '@' + revision[module_name] + ',' + organization_module[
                    module_name],
                namespace[module_name],
                conformance_type[module_name], self.vendor, self.platform,
                self.software_version,
                self.software_flavor, self.os, self.os_version, self.feature_set,
                reference, prefix[module_name], yang_version[module_name],
                # changed organization[module_name] for organization_module
                organization_module[module_name], description[module_name],
                contact[module_name],
                compilations_status[module_name], author_email[module_name], schema,
                features[module_name], working_group[module_name],
                compilations_result[module_name], deviations[module_name],
                self.get_submodule_info(includes[module_name]['name']), module_submodule,
                document_name,
                create_generated_from(namespace[module_name], module_name), wg, tree_type,
                'unknown', belongs_to[module_name])

            self.parse_imports_includes(includes[module_name]['name'], features, revision,
                                        name_revision,
                                        yang_version, namespace, prefix, organization, contact,
                                        description,
                                        includes, imports, conformance_type, deviations,
                                        module_names,
                                        compilations_status, author_email, working_group,
                                        organization_module, True, module_name,
                                        compilations_result, belongs_to)
            self.parse_imports_includes(imports[module_name], features, revision, name_revision,
                                        yang_version, namespace, prefix, organization, contact,
                                        description,
                                        includes, imports, conformance_type, deviations,
                                        module_names,
                                        compilations_status, author_email, working_group,
                                        organization_module, False, module_name,
                                        compilations_result, belongs_to)

        # restconf capability parsing
        # for module in self.root.iter('module'):
        #    module_name = module.find('name').text
        #    module_names.append(module_name)
        #    namespace[module_name] = module.find('namespace').text
        #    revision[module_name] = module.find('revision').text
        #    #schema[module_name] = module.find('schema').text`
        #    conformance_type[module_name] = module.find('conformance-type').text
        #    devs = {}
        #    names = []
        #    revs = []
        #    for dev in self.root.iter('deviation'):
        #        names.append(dev.find('name').text)
        #        if dev.find('revision').text is None:
        #            revs.append('1970-01-01')
        #        else:
        #            revs.append(dev.find('revision').text)
        #    devs['name'] = names
        #    devs['revision'] = revs
        #    deviations[module_name] = devs
        #    objs = []
        #    for feat in self.root.iter('feature'):
        #        objs.append(feat.text)
        #    features[module_name] = objs

        #    # Find yang file in the same directory as capability.xml file is
        #    # so we can parse all needed fields out of it
        #    yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
        #                                module_name + '@' + revision[module_name] + '.yang')

        #    if yang_file is None:
        #        # In case we didn`t find the module try to look for it in any other directory of this project
        #        self.integrity_checker.add_module(self.split, module_name)
        #        yang_file = find_first_file('/'.join(self.split[0:2]), module_name + '.yang',
        #                                    module_name + '@' + revision[module_name] + '.yang')

        #    # Parse rest of the fields out of the yang file
        #    self.find_yang_var(prefix, 'prefix', module_name, yang_file)
        #    self.find_yang_var(yang_version, 'yang-version', module_name, yang_file)
        #    self.find_yang_var(organization, 'organization', module_name, yang_file)
        #    self.find_yang_var(contact, 'contact', module_name, yang_file)
        #    self.find_yang_var(description, 'description', module_name, yang_file)
        #    self.find_yang_var(reference, 'reference', module_name, yang_file)
        #    self.find_yang_var(includes, 'include', module_name, yang_file)
        #    self.find_yang_var(imports, 'import', module_name, yang_file)

        self.integrity_checker.add_unique(name_revision)
        # Write dictionary to file
        # Create json dictionary out of parsed information
        LOGGER.debug('Creating normal.json file for vendors branch')
        with open('./' + self.json_dir + '/normal' + repr(self.index) + '.json', "w") as ietf_model:
            json.dump({
                'vendors': {
                    'vendor': [{
                        'name': self.vendor,
                        'platforms': {
                            'platform': [{
                                'name': self.platform,
                                'software-versions': {
                                    'software-version': [{
                                        'name': self.software_version,
                                        'software-flavors': {
                                            'software-flavor': [{
                                                'name': self.software_flavor,
                                                'protocols': {
                                                    'protocol': [{
                                                        'name': 'netconf',
                                                        'capabilities': capability,
                                                        'protocol-version': netconf_version,
                                                    }]
                                                },
                                                'modules': {
                                                    'module': [{
                                                        'name': module_names[k],
                                                        'revision': revision.get(module_names[k]),
                                                        'organization': organization_module.get(
                                                            module_names[k]),
                                                        'os-version': self.os_version,
                                                        'feature-set': self.feature_set,
                                                        'os-type': self.os,
                                                        'feature': features.get(module_names[k]),
                                                        'deviation': self.get_deviations(deviations,
                                                                                         module_names[
                                                                                             k]),
                                                        'conformance-type': conformance_type.get(
                                                            module_names[k])
                                                    } for k, val in enumerate(module_names)],
                                                }
                                            }]
                                        }
                                    }]
                                }
                            }]
                        }
                    }]
                }
            }, ietf_model)
            # pool = ThreadPool(1)
            # pool.map(nieco, modules)
            # pool.close()
            # pool.join()

    # parse capability xml and save to file
    def parse_and_dump(self):
        LOGGER.debug('Starting to parse files from vendor')
        capability = []
        tag = self.root.tag
        module_names = []
        name_revision = []
        deviations = {}
        features = {}
        revision = {}
        yang_version = {}
        namespace = {}
        prefix = {}
        organization = {}
        contact = {}
        description = {}
        includes = {}
        imports = {}
        conformance_type = {}
        compilations_status = {}
        working_group = {}
        author_email = {}
        netconf_version = ''
        compilations_result = {}
        organization_module = {}
        belongs_to = {}

        # Parse deviations and features from each module from netconf hello message
        def deviations_and_features(search_for):
            my_list = []
            if search_for in module_and_more:
                devs_or_features = module_and_more.split(search_for)[1]
                devs_or_features = devs_or_features.split('&')[0]
                my_list = devs_or_features.split(',')
            return my_list

        # netconf capability parsing
        modules = self.root.iter(tag.split('hello')[0] + 'capability')
        for module in modules:
        #def nieco(module):
            LOGGER.debug('Getting capabilities out of hello message')
            # Parse netconf version
            if ':netconf:base:' in module.text:
                netconf_version = module.text
                LOGGER.debug('Getting netconf version')
            # Parse capability together with version
            if ':capability:' in module.text:
                cap_with_version = module.text.split(':capability:')[1]
                capability.append(cap_with_version.split('?')[0])
                LOGGER.debug('Getting capabilities out of hello message')
            # Parse modules
            if 'module=' in module.text:
                # Parse name of the module
                module_and_more = module.text.split('module=')[1]
                module_name = module_and_more.split('&')[0]
                module_names.append(module_name)
                LOGGER.info('Starting to parse module {}'.format(module_name))
                devs = {}
                revs = []
                # Parse deviations of the module
                names = deviations_and_features('deviations=')
                # Find and parse deviated yang file so we can get a revision out of it
                for i in names:
                    yang_file = find_first_file('/'.join(self.split[0:-1]), i + '.yang',
                                                i + '.yang')
                    if yang_file is None:
                        self.integrity_checker.add_module(self.split, i)
                        revs.append('1970-01-01')
                    else:
                        self.parsed_yang = yangParser.parse(os.path.abspath(yang_file))
                        yang_variable = self.parsed_yang.search('revision')[0].arg

                        if isinstance(yang_variable, unicode):
                            revs.append(unicodedata.normalize('NFKD', yang_variable).encode('ascii', 'ignore'))
                        else:
                            revs.append(yang_variable)
                    if yang_file is not None:
                        self.integrity_checker.remove_one(self.split, yang_file)
                devs['name'] = names
                devs['revision'] = revs
                if len(devs['name']) == 0:
                    deviations[module_name] = None
                else:
                    deviations[module_name] = devs

                # Parse features of the module
                features[module_name] = deviations_and_features('features=')
                # Parse conformance type of the module
                conformance_type[module_name] = 'implement'

                # Parse revision of the module from capability.xml file
                my_var = ''
                if 'revision' in module.text:
                    revision_and_more = module.text.split('revision=')[1]
                    my_var = revision_and_more.split('&')[0]
                    revision[module_name] = my_var
                else:
                    yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
                                                module_name + '.yang')
                    self.find_yang_var(revision, 'revision', module_name, yang_file)
                name_revision.append(module_name + '@' + revision[module_name])
                # Find yang file in the same directory as capability.xml file is
                # so we can parse all needed fields out of it

                yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
                                            module_name + '@' + my_var + '.yang')

                if yang_file is None:
                    # In case we didn`t find the module try to look for it in any other directory of this project
                    self.integrity_checker.add_module(self.split, module_name)
                    yang_file = find_first_file('/'.join(self.split[0:1]), module_name + '.yang',
                                                module_name + '@' + my_var + '.yang')
                if yang_file is not None:
                    self.integrity_checker.remove_one(self.split, yang_file)
                self.parsed_yang = None
                namespace_exist = False
                # Parse rest of the fields out of the yang file
                self.find_yang_var(namespace, 'namespace', module_name, yang_file)
                LOGGER.debug('Parsing organization for module {}'.format(module_name))
                for ns, org in NS_MAP.items():
                    if self.os_version is '1651':
                        if 'urn:cisco' in namespace[module_name]:
                            if ns in namespace[module_name]:
                                organization_module[module_name] = 'cisco'
                                namespace_exist = True
                    else:
                        if ns in namespace[module_name]:
                            organization_module[module_name] = org
                            namespace_exist = True
                if organization_module.get(module_name) is None:
                    if 'urn:' in namespace[module_name]:
                        organization_module[module_name] = namespace[module_name].split('urn:')[1].split(':')[0]
                        namespace_exist = True
                    elif 'cisco' in namespace[module_name]:
                        organization_module[module_name] = 'cisco'
                if not namespace_exist:
                    if organization_module.get(module_name) is None:
                        organization_module[module_name] = MISSING_ELEMENT
                    if namespace[module_name] is None or namespace[module_name] == MISSING_ELEMENT:
                        self.integrity_checker.add_namespace(self.split, module_name + ' : ' + namespace[module_name])

                module_submodule = module_or_submodule(yang_file)
                LOGGER.debug('Parsing extractable fields')
                self.find_yang_var(prefix, 'prefix', module_name, yang_file)
                self.find_yang_var(yang_version, 'yang-version', module_name, yang_file)
                if 'urn:ietf:' in namespace:
                    organization[module_name] = 'ietf'
                else:
                    self.find_yang_var(organization, 'organization', module_name, yang_file)
                self.find_yang_var(contact, 'contact', module_name, yang_file)
                self.find_yang_var(description, 'description', module_name, yang_file)
                self.find_yang_var(includes, 'include', module_name, yang_file)
                self.find_yang_var(imports, 'import', module_name, yang_file)
                belongs_to[module_name] = None
                tree_type = get_tree_type(yang_file, module_submodule)
                reference = MISSING_ELEMENT
                document_name = MISSING_ELEMENT
                compilations_status[module_name] = self.parse_status(module_name, revision[module_name])
                if compilations_status[module_name] != 'passed':
                    compilations_result[module_name] = self.parse_result(module_name, revision[module_name])
                else:
                    compilations_result[module_name] = ''
                author_email[module_name] = self.parse_email(module_name, revision[module_name])
                working_group[module_name] = self.parse_maturityLevel(module_name, revision[module_name])
                if organization_module[module_name] == 'ietf':
                    wg = self.parse_wg(module_name, revision[module_name])
                else:
                    wg = None

                if yang_file:
                    if self.api:
                        schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' +\
                                 '/'.join(yang_file.split('/')[2:])
                    else:
                        schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' \
                                 + '/'.join(yang_file.split('/')[2:])
                else:
                    schema = None
                self.prepare.add_key(module_name + '@' + revision[module_name] + ',' + organization_module[module_name],
                                     namespace[module_name],
                                     conformance_type[module_name], self.vendor, self.platform, self.software_version,
                                     self.software_flavor, self.os, self.os_version, self.feature_set,
                                     reference, prefix[module_name], yang_version[module_name],# changed organization[module_name] for organization_module
                                     organization_module[module_name], description[module_name], contact[module_name],
                                     compilations_status[module_name], author_email[module_name], schema,
                                     features[module_name], working_group[module_name],
                                     compilations_result[module_name], deviations[module_name],
                                     self.get_submodule_info(includes[module_name]['name']), module_submodule,
                                     document_name,
                                     create_generated_from(namespace[module_name], module_name), wg, tree_type,
                                     'unknown', belongs_to[module_name])

                self.parse_imports_includes(includes[module_name]['name'], features, revision, name_revision,
                                            yang_version, namespace, prefix, organization, contact, description,
                                            includes, imports, conformance_type, deviations, module_names,
                                            compilations_status, author_email, working_group,
                                            organization_module, True, module_name, compilations_result, belongs_to)
                self.parse_imports_includes(imports[module_name], features, revision, name_revision,
                                            yang_version, namespace, prefix, organization, contact, description,
                                            includes, imports, conformance_type, deviations, module_names,
                                            compilations_status, author_email, working_group,
                                            organization_module, False, module_name, compilations_result, belongs_to)

        # restconf capability parsing
        #for module in self.root.iter('module'):
        #    module_name = module.find('name').text
        #    module_names.append(module_name)
        #    namespace[module_name] = module.find('namespace').text
        #    revision[module_name] = module.find('revision').text
        #    #schema[module_name] = module.find('schema').text`
        #    conformance_type[module_name] = module.find('conformance-type').text
        #    devs = {}
        #    names = []
        #    revs = []
        #    for dev in self.root.iter('deviation'):
        #        names.append(dev.find('name').text)
        #        if dev.find('revision').text is None:
        #            revs.append('1970-01-01')
        #        else:
        #            revs.append(dev.find('revision').text)
        #    devs['name'] = names
        #    devs['revision'] = revs
        #    deviations[module_name] = devs
        #    objs = []
        #    for feat in self.root.iter('feature'):
        #        objs.append(feat.text)
        #    features[module_name] = objs

        #    # Find yang file in the same directory as capability.xml file is
        #    # so we can parse all needed fields out of it
        #    yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
        #                                module_name + '@' + revision[module_name] + '.yang')

        #    if yang_file is None:
        #        # In case we didn`t find the module try to look for it in any other directory of this project
        #        self.integrity_checker.add_module(self.split, module_name)
        #        yang_file = find_first_file('/'.join(self.split[0:2]), module_name + '.yang',
        #                                    module_name + '@' + revision[module_name] + '.yang')

        #    # Parse rest of the fields out of the yang file
        #    self.find_yang_var(prefix, 'prefix', module_name, yang_file)
        #    self.find_yang_var(yang_version, 'yang-version', module_name, yang_file)
        #    self.find_yang_var(organization, 'organization', module_name, yang_file)
        #    self.find_yang_var(contact, 'contact', module_name, yang_file)
        #    self.find_yang_var(description, 'description', module_name, yang_file)
        #    self.find_yang_var(reference, 'reference', module_name, yang_file)
        #    self.find_yang_var(includes, 'include', module_name, yang_file)
        #    self.find_yang_var(imports, 'import', module_name, yang_file)

        self.integrity_checker.add_unique(name_revision)
        # Write dictionary to file
        # Create json dictionary out of parsed information
        LOGGER.debug('Creating normal.json file for vendors branch')
        with open('./' + self.json_dir + '/normal' + repr(self.index) + '.json', "w") as ietf_model:
            json.dump({
                'vendors': {
                    'vendor': [{
                        'name': self.vendor,
                        'platforms': {
                            'platform': [{
                                'name': self.platform,
                                'software-versions': {
                                    'software-version': [{
                                        'name': self.software_version,
                                        'software-flavors': {
                                            'software-flavor': [{
                                                'name': self.software_flavor,
                                                'protocols': {
                                                    'protocol': [{
                                                        'name': 'netconf',
                                                        'capabilities': capability,
                                                        'protocol-version': netconf_version,
                                                    }]
                                                },
                                                'modules': {
                                                    'module': [{
                                                        'name': module_names[k],
                                                        'revision': revision.get(module_names[k]),
                                                        'organization': organization_module.get(module_names[k]),
                                                        'os-version': self.os_version,
                                                        'feature-set': self.feature_set,
                                                        'os-type': self.os,
                                                        'feature': features.get(module_names[k]),
                                                        'deviation': self.get_deviations(deviations, module_names[k]),
                                                        'conformance-type': conformance_type.get(module_names[k])
                                                    } for k, val in enumerate(module_names)],
                                                }
                                            }]
                                        }
                                    }]
                                }
                            }]
                        }
                    }]
                }
            }, ietf_model)
        #pool = ThreadPool(1)
        #pool.map(nieco, modules)
        #pool.close()
        #pool.join()

    def get_deviations(self, deviations, key):
        if deviations[key] is None:
            return None
        else:
            return [
                      {'name': deviations.get(key)['name'][i],
                       'revision': deviations.get(key)['revision'][i]
                       } for
                      i, val in enumerate(deviations[key]['name'])
                   ]

    def get_submodule_info(self, imports_or_includes):
        if imports_or_includes is not None and bool(imports_or_includes):
            revision = {}
            schema = {}

            for imp in imports_or_includes:
                yang_file = find_first_file('/'.join(self.split[0:-1]), imp + '.yang', imp + '@*.yang')
                if yang_file is None:
                    self.integrity_checker.add_submodule(self.split, imp)
                    yang_file = find_first_file('/'.join(self.split[0:2]), imp + '.yang', imp + '@*.yang')
                self.parsed_yang = None
                self.find_yang_var(revision, 'revision', imp, yang_file)
                if yang_file:
                    if self.api:
                        schema[imp] = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' + \
                                 '/'.join(yang_file.split('/')[2:])
                    else:
                        schema[imp] = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' \
                                 + '/'.join(yang_file.split('/')[2:])
                else:
                    schema[imp] = None
            my_json = json.dumps([{'name': imports_or_includes[k],
                                   'schema': schema[imports_or_includes[k]],
                                   'revision': revision[imports_or_includes[k]]
                                   } for k, val
                                  in
                                  enumerate(imports_or_includes)])
            return my_json
        else:
            return '[]'

    def parse_imports_includes(self, imports_or_includes, features, revision, name_revision,
                               yang_version, namespace, prefix, organization, contact, description, includes,
                               imports, conformance_type, deviations, module_names, comp_status,
                               email, wg, organization_module, is_include, parent, comp_result, belongs_to):
        if imports_or_includes is not None:
            for imp in imports_or_includes:
                if imp not in module_names:
                    LOGGER.debug('Parsing import or include file with name {}'.format(imp))
                    yang_file = find_first_file('/'.join(self.split[0:-1]), imp + '.yang', imp + '@*.yang')
                    if yang_file is None:
                        if is_include:
                            self.integrity_checker.add_submodule(self.split, imp)
                        else:
                            self.integrity_checker.add_module(self.split, imp)
                        yang_file = find_first_file('/'.join(self.split[0:2]), imp + '.yang', imp + '@*.yang')
                    if yang_file is not None:
                        self.integrity_checker.remove_one(self.split, yang_file)
                    self.parsed_yang = None
                    #devs = {'name': [], 'revision': []}
                    deviations[imp] = None
                    if is_include:
                        namespace[imp] = namespace[parent]
                        organization_module[imp] = organization_module[parent]
                        prefix[imp] = prefix[parent]
                        self.find_yang_var(belongs_to, 'belongs-to', imp, yang_file)
                    else:
                        belongs_to[imp] = None
                        self.find_yang_var(namespace, 'namespace', imp, yang_file)
                        namespace_exist = False
                        for ns, org in NS_MAP.items():
                            if self.os_version is '1651':
                                if 'urn:cisco' in namespace[imp]:
                                    if ns in namespace[imp]:
                                        organization_module[imp] = 'cisco'
                                        namespace_exist = True
                            else:
                                if ns in namespace[imp]:
                                    organization_module[imp] = org
                                    namespace_exist = True
                        if organization_module.get(imp) is None:
                            if 'urn:' in namespace[imp]:
                                organization_module[imp] = namespace[imp].split('urn:')[1].split(':')[0]
                                namespace_exist = True
                            elif 'cisco' in namespace[imp]:
                                organization_module[imp] = 'cisco'
                        if not namespace_exist:
                            if organization_module.get(imp) is None:
                                organization_module[imp] = MISSING_ELEMENT
                            if namespace[imp] is None or namespace[imp] == MISSING_ELEMENT:
                                self.integrity_checker.add_namespace(self.split, imp + ' : missing data')
                        self.find_yang_var(prefix, 'prefix', imp, yang_file)

                    module_submodule = module_or_submodule(yang_file)
                    LOGGER.debug('Parsing extractable fields')
                    self.find_yang_var(yang_version, 'yang-version', imp, yang_file)
                    self.find_yang_var(contact, 'contact', imp, yang_file)
                    self.find_yang_var(description, 'description', imp, yang_file)
                    self.find_yang_var(includes, 'include', imp, yang_file)
                    self.find_yang_var(imports, 'import', imp, yang_file)
                    self.find_yang_var(revision, 'revision', imp, yang_file)
                    self.find_yang_var(features, 'feature', imp, yang_file)
                    tree_type = get_tree_type(yang_file, module_submodule)
                    comp_status[imp] = self.parse_status(imp, revision[imp])
                    if is_include:
                        conformance_type[imp] = None
                    else:
                        conformance_type[imp] = 'import'
                    if comp_status[imp] != 'passed':
                        comp_result[imp] = self.parse_result(imp, revision[imp])
                    else:
                        comp_result[imp] = ''

                    email[imp] = self.parse_email(imp, revision[imp])
                    wg[imp] = self.parse_maturityLevel(imp, revision[imp])
                    if organization_module[imp] == 'ietf':
                        working_group = self.parse_wg(imp, revision[imp])
                    else:
                        working_group = None

                    module_names.append(imp)
                    name_revision.append(imp + '@' + revision[imp])
                    reference = MISSING_ELEMENT
                    document_name = MISSING_ELEMENT

                    if self.api:
                        schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' + \
                                 '/'.join(yang_file.split('/')[2:])
                    else:
                        schema = github_raw + self.owner + '/' + self.repo + '/' + self.branch + '/' \
                                 + '/'.join(yang_file.split('/')[2:])

                    self.prepare.add_key(imp + '@' + revision[imp] + ',' + organization_module[imp], namespace[imp],
                                         conformance_type[imp], self.vendor,
                                         self.platform, self.software_version, self.software_flavor, self.os,
                                         self.os_version, self.feature_set, reference, prefix[imp], yang_version[imp],#chage that for organization_module organization[imp]
                                         organization_module[imp], description[imp], contact[imp], comp_status[imp],
                                         email[imp], schema, features[imp], wg[imp], comp_result[imp],
                                         deviations[imp], self.get_submodule_info(includes[imp]['name']),
                                         module_submodule, document_name,
                                         create_generated_from(namespace[imp], imp), working_group, tree_type,
                                         'unknown', belongs_to[imp])

                    self.parse_imports_includes(includes[imp]['name'], features, revision, name_revision,
                                                yang_version, namespace, prefix, organization, contact, description,
                                                includes, imports, conformance_type, deviations, module_names
                                                , comp_status, email, wg, organization_module, True
                                                , parent, comp_result, belongs_to)
                    self.parse_imports_includes(imports[imp], features, revision, name_revision,
                                                yang_version, namespace, prefix, organization, contact, description,
                                                includes, imports, conformance_type, deviations, module_names
                                                , comp_status, email, wg, organization_module, False
                                                , parent, comp_result, belongs_to)

    def parse_status(self, module_name, revision):
        LOGGER.debug('Parsing status of module {}'.format(module_name))
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in rfc without revision

        status = self.get_module_status(self.ietf_draft_json, module_name, revision, 3)
        if status == 'unknown':
            status = self.get_module_status(self.ietf_rfc_standard_json, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.bbf_json, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.ieee_standard_json, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.ieee_experimental_json, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xr611, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xr612, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xr613, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xr621, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xe1631, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xe1632, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xe1641, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xe1651, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.xe1661, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.nx703f11, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.nx703f21, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.nx703i51, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.nx703i61, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.nx703i52, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.huawei8910, module_name, revision, 0)
        if status == 'unknown':
            status = self.get_module_status(self.mef_experimental_json, module_name, revision, 0)
        return status

    @staticmethod
    def get_module_status(files_json, module_name, revision, index):
        # try to find in rfc without revision
        try:
            status = files_json[module_name + '.yang'][index]
            if status == 'PASSED WITH WARNINGS':
                status = 'passed-with-warnings'
            status = status.lower()
            return status
        except:
            pass
        # try to find in draft with revision
        try:
            status = files_json[module_name + '@' + revision + '.yang'][index]
            if status == 'PASSED WITH WARNINGS':
                status = 'passed-with-warnings'
            status = status.lower()
            return status
        except:
            pass
        return 'unknown'

    def parse_email(self, module_name, revision):
        LOGGER.debug('Parsing email of module {}'.format(module_name))
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in draft without revision
        try:
            email = self.ietf_draft_json[module_name + '.yang'][1].split('\">Email')[0].split('mailto:')[1]
            return email
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            email = \
                self.ietf_draft_json[module_name + '@' + revision + '.yang'][1].split('\">Email')[0].split('mailto:')[1]
            return email
        except KeyError:
            pass
        try:
            email = self.ietf_draft_example_json[module_name + '.yang'][1].split('\">Email')[0].split('mailto:')[1]
            return email
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            email = \
                self.ietf_draft_example_json[module_name + '@' + revision + '.yang'][1].split('\">Email')[0].split('mailto:')[1]
            return email
        except KeyError:
            pass
        return None

    def parse_result(self, module_name, revision):
        LOGGER.debug('Parsing compulation status of module {}'.format(module_name))
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in draft without revision
        result = {}
        try:
            result['pyang'] = self.ietf_draft_json[module_name + '.yang'][4]
            result['pyang_lint'] = self.ietf_draft_json[module_name + '.yang'][5]
            result['confdrc'] = self.ietf_draft_json[module_name + '.yang'][6]
            result['yumadump'] = self.ietf_draft_json[module_name + '.yang'][7]
            result['yanglint'] = self.ietf_draft_json[module_name + '.yang'][8]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result['pyang'] = self.ietf_draft_json[module_name + '@' + revision + '.yang'][4]
            result['pyang_lint'] = self.ietf_draft_json[module_name + '@' + revision + '.yang'][5]
            result['confdrc'] = self.ietf_draft_json[module_name + '@' + revision + '.yang'][6]
            result['yumadump'] = self.ietf_draft_json[module_name + '@' + revision + '.yang'][7]
            result['yanglint'] = self.ietf_draft_json[module_name + '@' + revision + '.yang'][8]
            return result
        except KeyError:
            pass
        try:
            result['pyang'] = self.bbf_json[module_name + '.yang'][1]
            result['pyang_lint'] = self.bbf_json[module_name + '.yang'][2]
            result['confdrc'] = self.bbf_json[module_name + '.yang'][3]
            result['yumadump'] = self.bbf_json[module_name + '.yang'][4]
            result['yanglint'] = self.bbf_json[module_name + '.yang'][5]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result['pyang'] = self.bbf_json[module_name + '@' + revision + '.yang'][1]
            result['pyang_lint'] = self.bbf_json[module_name + '@' + revision + '.yang'][2]
            result['confdrc'] = self.bbf_json[module_name + '@' + revision + '.yang'][3]
            result['yumadump'] = self.bbf_json[module_name + '@' + revision + '.yang'][4]
            result['yanglint'] = self.bbf_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        try:
            result['pyang'] = self.ieee_standard_json[module_name + '.yang'][1]
            result['pyang_lint'] = self.ieee_standard_json[module_name + '.yang'][2]
            result['confdrc'] = self.ieee_standard_json[module_name + '.yang'][3]
            result['yumadump'] = self.ieee_standard_json[module_name + '.yang'][4]
            result['yanglint'] = self.ieee_standard_json[module_name + '.yang'][5]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result['pyang'] = self.ieee_standard_json[module_name + '@' + revision + '.yang'][1]
            result['pyang_lint'] = self.ieee_standard_json[module_name + '@' + revision + '.yang'][2]
            result['confdrc'] = self.ieee_standard_json[module_name + '@' + revision + '.yang'][3]
            result['yumadump'] = self.ieee_standard_json[module_name + '@' + revision + '.yang'][4]
            result['yanglint'] = self.ieee_standard_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        try:
            result['pyang'] = self.ieee_experimental_json[module_name + '.yang'][1]
            result['pyang_lint'] = self.ieee_experimental_json[module_name + '.yang'][2]
            result['confdrc'] = self.ieee_experimental_json[module_name + '.yang'][3]
            result['yumadump'] = self.ieee_experimental_json[module_name + '.yang'][4]
            result['yanglint'] = self.ieee_experimental_json[module_name + '.yang'][5]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result['pyang'] = self.ieee_experimental_json[module_name + '@' + revision + '.yang'][1]
            result['pyang_lint'] = self.ieee_experimental_json[module_name + '@' + revision + '.yang'][2]
            result['confdrc'] = self.ieee_experimental_json[module_name + '@' + revision + '.yang'][3]
            result['yumadump'] = self.ieee_experimental_json[module_name + '@' + revision + '.yang'][4]
            result['yanglint'] = self.ieee_experimental_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        result = self.parse_res(module_name, revision, self.nx703i52)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.nx703i61)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.nx703i51)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.nx703f21)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.nx703f11)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xr621)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xr613)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xr612)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xr611)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xe1651)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xe1661)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xe1641)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xe1632)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.xe1631)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.huawei8910)
        if result != '':
            return result
        result = self.parse_res(module_name, revision, self.ietf_rfc_standard_json)
        if result != '':
            return result
        return ''

    def parse_res(self, module_name, revision, json_file):
        result = {}
        try:
            result['pyang'] = json_file[module_name + '.yang'][1]
            result['pyang_lint'] = json_file[module_name + '.yang'][2]
            result['confdrc'] = json_file[module_name + '.yang'][3]
            result['yumadump'] = json_file[module_name + '.yang'][4]
            result['yanglint'] = json_file[module_name + '.yang'][5]
            return result
        except :
            pass
        # try to find in draft with revision
        try:
            result['pyang'] = json_file[module_name + '@' + revision + '.yang'][1]
            result['pyang_lint'] = json_file[module_name + '@' + revision + '.yang'][2]
            result['confdrc'] = json_file[module_name + '@' + revision + '.yang'][3]
            result['yumadump'] = json_file[module_name + '@' + revision + '.yang'][4]
            result['yanglint'] = json_file[module_name + '@' + revision + '.yang'][5]
            return result
        except :
            pass
        return ''

    def parse_maturityLevel(self, module_name, revision):
        LOGGER.debug('Parsing maturity level of module {}'.format(module_name))
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in draft without revision
        try:
            wg = self.ietf_draft_json[module_name + '.yang'][0].split('</a>')[0].split('\">')[1].split('-')[1]
            if 'ietf' in wg:
                return 'adopted'
            else:
                return 'initial'
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            wg = \
                self.ietf_draft_json[module_name + '@' + revision + '.yang'][0].split('</a>')[0].split('\">')[1].split(
                    '-')[1]
            if 'ietf' in wg:
                return 'adopted'
            else:
                return 'initial'
        except KeyError:
            pass
        # try to find in rfc with revision
        try:
            wg = self.ietf_rfc_json[module_name + '@' + revision + '.yang']
            return 'ratified'
        except KeyError:
            pass
        try:
            wg = self.ietf_rfc_json[module_name + '.yang']
            return 'ratified'
        except KeyError:
            pass
        return None

    def parse_wg(self, module_name, revision):
        LOGGER.debug('Parsing working group of module {}'.format(module_name))
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in draft without revision
        try:
            return self.ietf_draft_json[module_name + '.yang'][0].split('</a>')[0].split('\">')[1].split('-')[2]
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            return self.ietf_draft_json[module_name + '@' + revision + '.yang'][0].split('</a>')[0].split('\">')[1]\
            .split('-')[2]
        except KeyError:
            pass
        # try to find in ietf RFC map with revision
        try:
            return IETF_RFC_MAP[module_name + '.yang']
        except KeyError:
            pass
        # try to find in ietf RFC map with revision
        try:
            return IETF_RFC_MAP[module_name + '@' + revision + '.yang']
        except KeyError:
            pass
        return None

    def parse_document_reference(self, module_name, revision):
        LOGGER.debug('Parsing document reference of module {}'.format(module_name))
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in draft without revision
        try:
            doc_name = self.ietf_draft_json[module_name + '.yang'][0].split('</a>')[0].split('\">')[1]
            doc_source = self.ietf_draft_json[module_name + '.yang'][0].split('a href=\"')[1].split('\">')[0]
            return [doc_name, doc_source]
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            doc_name = self.ietf_draft_json[module_name + '@' + revision + '.yang'][0].split('</a>')[0].split('\">')[1]
            doc_source = self.ietf_draft_json[module_name + '@' + revision + '.yang'][0].split('a href=\"')[1] \
                .split('\">')[0]
            return [doc_name, doc_source]
        except KeyError:
            pass
            # try to find in rfc with revision
            try:
                doc_name = self.ietf_rfc_json[module_name + '@' + revision + '.yang'].split('</a>')[0].split('\">')[1]
                doc_source = self.ietf_rfc_json[module_name + '@' + revision + '.yang'].split('a href=\"')[1]\
                    .split('\">')[0]
                return [doc_name, doc_source]
            except KeyError:
                pass
            try:
                doc_name = self.ietf_rfc_json[module_name + '.yang'].split('</a>')[0].split('\">')[1]
                doc_source = self.ietf_rfc_json[module_name + '.yang'].split('a href=\"')[1].split('\">')[0]
                return [doc_name, doc_source]
            except KeyError:
                pass
        return [MISSING_ELEMENT, MISSING_ELEMENT]
