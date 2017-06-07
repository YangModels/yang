from __future__ import print_function

import fnmatch
import os
import time

import capability as cap
import integrityChecker
import prepare


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


def do_stats():
    integrity_file = open('integrity.html', 'w')
    stats_file = open('stats.html', 'w')
    integrity.dump()
    integrity.dumps(integrity_file)
    integrity_file.close()
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
    stats_file.write('<tr><td>IETF RFCs</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../standard/ietf/RFC/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>IETF drafts</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../standard/ietf/DRAFT/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>BBF</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../standard/bbf', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>IEEE</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../standard/ieee', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')

    stats_file.write('<tr><td>Openconfig</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../experimental/openconfig', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
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
    stats_file.write('</table>')

    stats_file.write('<table><tr>'
                     + '<th>Vendor</th>'
                     + '<th>number in github</th>'
                     + '<th>number in the catalog</th>'
                     + '<th>% that pass compile</th>'
                     + '<th>% with NETCONF capabilities</th>'
                     + '<th>% with extra metadata</th></tr>')
    stats_file.write('<tr><td>Cisco</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../vendor/cisco/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>Ciena</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../vendor/ciena/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>Brocade</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../vendor/brocade/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>Yumaworks</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../vendor/yumaworks/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>Juniper</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../vendor/juniper/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')

    stats_file.write('<tr><td>NetconfCentral</td>')
    stats_file.write('<td>' + repr(len(list(find_files('./../../vendor/netconfcentral/', '*.yang')))) + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td>')
    stats_file.write('<td>' + 'unknown' + '</td></tr>')
    stats_file.write('</table>')
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
    stats_file.write('<p>Number of yang files in bbf standard ' + repr(
        len(list(find_files('./../../standard/bbf/standard/', '*.yang')))) + '</p>')
    stats_file.write('<p>Number of yang files in ietf RFC ' + repr(
        len(list(find_files('./../../standard/ietf/RFC/', '*.yang')))) + '</p>')
    stats_file.write('<p>Number of yang files in bbf DRAFT ' + repr(
        len(list(find_files('./../../standard/bbf/draft/', '*.yang')))) + '</p>')
    stats_file.write(
        '<p>Number of yang files in ieee DRAFT ' + repr(len(list(find_files('./../../standard/ieee/', '*.yang'))))
        + '</p>')
    stats_file.write('<p>Number of yang files in ietf DRAFT ' + repr(
        len(list(find_files('./../../standard/ietf/DRAFT/', '*.yang')))) + '</p>')
    stats_file.write('<p>Number of unique files parsed into yangcatalog ' + repr(len(integrity.number_of_unique_modules))
                     + '</p>')

    missing = []
    my_files = find_missing_hello('./../../vendor/', '*.yang')
    for name in set(my_files):
        if '.incompatible' not in name and 'MIBS' not in name:
            missing.append(name)
    missing = ', '.join(missing).replace('./../..', '')
    stats_file.write('<h3>Folders with yang files but missing hello message inside of vendor:</h3><p>' + missing
                     + '</p>')
    stats_file.write('</body></html>')
    stats_file.close()


start = time.time()
index = 1
prepare = prepare.Prepare("prepare")
update = True
for filename in find_files('../../vendor/', '*capabilit*.xml'):
    try:
        file_modification = open('fileModificationDate/' + '-'.join(filename.split('/')[-4:]) + '.txt', 'rw')
        time_in_file = file_modification.readline()
        if time.strptime(time_in_file, '%a %b %d %H:%M:%S %Y') == time.ctime(os.path.getmtime(filename)):
            update = False
            file_modification.close()
        else:
            file_modification.seek(0)
            file_modification.write(time.ctime(os.path.getmtime(filename)))
            file_modification.truncate()
            file_modification.close()
    except IOError:
        file_modification = open('fileModificationDate/' + '-'.join(filename.split('/')[-4:]) + '.txt', 'w')
        file_modification.write(str(time.ctime(os.path.getmtime(filename))))
        file_modification.close()
    if update:
        integrity = integrityChecker.Integrity(filename)
        print('Found xml source:' + filename)
        capability = cap.Capability(filename, index, prepare, integrity)
        capability.parse_and_dump()
        index += 1


prepare.dump()
# for filename in find_files('../', '*restconf-capabilit*.xml'):
#    print('Found xml source:' + filename)
#    capability = cap.Capability(filename)
#    capability.parse_and_dump()
do_stats()
end = time.time()
print(end - start)
