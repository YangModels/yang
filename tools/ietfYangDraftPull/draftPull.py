import ConfigParser
import argparse
import errno
import filecmp
import os
import shutil
import sys
import tarfile

import requests
from travispy import TravisPy
from travispy.errors import TravisError

import tools.utility.log as log
from tools.ietfYangDraftPull.draftPullLocal import check_name_no_revision_exist, \
    check_early_revisions
from tools.utility import repoutil, messageFactory

LOGGER = log.get_logger('draftPull', '/home/miroslav/log/jobs/yang.log')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-path', type=str,
                        default='../utility/config.ini',
                        help='Set path to config file')
    args = parser.parse_args()
    LOGGER.info('Starting Cron job IETF pull request')
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    token = config.get('DraftPull-Section', 'yang-catalog-token')
    username = config.get('DraftPull-Section', 'username')
    commit_dir = config.get('DraftPull-Section', 'commit-dir')
    config_name = config.get('General-Section', 'repo-config-name')
    config_email = config.get('General-Section', 'repo-config-email')
    private_credentials = config.get('General-Section', 'private-secret').split(' ')
    github_credentials = ''
    if len(username) > 0:
        github_credentials = username + ':' + token + '@'

    # Fork and clone the repository YangModles/yang
    LOGGER.info('Forking repository')
    reponse = requests.post(
        'https://' + github_credentials + 'api.github.com/repos/YangModels/yang/forks')
    repo = repoutil.RepoUtil(
        'https://' + token + '@github.com/' + username + '/yang.git')

    LOGGER.info('Cloning repo to local directory {}'.format(repo.localdir))
    repo.clone(config_name, config_email)
    yang_models_url = 'https://api.github.com/repos/yang-catalog/yang'
    try:
        LOGGER.info('Activating Travis')
        travis = TravisPy.github_auth(token)
    except:
        LOGGER.error(
            'Activating Travis - Failed. Removing local directory and deleting forked repository')
        requests.delete(yang_models_url,
                        headers={'Authorization': 'token ' + token})
        repo.remove()
        sys.exit(500)
    # Download all the latest yang modules out of https://new.yangcatalog.org/private/IETFYANGDraft.json and store them in tmp folder
    LOGGER.info(
        'Loading all files from https://new.yangcatalog.org/private/IETFDraft.json')
    ietf_draft_json = requests.get('https://new.yangcatalog.org/private/IETFDraft.json'
                                   , auth=(private_credentials[0], private_credentials[1])).json()
    try:
        os.makedirs(
            repo.localdir + '/experimental/ietf-extracted-YANG-modules/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise

    response = requests.get('https://new.yangcatalog.org/private/YANG-RFC.tgz'
                            , auth=(private_credentials[0], private_credentials[1]))
    zfile = open('./rfc.tgz', 'wb')
    zfile.write(response.content)
    zfile.close()
    tgz = tarfile.open(repo.localdir + '/tools/ietfYangDraftPull/rfc.tgz')
    try:
        os.makedirs(
            repo.localdir + '/standard/ietf/RFCtemp')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise
    tgz.extractall(repo.localdir + '/standard/ietf/RFCtemp')
    tgz.close()
    diff_files = []
    new_files = []

    for root, subdirs, sdos in os.walk(
                    repo.localdir + '/standard/ietf/RFCtemp'):
        for file_name in sdos:
            if '.yang' in file_name:
                if os.path.exists(repo.localdir + '/standard/ietf/RFC/'
                                          + file_name):
                    same = filecmp.cmp(repo.localdir + '/standard/ietf/RFC/'
                                       + file_name, root + '/' + file_name)
                    if not same:
                        diff_files.append(file_name)
                else:
                    new_files.append(file_name)
    shutil.rmtree(repo.localdir + '/standard/ietf/RFCtemp')
    os.remove(repo.localdir + '/tools/ietfYangDraftPull/rfc.tgz')
    if len(new_files) > 0 or len(diff_files) > 0:
        LOGGER.warning('new or modified RFC files found. Sending an E-mail')
        mf = messageFactory.MessageFactory()
        mf.send_new_rfc_message(new_files, diff_files)

    for key in ietf_draft_json:
        yang_file = open(
            repo.localdir + '/experimental/ietf-extracted-YANG-modules/' + key,
            'w+')
        yang_download_link = \
            ietf_draft_json[key][2].split('href="')[1].split('">Download')[0]
        try:
            yang_raw = requests.get(yang_download_link).content
            yang_file.write(yang_raw)
        except:
            LOGGER.warning('{} - {}'.format(key, yang_download_link))
            yang_file.write('')
        yang_file.close()
    check_name_no_revision_exist(
        repo.localdir + '/experimental/ietf-extracted-YANG-modules/')
    check_early_revisions(
        repo.localdir + '/experimental/ietf-extracted-YANG-modules/')
    try:
        travis_repo = travis.repo(username + '/yang')
        LOGGER.info('Enabling repo for Travis')
        travis_repo.enable()  # Switch is now on
        # Add commit and push to the forked repository
        LOGGER.info('Adding all untracked files locally')
        repo.add_all_untracked()
        LOGGER.info('Committing all files locally')
        repo.commit_all('Cronjob - every day pull of ietf draft yang files.')
        LOGGER.info('Pushing files to forked repository')
        LOGGER.info('Commit hash {}'.format(repo.repo.head.commit))
        with open(commit_dir, 'w+') as f:
            f.write('{}\n'.format(repo.repo.head.commit))
        repo.push()
    except TravisError as e:
        LOGGER.error('Error while pushing procedure {}'.format(e.message()))
        requests.delete(yang_models_url,
                        headers={'Authorization': 'token ' + token})
    except:
        LOGGER.error(
            'Error while pushing procedure {}'.format(sys.exc_info()[0]))
        requests.delete(yang_models_url,
                        headers={'Authorization': 'token ' + token})
    # Remove tmp folder
    LOGGER.info('Removing tmp directory')
    repo.remove()
