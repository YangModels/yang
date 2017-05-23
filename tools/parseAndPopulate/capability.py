from __future__ import print_function

import fnmatch
import json
import os
import unicodedata
import urllib2
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
            tries -= 1;
            if tries == 0:
                failed = False
            pass
    if tries == 0:
        throw_error('Couldn`t open a json file from url:' + url)
    return loaded_json


class Capability:
    def __init__(self, hello_message_file, index, prepare):
        self.index = index
        self.prepare = prepare
        self.parsed_yang = None
        # Get hello message root
        self.root = ET.parse(hello_message_file).getroot()
        # Split it so we can get vendor, os-type, os-version
        self.split = hello_message_file.split('/')
        self.hello_message_file = hello_message_file
        self.missing_revision = []

        self.vendor = self.split[2]
        # Solve for os-type
        if 'nx' in self.split[3]:
            self.os = 'NX-OS'
        elif 'xe' in self.split[3]:
            self.os = 'IOS-XE'
        elif 'xr' in self.split[3]:
            self.os = 'IOS-XR'
        else:
            self.os = 'Unknown'
        self.os_version = self.split[4]
        self.platform = self.split[5].split('-')[0]
        self.ietf_rfc_json = load_json_from_url('http://www.claise.be/IETFYANGRFC.json')
        self.ietf_draft_json = load_json_from_url('http://www.claise.be/IETFYANGDraft.json')

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
            self.missing_revision.append(module_name)
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

    # parse capability xml and save to file
    def parse_and_dump(self):
        capability = []
        tag = self.root.tag
        module_names = []
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
        missing_module = {}
        missing_includes = {}
        netconf_version = ''
        organization_module = {}

        # Parse deviations and features from each module from netconf hello message
        def deviations_and_features(search_for):
            my_list = []
            if search_for in module_and_more:
                devs_or_features = module_and_more.split(search_for)[1]
                devs_or_features = devs_or_features.split('&')[0]
                my_list = devs_or_features.split(',')
            return my_list

        print_once = False
        print('parsing hello message')
        # netconf capability parsing
        for cap in self.root.iter(tag.split('hello')[0] + 'capability'):
            # Parse netconf version
            if ':netconf:base:' in cap.text:
                netconf_version = cap.text
            # Parse capability together with version
            if ':capability:' in cap.text:
                cap_with_version = cap.text.split(':capability:')[1]
                capability.append(cap_with_version.split('?')[0])
            # Parse modules
            if 'module=' in cap.text:
                # Parse name of the module
                module_and_more = cap.text.split('module=')[1]
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
                        missing_module[module_name] = i
                        revs.append('1500-01-01')
                    else:
                        self.parsed_yang = yangParser.parse(os.path.abspath(yang_file))
                        yang_variable = self.parsed_yang.search('revision')[0].arg

                        if isinstance(yang_variable, unicode):
                            revs.append(unicodedata.normalize('NFKD', yang_variable).encode('ascii', 'ignore'))
                        else:
                            revs.append(yang_variable)
                devs['name'] = names
                devs['revision'] = revs
                deviations[module_name] = devs

                # Parse features of the module
                features[module_name] = deviations_and_features('features=')
                # Parse conformance type of the module
                conformance_type[module_name] = 'implement'

                # Parse revision of the module from capability.xml file
                my_var = ''
                if 'revision' in cap.text:
                    revision_and_more = cap.text.split('revision=')[1]
                    my_var = revision_and_more.split('&')[0]
                revision[module_name] = my_var

                # Find yang file in the same directory as capability.xml file is
                # so we can parse all needed fields out of it
                yang_file = find_first_file('/'.join(self.split[0:-1]), module_name + '.yang',
                                            module_name + '@' + my_var + '.yang')

                if yang_file is None:
                    # In case we didn`t find the module try to look for it in any other directory of this project
                    missing_module[module_name] = module_name
                    yang_file = find_first_file('/'.join(self.split[0:1]), module_name + '.yang',
                                                module_name + '@' + my_var + '.yang')
                self.parsed_yang = None
                if not print_once:
                    print('parsing yang files')
                    print_once = True

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
                        namespace[module_name] = 'missing data'
                    print(module_name + ' : ' + namespace[module_name])

                self.find_yang_var(prefix, 'prefix', module_name, yang_file)
                self.find_yang_var(yang_version, 'yang-version', module_name, yang_file)
                self.find_yang_var(organization, 'organization', module_name, yang_file)
                self.find_yang_var(contact, 'contact', module_name, yang_file)
                self.find_yang_var(description, 'description', module_name, yang_file)
                self.find_yang_var(includes, 'include', module_name, yang_file)
                self.find_yang_var(imports, 'import', module_name, yang_file)
                self.find_yang_var(reference, 'reference', module_name, yang_file)
                self.find_yang_var(schema, 'schema', module_name, yang_file)

                compilations_status[module_name] = self.parse_status(module_name, revision[module_name])
                author_email[module_name] = self.parse_email(module_name, revision[module_name])
                working_group[module_name] = self.parse_wg(module_name, revision[module_name])

                # If revision was not found in capability.xml file than look for it in yang file itself
                if '' in revision[module_name]:
                    self.find_yang_var(revision, 'revision', module_name, yang_file)

                self.prepare.add_key(module_name + '@' + revision[module_name] + '@' + namespace[module_name] + '@'
                                     + conformance_type[module_name])

                self.parse_imports_includes(includes[module_name]['name'],
                                            missing_module, missing_includes, features, revision,
                                            yang_version, namespace, prefix, organization, contact, description,
                                            includes, imports, reference, conformance_type, deviations, module_names,
                                            compilations_status, schema, author_email, working_group,
                                            organization_module, True, namespace[module_name])
                self.parse_imports_includes(imports[module_name], missing_module,
                                            missing_includes, features, revision,
                                            yang_version, namespace, prefix, organization, contact, description,
                                            includes, imports, reference, conformance_type, deviations, module_names,
                                            compilations_status, schema, author_email, working_group,
                                            organization_module, False, namespace[module_name])

        # restconf capability parsing
        for cap in self.root.iter('module'):
            module_name = cap.find('name').text
            module_names.append(module_name)
            namespace[module_name] = cap.find('namespace').text
            revision[module_name] = cap.find('revision').text
            schema[module_name] = cap.find('schema').text
            conformance_type[module_name] = cap.find('conformance-type').text
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
                missing_module[module_name] = module_name
                yang_file = find_first_file('/'.join(self.split[0:1]), module_name + '.yang',
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

        # write dictionary to file
        print('Making json dictionary and saving to file')

        # Create json dictionary out of parsed information
        with open('normal' + repr(self.index) + '.json', "w") as ietf_mode:
            json.dump({'vendor': self.vendor, 'os-type': self.os, 'os-version': self.os_version,
                       'platform': self.platform,
                       'feature-set': 'ALL',
                       'protocols': {
                           'protocol': [{
                               'name': 'netconf',
                               'capabilities': capability,
                               'netconf-version': netconf_version,
                           }]
                       },
                       'modules': {
                           'module': [
                               {
                                   'reference': reference.get(module_names[k]),
                                   'prefix': prefix.get(module_names[k]),
                                   'yang-version': yang_version.get(module_names[k]),
                                   'organization': organization_module.get(module_names[k]),
                                   'description': description.get(module_names[k]),
                                   'contact': contact.get(module_names[k]),
                                   'submodule': json.loads(
                                       self.get_submodule_info(includes[module_names[k]]['name'], missing_module)),
                                   # 'imports': json.loads(
                                   #    self.get_submodule_info(imports[module_names[k]]['name'], missing_module,
                                   #                            missing_includes)),
                                   'conformance-type': conformance_type.get(module_names[k]),
                                   'compilation-status': compilations_status.get(module_names[k]),
                                   'author-email': author_email.get(module_names[k]),
                                   'revision': revision.get(module_names[k]),
                                   'namespace': namespace.get(module_names[k]),
                                   'name': module_names[k],
                                   'schema': schema.get(module_names[k]),
                                   'feature': features.get(module_names[k]),
                                   'deviation': [
                                       {'name': deviations[module_names[k]]['name'][i],
                                        'revision': deviations[module_names[k]]['revision'][i]
                                        } for
                                       i, val in enumerate(deviations.get(module_names[k])['name'])],
                               }
                               for k, val in
                               enumerate(module_names)]
                       }
                       }, ietf_mode)

        print('missing imports')
        print(list(missing_module.keys()))
        print('missing submodules')
        print(list(missing_includes.keys()))
        print('missing revisions')
        print(self.missing_revision)
        print('\n')

    def get_submodule_info(self, imports_or_includes, missing_module):
        if imports_or_includes is not None and bool(imports_or_includes):
            revision = {}
            schema = {}

            for imp in imports_or_includes:
                yang_file = find_first_file('/'.join(self.split[0:-1]), imp + '.yang', imp + '@*.yang')
                if yang_file is None:
                    missing_module[imp] = imp
                    yang_file = find_first_file('/'.join(self.split[0:1]), imp + '.yang', imp + '@*.yang')
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

    def parse_imports_includes(self, imports_or_includes, missing_module, missing_includes, features,
                               revision, yang_version, namespace, prefix, organization, contact, description, includes,
                               imports, reference, conformance_type, deviations, module_names, comp_status, schema,
                               email, wg, organization_module, is_include, parent_ns):
        if imports_or_includes is not None:
            for imp in imports_or_includes:
                if imp not in module_names:
                    yang_file = find_first_file('/'.join(self.split[0:-1]), imp + '.yang', imp + '@*.yang')
                    if yang_file is None:
                        missing_module[imp] = imp
                        yang_file = find_first_file('/'.join(self.split[0:1]), imp + '.yang', imp + '@*.yang')
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
                        print(imp + ' : ' + namespace[imp])
                    self.find_yang_var(prefix, 'prefix', imp, yang_file)
                    self.find_yang_var(yang_version, 'yang-version', imp, yang_file)
                    self.find_yang_var(organization, 'organization', imp, yang_file)
                    self.find_yang_var(contact, 'contact', imp, yang_file)
                    self.find_yang_var(description, 'description', imp, yang_file)
                    self.find_yang_var(includes, 'include', imp, yang_file)
                    self.find_yang_var(imports, 'import', imp, yang_file)
                    self.find_yang_var(reference, 'reference', imp, yang_file)
                    self.find_yang_var(revision, 'revision', imp, yang_file)
                    self.find_yang_var(features, 'feature', imp, yang_file)
                    self.find_yang_var(schema, 'schema', imp, yang_file)

                    comp_status[imp] = self.parse_status(imp, revision[imp])
                    email[imp] = self.parse_email(imp, revision[imp])
                    wg[imp] = self.parse_wg(imp, revision[imp])
                    conformance_type[imp] = 'implement'
                    module_names.append(imp)

                    self.prepare.add_key(imp + '@' + revision[imp] + '@' + namespace[imp] + '@' + conformance_type[imp])

                    self.parse_imports_includes(includes[imp]['name'],
                                                missing_module, missing_includes, features, revision,
                                                yang_version, namespace, prefix, organization, contact, description,
                                                includes, imports, reference, conformance_type, deviations, module_names
                                                , comp_status, schema, email, wg, organization_module, True
                                                , namespace[imp])
                    self.parse_imports_includes(imports[imp], missing_module,
                                                missing_includes, features, revision,
                                                yang_version, namespace, prefix, organization, contact, description,
                                                includes, imports, reference, conformance_type, deviations, module_names
                                                , comp_status, schema, email, wg, organization_module, False
                                                , namespace[imp])

    def parse_status(self, module_name, revision):
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
        # try to find in draft without revision
        try:
            status = self.ietf_draft_json[module_name + '.yang'][3]
            return status
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            status = self.ietf_draft_json[module_name + '@' + revision + '.yang'][3]
            return status
        except KeyError:
            pass
        return 'missing element'

    def parse_email(self, module_name, revision):
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
        return 'missing element'

    def parse_wg(self, module_name, revision):
        # try to find in draft without revision
        try:
            wg = self.ietf_draft_json[module_name + '.yang'][0].split('</a>')[0].split('\">')[1].split('-')[1]
            return wg + 'working group'
        except KeyError:
            pass
        # try to find in draft with revision
        try:
            wg = \
                self.ietf_draft_json[module_name + '@' + revision + '.yang'][0].split('</a>')[0].split('\">')[1].split(
                    '-')[1]
            return wg + 'working group'
        except KeyError:
            pass
        return 'missing element'
