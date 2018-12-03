from __future__ import print_function

import ConfigParser
import argparse
import fnmatch
import os
import time

import capability as cap
import prepare
import statistics
import tools.utility.log as log
from tools.utility.util import get_curr_dir

LOGGER = log.get_logger('runCapabilities', '/home/miroslav/log/populate/yang.log')


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
    config = ConfigParser.ConfigParser()
    config.read('../utility/config.ini')
    path = config.get('Statistics-Section', 'file-location')
    integrity_file = open('{}/integrity.html'.format(path), 'w')
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
    parser.add_argument('--run-integrity', action='store_true', default=False,
                        help='If we are running integrity tool')
    parser.add_argument('--json-dir', type=str, help='Directory where json files to populate confd will be stored')
    parser.add_argument('--result-html-dir', default='/home/miroslav/results/', type=str,
                        help='Set dir where to write html result files. Default -> /home/miroslav/results/')
    parser.add_argument('--save-file-dir', default='/home/miroslav/results/',
                        type=str, help='Directory where the file will be saved')
    parser.add_argument('--api-protocol', type=str, default='https',
                        help='Whether api runs on http or https.'
                             ' Default is set to http')
    parser.add_argument('--api-port', default=8443, type=int,
                        help='Set port where the api is started. Default -> 8443')
    parser.add_argument('--api-ip', default='yangcatalog.org', type=str,
                        help='Set ip address where the api is started. Default -> yangcatalog.org')
    parser.add_argument('--config-path', type=str,
                        default='../utility/config.ini',
                        help='Set path to config file')

    args = parser.parse_args()
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    is_uwsgi = config.get('General-Section', 'uwsgi')
    private_credentials = config.get('General-Section', 'private-secret').split(' ')
    separator = ':'
    suffix = args.api_port
    if is_uwsgi == 'True':
        separator = '/'
        suffix = 'api'
    yangcatalog_api_prefix = '{}://{}{}{}/'.format(args.api_protocol,
                                                   args.api_ip, separator,
                                                   suffix)
    start = time.time()
    index = 1
    integrity = None
    sdo = args.sdo
    search_dirs = [args.dir]

    if sdo:
        stats_list = {'sdo': search_dirs}
    else:
        stats_list = {'vendor': search_dirs}
    if args.run_integrity:
        stats_list = {'vendor': [get_curr_dir(__file__) + '/../../vendor/cisco']}
    LOGGER.info('Starting to iterate through files')
    for key in stats_list:
        search_dirs = stats_list[key]
        if key == 'sdo':
            sdo = True
            prepare_sdo = prepare.Prepare("prepare", yangcatalog_api_prefix)
            for search_dir in search_dirs:

                LOGGER.info('Found directory for sdo {}'.format(search_dir))
                integrity = statistics.Statistics(search_dir)

                capability = cap.Capability(search_dir, index, prepare_sdo,
                                            integrity, args.api, sdo,
                                            args.json_dir, args.result_html_dir,
                                            args.save_file_dir, private_credentials)
                LOGGER.info('Starting to parse files in sdo directory')
                capability.parse_and_dump_sdo()
                index += 1
            prepare_sdo.dump_modules(args.json_dir)
        else:
            sdo = False
            prepare_vendor = prepare.Prepare("prepare", yangcatalog_api_prefix)
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
                                    LOGGER.info('{} is not modified. Skipping this file'.format(filename))
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
                            LOGGER.info('Found xml source {}'.format(filename))
                            if args.run_integrity:
                                prepare_vendor = prepare.Prepare("prepare",
                                                                 yangcatalog_api_prefix)
                                capability = cap.Capability(filename, index,
                                                            prepare_vendor,
                                                            integrity, args.api,
                                                            sdo, args.json_dir,
                                                            args.result_html_dir,
                                                            args.save_file_dir,
                                                            private_credentials,
                                                            args.run_integrity)
                            if 'ietf-yang-library' in pattern:
                                capability.parse_and_dump_yang_lib()
                            else:
                                capability.parse_and_dump()
                            index += 1
            if not args.run_integrity:
                prepare_vendor.dump_modules(args.json_dir)
                prepare_vendor.dump_vendors(args.json_dir)

    if integrity is not None and args.run_integrity:
        create_integrity()
    end = time.time()
    LOGGER.info('Time taken to parse all the files {} seconds'.format(end - start))
