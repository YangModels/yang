import ConfigParser
import argparse
import json
import os
import subprocess
import tarfile
import urllib
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-path', type=str, default='../utility/config.ini',
                        help='Set path to config file')
    args = parser.parse_args()
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    api_ip = config.get('DraftPullLocal-Section', 'api-ip')
    api_port = config.get('DraftPullLocal-Section', 'api-port')
    confd_ip = config.get('DraftPullLocal-Section', 'confd-ip')
    confd_port = config.get('DraftPullLocal-Section', 'confd-port')
    credentials = config.get('DraftPullLocal-Section', 'credentials').split(' ')
    result_html_dir = config.get('DraftPullLocal-Section', 'result-html-dir')
    protocol = config.get('DraftPullLocal-Section', 'protocol')
    notify = config.get('DraftPullLocal-Section', 'notify-index')

    LOGGER.info('Loading all files from http://www.claise.be/IETFYANGDraft.json')
    ietf_draft_json = load_json_from_url('http://www.claise.be/IETFYANGDraft.json')

    response = urllib.urlretrieve('http://www.claise.be/YANG-RFC.tar', './rfc.tar')

    tar = tarfile.open('./rfc.tar')
    tar.extractall('../../standard/ietf/RFC')
    tar.close()
    with open("log.txt", "wr") as f:
        try:
            LOGGER.info('Calling populate script')
            arguments = ["python", "../parseAndPopulate/populate.py", "--sdo", "--port", confd_port, "--ip",
                         confd_ip, "--api-protocol", protocol, "--api-port", api_port, "--api-ip", api_ip,
                         "--dir", "../../standard/ietf/RFC", "--result-html-dir", result_html_dir,
                         "--credentials", credentials[0], credentials[1]]
            if notify == 'True':
                arguments.append("--notify-indexing")
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            LOGGER.error('Error calling process populate.py {}'.format(e.message))
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
        for x in range(len(files) - 1, -1, -1):
            if year[x] != latest:
                files_to_delete.append(files[x])
                files.remove(files[x])
                year.remove(year[x])
                month.remove(month[x])
                day.remove(day[x])

        latest = max(month)
        for x in range(len(files) - 1, -1, -1):
            if month[x] != latest:
                files_to_delete.append(files[x])
                files.remove(files[x])
                year.remove(year[x])
                month.remove(month[x])
                day.remove(day[x])
        latest = max(day)
        for x in range(len(files) - 1, -1, -1):
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
            arguments = ["python", "../parseAndPopulate/populate.py", "--sdo", "--port", confd_port, "--ip",
                         confd_ip, "--api-protocol", protocol, "--api-port", api_port, "--api-ip", api_ip,
                         "--dir", "../../experimental/ietf-extracted-YANG-modules", "--result-html-dir",
                         result_html_dir, "--credentials", credentials[0], credentials[1]]
            if notify == 'True':
                arguments.append("--notify-indexing")
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            LOGGER.error('Error calling process populate.py {}'.format(e.message))
