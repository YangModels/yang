import ConfigParser
import argparse
import os
import subprocess
import tarfile
import urllib2
from datetime import datetime

import requests

import tools.utility.log as log
from tools.utility import yangParser
from tools.utility.util import get_curr_dir

LOGGER = log.get_logger('draftPullLocal', '/home/miroslav/log/jobs/yang.log')

def get_latest_revision(f):
    stmt = yangParser.parse(f)

    rev = stmt.search_one('revision')
    if rev is None:
        return None

    return rev.arg


def check_name_no_revision_exist(directory):
    LOGGER.info('Checking revision for directory: {}'.format(directory))
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if '@' in basename:
                yang_file_name = basename.split('@')[0] + '.yang'
                revision = basename.split('@')[1].split('.')[0]
                exists = os.path.exists(directory + yang_file_name)
                if exists:
                    compared_revision = get_latest_revision(os.path.abspath(directory + yang_file_name))
                    if compared_revision is None:
                        continue
                    if revision == compared_revision:
                        os.remove(directory + yang_file_name)


def check_early_revisions(directory):
    for f in os.listdir(directory):
        fname = f.split('.yang')[0].split('@')[0]
        files_to_delete = []
        revisions = []
        for f2 in os.listdir(directory):
            if f2.split('.yang')[0].split('@')[0] == fname:
                if f2.split(fname)[1].startswith('.') or f2.split(fname)[1].startswith('@'):
                    files_to_delete.append(f2)
                    revision = f2.split(fname)[1].split('.')[0].replace('@', '')
                    if revision == '':
                        revision = get_latest_revision(os.path.abspath(directory + f2))
                        if revision is None:
                            continue
                    year = int(revision.split('-')[0])
                    month = int(revision.split('-')[1])
                    day = int(revision.split('-')[2])
                    try:
                        revisions.append(datetime(year, month, day))
                    except Exception:
                        LOGGER.error('Failed to process revision for {}: (rev: {})'.format(f2, revision))
                        if month == 2 and day == 29:
                            revisions.append(datetime(year, month, 28))
        if len(revisions) == 0:
            continue
        latest = revisions.index(max(revisions))
        files_to_delete.remove(files_to_delete[latest])
        for fi in files_to_delete:
            if 'iana-if-type' in fi:
                break
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
    api_port = config.get('General-Section', 'api-port')
    confd_ip = config.get('General-Section', 'confd-ip')
    confd_port = config.get('General-Section', 'confd-port')
    credentials = config.get('General-Section', 'credentials').split(' ')
    result_html_dir = config.get('DraftPullLocal-Section', 'result-html-dir')
    protocol = config.get('General-Section', 'protocol-api')
    notify = config.get('DraftPullLocal-Section', 'notify-index')
    save_file_dir = config.get('DraftPullLocal-Section', 'save-file-dir')
    private_credentials = config.get('General-Section', 'private-secret').split(' ')
    LOGGER.info('Loading all files from https://new.yangcatalog.org/private/IETFDraft.json')
    ietf_draft_json = requests.get('https://new.yangcatalog.org/private/IETFDraft.json'
                                   , auth=(private_credentials[0], private_credentials[1])).json()
    response = requests.get('https://new.yangcatalog.org/private/YANG-RFC.tgz'
                            , auth=(private_credentials[0], private_credentials[1]))
    zfile = open(get_curr_dir(__file__) + '/rfc.tgz', 'wb')
    zfile.write(response.content)
    zfile.close()
    tgz = tarfile.open(get_curr_dir(__file__) + '/rfc.tgz')
    tgz.extractall(get_curr_dir(__file__) + '/../../standard/ietf/RFC')
    tgz.close()
    os.remove(get_curr_dir(__file__) + '/rfc.tgz')
    check_name_no_revision_exist(get_curr_dir(__file__) + '/../../standard/ietf/RFC/')
    check_early_revisions(get_curr_dir(__file__) + '/../../standard/ietf/RFC/')
    with open("log.txt", "wr") as f:
        try:
            LOGGER.info('Calling populate script')
            arguments = ["python", "../parseAndPopulate/populate.py", "--sdo", "--port", confd_port, "--ip",
                         confd_ip, "--api-protocol", protocol, "--api-port", api_port, "--api-ip", api_ip,
                         "--dir", get_curr_dir(__file__) + "/../../standard/ietf/RFC", "--result-html-dir", result_html_dir,
                         "--credentials", credentials[0], credentials[1],
                         "--save-file-dir", save_file_dir]
            if notify == 'True':
                arguments.append("--notify-indexing")
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            LOGGER.error('Error calling process populate.py {}'.format(e.message))
    for key in ietf_draft_json:
        yang_file = open(get_curr_dir(__file__) + '/../../experimental/ietf-extracted-YANG-modules/' + key, 'w+')
        yang_download_link = ietf_draft_json[key][2].split('href="')[1].split('">Download')[0]
        try:
            yang_raw = urllib2.urlopen(yang_download_link).read()
            yang_file.write(yang_raw)
        except:
            LOGGER.warning('{} - {}'.format(key, yang_download_link))
            yang_file.write('')
        yang_file.close()
    check_name_no_revision_exist(get_curr_dir(__file__) + '/../../experimental/ietf-extracted-YANG-modules/')
    check_early_revisions(get_curr_dir(__file__) + '/../../experimental/ietf-extracted-YANG-modules/')

    with open("log.txt", "wr") as f:
        try:
            LOGGER.info('Calling populate script')
            arguments = ["python", "../parseAndPopulate/populate.py", "--sdo", "--port", confd_port, "--ip",
                         confd_ip, "--api-protocol", protocol, "--api-port", api_port, "--api-ip", api_ip,
                         "--dir", get_curr_dir(__file__) + "/../../experimental/ietf-extracted-YANG-modules", "--result-html-dir",
                         result_html_dir, "--credentials", credentials[0], credentials[1],
                         "--save-file-dir", save_file_dir]
            if notify == 'True':
                arguments.append("--notify-indexing")
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            LOGGER.error('Error calling process populate.py {}'.format(e.message))
