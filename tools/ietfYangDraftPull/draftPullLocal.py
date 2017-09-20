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
from tools.utility import yangParser

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


def check_name_no_revision_exist(directory):
    LOGGER.info('Checking revision for directory: {}'.format(directory))
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if '@' in basename:
                yang_file_name = basename.split('@')[0] + '.yang'
                revision = basename.split('@')[1].split('.')[0]
                exists = os.path.exists(directory + yang_file_name)
                if exists:
                    parsed_yang = yangParser.parse(os.path.abspath(directory + yang_file_name))
                    comapred_revision = parsed_yang.search('revision')[0].arg
                    if revision == comapred_revision:
                        os.remove(directory + yang_file_name)


def check_early_revisions(directory):
    for f in os.listdir(directory):
        fname = f.split('.yang')[0].split('@')[0]
        files = []
        year = []
        month = []
        day = []
        for f2 in os.listdir(directory):
            if f2.startswith(fname) and '@' in f2:
                if f2.split(fname)[1].startswith('.') or f2.split(fname)[1].startswith('@'):
                    files.append(f2)
                    revision = f2.split(fname)[1].split('.')[0].replace('@', '')
                    year.append(int(revision.split('-')[0]))
                    month.append(int(revision.split('-')[1]))
                    day.append(int(revision.split('-')[2]))
        latest = max(year)
        files_to_delete = []
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
            os.remove(directory + fi)


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
    os.remove('./rfc.tar')
    check_name_no_revision_exist('../../standard/ietf/RFC/')
    check_early_revisions('../../standard/ietf/RFC/')
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
    check_name_no_revision_exist('../../experimental/ietf-extracted-YANG-modules/')
    check_early_revisions('../../experimental/ietf-extracted-YANG-modules/')

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
