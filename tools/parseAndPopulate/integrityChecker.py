import glob


class Integrity:
    useless_modules = {}
    missing_modules = {}
    missing_submodules = {}
    missing_revision = {}
    missing_wrong_namespaces = {}
    number_of_unique_modules = set()

    def __init__(self, path):
        Integrity.missing_modules[path] = set()
        Integrity.missing_submodules[path] = set()
        Integrity.missing_wrong_namespaces[path] = set()
        Integrity.missing_revision[path] = set()
        folder = path.split('/')
        folder.remove(path.split('/')[-1])
        folder = '/'.join(folder)
        if folder not in Integrity.useless_modules:
            Integrity.useless_modules[folder] = glob.glob(folder + '/*.yang')

    @staticmethod
    def add_unique(modules_revision):
        Integrity.number_of_unique_modules.update(set(modules_revision))

    @staticmethod
    def remove_one(key, value):
        new_key = key[:]
        new_key.remove(new_key[-1])
        new_key = '/'.join(new_key)
        if value in Integrity.useless_modules[new_key]:
            Integrity.useless_modules[new_key].remove(value)

    @staticmethod
    def dump():
        for key in Integrity.useless_modules:
            if len(Integrity.useless_modules[key]) > 0:
                print('\nfiles that are extra in folder ' + key + ':')
                print(', '.join([value.split('/')[-1] for value in Integrity.useless_modules[key]]))
        print('\n')
        for key in Integrity.missing_modules:
            print('\nmissing modules in hello message ' + key + ':')
            print(', '.join([value.split('/')[-1] for value in Integrity.missing_modules[key]]))
        print('\n')
        for key in Integrity.missing_submodules:
            print('\nmissing submodules in hello message ' + key + ':')
            print(', '.join([value.split('/')[-1] for value in Integrity.missing_submodules[key]]))
        print('\n')
        for key in Integrity.missing_revision:
            print('\nmissing revision in module in hello message ' + key + ':')
            print(', '.join([value.split('/')[-1] for value in Integrity.missing_revision[key]]))
        print('\n')
        for key in Integrity.missing_wrong_namespaces:
            print('\nmissing or wrong namespace in module in hello message ' + key + ':')
            for value in Integrity.missing_wrong_namespaces[key]:
                print(str(value))
        print('\n')

    @staticmethod
    def add_unique(modules_revision):
        Integrity.number_of_unique_modules.update(set(modules_revision))

    @staticmethod
    def remove_one(key, value):
        new_key = key[:]
        new_key.remove(new_key[-1])
        new_key = '/'.join(new_key)
        if value in Integrity.useless_modules[new_key]:
            Integrity.useless_modules[new_key].remove(value)

    @staticmethod
    def dumps(file):
        file.write('<!DOCTYPE html><html><body><h1>Yangcatalog statistics</h1>')
        file.write('<h3>YANG modules in directory but not present in any NETCONF hello message in that directory:</h3>')
        for key in Integrity.useless_modules:
            if len(Integrity.useless_modules[key]) > 0:
                file.write('<h5>' + key + ':</h5>')
                file.write('<p>' + ', '.join([value.split('/')[-1] for value in Integrity.useless_modules[key]])
                           + '</p>')
        file.write('<h3>YANG modules in NETCONF hello messages for a directory but the YANG modules is not present'
                   + ' in that directory:</h3>')
        for key in Integrity.missing_modules:
            file.write('<h5>' + key + ':</h5>')
            file.write('<p>' + ', '.join([value.split('/')[-1] for value in Integrity.missing_modules[key]]) + '</p>')
        file.write('<h3>YANG modules in NETCONF hello messages for a directory but their'
                   + ' submodules are missing:</h3>')
        for key in Integrity.missing_submodules:
            file.write('<h5>' + key + ':</h5>')
            file.write('<p>' + ', '.join([value.split('/')[-1] for value in Integrity.missing_submodules[key]])
                       + '</p>')
        file.write('<h3>YANG modules in NETCONF hello messages for a directory but their'
                   + ' revision date is missing:</h3>')
        for key in Integrity.missing_revision:
            file.write('<h5>' + key + ':</h5>')
            file.write('<p>' + ', '.join([value.split('/')[-1] for value in Integrity.missing_revision[key]]) + '</p>')

        file.write('<h3>YANG modules in NETCONF hello messages for a directory but their'
                   + ' namespace is wrong or missing:</h3>')
        for key in Integrity.missing_wrong_namespaces:
            file.write('<h5>' + key + ':</h5>')
            for value in Integrity.missing_wrong_namespaces[key]:
                file.write('<p>' + str(value) + '</p>')
        file.write('</body></html>')

    @staticmethod
    def add_submodule(path, value):
        Integrity.missing_submodules['/'.join(path)].add(value)

    @staticmethod
    def add_module(path, value):
        Integrity.missing_modules['/'.join(path)].add(value)

    @staticmethod
    def add_namespace(path, value):
        Integrity.missing_wrong_namespaces['/'.join(path)].add(value)

    @staticmethod
    def add_revision(path, value):
        Integrity.missing_revision['/'.join(path)].add(value)
