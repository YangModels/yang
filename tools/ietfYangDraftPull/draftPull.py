import argparse
import errno
import json
import os
import urllib2

import requests
from numpy.f2py.auxfuncs import throw_error
from travispy import TravisPy

# from ..api import repoutil
import repoutil


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
    parser.add_argument('--username', type=str, default='',
                        help='Set name of the repository for automatic push')
    parser.add_argument('--token', type=str, default='',
                        help='Set token of the repository for automatic push')
    args = parser.parse_args()

    github_credentials = ''
    if len(args.username) > 0:
        github_credentials = args.username + ':' + args.token + '@'

    # Fork and clone the repository YangModles/yang
    reponse = requests.post('https://' + github_credentials + 'api.github.com/repos/YangModels/yang/forks')
    repo = repoutil.RepoUtil('https://github.com/' + args.username + '/yang.git')

    repo.clone()
    travis = TravisPy.github_auth(args.token)
    # Download all the latest yang modules out of http://www.claise.be/IETFYANGDraft.json and store them in tmp folder
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
            print(key + ' - ' + yang_download_link)
            yang_file.write('')
        yang_file.close()

    travis_repo = travis.repo(args.username + '/yang')
    travis_repo.enable()  # Switch is now on
    # Add commit and push to the forked repository
    repo.add_all_untracked()
    repo.commit_all('Crone job - every day pull of ietf draft yang files.')
    repo.push()
    # Remove tmp folder
    repo.remove()
