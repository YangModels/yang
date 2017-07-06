from __future__ import print_function

import argparse
import fnmatch
import os
import time

import capability as cap
import statistics
import prepare
import yangIntegrity
from tools.parseAndPopulate import statisticsInCatalog


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


def do_stats():
    stats_file = open('stats.html', 'w')
    unique_files = set()
    files = find_files('./../../vendor/', '*.yang')
    for file in files:
        name = file.split('/')[-1]
        unique_files.add(name)

    stats_file.write('<!DOCTYPE html><html><body>'
                     + '<style>table { font-family: arial, sans-serif; border-collapse: collapse;  width: 100%;}'
                     + 'td, th {border: 1px solid #dddddd; text-align: left;padding: 8px;}'
                     + '</style></head>')
    stats_file.write('<table><tr>'
                     + '<th>SDOs and Opensource</th>'
                     + '<th>number in github</th>'
                     + '<th>number in the catalog</th>'
                     + '<th>% that pass compile</th>'
                     + '<th>% with metadata</th></tr>')
    count = len(list(find_files('./../../standard/ietf/RFC/', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('standard/ietf/RFC') / float(count)) * 100, 2))
    stats_file.write('<tr><td>IETF RFCs</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('standard/ietf/RFC')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    count = len(list(find_files('./../../standard/ietf/DRAFT/', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('standard/ietf/DRAFT') / float(count)) * 100, 2))
    stats_file.write('<tr><td>IETF drafts</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('standard/ietf/DRAFT')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    count = len(list(find_files('./../../standard/bbf/standard', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('standard/bbf/standard') / float(count)) * 100))
    stats_file.write('<tr><td>BBF standard</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('standard/bbf/standard')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    count = len(list(find_files('./../../standard/bbf/draft', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('standard/bbf/draft') / float(count)) * 100))
    stats_file.write('<tr><td>BBF draft</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('standard/bbf/draft')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    count = len(list(find_files('./../../standard/ieee/802.1', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('standard/ieee/802.1') / float(count)) * 100))
    stats_file.write('<tr><td>IEEE 802.1 with par</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('standard/ieee/802.1')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')

    count = len(list(find_files('./../../experimental/ieee/802.1', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('experimental/ieee/802.1') / float(count)) * 100))
    stats_file.write('<tr><td>IEEE 802.1 no par</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('experimental/ieee/802.1')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')

    count = len(list(find_files('./../../standard/ieee/802.3', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('standard/ieee/802.3') / float(count)) * 100))
    stats_file.write('<tr><td>IEEE 802.3 with par</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('standard/ieee/802.3')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')

    count = len(list(find_files('./../../experimental/ieee/802.3', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('experimental/ieee/802.3') / float(count)) * 100))
    stats_file.write('<tr><td>IEEE 802.3 no par</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('experimental/ieee/802.3')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')

    count = len(list(find_files('./../../standard/ieee/draft', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('standard/ieee/draft') / float(count)) * 100))
    stats_file.write('<tr><td>IEEE draft with par</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('standard/ieee/draft')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')

    count = len(list(find_files('./../../experimental/openconfig', '*.yang')))
    if count is 0:
        percent = repr(0)
    else:
        percent = repr(round((statistics_in_catalog.get_passed('experimental/openconfig') / float(count)) * 100))
    stats_file.write('<tr><td>Openconfig</td>')
    stats_file.write('<td>' + repr(count) + '</td>')
    stats_file.write('<td>' + repr(statistics_in_catalog.get_in_catalog('experimental/openconfig')) + '</td>')
    stats_file.write('<td>' + percent + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>MEF standard</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>MEF draft</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')
    stats_file.write('</table></p>')

    stats_file.write('<table><tr>'
                     + '<th>Vendor</th>'
                     + '<th>number in github</th>'
                     + '<th>number in the catalog</th>'
                     + '<th>% that pass compile</th>'
                     + '<th>% with extra metadata</th></tr>')

    generator = os.walk('./../../vendor/')

    directories = next(generator)[1]
    for vendor in directories:
        files_counter = 0
        for key in integrity.useless_modules:
            if vendor in key:
                files_counter += len(integrity.useless_modules[key])

        missing = []
        missing_folders = find_missing_hello('./../../vendor/' + vendor, '*.yang')
        for name in set(missing_folders):
            if '.incompatible' not in name and 'MIBS' not in name:
                missing.append(name)
        for missing_folder in missing:
            files_counter += len(list(find_files(missing_folder, '*.yang')))
        number_of_yang_files = len(list(find_files('./../../vendor/' + vendor, '*.yang')))
        number_in_catalog = number_of_yang_files - files_counter

        stats_file.write('<tr><td>' + vendor + '</td>')
        stats_file.write('<td>' + repr(number_of_yang_files) + '</td>')
        stats_file.write('<td>' + repr(number_in_catalog) + '</td>')
        stats_file.write('<td>' + 'in progress' + '</td>')
        stats_file.write('<td>' + 'unknown' + '</td></tr>')
    stats_file.write('</table></p>')

    for key in integrity.os:
        generator = os.walk(key)
        directories = next(generator)[1]
        platforms = []
        stats_file.write('<table><tr><th>' + key.split('/')[-1] + ' - version\platform</th>')
        for platform in list(integrity.os[key]):
            stats_file.write('<th>' + platform + '</th>')
            platforms.append(platform)
        stats_file.write('</tr>')
        for directory in directories:
            stats_file.write('<tr>')
            for x in range(0, len(platforms) + 1):
                if x is 0:
                    stats_file.write('<th>' + directory + '</th>')
                else:
                    exist = False
                    for xml in find_files(key + '/' + directory, '*.xml'):
                        if platforms[x-1] in xml:
                            exist = True
                    if exist:
                        stats_file.write('<td>X</td>')
                    else:
                        stats_file.write('<td>O</td>')
            stats_file.write('</tr>')
        stats_file.write('</table></p>')

    stats_file.write('<h3>Basic statistics:</h3>'
                     + '<p>Number of yang files in vendor '
                     + repr(len(list(find_files('./../../vendor/', '*.yang')))) + '</p>')
    stats_file.write('<p>Number of yang files in vendor no duplicates ' + repr(len(unique_files)) + '</p>')
    stats_file.write('<p>Number of yang files in standard all together ' + repr(
        len(list(find_files('./../../standard/', '*.yang')))) + '</p>')
    unique_files = set()
    files = find_files('./../../standard/', '*.yang')
    for file in files:
        name = file.split('/')[-1]
        unique_files.add(name)
    stats_file.write('<p>Number of yang files in standard all together no duplicates ' + repr(len(unique_files))
                     + '</p>')
    stats_file.write('<p>Number of unique files parsed into yangcatalog ' +
                     repr(len(integrity.unique_modules_per_vendor)) + '</p>')
    stats_file.write('</body></html>')
    stats_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='../../vendor', type=str,
                        help='Set dir where to look for hello message xml files.Default -> ../../vendor')
    parser.add_argument('--save-modification-date', action='store_true', default=False,
                        help='if True than it will create a file with modification date and also it will check if '
                             'file was modified from last time if not it will skip it.')
    parser.add_argument('--api', action='store_true', default=False, help='if we are doing apis')
    parser.add_argument('--sdo', action='store_true', default=False, help='if we are doing sdos')
    parser.add_argument('--run-statistics', action='store_true', default=False, help='if we are running statistics. '
                                                                                     'Also if this is true it will run'
                                                                                     ' all -SDOs and Vendors brought '
                                                                                     'via api or not')
    args = parser.parse_args()
    start = time.time()
    index = 1

    integrity = None
    statistics_in_catalog = None
    sdo = args.sdo
    search_dirs = [args.dir]

    if sdo:
        stats_list = {'sdo': search_dirs}
    else:
        stats_list = {'vendor': search_dirs}
    if args.run_statistics:
        stats_list = {'sdo': ['../../experimental', '../../standard',  '../../api/sdo'], 'vendor': ['../../vendor',
                      '../../api/vendor']}
    statistics_in_catalog = statisticsInCatalog.StatisticsInCatalog()
    for key in stats_list:
        search_dirs = stats_list[key]
        if key == 'sdo':
            sdo = True
            prepare_sdo = prepare.Prepare("prepare-sdo")
            for search_dir in search_dirs:

                print('Found dir:' + search_dir)
                capability = cap.Capability(search_dir, index, prepare_sdo, integrity, args.api, sdo,
                                            args.run_statistics, statistics_in_catalog)
                capability.parse_and_dump_sdo()
                index += 1
            prepare_sdo.dump_sdo()
        else:
            sdo = False
            prepare_vendor = prepare.Prepare("prepare")
            for search_dir in search_dirs:
                for filename in find_files(search_dir, '*capabilit*.xml'):
                    update = True
                    if not args.api and args.save_modification_date:
                        try:
                            file_modification = open('fileModificationDate/' + '-'.join(filename.split('/')[-4:]) +
                                                     '.txt', 'rw')
                            time_in_file = file_modification.readline()
                            if time_in_file in str(time.ctime(os.path.getmtime(filename))):
                                update = False
                                print (filename + ' is not modified. Skipping this file.')
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
                        print('Found xml source:' + filename)
                        capability = cap.Capability(filename, index, prepare_vendor, integrity, args.api, sdo,
                                                    args.run_statistics)
                        capability.parse_and_dump()
                        index += 1
            prepare_vendor.dump()

    # for filename in find_files('../', '*restconf-capabstatisticilit*.xml'):
    #    print('Found xml source:' + filename)
    #    capability = cap.Capability(filename)
    #    capability.parse_and_dump()
    if integrity is not None:
        create_integrity()
    if statistics_in_catalog is not None and args.run_statistics:
        do_stats()
    end = time.time()
    print(end - start)
    if args.run_statistics:
        for item in os.listdir('./'):
            if item.endswith(".json") or ('log' in item and '.txt' in item):
                os.remove(item)
