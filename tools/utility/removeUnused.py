import argparse
import math
import os
import shutil
import time

import datetime

import tools.utility.log as lo
from tools.utility import messageFactory

LOGGER = lo.get_logger('removeUnused')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--remove-dir', type=str,
                        default='.',
                        help='Set path to config file')
    parser.add_argument('--remove-dir2', type=str,
                        default='.',
                        help='Set path to yangsuite users')
    parser.add_argument('--remove-dir3', type=str,
                        default='/home/miroslav/yangsuite-users/',
                        help='Set path to yangsuite saved users')
    parser.add_argument('--logs-path', type=str,
                        default='.',
                        help='Set path to config file')
    args = parser.parse_args()
    mf = messageFactory.MessageFactory()
    LOGGER.info('Removing unused files')
    to_remove = []
    for root, dirs, files in os.walk(args.remove_dir):
        for fi_name in files:
            with open(args.logs_path, 'r') as f:
                remove = True
                for line in f:
                    if fi_name in line:
                        remove = False
                        break
                if remove:
                    remove_path = '{}/{}'.format(root, fi_name)
                    st = os.stat(remove_path)
                    c_time = st.st_ctime
                    c_time = time.time() - c_time
                    c_time = c_time / 60 / 60 / 24
                    if math.floor(c_time) != 0:
                        to_remove.append(remove_path)
    mf.send_removed_temp_diff_files()
    for remove in to_remove:
        try:
            os.remove(remove)
        except OSError as e:
            mf.send_automated_procedure_failed('Remove unused diff files',
                                               e.message)
    dirs = os.listdir(args.remove_dir2)
    for dir in dirs:
        abs = os.path.abspath(args.remove_dir2 + '/' + dir)
        if not abs.endswith('yangcat') and not abs.endswith('miott'):
            try:
                shutil.rmtree(abs)
            except:
                pass
    dirs = os.listdir(args.remove_dir3)
    for dir in dirs:
        abs = os.path.abspath(args.remove_dir3 + '/' + dir)
        if not abs.endswith('yangcatalog'):
            try:
                shutil.rmtree(abs)
            except:
                pass

    # removing correlation ids from file that are older than a day
    f = open('./../api/correlation_ids', 'r')
    lines = f.readlines()
    f.close()
    with open('./../api/correlation_ids', 'w') as f:
        for line in lines:
            line_datetime = line.split(' -')[0]
            t = datetime.datetime.strptime(line_datetime,
                                           "%a %b %d %H:%M:%S %Y")
            diff = datetime.datetime.now() - t
            if diff.days == 0:
                f.write(line)
