import fnmatch
import os

from tools.utility import yangParser
import tools.utility.log as log
from tools.utility.util import get_curr_dir

LOGGER = log.get_logger('dependencies', '/home/miroslav/log/populate/yang.log')


def search_dependencies(base):
    for root, dirs, files in os.walk(base):
        for basename in files:
            if fnmatch.fnmatch(basename, '*.yang'):
                filename = os.path.join(root, basename)
                LOGGER.info('Parsing file {}'.format(filename))
                try:
                    yangFile = yangParser.parse(os.path.abspath(filename))
                    try:
                        revision = yangFile.search('revision')[0].arg
                    except:
                        revision = '1970-01-01'
                    name = filename.split('/')[-1].split('.')[0].split('@')[0]
                    key = '{}@{}.yang'.format(name, revision)
                    if key not in dependencies:
                        dependencies[key] = set()
                    yangImport = yangFile.search('import')
                    yangInclude = yangFile.search('include')
                    for imp in yangImport:
                        impName = imp.arg
                        impRev = None
                        for sub in imp.substmts:
                            if sub.keyword == 'revision-date':
                                impRev = sub.arg
                        if impRev:
                            name_rev = '{}@{}'.format(impName, impRev)
                            dependencies[key].add(name_rev)
                            if name_rev not in dependants:
                                dependants[name_rev] = set()
                            dependants[name_rev].add(key)
                        else:
                            dependencies[key].add(impName)
                            if impName not in dependants:
                                dependants[impName] = set()
                            dependants[impName].add(key)
                    for inc in yangInclude:
                        incName = inc.arg
                        incRev = None
                        for sub in inc.substmts:
                            if sub.keyword == 'revision-date':
                                incRev = sub.arg
                        if incRev:
                            name_rev = '{}@{}'.format(incName, incRev)
                            dependencies[key].add(name_rev)
                            if name_rev not in dependants:
                                dependants[name_rev] = set()
                            dependants[name_rev].add(key)
                        else:
                            dependencies[key].add(incName)
                            if incName not in dependants:
                                dependants[incName] = set()
                            dependants[incName].add(key)
                except:
                    pass


if __name__ == "__main__":
    dependencies = {}
    dependants = {}
    for dir in [get_curr_dir(__file__) + '/../../experimental',
                get_curr_dir(__file__) + '/../../standard',
                get_curr_dir(__file__) + '/../../vendor']:
        search_dependencies(dir)
    pass
