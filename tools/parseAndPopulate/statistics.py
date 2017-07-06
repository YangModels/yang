import fnmatch
import glob
import os


def find_missing_hello(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                if not any(".xml" in name for name in files):
                    yield root


class Statistics:
    useless_modules = {}
    missing_modules = {}
    missing_submodules = {}
    missing_revision = {}
    missing_wrong_namespaces = {}
    unique_modules_per_vendor = set()
    os = {}

    def __init__(self, path):
        Statistics.missing_modules[path] = set()
        Statistics.missing_submodules[path] = set()
        Statistics.missing_wrong_namespaces[path] = set()
        Statistics.missing_revision[path] = set()
        folder = path.split('/')
        os_type = '/'.join(path.split('/')[:-2])
        folder.remove(path.split('/')[-1])
        folder = '/'.join(folder)
        if os_type not in Statistics.os:
            Statistics.os[os_type] = set()
        if folder not in Statistics.useless_modules:
            Statistics.useless_modules[folder] = glob.glob(folder + '/*.yang')

    @staticmethod
    def add_platform(os_type, platform):
        Statistics.os[os_type].add(platform)

    @staticmethod
    def remove_one(key, value):
        new_key = key[:]
        new_key.remove(new_key[-1])
        new_key = '/'.join(new_key)
        if value in Statistics.useless_modules[new_key]:
            Statistics.useless_modules[new_key].remove(value)

    @staticmethod
    def dump():
        for key in Statistics.useless_modules:
            if len(Statistics.useless_modules[key]) > 0:
                print('\nfiles that are extra in folder ' + key + ':')
                print(', '.join([value.split('/')[-1] for value in Statistics.useless_modules[key]]))
        print('\n')
        for key in Statistics.missing_modules:
            print('\nmissing modules in hello message ' + key + ':')
            print(', '.join([value.split('/')[-1] for value in Statistics.missing_modules[key]]))
        print('\n')
        for key in Statistics.missing_submodules:
            print('\nmissing submodules in hello message ' + key + ':')
            print(', '.join([value.split('/')[-1] for value in Statistics.missing_submodules[key]]))
        print('\n')
        for key in Statistics.missing_revision:
            print('\nmissing revision in module in hello message ' + key + ':')
            print(', '.join([value.split('/')[-1] for value in Statistics.missing_revision[key]]))
        print('\n')
        for key in Statistics.missing_wrong_namespaces:
            print('\nmissing or wrong namespace in module in hello message ' + key + ':')
            for value in Statistics.missing_wrong_namespaces[key]:
                print(str(value))
        print('\n')

    @staticmethod
    def add_unique(modules_revision):
        Statistics.unique_modules_per_vendor.update(set(modules_revision))

    @staticmethod
    def remove_one(key, value):
        new_key = key[:]
        new_key.remove(new_key[-1])
        new_key = '/'.join(new_key)
        if value in Statistics.useless_modules[new_key]:
            Statistics.useless_modules[new_key].remove(value)

    @staticmethod
    def dumps(file):
        file.write('<!DOCTYPE html><html><body><h1>Yangcatalog statistics</h1>')
        file.write('<h3>YANG modules in directory but not present in any NETCONF hello message in that directory:</h3>')
        for key in Statistics.useless_modules:
            if len(Statistics.useless_modules[key]) > 0:
                file.write('<h5>' + key + ':</h5>')
                file.write('<p>' + ', '.join([value.split('/')[-1] for value in Statistics.useless_modules[key]])
                           + '</p>')
        file.write('<h3>YANG modules in NETCONF hello messages for a directory but the YANG modules is not present'
                   + ' in that directory:</h3>')
        for key in Statistics.missing_modules:
            file.write('<h5>' + key + ':</h5>')
            file.write('<p>' + ', '.join([value.split('/')[-1] for value in Statistics.missing_modules[key]]) + '</p>')
        file.write('<h3>YANG modules in NETCONF hello messages for a directory but their'
                   + ' submodules are missing:</h3>')
        for key in Statistics.missing_submodules:
            file.write('<h5>' + key + ':</h5>')
            file.write('<p>' + ', '.join([value.split('/')[-1] for value in Statistics.missing_submodules[key]])
                       + '</p>')
        file.write('<h3>YANG modules in NETCONF hello messages for a directory but their'
                   + ' revision date is missing:</h3>')
        for key in Statistics.missing_revision:
            file.write('<h5>' + key + ':</h5>')
            file.write('<p>' + ', '.join([value.split('/')[-1] for value in Statistics.missing_revision[key]]) + '</p>')

        file.write('<h3>YANG modules in NETCONF hello messages for a directory but their'
                   + ' namespace is wrong or missing:</h3>')
        for key in Statistics.missing_wrong_namespaces:
            file.write('<h5>' + key + ':</h5>')
            for value in Statistics.missing_wrong_namespaces[key]:
                file.write('<p>' + str(value) + '</p>')
        missing = []
        my_files = find_missing_hello('./../../vendor/', '*.yang')
        for name in set(my_files):
            if '.incompatible' not in name and 'MIBS' not in name:
                missing.append(name)
        missing = ', '.join(missing).replace('./../..', '')
        file.write('<h3>Folders with yang files but missing hello message inside of file:</h3><p>' + missing + '</p>')
        file.write('</body></html>')

    @staticmethod
    def add_submodule(path, value):
        Statistics.missing_submodules['/'.join(path)].add(value)

    @staticmethod
    def add_module(path, value):
        Statistics.missing_modules['/'.join(path)].add(value)

    @staticmethod
    def add_namespace(path, value):
        Statistics.missing_wrong_namespaces['/'.join(path)].add(value)

    @staticmethod
    def add_revision(path, value):
        Statistics.missing_revision['/'.join(path)].add(value)
