import os

from tools.parseAndPopulate.modules import Modules
from tools.utility.util import get_curr_dir

if __name__ == '__main__':
    for root, subdirs, files in os.walk(get_curr_dir(__file__) + '/../../.'):
        for f in files:
            if f.endswith('.yang'):
                name = f.split('@')[0].split('.')[0]
                mod = Modules(root + '/' + f, None, None, None)
                mod.parse_all(name, 'foo', None, '/home/miroslav/results/')
