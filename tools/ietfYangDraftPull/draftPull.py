import ConfigParser
import argparse
import errno
import json
import os
import sys
import urllib2

import requests
from numpy.f2py.auxfuncs import throw_error
from travispy import TravisPy

import tools.utility.log as log
from tools.utility import repoutil

LOGGER = log.get_logger('draftPull')


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
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-path', type=str, default='../utility/config.ini',
                        help='Set path to config file')
    args = parser.parse_args()
    LOGGER.info('Starting Cron job IETF pull request')
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    token = config.get('DraftPull-Section', 'yang-catalog-token')
    username = config.get('DraftPull-Section', 'username')
    github_credentials = ''
    if len(username) > 0:
        github_credentials = username + ':' + token + '@'

    # Fork and clone the repository YangModles/yang
    LOGGER.info('Forking repository')
    reponse = requests.post('https://' + github_credentials + 'api.github.com/repos/YangModels/yang/forks')
    repo = repoutil.RepoUtil('https://' + token + '@github.com/' + username + '/yang.git')

    LOGGER.info('Cloning repo to local directory {}'.format(repo.localdir))
    repo.clone()
    yang_models_url = 'https://api.github.com/repos/yang-catalog/yang'
    try:
        LOGGER.info('Activating Travis')
        travis = TravisPy.github_auth(token)
    except:
        LOGGER.error('Activating Travis - Failed. Removing local directory and deleting forked repository')
        requests.delete(yang_models_url, headers={'Authorization': 'token ' + token})
        repo.remove()
        sys.exit(500)
    # Download all the latest yang modules out of http://www.claise.be/IETFYANGDraft.json and store them in tmp folder
    LOGGER.info('Loading all files from http://www.claise.be/IETFYANGDraft.json')
    ietf_draft_json = load_json_from_url('http://www.claise.be/IETFYANGDraft.json')
    try:
        os.makedirs(repo.localdir + '/experimental/ietf-extracted-YANG-modules/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise
    for key in ietf_draft_json:
        yang_file = open(repo.localdir + '/experimental/ietf-extracted-YANG-modules/' + key, 'w+')
        yang_download_link = ietf_draft_json[key][2].split('href="')[1].split('">Download')[0]
        try:
            yang_raw = urllib2.urlopen(yang_download_link).read()
            yang_file.write(yang_raw)
        except:
            LOGGER.warning('{} - {}'.format(key, yang_download_link))
            yang_file.write('')
        yang_file.close()
    try:
        travis_repo = travis.repo(username + '/yang')
        LOGGER.info('Enabling repo for Travis')
        travis_repo.enable()  # Switch is now on
        # Add commit and push to the forked repository
        LOGGER.info('Adding all untracked files locally')
        repo.add_all_untracked()
        LOGGER.info('Committing all files locally')
        repo.commit_all('Crone job - every day pull of ietf draft yang files.')
        LOGGER.info('Pushing files to forked repository')
        repo.push()
    except:
        LOGGER.error('Error while pushing procedure {}'.format(sys.exc_info()[0]))
        requests.delete(yang_models_url, headers={'Authorization': 'token ' + token})
    # Remove tmp folder
    LOGGER.info('Removing tmp directory')
    repo.remove()
