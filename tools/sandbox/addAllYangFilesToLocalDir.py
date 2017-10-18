import os

from tools.parseAndPopulate.modules import Modules

if __name__ == '__main__':
    for root, subdirs, files in os.walk('../../.'):
        for f in files:
            if f.endswith('.yang'):
                name = f.split('@')[0].split('.')[0]
                mod = Modules(root + '/' + f, None, None, None)
                mod.parse_all(name, None, '/home/miroslav/results/')