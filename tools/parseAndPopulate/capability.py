from __future__ import print_function

import fnmatch
import json
import os
import unicodedata
import urllib2
import fileinput
import xml.etree.ElementTree as ET

from numpy.f2py.auxfuncs import throw_error

import yangParser

NS_MAP = {
    "http://cisco.com/ns/yang/": "cisco",
    "http://www.huawei.com/netconf": "huawei",
    "http://openconfig.net/yang/": "openconfig",
    "http://tail-f.com/": "tail-f",
    "urn:ietf": "ietf",
    "urn:cisco": "cisco"
}

github = 'https://github.com/'


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
                return 'submodule'
            if module_position >= 0 and (module_position < cpos or cpos == -1) and not commented_out:
                return 'module'
        print ('File ' + input_file + ' not yang file or not well formated')
        return 'wrong file'
    else:
        return None


class Capability:
    def __init__(self, hello_message_file, index, prepare, integrity_checker, api, sdo,
                 statistics_in_catalog=None):
        self.statistics_in_catalog = statistics_in_catalog
        self.index = index
        self.prepare = prepare
        self.integrity_checker = integrity_checker
        self.parsed_yang = None
        self.api = api
        self.sdo = sdo
        # Get hello message root
        if 'xml' in hello_message_file:
            try:
                self.root = ET.parse(hello_message_file).getroot()
            except:
                #try to change & to &amp
                hello_file = fileinput.FileInput(hello_message_file, inplace=True)
                for line in hello_file:
                    print(line.replace('&', '&amp;'), end='')
                hello_file.close()
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
                self.owner = 'YangModels'
                self.repo = 'https://github.com/YangModels/yang/'
                self.repo_file_path = None
                self.local_file_path = None
                self.feature_set = 'ALL'
                self.software_version = repr(165) + self.feature_set
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
                self.software_flavor = self.os + '|' + self.os_version
            integrity_checker.add_platform('/'.join(self.split[:-2]), self.platform)

        self.ietf_rfc_json = {}
        self.ietf_draft_json = {}
        self.ietf_draft_example_json = {}
        self.bbf_json = {}
        self.ieee_standard_json = {}
        self.ieee_experimental_json = {}
        self.ietf_rfc_json = load_json_from_url('http://www.claise.be/IETFYANGRFC.json')
        self.bbf_json = load_json_from_url('http://www.claise.be/BBF.json')
        self.ieee_standard_json = load_json_from_url('http://www.claise.be/IEEEStandard.json')
        self.ieee_experimental_json = load_json_from_url('http://www.claise.be/IEEEExperimental.json')
        self.ietf_draft_json = load_json_from_url('http://www.claise.be/IETFYANGDraft.json')

    def initialize(self, impl):
        if impl['capabilities-file']['path'] in self.hello_message_file:
            self.feature_set = 'ALL'
            self.os_version = impl['software-version']
            self.software_flavor = impl['software-flavor']
            self.vendor = impl['vendor']
            self.platform = impl['name']
            self.os = impl['os-type']
            self.software_version = repr(165) + self.feature_set
            self.owner = impl['capabilities-file']['owner']
            self.repo = github + '/' + self.owner + impl['capabilities-file']['repo']
            self.repo_file_path = impl['capabilities-file']['path']
            self.local_file_path = 'api/vendor/' + self.owner + '/' + impl['capabilities-file']['repo'] + '/'\
                                    + self.repo_file_path

    def handle_exception(self, field, object, module_name):
        # In case of include exception create empty
        if 'include' in field:
            names = []
            revs = []
            incl = {'name': names, 'revision': revs}
            object[module_name] = incl
        # In case of revision exception create dummy revision -> '1500-01-01'
        elif 'revision' in field:
            object[module_name] = '1500-01-01'
            self.integrity_checker.add_revision(self.split, module_name)
        # In case of yang-version exception create version 1.0 because
        # if yang doesn`t contain any version value it is 1.0 by default
        elif 'yang-version' in field:
            object[module_name] = '1.0'
        # In case of namespace exception create dummy exception -> 'urn:dummy'
        elif 'namespace' in field:
            object[module_name] = 'missing element'
        # For everything else insert null value
        elif 'import' in field:
            object[module_name] = None
        elif 'feature' in field:
            object[module_name] = 'missing-element'
        elif 'compilation-status' in field:
            object[module_name] = 'MISSING'
        else:
            object[module_name] = 'missing element'

    # pyang parsing variables and saving field value
    def find_yang_var(self, object, field, module_name, yang_file):
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

                if isinstance(yang_variable, unicode):
                    object[module_name] = unicodedata.normalize('NFKD', yang_variable).encode('ascii', 'ignore')
                else:
                    object[module_name] = yang_variable

        # In case of exception hande them
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
            sdos_json = json.load(open('./prepare-sdo.json', 'r'))
            sdos_list = sdos_json['modules']['module']
            for sdo in sdos_list:
                owner = sdo['sdo-file']['owner']
                repo = github + '/' + owner + '/' + sdo['sdo-file']['repo'].split('.')[0]
                repo_file_path = sdo['sdo-file']['path']
                root = owner + '/' + sdo['sdo-file']['repo'].split('.')[0] + '/'\
                       + '/'.join(repo_file_path.split('/')[:-1])
                root = 'temp/' + unicodedata.normalize('NFKD', root).encode('ascii', 'ignore')
                file_name = unicodedata.normalize('NFKD', sdo['sdo-file']['path'].split('/')[-1])\
                    .encode('ascii', 'ignore')
                local_file_path = 'api/sdo/' + owner + '/' + sdo['sdo-file']['repo'].split('.')[0] + '/'\
                                  + repo_file_path
                self.parsed_yang = None
                prefix = {}
                yang_version = {}
                organization = {}
                contact = {}
                includes = {}
                imports = {}
                description = {}
                schema = {}
                revision = {}
                namespace = {}
                features = {}

                module_submodule = module_or_submodule(root + '/' + file_name)
                if '[1]' in file_name:
                    print('file name contains invalid characters')
                    module_submodule = 'wrong file'
                if module_submodule != 'wrong file':
                    conformance_type = unicodedata.normalize('NFKD', sdo['conformance-type']).encode('ascii', 'ignore')
                    self.find_yang_var(prefix, 'prefix', file_name, root + '/' + file_name)
                    self.find_yang_var(yang_version, 'yang-version', file_name, root + '/' + file_name)
                    self.find_yang_var(organization, 'organization', file_name, root + '/' + file_name)
                    self.find_yang_var(contact, 'contact', file_name, root + '/' + file_name)
                    self.find_yang_var(description, 'description', file_name, root + '/' + file_name)
                    self.find_yang_var(includes, 'include', file_name, root + '/' + file_name)
                    self.find_yang_var(imports, 'import', file_name, root + '/' + file_name)
                    self.find_yang_var(schema, 'schema', file_name, root + '/' + file_name)
                    self.find_yang_var(namespace, 'namespace', file_name, root + '/' + file_name)
                    self.find_yang_var(features, 'feature', file_name, root + '/' + file_name)
                    self.find_yang_var(revision, 'revision', file_name, root + '/' + file_name)
                    compilations_status = self.parse_status(file_name, revision[file_name])
                    if compilations_status != 'PASSED':
                        compilations_result = self.parse_result(file_name, revision[file_name])
                    else:
                        compilations_result = ''
                    author_email = unicodedata.normalize('NFKD', self.get_json(sdo.get('author-email')))\
                        .encode('ascii', 'ignore')
                    if author_email == 'missing element':
                        author_email = None
                    working_group = unicodedata.normalize('NFKD', self.get_json(sdo.get('maturity-level')))\
                        .encode('ascii', 'ignore')
                    reference = unicodedata.normalize('NFKD', self.get_json(sdo.get('reference')))\
                        .encode('ascii', 'ignore')
                    document_name = unicodedata.normalize('NFKD', self.get_json(sdo.get('document-name')))\
                        .encode('ascii', 'ignore')
                    self.prepare.add_key_sdo(file_name + '@' + revision.get(file_name), namespace.get(file_name),
                                             conformance_type, reference, prefix.get(file_name),
                                             yang_version.get(file_name), organization.get(file_name),
                                             description.get(file_name), contact.get(file_name), schema.get(file_name),
                                             features.get(file_name),
                                             self.get_submodule_info(includes.get(file_name)['name']),
                                             compilations_status, author_email, working_group, compilations_result,
                                             module_submodule, document_name, owner, repo,
                                             repo_file_path, local_file_path)

        if not self.api:
            for root, subdirs, sdos in os.walk('/'.join(self.split)):
                for file_name in sdos:
                    if '.yang' in file_name and ('vendor' not in root or 'odp' not in root):
                        self.parsed_yang = None
                        prefix = {}
                        yang_version = {}
                        organization = {}
                        contact = {}
                        includes = {}
                        imports = {}
                        description = {}
                        schema = {}
                        revision = {}
                        namespace = {}
                        features = {}
                        module_submodule = module_or_submodule(root + '/' + file_name)

                        if '[1]' in file_name:
                            print('file name contains invalid characters')
                            module_submodule = 'wrong file'
                        if module_submodule != 'wrong file':
                            owner = 'YangModels'
                            repo_file_path = root + '/' + file_name
                            repo = github + '/' + owner + '/yang'
                            local_file_path = root + '/' + file_name
                            conformance_type = 'implement'
                            self.find_yang_var(prefix, 'prefix', file_name, root + '/' + file_name)
                            self.find_yang_var(yang_version, 'yang-version', file_name, root + '/' + file_name)
                            self.find_yang_var(organization, 'organization', file_name, root + '/' + file_name)
                            self.find_yang_var(contact, 'contact', file_name, root + '/' + file_name)
                            self.find_yang_var(description, 'description', file_name, root + '/' + file_name)
                            self.find_yang_var(includes, 'include', file_name, root + '/' + file_name)
                            self.find_yang_var(imports, 'import', file_name, root + '/' + file_name)
                            self.find_yang_var(schema, 'schema', file_name, root + '/' + file_name)
                            self.find_yang_var(revision, 'revision', file_name, root + '/' + file_name)
                            self.find_yang_var(namespace, 'namespace', file_name, root + '/' + file_name)
                            self.find_yang_var(features, 'feature', file_name, root + '/' + file_name)
                            reference = 'missing element'
                            document_name = 'missing element'
                            compilations_status = self.parse_status(file_name, revision[file_name])
                            if 'bbf-l2-forwarding-base' in file_name:
                                pass
                            self.statistics_in_catalog.set_passed(root, compilations_status)
                            if compilations_status != 'PASSED':
                                compilations_result = self.parse_result(file_name, revision[file_name])
                            else:
                                compilations_result = ''
                            author_email = self.parse_email(file_name, revision[file_name])
                            working_group = self.parse_wg(file_name, revision[file_name])
                            self.statistics_in_catalog.add_in_catalog(root)
                            self.prepare.add_key_sdo(file_name + '@' + revision.get(file_name),
                                                     namespace.get(file_name), conformance_type, reference,
                                                     prefix.get(file_name), yang_version.get(file_name),
                                                     organization.get(file_name), description.get(file_name),
                                                     contact.get(file_name), schema.get(file_name),
                                                     features.get(file_name),
                                                     self.get_submodule_info(includes.get(file_name)['name']),
                                                     compilations_status, author_email, working_group,
                                                     compilations_result, module_submodule, document_name, owner,
                                                     repo, repo_file_path, local_file_path)

    # parse capability xml and save to file
    def parse_and_dump(self):
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
        schema = {}
        imports = {}
        reference = {}
        conformance_type = {}
        compilations_status = {}
        working_group = {}
        author_email = {}
        netconf_version = ''
        compilations_result = {}
        organization_module = {}
        module_submodule = {}

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
            # Parse netconf version
            if ':netconf:base:' in module.text:
                netconf_version = module.text
            # Parse capability together with version
            if ':capability:' in module.text:
                cap_with_version = module.text.split(':capability:')[1]
                capability.append(cap_with_version.split('?')[0])
            # Parse modules
            if 'module=' in module.text:
                # Parse name of the module
                module_and_more = module.text.split('module=')[1]
                module_name = module_and_more.split('&')[0]
                module_names.append(module_name)
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
                        revs.append('1500-01-01')
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
                for ns, org in NS_MAP.items():
                    if self.os_version is '1651':
                        if ns is 'urn:cisco':
                            if ns in namespace[module_name]:
                                organization_module[module_name] = org
                                namespace_exist = True
                    else:
                        if ns in namespace[module_name]:
                            organization_module[module_name] = org
                            namespace_exist = True
                if not namespace_exist:
                    organization_module[module_name] = 'missing_data'
                    if namespace[module_name] is None:
                        self.integrity_checker.add_namespace(self.split, module_name + ' : missing data')
                        namespace[module_name] = 'missing data'
                    self.integrity_checker.add_namespace(self.split, module_name + ' : ' + namespace[module_name])

                module_submodule = module_or_submodule(yang_file)
                self.find_yang_var(prefix, 'prefix', module_name, yang_file)
                self.find_yang_var(yang_version, 'yang-version', module_name, yang_file)
                self.find_yang_var(organization, 'organization', module_name, yang_file)
                self.find_yang_var(contact, 'contact', module_name, yang_file)
                self.find_yang_var(description, 'description', module_name, yang_file)
                self.find_yang_var(includes, 'include', module_name, yang_file)
                self.find_yang_var(imports, 'import', module_name, yang_file)
                self.find_yang_var(schema, 'schema', module_name, yang_file)

                reference = 'missing element'
                document_name = 'missing element'
                compilations_status[module_name] = self.parse_status(module_name, revision[module_name])
                if compilations_status[module_name] not in 'PASSED':
                    compilations_result[module_name] = self.parse_result(module_name, revision[module_name])
                else:
                    compilations_result[module_name] = ''
                author_email[module_name] = self.parse_email(module_name, revision[module_name])
                working_group[module_name] = self.parse_wg(module_name, revision[module_name])

                if self.repo_file_path is None:
                    self.repo_file_path = yang_file
                    self.local_file_path = yang_file

                self.prepare.add_key(module_name + '@' + revision[module_name], namespace[module_name],
                                     conformance_type[module_name], self.vendor, self.platform, self.software_version,
                                     self.software_flavor, self.os, self.os_version, self.feature_set,
                                     reference, prefix[module_name], yang_version[module_name],
                                     organization[module_name], description[module_name], contact[module_name],
                                     compilations_status[module_name], author_email[module_name], schema[module_name],
                                     features[module_name], working_group[module_name],
                                     compilations_result[module_name], deviations[module_name],
                                     self.get_submodule_info(includes[module_name]['name']), module_submodule,
                                     document_name, self.owner, self.repo, self.repo_file_path, self.local_file_path)

                self.parse_imports_includes(includes[module_name]['name'], features, revision, name_revision,
                                            yang_version, namespace, prefix, organization, contact, description,
                                            includes, imports, conformance_type, deviations, module_names,
                                            compilations_status, schema, author_email, working_group,
                                            organization_module, True, namespace[module_name], compilations_result)
                self.parse_imports_includes(imports[module_name], features, revision, name_revision,
                                            yang_version, namespace, prefix, organization, contact, description,
                                            includes, imports, conformance_type, deviations, module_names,
                                            compilations_status, schema, author_email, working_group,
                                            organization_module, False, namespace[module_name], compilations_result)

        # restconf capability parsing
        for module in self.root.iter('module'):
            module_name = module.find('name').text
            module_names.append(module_name)
            namespace[module_name] = module.find('namespace').text
            revision[module_name] = module.find('revision').text
            schema[module_name] = module.find('schema').text
            conformance_type[module_name] = module.find('conformance-type').text
            devs = {}
            names = []
            revs = []
            for dev in self.root.iter('deviation'):
                names.append(dev.find('name').text)
                if dev.find('revision').text is None:
                    revs.append('1500-01-01')
                else:
                    revs.append(dev.find('revision').text)
            devs['name'] = names
            devs['revision'] = revs
            deviations[module_name] = devs
            objs = []
            for feat in self.root.iter('feature'):
                objs.append(feat.text)
            features[module_name] = objs

            # Find yang file in the same directory as capability.xml file is
            # so we can parse all needed fields out of it
            yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
                                        module_name + '@' + revision[module_name] + '.yang')

            if yang_file is None:
                # In case we didn`t find the module try to look for it in any other directory of this project
                self.integrity_checker.add_module(self.split, module_name)
                yang_file = find_first_file('/'.join(self.split[0:2]), module_name + '.yang',
                                            module_name + '@' + revision[module_name] + '.yang')

            # Parse rest of the fields out of the yang file
            self.find_yang_var(prefix, 'prefix', module_name, yang_file)
            self.find_yang_var(yang_version, 'yang-version', module_name, yang_file)
            self.find_yang_var(organization, 'organization', module_name, yang_file)
            self.find_yang_var(contact, 'contact', module_name, yang_file)
            self.find_yang_var(description, 'description', module_name, yang_file)
            self.find_yang_var(reference, 'reference', module_name, yang_file)
            self.find_yang_var(includes, 'include', module_name, yang_file)
            self.find_yang_var(imports, 'import', module_name, yang_file)

        self.integrity_checker.add_unique(name_revision)
        # Write dictionary to file
        # Create json dictionary out of parsed information
        with open('normal' + repr(self.index) + '.json', "w") as ietf_model:
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
                                                        'revision': revision.get(module_names[k])
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
                self.find_yang_var(schema, 'schema', imp, yang_file)
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
                               imports, conformance_type, deviations, module_names, comp_status, schema,
                               email, wg, organization_module, is_include, parent_ns, comp_result):
        if imports_or_includes is not None:
            for imp in imports_or_includes:
                if imp not in module_names:
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
                    devs = {'name': [], 'revision': []}
                    deviations[imp] = devs
                    if is_include:
                        namespace[imp] = parent_ns
                    else:
                        self.find_yang_var(namespace, 'namespace', imp, yang_file)
                    namespace_exist = False
                    for ns, org in NS_MAP.items():
                        if self.os_version is '1651':
                            if ns is 'urn:cisco':
                                if ns in namespace[imp]:
                                    organization_module[imp] = org
                                    namespace_exist = True
                        else:
                            if ns in namespace[imp]:
                                organization_module[imp] = org
                                namespace_exist = True
                    if not namespace_exist:
                        organization_module[imp] = 'missing_element'
                        if namespace[imp] is None:
                            namespace[imp] = 'missing data'
                        self.integrity_checker.add_namespace(self.split, imp + ' : ' + namespace[imp])
                    module_submodule = module_or_submodule(yang_file)
                    self.find_yang_var(prefix, 'prefix', imp, yang_file)
                    self.find_yang_var(yang_version, 'yang-version', imp, yang_file)
                    self.find_yang_var(organization, 'organization', imp, yang_file)
                    self.find_yang_var(contact, 'contact', imp, yang_file)
                    self.find_yang_var(description, 'description', imp, yang_file)
                    self.find_yang_var(includes, 'include', imp, yang_file)
                    self.find_yang_var(imports, 'import', imp, yang_file)
                    self.find_yang_var(revision, 'revision', imp, yang_file)
                    self.find_yang_var(features, 'feature', imp, yang_file)
                    self.find_yang_var(schema, 'schema', imp, yang_file)

                    comp_status[imp] = self.parse_status(imp, revision[imp])
                    if comp_status[imp] is not 'PASSED':
                        comp_result[imp] = self.parse_result(imp, revision[imp])
                    else:
                        comp_result[imp] = ''
                    email[imp] = self.parse_email(imp, revision[imp])
                    wg[imp] = self.parse_wg(imp, revision[imp])
                    conformance_type[imp] = 'implement'
                    module_names.append(imp)
                    name_revision.append(imp + '@' + revision[imp])
                    reference = 'missing element'
                    document_name = 'missing element'

                    if self.repo_file_path is None:
                        self.repo_file_path = yang_file
                        self.local_file_path = yang_file
                    self.prepare.add_key(imp + '@' + revision[imp], namespace[imp], conformance_type[imp], self.vendor,
                                         self.platform, self.software_version, self.software_flavor, self.os,
                                         self.os_version, self.feature_set, reference, prefix[imp], yang_version[imp],
                                         organization[imp], description[imp], contact[imp], comp_status[imp],
                                         email[imp], schema[imp], features[imp], wg[imp], comp_result[imp],
                                         deviations[imp], self.get_submodule_info(includes[imp]['name']),
                                         module_submodule, document_name, self.owner, self.repo, self.repo_file_path,
                                         self.local_file_path)

                    self.parse_imports_includes(includes[imp]['name'], features, revision, name_revision,
                                                yang_version, namespace, prefix, organization, contact, description,
                                                includes, imports, conformance_type, deviations, module_names
                                                , comp_status, schema, email, wg, organization_module, True
                                                , namespace[imp], comp_result)
                    self.parse_imports_includes(imports[imp], features, revision, name_revision,
                                                yang_version, namespace, prefix, organization, contact, description,
                                                includes, imports, conformance_type, deviations, module_names
                                                , comp_status, schema, email, wg, organization_module, False
                                                , namespace[imp], comp_result)

    def parse_status(self, module_name, revision):
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in rfc without revision
        try:
            if module_name + '.yang' in self.ietf_rfc_json.keys():
                return 'PASSED'
        except KeyError:
            pass
        # try to find in rfc with revision
        try:
            if module_name + '@' + revision + '.yang' in self.ietf_rfc_json.keys():
                return 'PASSED'
        except KeyError:
            pass

        status = self.get_module_status(self.ietf_draft_json, module_name, revision, 3)
        if status == 'MISSING':
            status = self.get_module_status(self.bbf_json, module_name, revision, 0)
        if status == 'MISSING':
            status = self.get_module_status(self.ieee_standard_json, module_name, revision, 0)
        if status == 'MISSING':
            status = self.get_module_status(self.ieee_experimental_json, module_name, revision, 0)
        return status

    @staticmethod
    def get_module_status(files_json, module_name, revision, index):
        # try to find in rfc without revision
        try:
            status = files_json[module_name + '.yang'][index]
            if status == 'PASSED WITH WARNINGS':
                status = 'PASSED-WITH-WARNINGS'
            return status
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            status = files_json[module_name + '@' + revision + '.yang'][index]
            if status == 'PASSED WITH WARNINGS':
                status = 'PASSED-WITH-WARNINGS'
            return status
        except KeyError:
            pass
        return 'MISSING'

    def parse_email(self, module_name, revision):
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
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in draft without revision
        result = ''
        try:
            result += self.ietf_draft_json[module_name + '.yang'][4]
            result += self.ietf_draft_json[module_name + '.yang'][5]
            result += self.ietf_draft_json[module_name + '.yang'][6]
            result += self.ietf_draft_json[module_name + '.yang'][7]
            result += self.ietf_draft_json[module_name + '.yang'][8]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result += self.ietf_draft_json[module_name + '@' + revision + '.yang'][4]
            result += self.ietf_draft_json[module_name + '@' + revision + '.yang'][5]
            result += self.ietf_draft_json[module_name + '@' + revision + '.yang'][6]
            result += self.ietf_draft_json[module_name + '@' + revision + '.yang'][7]
            result += self.ietf_draft_json[module_name + '@' + revision + '.yang'][8]
            return result
        except KeyError:
            pass
        try:
            result += self.bbf_json[module_name + '@' + revision + '.yang'][1]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][2]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][3]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][4]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result += self.bbf_json[module_name + '@' + revision + '.yang'][1]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][2]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][3]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][4]
            result += self.bbf_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        try:
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][1]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][2]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][3]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][4]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][1]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][2]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][3]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][4]
            result += self.ieee_standard_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        try:
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][1]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][2]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][3]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][4]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][1]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][2]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][3]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][4]
            result += self.ieee_experimental_json[module_name + '@' + revision + '.yang'][5]
            return result
        except KeyError:
            pass
        return ''

    def parse_wg(self, module_name, revision):
        # if module name contains .yang get only name
        module_name = module_name.split('.')[0]
        # try to find in draft without revision
        try:
            wg = self.ietf_draft_json[module_name + '.yang'][0].split('</a>')[0].split('\">')[1].split('-')[1]
            if 'ietf' in wg:
                return 'working-group'
            else:
                return 'individual'
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            wg = \
                self.ietf_draft_json[module_name + '@' + revision + '.yang'][0].split('</a>')[0].split('\">')[1].split(
                    '-')[1]
            if 'ietf' in wg:
                return 'working-group'
            else:
                return 'individual'
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
