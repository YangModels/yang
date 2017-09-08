from __future__ import print_function

import argparse
import fnmatch
import os
import time

import capability as cap
import prepare
import statistics
import tools.utility.log as log

LOGGER = log.get_logger('runCapabilities')


def find_missing_hello(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                if not any(".xml" in name for name in files):
                    yield root


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def create_integrity():
    integrity_file = open('integrity.html', 'w')
    integrity.dump()
    integrity.dumps(integrity_file)
    integrity_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='../../vendor', type=str,
                        help='Set dir where to look for hello message xml files. Default -> ../../vendor')
    parser.add_argument('--save-modification-date', action='store_true', default=False,
                        help='if True than it will create a file with modification date and also it will check if '
                             'file was modified from last time if not it will skip it.')
    parser.add_argument('--api', action='store_true', default=False, help='if we are doing apis')
    parser.add_argument('--sdo', action='store_true', default=False, help='if we are doing sdos')
    parser.add_argument('--run-statistics', action='store_true', default=False, help='if we are running statistics. '
                                                                                     'Also if this is true it will run'
                                                                                     ' all -SDOs and Vendors brought '
                                                                                     'via api or not')
    parser.add_argument('--json-dir', type=str, help='Directory where json files to populate confd will be stored')
    parser.add_argument('--result-html-dir', default='/home/miroslav/results/', type=str,
                        help='Set dir where to write html result files. Default -> /home/miroslav/results/')

    args = parser.parse_args()
    start = time.time()
    index = 1

    integrity = None
    sdo = args.sdo
    search_dirs = [args.dir]

    if sdo:
        stats_list = {'sdo': search_dirs}
    else:
        stats_list = {'vendor': search_dirs}
    if args.run_statistics:
        stats_list = {'sdo': ['../../experimental', '../../standard'], 'vendor': ['../../vendor']}
    LOGGER.info('Starting to iterate through files')
    for key in stats_list:
        search_dirs = stats_list[key]
        if key == 'sdo':
            sdo = True
            prepare_sdo = prepare.Prepare("prepare", args.result_html_dir)
            for search_dir in search_dirs:

                LOGGER.info('Found directory for sdo {}'.format(search_dir))
                integrity = statistics.Statistics(search_dir)
                capability = cap.Capability(search_dir, index, prepare_sdo, integrity, args.api, sdo, args.json_dir)
                LOGGER.info('Starting to parse files in sdo directory')
                capability.parse_and_dump_sdo()
                index += 1
            prepare_sdo.dump_sdo(args.json_dir)
        else:
            sdo = False
            prepare_vendor = prepare.Prepare("prepare", args.result_html_dir)
            for search_dir in search_dirs:
                patterns = ['*ietf-yang-library*.xml', '*capabilit*.xml']
                for pattern in patterns:
                    for filename in find_files(search_dir, pattern):
                        update = True
                        if not args.api and args.save_modification_date:
                            try:
                                file_modification = open('fileModificationDate/' + '-'.join(filename.split('/')[-4:]) +
                                                         '.txt', 'rw')
                                time_in_file = file_modification.readline()
                                if time_in_file in str(time.ctime(os.path.getmtime(filename))):
                                    update = False
                                    LOGGER.warning('{} is not modified. Skipping this file'.format(filename))
                                    file_modification.close()
                                else:
                                    file_modification.seek(0)
                                    file_modification.write(time.ctime(os.path.getmtime(filename)))
                                    file_modification.truncate()
                                    file_modification.close()
                            except IOError:
                                file_modification = open('fileModificationDate/' + '-'.join(filename.split('/')[-4:]) +
                                                         '.txt', 'w')
                                file_modification.write(str(time.ctime(os.path.getmtime(filename))))
                                file_modification.close()
                        if update:
                            integrity = statistics.Statistics(filename)
                            LOGGER.warning('Found xml source {}'.format(filename))
                            capability = cap.Capability(filename, index, prepare_vendor, integrity, args.api, sdo,
                                                        args.json_dir)
                            if 'ietf-yang-library' in pattern:
                                capability.parse_and_dump_yang_lib()
                            else:
                                capability.parse_and_dump()
                            index += 1
            prepare_vendor.dump(args.json_dir)

    if integrity is not None:
        create_integrity()
    end = time.time()
    LOGGER.info('Time taken to parse all the files {} seconds'.format(end - start))
    if args.run_statistics:
        for item in os.listdir('./'):
            if item.endswith(".json") or ('log' in item and '.txt' in item):
                LOGGER.debug('Removing file {}'.format(item))
                os.remove(item)
