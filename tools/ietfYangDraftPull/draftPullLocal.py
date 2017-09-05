import json
import os
import subprocess
import urllib2

from numpy.f2py.auxfuncs import throw_error

import tools.utility.log as log

LOGGER = log.get_logger('draftPullLocal')


def load_json_from_url(url):
    failed = True
    loaded_json = None
    tries = 10
    while failed:
        try:
            response = urllib2.urlopen(url).read()
            loaded_json = json.loads(response)
            failed = False
        except:
            tries -= 1
            if tries == 0:
                failed = False
            pass
    if tries == 0:
        raise throw_error('Couldn`t open a json file from url: ' + url)
    return loaded_json


if __name__ == "__main__":
    LOGGER.info('Starting Cron job IETF pull request local')

    LOGGER.info('Loading all files from http://www.claise.be/IETFYANGDraft.json')
    ietf_draft_json = load_json_from_url('http://www.claise.be/IETFYANGDraft.json')

    for key in ietf_draft_json:
        yang_file = open('../../experimental/ietf-extracted-YANG-modules/' + key, 'w+')
        yang_download_link = ietf_draft_json[key][2].split('href="')[1].split('">Download')[0]
        try:
            yang_raw = urllib2.urlopen(yang_download_link).read()
            yang_file.write(yang_raw)
        except:
            LOGGER.warning('{} - {}'.format(key, yang_download_link))
            yang_file.write('')
        yang_file.close()
    for f in os.listdir('../../experimental/ietf-extracted-YANG-modules/'):
        fname = f.split('.yang')[0].split('@')[0]
        files = []
        year = []
        month = []
        day = []
        for f2 in os.listdir('../../experimental/ietf-extracted-YANG-modules/'):
            if f2.startswith(fname):
                if f2.split(fname)[1].startswith('.') or f2.split(fname)[1].startswith('@'):
                    files.append(f2)
                    revision = f2.split(fname)[1].split('.')[0].replace('@', '')
                    year.append(int(revision.split('-')[0]))
                    month.append(int(revision.split('-')[1]))
                    day.append(int(revision.split('-')[2]))
        latest = max(year)
        files_to_delete = []
        remove = []
        for x in range(len(files)-1, -1, -1):
            if year[x] != latest:
                files_to_delete.append(files[x])
                files.remove(files[x])
                year.remove(year[x])
                month.remove(month[x])
                day.remove(day[x])

        latest = max(month)
        for x in range(len(files)-1, -1, -1):
            if month[x] != latest:
                files_to_delete.append(files[x])
                files.remove(files[x])
                year.remove(year[x])
                month.remove(month[x])
                day.remove(day[x])
        latest = max(day)
        for x in range(len(files)-1, -1, -1):
            if day[x] != latest:
                files_to_delete.append(files[x])
                files.remove(files[x])
                year.remove(year[x])
                month.remove(month[x])
                day.remove(day[x])
        for fi in files_to_delete:
            os.remove('../../experimental/ietf-extracted-YANG-modules/' + fi)

    with open("log.txt", "wr") as f:
        try:
            LOGGER.info('Calling populate script')
            subprocess.check_call(["python", "../parseAndPopulate/populate.py", "--sdo", "--port", "8008", "--ip", "yangcatalog.org",
                                   "--api-protocol", "https", "--api-port", "8443", "--api-ip", "yangcatalog.org",
                                   "--dir", "../../experimental/ietf-extracted-YANG-modules"], stderr=f)
        except subprocess.CalledProcessError as e:
            LOGGER.error('Error calling process populate.py {}'.format(e.message))

