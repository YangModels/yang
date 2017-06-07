import fnmatch
import glob
import os
import unicodedata
import xml.etree.ElementTree as ET

import yangParser

NS_MAP = {
    "http://cisco.com/ns/yang/": "cisco",
    "http://www.huawei.com/netconf": "huawei",
    "http://openconfig.net/yang/": "openconfig",
    "http://tail-f.com/": "tail-f",
    "urn:ietf": "ietf",
    "urn:cisco": "cisco"
}


class Integrity:
    @staticmethod
    def deserialize(yang_variable):
        if isinstance(yang_variable, unicode):
            return unicodedata.normalize('NFKD', yang_variable).encode('ascii', 'ignore')
        else:
            return yang_variable

    @staticmethod
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

    def __init__(self, path, *capabilities):
        self.useless_modules = []
        self.missing_modules = set()
        self.missing_submodules = set()
        self.missing_wrong_namespaces = set()
        self.missing_revision = set()
        self.ctx = yangParser.create_context(path)
        self.parsed_yang = {}
        if path.endswith('/'):
            path = path[:-1]
        self.useless_modules = glob.glob(path + '/*.yang')
        for caps in capabilities:
            self.root = ET.parse(path + '/' + caps).getroot()
            tag = self.root.tag
            for cap in self.root.iter(tag.split('hello')[0] + 'capability'):
                if 'module=' in cap.text:
                    module_and_more = cap.text.split('module=')[1]
                    module_name = module_and_more.split('&')[0]
                    self.check(module_name, path)

    def check_namespace(self, path, namespace, module_name):
        namespace_exist = False
        for ns, org in NS_MAP.items():
            if '1651' in path.split('/'):
                if ns is 'urn:cisco':
                    if ns in namespace:
                        namespace_exist = True
            else:
                if ns in namespace:
                    namespace_exist = True
        if not namespace_exist:
            self.missing_wrong_namespaces.add(module_name + namespace)

    def check(self, module_name, path):
        module_path = Integrity.find_first_file(path, module_name + '.yang', module_name + '@*.yang')
        if module_path is None:
            self.missing_modules.add(module_name)
            return
        if module_path in self.useless_modules:
            self.useless_modules.remove(module_path)
        if module_name not in self.parsed_yang:
            self.parsed_yang[module_name] = yangParser.parse(os.path.abspath(module_path), self.ctx)
        namespace = None
        try:
            namespace = self.deserialize(self.parsed_yang[module_name].search('namespace')[0].arg)
        except IndexError:
            self.missing_wrong_namespaces.add(module_name + ': missing_data')
        try:
            self.deserialize(self.parsed_yang[module_name].search('revision')[0].arg)
        except IndexError:
            self.missing_revision.add(module_name)
        try:
            imports = self.parsed_yang[module_name].search('import')
            for imp in imports:
                self.check(self.deserialize(imp.arg), path)
        except IndexError:
            pass
        try:
            includes = self.parsed_yang[module_name].search('include')
            for include in includes:
                self.check_include(self.deserialize(include.arg), path)
        except IndexError:
            pass
        if namespace is not None:
            self.check_namespace(path, namespace, module_name)

    def check_include(self, include, path):
        module_path = Integrity.find_first_file(path, include + '.yang', include + '@*.yang')
        if module_path is None:
            self.missing_submodules.add(include)
        if module_path in self.useless_modules:
            self.useless_modules.remove(module_path)
        if include not in self.parsed_yang:
            self.parsed_yang[include] = yangParser.parse(os.path.abspath(module_path), self.ctx)
        try:
            self.deserialize(self.parsed_yang[include].search('revision')[0].arg)
        except IndexError:
            self.missing_revision.add(include)
        try:
            imports = self.parsed_yang[include].search('import')
            for imp in imports:
                self.check(self.deserialize(imp.arg), path)
        except IndexError:
            pass
        try:
            includes = self.parsed_yang[include].search('include')
            for include in includes:
                self.check_include(self.deserialize(include.arg), path)
        except IndexError:
            pass

    def get_misssing_modules(self):
        return self.missing_modules

    def get_misssing_revision(self):
        return self.missing_revision

    def get_misssing_submodules(self):
        return self.missing_submodules

    def get_misssing_wrong_namespace(self):
        return self.missing_wrong_namespaces

    def get_extra_modules(self):
        return self.useless_modules
