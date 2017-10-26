import ConfigParser
import argparse
import json
import os

import requests

import tools.utility.log as log
from tools.utility import repoutil, yangParser

LOGGER = log.get_logger('openconfigPullLocal')


def resolve_revision(yang_file):
    try:
        parsed_yang = yangParser.parse(os.path.abspath(yang_file))
        revision = parsed_yang.search('revision')[0].arg
    except:
        revision = '1970-01-01'
    return revision

if __name__ == "__main__":
    LOGGER.info('Starting Cron job openconfig pull request local')
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-path', type=str,
                        default='../utility/config.ini',
                        help='Set path to config file')
    args = parser.parse_args()
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    api_ip = config.get('DraftPullLocal-Section', 'api-ip')
    api_port = config.get('DraftPullLocal-Section', 'api-port')
    credentials = config.get('DraftPullLocal-Section', 'credentials').split(' ')
    token = config.get('DraftPull-Section', 'yang-catalog-token')
    username = config.get('DraftPull-Section', 'username')
    api_protocol = config.get('DraftPullLocal-Section', 'protocol')
    github_credentials = ''
    if len(username) > 0:
        github_credentials = username + ':' + token + '@'

    LOGGER.info('Loading all files from http://www.claise.be/IETFYANGDraft.json')
    LOGGER.info('Forking repository')
    reponse = requests.post(
        'https://' + github_credentials + 'api.github.com/repos/openconfig/public/forks')
    repo = repoutil.RepoUtil(
        'https://github.com/yang-catalog/public.git')

    LOGGER.info('Cloning repo to local directory {}'.format(repo.localdir))
    repo.clone()

    mods = []

    for root, dirs, files in os.walk(repo.localdir + '/release/models/'):
        for basename in files:
            if '.yang' in basename:
                mod = {}
                name = basename.split('.')[0].split('@')[0]
                mod['generated-from'] = 'not-applicable'
                mod['module-classification'] = 'unknown'
                mod['name'] = name
                mod['revision'] = resolve_revision('{}/{}'.format(root,
                                                                  basename))
                path = root.split(repo.localdir)[1].replace('/', '', 1)
                if not path.endswith('/'):
                    path += '/'
                path += basename
                mod['organization'] = 'openconfig'
                mod['source-file'] = {'owner': 'openconfig', 'path': path,
                                      'repository': 'public'}
                mods.append(mod)
    output = json.dumps({'modules': {'module': mods}})
    openconfig_models_url = 'https://api.github.com/repos/yang-catalog/public'
    requests.delete(openconfig_models_url,
                    headers={'Authorization': 'token ' + token})
    repo.remove()
    api_path = '{}://{}:{}/modules'.format(api_protocol, api_ip, api_port)
    requests.post(api_path, output, auth=(credentials[0], credentials[1]),
                 headers={'Content-Type': 'application/json'})
