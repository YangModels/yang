import ConfigParser
import base64
import collections
import errno
import grp
import hashlib
import json
import math
import os
import pwd
import re
import shutil
import subprocess
import sys
import urllib2
import uuid
from copy import deepcopy
from datetime import datetime
from threading import Lock
from urllib2 import URLError

import MySQLdb
import jinja2
import requests
import uwsgi as uwsgi
from OpenSSL.crypto import load_publickey, FILETYPE_PEM, X509, verify
from flask import Flask, jsonify, abort, make_response, request, Response, \
    redirect
from flask_httpauth import HTTPBasicAuth

import tools.utility.log as lo
import yangSearch.index as index
import yangSearch.mysql_index as ind
from tools.api.prometheus.main import monitor
from tools.api.sender import Sender
from tools.utility import repoutil, yangParser, messageFactory
from tools.utility.util import get_curr_dir
from yangSearch.module import Module
from yangSearch.rester import Rester, RestException

LOGGER = lo.get_logger('api', '/home/miroslav/log/api/yang.log')
url = 'https://github.com/'

github_api_url = 'https://api.github.com'
github_repos_url = github_api_url + '/repos'
yang_models_url = github_repos_url + '/YangModels/yang'

auth = HTTPBasicAuth()


class MyFlask(Flask):

    def __init__(self, import_name): 
        super(MyFlask, self).__init__(import_name)
        self.response = None
        self.ys_set = 'set'
        LOGGER.info('Loading all configuration')
        config_path = os.path.abspath('.') + '/../utility/config.ini'
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        self.result_dir = config.get('API-Section', 'result-html-dir')
        self.sender = Sender()
        self.dbHost = config.get('API-Section', 'dbIp')
        self.dbName = config.get('API-Section', 'dbName')
        self.dbNameSearch = config.get('API-Section', 'dbNameSearch')
        self.dbUser = config.get('API-Section', 'dbUser')
        self.dbPass = config.get('API-Section', 'dbPassword')
        self.credentials = config.get('General-Section', 'credentials').split(' ')
        self.confd_ip = config.get('General-Section', 'confd-ip')
        self.confdPort = int(config.get('General-Section', 'confd-port'))
        self.protocol = config.get('General-Section', 'protocol')
        self.save_requests = config.get('API-Section', 'save-requests')
        self.save_file_dir = config.get('API-Section', 'save-file-dir')
        self.token = config.get('API-Section', 'yang-catalog-token')
        self.admin_token = config.get('API-Section', 'admin-token')
        self.commit_msg_file = config.get('API-Section', 'commit-dir')
        self.integrity_file_location = config.get('API-Section',
                                             'integrity-file-location')
        self.diff_file_dir = config.get('API-Section', 'save-diff-dir')
        self.ip = config.get('API-Section', 'ip')
        self.api_port = int(config.get('General-Section', 'api-port'))
        self.log = open('api_log_file.txt', 'w')
        self.api_protocol = config.get('General-Section', 'protocol-api')
        self.is_uwsgi = config.get('General-Section', 'uwsgi')
        self.config_name = config.get('General-Section', 'repo-config-name')
        self.config_email = config.get('General-Section', 'repo-config-email')
        separator = ':'
        suffix = self.api_port
        if self.is_uwsgi == 'True':
            separator = '/'
            suffix = 'api'
        self.yangcatalog_api_prefix = '{}://{}{}{}/'.format(self.api_protocol, self.ip,
                                                       separator, suffix)
        LOGGER.debug('Starting api')

    def process_response(self, response):
        self.response = response
        self.create_response_only_latest_revision()
        self.create_response_with_yangsuite_link()

        return self.response

    def create_response_only_latest_revision(self):
        if request.args.get('latest-revision'):
            if 'True' == request.args.get('latest-revision'):
                if self.response.data:
                    json_data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(self.response.data)
                else:
                    return self.response
                modules = None
                if json_data.get('yang-catalog:modules') is not None:
                    if json_data.get('yang-catalog:modules').get(
                            'module') is not None:
                        modules = json_data.get('yang-catalog:modules').get(
                            'module')
                elif json_data.get('module') is not None:
                    modules = json_data.get('module')
                modules_to_remove = []
                if modules:
                    if len(modules) > 0:
                        newlist = sorted(modules, key=lambda k: k['name'])
                        temp_module = None
                        i = 0
                        for mod in newlist:
                            name = mod['name']
                            if temp_module:
                                if temp_module['name'] == name:
                                    revisions = []
                                    mod['index'] = i
                                    year = int(temp_module['revision'].split('-')[0])
                                    month = int(temp_module['revision'].split('-')[1])
                                    day = int(temp_module['revision'].split('-')[2])
                                    revisions.append(datetime(year, month, day))
                                    year = int(mod['revision'].split('-')[0])
                                    month = int(mod['revision'].split('-')[1])
                                    day = int(mod['revision'].split('-')[2])
                                    revisions.append(datetime(year, month, day))
                                    latest = revisions.index(max(revisions))
                                    if latest == 0:
                                        modules_to_remove.append(mod['index'])
                                    elif latest == 1:
                                        modules_to_remove.append(temp_module['index'])
                                else:
                                    mod['index'] = i
                                    temp_module = mod
                            else:
                                mod['index'] = i
                                temp_module = mod
                            i += 1
                        for mod_to_remove in reversed(modules_to_remove):
                            newlist.remove(newlist[mod_to_remove])
                        for mod in newlist:
                            if mod.get('index'):
                                del mod['index']
                        self.response.data = json.dumps(newlist)

    def get_dependencies(self, mod, mods, inset):
        if mod.get('dependencies'):
            for dep in mod['dependencies']:
                if dep['name'] in inset:
                    continue
                if dep.get('revision'):
                    mods.add(dep['name'] + '@' + dep[
                        'revision'] + '.yang')
                    inset.add(dep['name'])
                    search_filter = json.dumps({
                        'input': {
                            'name': dep['name'],
                            'revision': dep['revision']
                        }
                    })
                    rp = requests.post('{}/search-filter'.format(
                        self.yangcatalog_api_prefix), search_filter,
                        headers={
                            'Content-type': 'application/json',
                            'Accept': 'application/json'}
                    )
                    mo = rp.json()['yang-catalog:modules']['module'][0]
                    self.get_dependencies(mo, mods, inset)
                else:
                    rp = requests.get('{}/search/name/{}'
                                      .format(self.yangcatalog_api_prefix,
                                              dep['name']))
                    if rp.status_code == 404:
                        continue
                    mo = rp.json()['yang-catalog:modules']['module']
                    revisions = []
                    for m in mo:
                        revision = m['revision']
                        year = int(revision.split('-')[0])
                        month = int(revision.split('-')[1])
                        day = int(revision.split('-')[2])
                        revisions.append(datetime(year, month, day))
                    latest = revisions.index(max(revisions))
                    inset.add(dep['name'])
                    mods.add('{}@{}.yang'.format(dep['name'],
                                                 mo[latest][
                                                     'revision']))
                    self.get_dependencies(mo[latest], mods, inset)

    def create_response_with_yangsuite_link(self):
        if request.headers.environ.get('HTTP_YANGSUITE'):
            if 'true' != request.headers.environ['HTTP_YANGSUITE']:
                return self.response
            if request.headers.environ.get('HTTP_YANGSET_NAME'):
                self.ys_set = request.headers.environ.get(
                    'HTTP_YANGSET_NAME').replace('/', '_')
        else:
            return self.response

        if self.response.data:
            json_data = json.loads(self.response.data)
        else:
            return self.response
        modules = None
        if json_data.get('yang-catalog:modules') is not None:
            if json_data.get('yang-catalog:modules').get('module') is not None:
                modules = json_data.get('yang-catalog:modules').get('module')
        elif json_data.get('module') is not None:
            modules = json_data.get('module')
        if modules:
            if len(modules) > 0:
                ys_dir = '/home/miott/ysuite/yangsuite/data/users/'

                id = uuid.uuid4().hex
                ys_dir += id + '/repositories/' + modules[0]['name'].lower()
                try:
                    os.makedirs(ys_dir)
                except OSError as e:
                    # be happy if someone already created the path
                    if e.errno != errno.EEXIST:
                        return 'Server error - could not create directory'
                mods = set()
                inset = set()
                if len(modules) == 1:
                    defmod = modules[0]['name']
                for mod in modules:
                    name = mod['name']
                    if name in inset:
                        continue
                    name += '@{}.yang'.format(mod['revision'])
                    mods.add(name)
                    inset.add(mod['name'])
                    self.get_dependencies(mod, mods, inset)
                if (('openconfig-interfaces' in inset
                    or 'ietf-interfaces' in inset)
                    and 'iana-if-type' not in inset):
                    resp = requests.get(
                        'https://yangcatalog.org/api/search/name/iana-if-type?latest-revision=True',
                        headers={
                            'Content-type': 'application/json',
                            'Accept': 'application/json'})
                    name = '{}@{}.yang'.format(resp.json()[0]['name'],
                                               resp.json()[0]['revision'])
                    mods.add(name)
                    inset.add(resp.json()[0]['name'])
                    self.get_dependencies(resp.json()[0], mods, inset)

                modules = []
                for mod in mods:
                    if not os.path.exists(self.save_file_dir + '/' + mod):
                        continue
                    shutil.copy(self.save_file_dir + '/' + mod, ys_dir)
                    modules.append([mod.split('@')[0], mod.split('@')[1]
                                   .replace('.yang', '')])
                ys_dir = '/home/miott/ysuite/yangsuite/data/users/'
                ys_dir += id + '/yangsets'
                try:
                    os.makedirs(ys_dir)
                except OSError as e:
                    # be happy if someone already created the path
                    if e.errno != errno.EEXIST:
                        return 'Server error - could not create directory'
                json_set = {'owner': id,
                            'repository': id + '+' + defmod.split('@')[0],
                            'setname': defmod.split('@')[0],
                            'defmod': defmod.split('@')[0],
                            'modules': modules}

                with open(ys_dir + '/' + defmod.split('@')[0].lower(), 'w') as f:
                    f.write(json.dumps(json_set, indent=4))
                uid = pwd.getpwnam("miroslav").pw_uid
                gid = grp.getgrnam("yang").gr_gid
                path = '/home/miott/ysuite/yangsuite/data/users/' + id
                for root, dirs, files in os.walk(path):
                    for momo in dirs:
                        os.chown(os.path.join(root, momo), uid, gid)
                    for momo in files:
                        os.chown(os.path.join(root, momo), uid, gid)
                os.chown(path, uid, gid)
                json_data['yangsuite-url'] = (
                    '{}/yangsuite/{}'.format(self.yangcatalog_api_prefix, id))
                self.response.data = json.dumps(json_data)
                return self.response
            else:
                return self.response
        else:
            return self.response


application = MyFlask(__name__)
monitor(application)
lock_uwsgi_cache1 = Lock()
lock_uwsgi_cache2 = Lock()
lock_for_load = Lock()

NS_MAP = {
    "http://cisco.com/": "cisco",
    "http://www.huawei.com/netconf": "huawei",
    "http://openconfig.net/yang/": "openconfig",
    "http://tail-f.com/": "tail-f"
}


def make_cache(credentials, response, cache_chunks, main_cache, is_uwsgi=True):
    """After we delete or add modules we need to reload all the modules to the file
    for quicker search. This module is then loaded to the memory.
            Arguments:
                :param response: (str) Contains string 'work' which will be sent back if
                    everything went through fine
                :param credentials: (list) Basic authorization credentials - username, password
                    respectively
                :return 'work' if everything went through fine otherwise send back the reason
                    why it failed.
    """
    try:
        path = application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/catalog?deep'
        data = http_request(path, 'GET', '', credentials, 'application/vnd.yang.data+json').read()

        if is_uwsgi == 'True':
            chunks = int(math.ceil(len(data)/float(64000)))
            for i in range(0, chunks, 1):
                uwsgi.cache_set('data{}'.format(i), data[i*64000: (i+1)*64000],
                                0, main_cache)
            LOGGER.info('all {} chunks are set in uwsgi cache'.format(chunks))
            uwsgi.cache_set('chunks-data', repr(chunks), 0, cache_chunks)
        else:
            return response, data
    except:
        e = sys.exc_info()[0]
        LOGGER.error('Could not load json to cache. Error: {}'.format(e))
        return 'Server error - downloading cache', None
    return response, data


def create_response(body, status, headers=None):
    """Creates flask response that can be sent to sender.
            Arguments:
                :param body: (Str) Message body of the response
                :param status: (int) Status code of the response
                :param headers: (list) List of tuples containing headers information
                :return: Response that can be returned.
    """
    if headers is None:
        headers = []
    resp = Response(body, status=status)
    if headers:
        for item in headers:
            if item[0] == 'Content-Length' or 'Content-Encoding' in item[0]:
                continue
            resp.headers[item[0]] = item[1]

    return resp


# Make a http request on path with json_data
def http_request(path, method, json_data, http_credentials, header):
    """Create HTTP request
            Arguments:
                :param header: (str) to set Content-type and Accept headers to this variable
                :param http_credentials: (list) Basic authorization credentials - username, password
                    respectively
                :param json_data: (dict) Body of the payload send via request
                :param method: (str) Request method.
                :param path : (str) Path of the request.
                :return a response from the request.
    """
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(path, data=json_data)
        request.add_header('Content-Type', header)
        request.add_header('Accept', header)
        base64string = base64.b64encode('%s:%s' % (http_credentials[0], http_credentials[1]))
        request.add_header("Authorization", "Basic %s" % base64string)
        request.get_method = lambda: method
        return opener.open(request)
    except urllib2.HTTPError as e:
        if method == 'DELETE':
            return
        LOGGER.error('Could not send request with body {} and path {}'.format(json_data, path))
        raise e
    except URLError as e:
        LOGGER.error('Could not send request with body {} and path {} {}'.format(json_data, path, e))
        raise e


@application.errorhandler(404)
def not_found():
    """Error handler for 404"""
    return make_response(jsonify({'error': 'Not found'}), 404)


def authorize_for_sdos(request, organizations_sent, organization_parsed):
    """Authorize sender whether he has rights to send data via API to confd.
            Arguments:
                :param organization_parsed: (str) organization of a module sent by sender.
                :param organizations_sent: (str) organization of a module parsed from module.
                :param request: (request) Request sent to api.
                :return whether authorization passed.
    """
    username = request.authorization['username']
    LOGGER.info('Checking sdo authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=application.dbHost, db=application.dbName, user=application.dbUser, passwd=application.dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM `users`")
        data = cursor.fetchall()

        for row in data:
            if row[1] == username:
                accessRigths = row[7]
                break
        db.close()
    except MySQLdb.MySQLError as err:
        LOGGER.error('Cannot connect to database. MySQL error: {}'.format(err))

    passed = False
    if accessRigths == '/':
        if organization_parsed != organizations_sent:
            return "module`s organization is not the same as organization provided"
        return True
    if organizations_sent in accessRigths:
        if organization_parsed != organizations_sent:
            return "module`s organization is not the same as organization provided"
        passed = True
    return passed


def authorize_for_vendors(request, body):
    """Authorize sender whether he has rights to send data via API to confd.
       Checks if sender has access on a given branch
                Arguments:
                    :param body: (str) json body of the request.
                    :param request: (request) Request sent to api.
                    :return whether authorization passed.
    """
    username = request.authorization['username']
    LOGGER.info('Checking vendor authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=application.dbHost, db=application.dbName, user=application.dbUser, passwd=application.dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM `users`")
        data = cursor.fetchall()

        for row in data:
            if row[1] == username:
                accessRigths = row[8]
                break
        db.close()
    except MySQLdb.MySQLError as err:
        LOGGER.error('Cannot connect to database. MySQL error: {}'.format(err))

    rights = accessRigths.split('/')
    check_vendor = None
    check_platform = None
    check_software_version = None
    check_software_flavor = None
    if rights[1] is '':
        return 'passed'
    else:
        check_vendor = rights[1]
    if len(rights) > 2:
        check_platform = rights[2]
    if len(rights) > 3:
        check_software_version = rights[3]
    if len(rights) > 4:
        check_software_flavor = rights[4]

    for platform in body['platforms']['platform']:
        vendor = platform['vendor']
        platform_name = platform['name']
        software_version = platform['software-version']
        software_flavor = platform['software-flavor']

        if check_platform and platform_name != check_platform:
            return unauthorized()
        if check_software_version and software_version != check_software_version:
            return unauthorized()
        if check_software_flavor and software_flavor != check_software_flavor:
            return unauthorized()
        if vendor != check_vendor:
            return unauthorized()
    return 'passed'


@application.route('/', defaults={'path': ''})
@application.route('/<path:path>', methods=['PUT', 'POST', 'GET', 'DELETE', 'PATCH'])
def catch_all(path):
    """Catch all the rest api requests that are not supported"""
    return make_response(jsonify(
        {
            'error': 'Path "/{}" does not exist'.format(path)
        }), 400)


def check_authorized(signature, payload):
    """Convert the PEM encoded public key to a format palatable for pyOpenSSL,
    then verify the signature
            Arguments:
                :param signature: (str) Signature returned by sign function
                :param payload: (str) String that is encoded
    """
    response = requests.get('https://api.travis-ci.org/config', timeout=10.0)
    response.raise_for_status()
    public_key = response.json()['config']['notifications']['webhook']['public_key']
    pkey_public_key = load_publickey(FILETYPE_PEM, public_key)
    certificate = X509()
    certificate.set_pubkey(pkey_public_key)
    verify(certificate, base64.b64decode(signature), payload, str('SHA1'))


@application.route('/yangsuite/<id>', methods=['GET'])
def yangsuite_redirect(id):
    local_ip = '127.0.0.1'
    if application.is_uwsgi:
        local_ip = 'yangcatalog.org'
#    return redirect('http://{}:8000/ydk/aaa/{}'.format(local_ip, id))
    return redirect('https://{}/yangsuite/ydk/aaa/{}'.format(local_ip, id))


@auth.login_required
@application.route('/ietf', methods=['GET'])
def trigger_ietf_pull():
    username = request.authorization['username']
    if username != 'admin':
        return unauthorized
    job_id = application.sender.send('run_ietf')
    LOGGER.info('job_id {}'.format(job_id))
    return make_response(jsonify({'job-id': job_id}), 202)


@application.route('/checkComplete', methods=['POST'])
def check_local():
    """Authorize sender if it is Travis, if travis job was sent from yang-catalog
    repository and job passed fine and Travis run a job on pushed patch, create
    a pull request to YangModules repository. If the job passed on this pull request,
    merge the pull request and remove the repository at yang-catalog repository
            :return response to the request
    """
    LOGGER.info('Starting pull request job')
    body = json.loads(request.form['payload'])
    LOGGER.info('Body of travis {}'.format(json.dumps(body)))
    LOGGER.info('type of job {}'.format(body['type']))
    try:
        check_authorized(request.headers.environ['HTTP_SIGNATURE'], request.form['payload'])
        LOGGER.info('Authorization successful')
    except:
        LOGGER.critical('Authorization failed.'
                        ' Request did not come from Travis')
        mf = messageFactory.MessageFactory()
        mf.send_travis_auth_failed()
        return unauthorized()

    global yang_models_url

    verify_commit = False
    LOGGER.info('Checking commit SHA if it is the commit sent by yang-catalog'
                'user.')
    if body['repository']['owner_name'] == 'yang-catalog':
        commit_sha = body['commit']
    else:
        commit_sha = body['head_commit']
    try:
        commit_file = file(application.commit_msg_file)
        for line in commit_file:
            if commit_sha in line:
                verify_commit = True
                break
    except:
        return not_found()

    if verify_commit:
        LOGGER.info('commit verified')
        if body['repository']['owner_name'] == 'yang-catalog':
            if body['result_message'] == 'Passed':
                if body['type'] == 'push':
                    # After build was successful only locally
                    json_body = json.loads(json.dumps({
                        "title": "Cronjob - every day pull and update of ietf draft yang files.",
                        "body": "ietf extracted yang modules",
                        "head": "yang-catalog:master",
                        "base": "master"
                    }))

                    r = requests.post(yang_models_url + '/pulls',
                                      json=json_body, headers={'Authorization': 'token ' + application.token})
                    if r.status_code == requests.codes.created:
                        LOGGER.info('Pull request created successfully')
                        return make_response(jsonify({'info': 'Success'}), 201)
                    else:
                        LOGGER.error('Could not create a pull request {}'.format(r.status_code))
                        return make_response(jsonify({'Error': 'PR creation failed'}), 400)
            else:
                LOGGER.warning('Travis job did not pass. Removing forked repository.')
                requests.delete('https://api.github.com/repos/yang-catalog/yang',
                                headers={'Authorization': 'token ' + application.token})
                return make_response(jsonify({'info': 'Failed'}), 406)
        elif body['repository']['owner_name'] == 'YangModels':
            if body['result_message'] == 'Passed':
                if body['type'] == 'pull_request':
                    # If build was successful on pull request
                    pull_number = body['pull_request_number']
                    LOGGER.info('Pull request was successful {}. sending review.'.format(repr(pull_number)))
                    url = 'https://api.github.com/repos/YangModels/yang/pulls/'+ repr(pull_number) +'/reviews'
                    data = json.dumps({
                        'body': 'AUTOMATED YANG CATALOG APPROVAL',
                        'event': 'APPROVE'
                    })
                    response = requests.post(url, data, headers={'Authorization': 'token ' + application.admin_token})
                    LOGGER.info('review response code {}. Merge response {}.'.format(
                            response.status_code, response.content))
                    data = json.dumps({'commit-title': 'Travis job passed',
                                       'sha': body['head_commit']})
                    response = requests.put('https://api.github.com/repos/YangModels/yang/pulls/' + repr(pull_number) +
                                 '/merge', data, headers={'Authorization': 'token ' + application.admin_token})
                    LOGGER.info('Merge response code {}. Merge response {}.'.format(response.status_code, response.content))
                    requests.delete('https://api.github.com/repos/yang-catalog/yang',
                                    headers={'Authorization': 'token ' + application.token})
                    return make_response(jsonify({'info': 'Success'}), 201)
            else:
                LOGGER.warning('Travis job did not pass. Removing pull request')
                pull_number = body['pull_request_number']
                json_body = json.loads(json.dumps({
                    "title": "Cron job - every day pull and update of ietf draft yang files.",
                    "body": "ietf extracted yang modules",
                    "state": "closed",
                    "base": "master"
                }))
                requests.patch('https://api.github.com/repos/YangModels/yang/pulls/' + pull_number, json=json_body,
                               headers={'Authorization': 'token ' + application.token})
                LOGGER.warning(
                    'Travis job did not pass. Removing forked repository.')
                requests.delete(
                    'https://api.github.com/repos/yang-catalog/yang',
                    headers={'Authorization': 'token ' + application.token})
                return make_response(jsonify({'info': 'Failed'}), 406)
        else:
            LOGGER.warning('Owner name verification failed. Owner -> {}'
                           .format(body['repository']['owner_name']))
            return make_response(jsonify({'Error': 'Owner verfication failed'}),
                                 401)
    else:
        LOGGER.info('Commit verification failed. Commit sent by someone else.'
                    'Not doing anything.')
    return make_response(jsonify({'Error': 'Fails'}), 500)


@application.route('/modules/module/<name>,<revision>,<organization>', methods=['DELETE'])
@auth.login_required
def delete_module(name, revision, organization):
    """Delete a specific module defined with name, revision and organization. This is
    not done right away but it will send a request to receiver which will work on deleting
    while this request will send a job_id of the request which user can use to see the job
    process.
            Arguments:
                :param name: (str) name of the module
                :param revision: (str) revision of the module
                :param organization: (str) organization of the module
                :return response to the request with job_id that user can use to
                    see if the job is still on or Failed or Finished successfully
    """
    LOGGER.info('deleting module with name, revision and organization {} {} {}'.format(name, revision, organization))
    username = request.authorization['username']
    LOGGER.debug('Checking authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=application.dbHost, db=application.dbName, user=application.dbUser, passwd=application.dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM `users`")
        data = cursor.fetchall()

        for row in data:
            if row[1] == username:
                accessRigths = row[7]
                break
        db.close()
    except MySQLdb.MySQLError as err:
        LOGGER.error('Cannot connect to database. MySQL error: {}'.format(err))
    try:
        response = http_request(
            application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/catalog/modules/module/' + name +
            ',' + revision + ',' + organization, 'GET', None, application.credentials, 'application/vnd.yang.data+json')
    except urllib2.HTTPError as e:
        return not_found()

    read = json.loads(response.read())
    if read['yang-catalog:module']['organization'] != accessRigths and accessRigths != '/':
        return unauthorized()

    if read['yang-catalog:module'].get('implementations') is not None:
        return make_response(jsonify({'error': 'This module has reference in vendors branch'}), 400)

    path_to_delete = application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/catalog/modules/module/' \
                     + name + ',' + revision + ',' + organization

    arguments = [application.protocol, application.confd_ip, repr(application.confdPort), application.credentials[0],
                 application.credentials[1], path_to_delete, 'DELETE', application.api_protocol, repr(application.api_port)]
    job_id = application.sender.send('#'.join(arguments))

    LOGGER.info('job_id {}'.format(job_id))
    return make_response(jsonify({'info': 'Verification successful', 'job-id': job_id}), 202)


@application.route('/modules', methods=['DELETE'])
@auth.login_required
def delete_modules():
    """Delete a specific modules defined with name, revision and organization. This is
    not done right away but it will send a request to receiver which will work on deleting
    while this request will send a job_id of the request which user can use to see the job
    process.
            Arguments:
                :return response to the request with job_id that user can use to
                    see if the job is still on or Failed or Finished successfully
    """
    if not request.json:
        abort(400)
    username = request.authorization['username']
    LOGGER.debug('Checking authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=application.dbHost, db=application.dbName, user=application.dbUser, passwd=application.dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM `users`")
        data = cursor.fetchall()

        for row in data:
            if row[1] == username:
                accessRigths = row[7]
                break
        db.close()
    except MySQLdb.MySQLError as err:
        LOGGER.error('Cannot connect to database. MySQL error: {}'.format(err))

    rpc = request.json
    if rpc.get('input'):
        modules = rpc['input'].get('modules')
    else:
        return not_found()
    for mod in modules:
        try:
            response = http_request(
                application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/catalog/modules/module/' + mod['name'] +
                ',' + mod['revision'] + ',' + mod['organization'], 'GET', None, application.credentials, 'application/vnd.yang.data+json')
            read = json.loads(response.read())

            if read['yang-catalog:module'][
                'organization'] != accessRigths and accessRigths != '/':
                return unauthorized()

            if read['yang-catalog:module'].get('implementations') is not None:
                return make_response(jsonify(
                    {'error': 'This module has reference in vendors branch'}),
                                     400)
        except urllib2.HTTPError as e:
            return not_found()

    path_to_delete = json.dumps(rpc['input'])

    arguments = [application.protocol, application.confd_ip, repr(application.confdPort), application.credentials[0],
                 application.credentials[1], path_to_delete, 'DELETE_MULTIPLE',
                 application.api_protocol, repr(application.api_port)]
    job_id = application.sender.send('#'.join(arguments))

    LOGGER.info('job_id {}'.format(job_id))
    return make_response(jsonify({'info': 'Verification successful', 'job-id': job_id}), 202)


@application.route('/vendors/<path:value>', methods=['DELETE'])
@auth.login_required
def delete_vendor(value):
    """Delete a specific vendor defined with path. This is not done right away but it
    will send a request to receiver which will work on deleting while this request
    will send a job_id of the request which user can use to see the job
        process.
            Arguments:
                :param value: (str) path to the branch that needs to be deleted
                :return response to the request with job_id that user can use to
                    see if the job is still on or Failed or Finished successfully
    """
    LOGGER.info('Deleting vendor on path {}'.format(value))
    username = request.authorization['username']
    LOGGER.debug('Checking authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=application.dbHost, db=application.dbName, user=application.dbUser, passwd=application.dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM `users`")
        data = cursor.fetchall()

        for row in data:
            if row[1] == username:
                accessRigths = row[8]
                break
        db.close()
    except MySQLdb.MySQLError as err:
        LOGGER.error('Cannot connect to database. MySQL error: {}'.format(err))

    rights = accessRigths.split('/')
    check_vendor = None
    check_platform = None
    check_software_version = None
    check_software_flavor = None
    if not rights[1] is '':
        check_vendor = rights[1]
        if len(rights) > 2:
            check_platform = rights[2]
        if len(rights) > 3:
            check_software_version = rights[3]
        if len(rights) > 4:
            check_software_flavor = rights[4]

    path_to_delete = application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/catalog/vendors/' \
                     + value + '?deep'

    vendor = 'None'
    platform = 'None'
    software_version = 'None'
    software_flavor = 'None'
    if '/vendor/' in path_to_delete:
        vendor = path_to_delete.split('?deep')[0].split('/vendor/')[1].split('/')[0]
    if '/platform/' in path_to_delete:
        platform = path_to_delete.split('?deep')[0].split('/platform/')[1].split('/')[0]
    if '/software-version/' in path_to_delete:
        software_version = path_to_delete.split('?deep')[0].split('/software-version/')[1].split('/')[0]
    if 'software-version/' in path_to_delete:
        software_flavor = path_to_delete.split('?deep')[0].split('/software-version/')[1].split('/')[0]

    if check_platform and platform != check_platform:
        return unauthorized()
    if check_software_version and software_version != check_software_version:
        return unauthorized()
    if check_software_flavor and software_flavor != check_software_flavor:
        return unauthorized()
    if check_vendor and vendor != check_vendor:
        return unauthorized()

    arguments = [vendor, platform, software_version, software_flavor, application.protocol, application.confd_ip, repr(application.confdPort), application.credentials[0],
                 application.credentials[1], path_to_delete, 'DELETE', application.api_protocol, repr(application.api_port)]
    job_id = application.sender.send('#'.join(arguments))

    LOGGER.info('job_id {}'.format(job_id))
    return make_response(jsonify({'info': 'Verification successful', 'job-id': job_id}), 202)


@application.route('/modules', methods=['PUT', 'POST'])
@auth.login_required
def add_modules():
    """Add a new module. Use PUT request when we want to update every module there is
    in the request, use POST request if you want to create just modules that are not
    in confd yet. This is not done right away. First it checks if the request sent is
    ok and if it is, it will send a request to receiver which will work on deleting
    while this request will send a job_id of the request which user can use to see
    the job process.
            Arguments:
                :return response to the request with job_id that user can use to
                    see if the job is still on or Failed or Finished successfully
    """
    if not request.json:
        abort(400)
    body = request.json
    LOGGER.info('Adding modules with body {}'.format(body))
    tree_created = False

    with open('./prepare-sdo.json', "w") as plat:
        json.dump(body, plat)
    shutil.copy('./prepare-sdo.json', application.save_requests + '/sdo-'
                + str(datetime.utcnow()).split('.')[0].replace(' ', '_') + '-UTC.json')
    try:
        http_request(application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/modules/',
                     'DELETE', None, application.credentials, 'application/vnd.yang.collection+json')
    except:
        pass
    path = application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/modules'

    base64string = base64.b64encode('%s:%s' % (application.credentials[0], application.credentials[1]))
    response = requests.put(path, json.dumps(body), headers={'Authorization': 'Basic ' + base64string,
                                                             'Content-type': 'application/vnd.yang.data+json',
                                                             'Accept': 'application/vnd.yang.data+json'})

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 204:
        return create_response(response.content, response.status_code, response.headers.items())
    repo = {}
    warning = []

    direc = 0
    while True:
        if os.path.isdir('../parseAndPopulate/' + repr(direc)):
            direc += 1
        else:
            break
    direc = '../parseAndPopulate/' + repr(direc)
    try:
        os.makedirs(direc)
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise
    for mod in body['modules']['module']:
        sdo = mod['source-file']
        orgz = mod['organization']
        if request.method == 'POST':
            try:
                path = application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/catalog/modules/module/' + \
                       mod['name'] + ',' + mod['revision'] + ',' + mod['organization']
                http_request(path, 'GET', None, application.credentials, 'application/vnd.yang.data+json')
                continue
            except urllib2.HTTPError as e:
                pass
        directory = '/'.join(sdo['path'].split('/')[:-1])

        repo_url = url + sdo['owner'] + '/' + sdo['repository']
        LOGGER.debug('Cloning repository')
        if repo_url not in repo:
            repo[repo_url] = repoutil.RepoUtil(repo_url)
            repo[repo_url].clone(application.config_name, application.config_email)

        for submodule in repo[repo_url].repo.submodules:
            submodule.update(init=True)

        if sdo.get('branch'):
            branch = sdo.get('branch')
        else:
            branch = 'master'
        save_to = direc + '/temp/' + sdo['owner'] + '/' + sdo['repository'].split('.')[0] \
                  + '/' + branch + '/' + directory
        try:
            os.makedirs(save_to)
        except OSError as e:
            # be happy if someone already created the path
            if e.errno != errno.EEXIST:
                raise
        shutil.copy(repo[repo_url].localdir + '/' + sdo['path'], save_to)

        tree_created = True
        organization = ''
        try:
            namespace = yangParser.parse(os.path.abspath(save_to + '/' + sdo['path'].split('/')[-1])) \
                .search('namespace')[0].arg

            for ns, org in NS_MAP.items():
                if ns in namespace:
                    organization = org
            if organization == '':
                if 'urn:' in namespace:
                    organization = namespace.split('urn:')[1].split(':')[0]
        except:
            while True:
                try:
                    belongs_to = yangParser.parse(os.path.abspath(repo[repo_url].localdir + '/' + sdo['path'])) \
                        .search('belongs-to')[0].arg
                except:
                    break
                try:
                    namespace = yangParser.parse(os.path.abspath(repo[repo_url].localdir + '/' + '/'.join(
                        sdo['path'].split('/')[:-1]) + '/' + belongs_to + '.yang')).search('namespace')[0].arg
                    for ns, org in NS_MAP.items():
                        if ns in namespace:
                            organization = org
                    if organization == '':
                        if 'urn:' in namespace:
                            organization = namespace.split('urn:')[1].split(':')[0]
                    break
                except:
                    pass
        resolved_authorization = authorize_for_sdos(request, orgz, organization)
        if not resolved_authorization:
            shutil.rmtree(direc)
            for key in repo:
                repo[key].remove()
            return unauthorized()
        if 'organization' in repr(resolved_authorization):
            warning.append(sdo['path'].split('/')[-1] + ' ' + resolved_authorization)

    if os.path.isfile('./prepare-sdo.json'):
        shutil.move('./prepare-sdo.json', direc)
    for key in repo:
        repo[key].remove()

    LOGGER.debug('Sending a new job')
    arguments = ["python", "../parseAndPopulate/populate.py", "--sdo", "--port",
                 repr(application.confdPort), "--dir", direc + "/temp", "--api", "--ip",
                 application.confd_ip, "--credentials", application.credentials[0], application.credentials[1],
                 repr(tree_created), application.protocol, application.api_protocol, repr(application.api_port)]
    job_id = application.sender.send('#'.join(arguments))
    LOGGER.info('job_id {}'.format(job_id))
    if len(warning) > 0:
        return jsonify({'info': 'Verification successful', 'job-id': job_id, 'warnings': [{'warning': val}
                                                                                          for val in warning]})
    else:
        return make_response(jsonify({'info': 'Verification successful', 'job-id': job_id}), 202)


@application.route('/platforms', methods=['PUT', 'POST'])
@auth.login_required
def add_vendors():
    """Add a new vendors. Use PUT request when we want to update every module there is
    in the request, use POST request if you want to create just modules that are not
    in confd yet. This is not done right away. First it checks if the request sent is
    ok and if it is, it will send a request to receiver which will work on deleting
    while this request will send a job_id of the request which user can use to see
    the job process.
            Arguments:
                :return response to the request with job_id that user can use to
                    see if the job is still on or Failed or Finished successfully
    """
    if not request.json:
        abort(400)
    body = request.json
    LOGGER.info('Adding vendor with body {}'.format(body))
    tree_created = False
    resolved_authorization = authorize_for_vendors(request, body)
    if 'passed' != resolved_authorization:
        return resolved_authorization
    with open(application.save_requests + '/vendor-' + str(datetime.utcnow()).split('.')[0].replace(' ', '_') +
              '-UTC.json', "w") as plat:
        json.dump(body, plat)

    try:
        http_request(application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/platforms/',
                     'DELETE', None, application.credentials, 'application/vnd.yang.collection+json')
    except:
        pass
    path = application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/platforms'

    base64string = base64.b64encode('%s:%s' % (application.credentials[0], application.credentials[1]))
    response = requests.put(path, json.dumps(body), headers={'Authorization': 'Basic ' + base64string,
                                                             'Content-type': 'application/vnd.yang.data+json',
                                                             'Accept': 'application/vnd.yang.data+json'})

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 204:
        return create_response(response.content, response.status_code, response.headers.items())

    repo = {}

    direc = 0
    while True:
        if os.path.isdir('../parseAndPopulate/' + repr(direc)):
            direc += 1
        else:
            break
    direc = '../parseAndPopulate/' + repr(direc)
    try:
        os.makedirs(direc)
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise
    for platform in body['platforms']['platform']:
        capability = platform['module-list-file']
        file_name = capability['path'].split('/')[-1]
        if request.method == 'POST':
            repo_split = capability['repository'].split('.')[0]
            if os.path.isfile(get_curr_dir(__file__) + '/../../api/vendor/' + capability['owner'] + '/' + repo_split + '/' + capability['path']):
                continue

        repo_url = url + capability['owner'] + '/' + capability['repository']

        if repo_url not in repo:
            repo[repo_url] = repoutil.RepoUtil(repo_url)
            repo[repo_url].clone(application.config_name, application.config_email)

        for submodule in repo[repo_url].repo.submodules:
            submodule.update(init=True)

        if capability.get('branch'):
            branch = capability.get('branch')
        else:
            branch = 'master'
        directory = '/'.join(capability['path'].split('/')[:-1])
        save_to = direc + '/temp/' + capability['owner'] + '/' \
                  + capability['repository'].split('.')[0] + '/' + branch + '/' + directory

        try:
            shutil.copytree(repo[repo_url].localdir + '/' + directory, save_to,
                            ignore=shutil.ignore_patterns('*.json', '*.xml', '*.sh', '*.md', '*.txt', '*.bin'))
        except OSError:
            pass
        with open(save_to + '/' + file_name.split('.')[0] + '.json', "w") as f:
            json.dump(platform, f)
        shutil.copy(repo[repo_url].localdir + '/' + capability['path'], save_to)
        tree_created = True

    for key in repo:
        repo[key].remove()
    arguments = ["python", "../parseAndPopulate/populate.py", "--port",
                 repr(application.confdPort), "--dir", direc + "/temp", "--api", "--ip",
                 application.confd_ip, "--credentials", application.credentials[0], application.credentials[1],
                 repr(tree_created), application.integrity_file_location, application.protocol,
                 application.api_protocol, repr(application.api_port)]
    job_id = application.sender.send('#'.join(arguments))
    LOGGER.info('job_id {}'.format(job_id))
    return make_response(jsonify({'info': 'Verification successful', 'job-id': job_id}), 202)


@application.route('/index/search', methods=['POST'])
def index_search():
    """Search through the YANG keyword index for a given search pattern.
       The arguments are a payload specifying search options and filters.
    """
    if not request.json:
        abort(400)

    payload = request.json
    if 'search' not in payload:
        return make_response(jsonify({'error': 'You must specify a "search" argument'}), 400)
    try:
        search_res = index.do_search(json.dumps(payload))
        res = []
        rest = Rester(application.yangcatalog_api_prefix)
        rejects = {}
        not_founds = {}

        for row in search_res:
            res_row = {}
            res_row['node'] = row['node']
            if 'filter' not in payload or 'module' in payload['filter']:
                mod_obj = Module.module_factory(rest, row['module']['name'], row['module'][
                                                'revision'], row['module']['organization'])
                mod_sig = mod_obj.get_mod_sig()
                if mod_sig in rejects:
                    continue

                if 'latest-revisions' in payload and payload['latest-revisions'] is True:
                    if row['module']['revision'] != row['module']['latest_revision']:
                        rejects[mod_sig] = True
                        continue

                mod_meta = None
                try:
                    if mod_sig not in not_founds:
                        try:
                            mod_meta = mod_obj.to_dict()
                        except RestException as reste:
                            if reste.get_response_code() == 404:
                                not_founds[mod_sig] = True
                            else:
                                res_row['module'] = {
                                    'error': 'Search failed at {}: {}'.format(mod_sig, reste)}

                    if mod_meta is not None and ('include-mibs' not in payload or payload['include-mibs'] is False):
                        if re.search('yang:smiv2:', mod_obj.get('namespace')):
                            rejects[mod_sig] = True
                            continue

                    if mod_meta is not None and 'yang-versions' in payload and len(payload['yang-versions']) > 0:
                        if mod_obj.get('yang-version') not in payload['yang-versions']:
                            rejects[mod_sig] = True
                            continue

                    if mod_meta is not None:
                        if 'filter' not in payload:
                            # If the filter is not specified, return all
                            # fields.
                            res_row['module'] = mod_meta
                        elif 'module' in payload['filter']:
                            res_row['module'] = {}
                            for field in payload['filter']['module']:
                                if field in mod_meta:
                                    res_row['module'][field] = mod_meta[field]
                except Exception as e:
                    res_row['module'] = {
                        'error': 'Search failed at {}: {}'.format(mod_sig, e)}

            res.append(res_row)

        return jsonify({'results': res})
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)


@application.route('/slow', methods=['POST'])
def slow_search():
    """Search through the YANG keyword index for a given search pattern.
       The arguments are a payload specifying search options and filters.
    """
    if not request.json:
        abort(400)

    payload = request.json
    if 'search' not in payload:
        return make_response(jsonify({'error': 'You must specify a "search" argument'}), 400)
    try:
        search_res = ind.do_search(json.dumps(payload), application.dbHost,
                                   application.dbNameSearch, application.dbPass,
                                   application.dbUser)
        res = []
        rest = Rester(application.yangcatalog_api_prefix)
        rejects = {}
        not_founds = {}

        for row in search_res:
            res_row = {}
            res_row['node'] = row['node']
            if 'filter' not in payload or 'module' in payload['filter']:
                mod_obj = Module.module_factory(rest, row['module']['name'], row['module'][
                                                'revision'], row['module']['organization'])
                mod_sig = mod_obj.get_mod_sig()
                if mod_sig in rejects:
                    continue

                if 'latest-revisions' in payload and payload['latest-revisions'] is True:
                    if row['module']['revision'] != row['module']['latest_revision']:
                        rejects[mod_sig] = True
                        continue

                mod_meta = None
                try:
                    if mod_sig not in not_founds:
                        try:
                            mod_meta = mod_obj.to_dict()
                        except RestException as reste:
                            if reste.get_response_code() == 404:
                                not_founds[mod_sig] = True
                            else:
                                res_row['module'] = {
                                    'error': 'Search failed at {}: {}'.format(mod_sig, reste)}

                    if mod_meta is not None and ('include-mibs' not in payload or payload['include-mibs'] is False):
                        if re.search('yang:smiv2:', mod_obj.get('namespace')):
                            rejects[mod_sig] = True
                            continue

                    if mod_meta is not None and 'yang-versions' in payload and len(payload['yang-versions']) > 0:
                        if mod_obj.get('yang-version') not in payload['yang-versions']:
                            rejects[mod_sig] = True
                            continue

                    if mod_meta is not None:
                        if 'filter' not in payload:
                            # If the filter is not specified, return all
                            # fields.
                            res_row['module'] = mod_meta
                        elif 'module' in payload['filter']:
                            res_row['module'] = {}
                            for field in payload['filter']['module']:
                                if field in mod_meta:
                                    res_row['module'][field] = mod_meta[field]
                except Exception as e:
                    res_row['module'] = {
                        'error': 'Search failed at {}: {}'.format(mod_sig, e)}

            res.append(res_row)

        return jsonify({'results': res})
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)


@application.route('/search/<path:value>', methods=['GET'])
def search(value):
    """Search for a specific leaf from yang-catalog.yang module in modules
    branch. The key searched is defined in @module_keys variable.
            Arguments:
                :param value: (str) path that contains one of the @module_keys and
                    ends with /value searched for
                :return response to the request.
    """
    path = value
    LOGGER.info('Searching for {}'.format(value))
    split = value.split('/')[:-1]
    key = '/'.join(value.split('/')[:-1])
    value = value.split('/')[-1]
    module_keys = ['ietf/ietf-wg', 'maturity-level', 'document-name', 'author-email', 'compilation-status', 'namespace',
                   'conformance-type', 'module-type', 'organization', 'yang-version', 'name', 'revision', 'tree-type',
                   'belongs-to', 'generated-from', 'expires', 'expired']
    for module_key in module_keys:
        if key == module_key:
            active_cache = get_active_cache()
            with active_cache[0]:
                data = modules_data(active_cache[1]).get('module')
            if data is None:
                return not_found()
            passed_data = []
            for module in data:
                count = -1
                process(module, passed_data, value, module, split, count)

            if len(passed_data) > 0:
                modules = json.JSONDecoder(object_pairs_hook=collections.OrderedDict) \
                    .decode(json.dumps(passed_data))
                return Response(json.dumps({
                    'yang-catalog:modules': {
                        'module': modules
                    }
                }), mimetype='application/json')
            else:
                return not_found()
    return Response(json.dumps({'error': 'Search on path {} is not supported'.format(path)})
                    , mimetype='application/json', status=400)


@application.route('/search-filter/<leaf>', methods=['POST'])
def rpc_search_get_one(leaf):
    rpc = request.json
    if rpc.get('input'):
        recursive = rpc['input'].get('recursive')
    else:
        return not_found()
    if recursive:
        rpc['input'].pop('recursive')
    response = rpc_search(rpc)
    modules = json.loads(response.get_data()).get('yang-catalog:modules')
    if modules is None:
        return not_found()
    modules = modules.get('module')
    if modules is None:
        return not_found()
    output = set()
    for module in modules:
        if recursive:
            search_recursive(output, module, leaf)
        meta_data = module.get(leaf)
        output.add(meta_data)
    if None in output:
        output.remove(None)
    if len(output) == 0:
        return not_found()
    else:
        return Response(json.dumps({'output': {leaf: list(output)}}),
                        mimetype='application/json', status=201)


def search_recursive(output, module, leaf):
    r_name = module['name']
    response = rpc_search({'input':{'dependencies': [{'name': r_name}]}})
    modules = json.loads(response.get_data()).get('yang-catalog:modules')
    if modules is None:
        return
    modules = modules.get('module')
    if modules is None:
        return
    for mod in modules:
        search_recursive(output, mod, leaf)
        meta_data = mod.get(leaf)
        output.add(meta_data)


@application.route('/services/tree/<f1>@<r1>.yang', methods=['GET'])
def create_tree(f1, r1):
    try:
        os.makedirs(get_curr_dir(__file__) + '/temp')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return 'Server error - could not create directory'
    path_to_yang = '{}{}@{}.yang'.format(application.save_file_dir, f1, r1)
    arguments = ['pyang', '-p', application.save_file_dir, '-f', 'tree', path_to_yang]
    pyang = subprocess.Popen(arguments,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    stdout, stderr = pyang.communicate()
    if stdout == '' and stderr != '':
        return create_bootstrap_danger()
    elif stdout != '' and stderr != '':
        return create_bootstrap_warning(stdout)
    else:
        return '<html><body><pre>{}</pre></body></html>'.format(stdout)


@application.route('/services/reference/<f1>@<r1>.yang', methods=['GET'])
def create_reference(f1, r1):
    try:
        os.makedirs(get_curr_dir(__file__) + '/temp')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return 'Server error - could not create directory'
    schema1 = '{}{}@{}.yang'.format(application.save_file_dir, f1, r1)
    arguments = ['pyang', '-p', application.save_file_dir, '-f', 'tree', schema1]
    pyang = subprocess.Popen(arguments,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    stdout, stderr = pyang.communicate()
    if stdout == '' and stderr != '':
        return create_bootstrap_danger()
    elif stdout != '' and stderr != '':
        return create_bootstrap_warning(stdout)
    else:
        return '<html><body><pre>{}</pre></body></html>'.format(stdout)


def create_bootstrap_info():
    with open(get_curr_dir(__file__) + '/template/info.html', 'r') as f:
        template = f.read()
    return template


def create_bootstrap_warning(tree):
    LOGGER.info('Rendering bootstrap data')
    context = {'tree': tree}
    path, filename = os.path.split(
        get_curr_dir(__file__) + '/template/warning.html')
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                              ).get_template(filename).render(context)


def create_bootstrap_danger():
    with open(get_curr_dir(__file__) + '/template/danger.html', 'r') as f:
        template = f.read()
    return template


@application.route('/services/file1=<f1>@<r1>/check-update-from/file2=<f2>@<r2>',
           methods=['GET'])
def create_update_from(f1, r1, f2, r2):
    try:
        os.makedirs(get_curr_dir(__file__) + '/temp')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return 'Server error - could not create directory'
    schema1 = '{}{}@{}.yang'.format(application.save_file_dir, f1, r1)
    schema2 = '{}{}@{}.yang'.format(application.save_file_dir, f2, r2)
    arguments = ['pyang', '-P', get_curr_dir(__file__) + '/../../.', '-p',
                 get_curr_dir(__file__) + '/../../.',
                 schema1, '--check-update-from',
                 schema2]
    pyang = subprocess.Popen(arguments,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    stdout, stderr = pyang.communicate()
    return '<html><body><pre>{}</pre></body></html>'.format(stderr)


@application.route('/services/diff-file/file1=<f1>@<r1>/file2=<f2>@<r2>',
           methods=['GET'])
def create_diff_file(f1, r1, f2, r2):
    try:
        os.makedirs(get_curr_dir(__file__) + '/temp')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return 'Server error - could not create directory'
    schema1 = '{}{}@{}.yang'.format(application.save_file_dir, f1, r1)
    schema2 = '{}{}@{}.yang'.format(application.save_file_dir, f2, r2)

    arguments = ['cat', schema1]
    cat = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, stderr = cat.communicate()
    file_name1 = 'schema1.txt'
    with open('{}{}'.format(application.diff_file_dir, file_name1), 'w+') as f:
        f.write('<pre>{}</pre>'.format(stdout))
    arguments = ['cat', schema2]
    cat = subprocess.Popen(arguments, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, stderr = cat.communicate()
    file_name2 = 'schema2.txt'
    with open('{}{}'.format(application.diff_file_dir, file_name2), 'w+') as f:
        f.write('<pre>{}</pre>'.format(stdout))
    tree1 = 'https://yangcatalog.org/compatibility/{}'.format(file_name1)
    tree2 = 'https://yangcatalog.org/compatibility/{}'.format(file_name2)
    diff_url = ('https://www.ietf.org/rfcdiff/rfcdiff.pyht?url1={}&url2={}'
                .format(tree1, tree2))
    response = requests.get(diff_url)
    os.remove(application.diff_file_dir + '/' + file_name1)
    os.remove(application.diff_file_dir + '/' + file_name2)
    return '<html><body>{}</body></html>'.format(response.content)


@application.route('/services/diff-tree/file1=<f1>@<r1>/file2=<f2>@<r2>', methods=['GET'])
def create_diff_tree(f1, r1, f2, r2):
    try:
        os.makedirs(get_curr_dir(__file__) + '/temp')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            return 'Server error - could not create directory'
    schema1 = '{}{}@{}.yang'.format(application.save_file_dir, f1, r1)
    schema2 = '{}{}@{}.yang'.format(application.save_file_dir, f2, r2)

    arguments = ['pyang', '-p', application.save_file_dir, '-f', 'tree', schema1]
    pyang = subprocess.Popen(arguments,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    stdout, stderr = pyang.communicate()
    file_name1 = 'schema1.txt'
    with open('{}{}'.format(application.diff_file_dir, file_name1), 'w+') as f:
        f.write('<pre>{}</pre>'.format(stdout))
    arguments = ['pyang', '-p', application.save_file_dir, '-f', 'tree', schema2]
    pyang = subprocess.Popen(arguments,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    stdout, stderr = pyang.communicate()
    file_name2 = 'schema2.txt'
    with open('{}{}'.format(application.diff_file_dir, file_name2), 'w+') as f:
        f.write('<pre>{}</pre>'.format(stdout))
    tree1 = 'https://yangcatalog.org/compatibility/{}'.format(file_name1)
    tree2 = 'https://yangcatalog.org/compatibility/{}'.format(file_name2)
    diff_url = ('https://www.ietf.org/rfcdiff/rfcdiff.pyht?url1={}&url2={}'
                .format(tree1, tree2))
    response = requests.get(diff_url)
    os.remove(application.diff_file_dir + '/' + file_name1)
    os.remove(application.diff_file_dir + '/' + file_name2)
    return '<html><body>{}</body></html>'.format(response.content)


@application.route('/get-common', methods=['POST'])
def get_common():
    body = request.json
    if body is None:
        return make_response(jsonify({'error': 'body of request is empty'}), 400)
    if body.get('input') is None:
        return make_response(jsonify
                             ({'error':
                                   'body of request need to start with input'}),
                             400)
    if body['input'].get('first') is None or body['input'].get('second') is None:
        return make_response(jsonify
                             ({'error':
                                   'body of request need to contain first and '
                                   'second container'}),
                             400)
    response_first = rpc_search({'input': body['input']['first']})
    response_second = rpc_search({'input': body['input']['second']})

    if response_first.status_code == 404 or response_second.status_code == 404:
        return not_found()

    data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict) \
        .decode(response_first.data)
    modules_first = data['yang-catalog:modules']['module']
    data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)\
        .decode(response_second.data)
    modules_second = data['yang-catalog:modules']['module']

    output_modules_list = []
    names = []
    for mod_first in modules_first:
        for mod_second in modules_second:
            if mod_first['name'] == mod_second['name']:
                if mod_first['name'] not in names:
                    names.append(mod_first['name'])
                    output_modules_list.append(mod_first)
    if len(output_modules_list) == 0:
        return not_found()
    return Response(json.dumps({'output': output_modules_list}),
                    mimetype='application/json')


@application.route('/check-semantic-version', methods=['POST'])
def check_semver():
    body = request.json
    if body is None:
        return make_response(jsonify({'error': 'body of request is empty'}), 400)
    if body.get('input') is None:
        return make_response(jsonify
                             ({'error':
                                   'body of request need to start with input'}),
                             400)
    if body['input'].get('old') is None or body['input'].get('new') is None:
        return make_response(jsonify
                             ({'error':
                                   'body of request need to contain new'
                                   ' and old container'}),
                             400)
    response_new = rpc_search({'input': body['input']['new']})
    response_old = rpc_search({'input': body['input']['old']})

    if response_new.status_code == 404 or response_old.status_code == 404:
        return not_found()

    data = json.loads(response_new.data)
    modules_new = data['yang-catalog:modules']['module']
    data = json.loads(response_old.data)
    modules_old = data['yang-catalog:modules']['module']

    output_modules_list = []
    for mod_old in modules_old:
        name_new = None
        semver_new = None
        revision_new = None
        status_new = None
        name_old = mod_old['name']
        revision_old = mod_old['revision']
        organization_old = mod_old['organization']
        status_old = mod_old['compilation-status']
        for mod_new in modules_new:
            name_new = mod_new['name']
            revision_new = mod_new['revision']
            organization_new = mod_new['organization']
            status_new = mod_new['compilation-status']
            if name_new == name_old and organization_new == organization_old:
                if revision_old == revision_new:
                    break
                semver_new = mod_new.get('derived-semantic-version')
                break
        if semver_new:
            semver_old = mod_old.get('derived-semantic-version')
            if semver_old:
                if semver_new != semver_old:
                    output_mod = {}
                    if status_old != 'passed' and status_new != 'passed':
                        reason = 'Both modules failed compilation'
                    elif status_old != 'passed' and status_new == 'passed':
                        reason = 'Older module failed compilation'
                    elif status_new != 'passed' and status_old == 'passed':
                        reason = 'Newer module failed compilation'
                    else:
                        file_name = ('{}/services/file1={}@{}/check-update-from/file2={}@{}'
                                     .format(application.yangcatalog_api_prefix, name_new,
                                             revision_new, name_old,
                                             revision_old))
                        reason = ('pyang --check-update-from output: {}'.
                                  format(file_name))

                        diff = (
                            '{}/services/diff-tree/file1={}@{}/file2={}@{}'.
                                format(application.yangcatalog_api_prefix, name_old,
                                       revision_old, name_new, revision_new))

                        output_mod['yang-module-pyang-tree-diff'] = diff

                    output_mod['name'] = name_old
                    output_mod['revision-old'] = revision_old
                    output_mod['revision-new'] = revision_new
                    output_mod['organization'] = organization_old
                    output_mod['old-derived-semantic-version'] = semver_old
                    output_mod['new-derived-semantic-version'] = semver_new
                    output_mod['derived-semantic-version-results'] = reason
                    diff = ('{}/services/diff-file/file1={}@{}/file2={}@{}'
                            .format(application.yangcatalog_api_prefix, name_old,
                                    revision_old, name_new, revision_new))
                    output_mod['yang-module-diff'] = diff
                    output_modules_list.append(output_mod)
    if len(output_modules_list) == 0:
        return not_found()
    output = {'output': output_modules_list}
    return make_response(jsonify(output), 200)


@application.route('/search-filter', methods=['POST'])
def rpc_search(body=None):
    if body is None:
        body = request.json
    LOGGER.info('Searching and filtering modules based on RPC {}'
                .format(json.dumps(body)))
    active_cache = get_active_cache()
    with active_cache[0]:
        data = modules_data(active_cache[1])['module']
    body = body.get('input')
    if body:
        partial = body.get('partial')
        if partial is None:
            partial = False
        passed_modules = []
        if partial:
            for module in data:
                passed = True
                if 'dependencies' in body:
                    submodules = deepcopy(module.get('dependencies'))
                    if submodules is None:
                        continue
                    for sub in body['dependencies']:
                        found = True
                        name = sub.get('name')
                        revision = sub.get('revision')
                        schema = sub.get('schema')
                        for submodule in submodules:
                            found = True
                            if name:
                                if name not in submodule['name']:
                                    found = False
                            if not found:
                                continue
                            if revision:
                                if revision not in submodule['revision']:
                                    found = False
                            if not found:
                                continue
                            if schema:
                                if schema not in submodule['schema']:
                                    found = False
                            if found:
                                break

                        if not found:
                            passed = False
                            break
                if not passed:
                    continue
                if 'dependents' in body:
                    submodules = deepcopy(module.get('dependents'))
                    if submodules is None:
                        continue
                    for sub in body['dependents']:
                        found = True
                        name = sub.get('name')
                        revision = sub.get('revision')
                        schema = sub.get('schema')
                        for submodule in submodules:
                            found = True
                            if name:
                                if name not in submodule['name']:
                                    found = False
                            if not found:
                                continue
                            if revision:
                                if revision not in submodule['revision']:
                                    found = False
                            if not found:
                                continue
                            if schema:
                                if schema not in submodule['schema']:
                                    found = False
                            if found:
                                break

                        if not found:
                            passed = False
                            break
                if not passed:
                    continue
                if 'submodule' in body:
                    submodules = deepcopy(module.get('submodule'))
                    if submodules is None:
                        continue
                    for sub in body['submodule']:
                        found = True
                        name = sub.get('name')
                        revision = sub.get('revision')
                        schema = sub.get('schema')
                        for submodule in submodules:
                            found = True
                            if name:
                                if name not in submodule['name']:
                                    found = False
                            if not found:
                                continue
                            if revision:
                                if revision not in submodule['revision']:
                                    found = False
                            if not found:
                                continue
                            if schema:
                                if schema not in submodule['schema']:
                                    found = False
                            if found:
                                break

                        if not found:
                            passed = False
                            break
                if not passed:
                    continue
                if 'implementations' in body:
                    implementations = deepcopy(module.get('implementations'))
                    if implementations is None:
                        continue
                    passed = True
                    for imp in body['implementations']['implementation']:
                        if not passed:
                            break
                        for leaf in imp:
                            found = False
                            impls = []
                            if leaf == 'deviation':
                                for implementation in implementations[
                                    'implementation']:
                                    deviations = implementation.get('deviation')
                                    if deviations is None:
                                        continue
                                    for dev in imp[leaf]:
                                        found = True
                                        name = dev.get('name')
                                        revision = dev.get('revision')
                                        for deviation in deviations:
                                            found = True
                                            if name:
                                                if name not in deviation['name']:
                                                    found = False
                                            if not found:
                                                continue
                                            if revision:
                                                if revision not in deviation['revision']:
                                                    found = False
                                            if found:
                                                break
                                        if not found:
                                            break
                                    if not found:
                                        continue
                                    else:
                                        impls.append(implementation)
                                if not found:
                                    passed = False
                                    break
                            elif leaf == 'feature':
                                for implementation in implementations['implementation']:
                                    if implementation.get(leaf) is None:
                                        continue
                                    if imp[leaf] in implementation[leaf]:
                                        found = True
                                        impls.append(implementation)
                                        continue
                                if not found:
                                    passed = False
                            else:
                                for implementation in implementations['implementation']:
                                    if implementation.get(leaf) is None:
                                        continue
                                    if imp[leaf] in implementation[leaf]:
                                        found = True
                                        impls.append(implementation)
                                        continue
                                if not found:
                                    passed = False
                            if not passed:
                                break
                            implementations['implementation'] = impls
                if not passed:
                    continue
                for leaf in body:
                    if leaf != 'implementations' and leaf != 'submodule':
                        module_leaf = module.get(leaf)
                        if module_leaf:
                            if body[leaf] not in module_leaf:
                                passed = False
                                break
                if passed:
                    passed_modules.append(module)
        else:
            for module in data:
                passed = True
                if 'dependencies' in body:
                    submodules = deepcopy(module.get('dependencies'))
                    if submodules is None:
                        continue
                    for sub in body['dependencies']:
                        found = True
                        name = sub.get('name')
                        revision = sub.get('revision')
                        schema = sub.get('schema')
                        for submodule in submodules:
                            found = True
                            if name:
                                if name != submodule['name']:
                                    found = False
                            if not found:
                                continue
                            if revision:
                                if revision != submodule['revision']:
                                    found = False
                            if not found:
                                continue
                            if schema:
                                if schema != submodule['schema']:
                                    found = False
                            if found:
                                break

                        if not found:
                            passed = False
                            break
                if not passed:
                    continue
                if 'dependents' in body:
                    submodules = deepcopy(module.get('dependents'))
                    if submodules is None:
                        continue
                    for sub in body['dependents']:
                        found = True
                        name = sub.get('name')
                        revision = sub.get('revision')
                        schema = sub.get('schema')
                        for submodule in submodules:
                            found = True
                            if name:
                                if name != submodule['name']:
                                    found = False
                            if not found:
                                continue
                            if revision:
                                if revision!= submodule['revision']:
                                    found = False
                            if not found:
                                continue
                            if schema:
                                if schema != submodule['schema']:
                                    found = False
                            if found:
                                break

                        if not found:
                            passed = False
                            break
                if not passed:
                    continue
                if 'submodule' in body:
                    submodules = deepcopy(module.get('submodule'))
                    if submodules is None:
                        continue
                    for sub in body['submodule']:
                        found = True
                        name = sub.get('name')
                        revision = sub.get('revision')
                        schema = sub.get('schema')
                        for submodule in submodules:
                            found = True
                            if name:
                                if name != submodule['name']:
                                    found = False
                            if not found:
                                continue
                            if revision:
                                if revision != submodule['revision']:
                                    found = False
                            if not found:
                                continue
                            if schema:
                                if schema != submodule['schema']:
                                    found = False
                            if found:
                                break

                        if not found:
                            passed = False
                            break
                if not passed:
                    continue
                if 'implementations' in body:
                    implementations = deepcopy(module.get('implementations'))
                    if implementations is None:
                        continue
                    passed = True
                    for imp in body['implementations']['implementation']:
                        if not passed:
                            break
                        for leaf in imp:
                            found = False
                            impls = []
                            if leaf == 'deviation':
                                for implementation in implementations[
                                    'implementation']:
                                    deviations = implementation.get('deviation')
                                    if deviations is None:
                                        continue
                                    for dev in imp[leaf]:
                                        found = True
                                        name = dev.get('name')
                                        revision = dev.get('revision')
                                        for deviation in deviations:
                                            found = True
                                            if name:
                                                if name != deviation['name']:
                                                    found = False
                                            if not found:
                                                continue
                                            if revision:
                                                if revision != deviation['revision']:
                                                    found = False
                                            if found:
                                                break
                                        if not found:
                                            break
                                    if not found:
                                        continue
                                    else:
                                        impls.append(implementation)
                                if not found:
                                    passed = False
                                    break
                            elif leaf == 'feature':
                                for implementation in implementations['implementation']:
                                    if implementation.get(leaf) is None:
                                        continue
                                    if imp[leaf] == implementation[leaf]:
                                        found = True
                                        impls.append(implementation)
                                        continue
                                if not found:
                                    passed = False
                            else:
                                for implementation in implementations['implementation']:
                                    if implementation.get(leaf) is None:
                                        continue
                                    if imp[leaf] == implementation[leaf]:
                                        found = True
                                        impls.append(implementation)
                                        continue
                                if not found:
                                    passed = False
                            if not passed:
                                break
                            implementations['implementation'] = impls
                if not passed:
                    continue
                for leaf in body:
                    if (leaf != 'implementations' and leaf != 'submodule'
                        and leaf != 'dependencies' and leaf != 'dependents'):
                        if body[leaf] != module.get(leaf):
                            passed = False
                            break
                if passed:
                    passed_modules.append(module)
        if len(passed_modules) > 0:
            modules = json.JSONDecoder(object_pairs_hook=collections.OrderedDict) \
                .decode(json.dumps(passed_modules))
            return Response(json.dumps({
                'yang-catalog:modules': {
                    'module': modules
                }
            }), mimetype='application/json')
        else:
            return not_found()
    else:
        return make_response(
            jsonify({'error': 'body request has to start with "input" container'}),
            400)


@application.route('/search/vendors/<path:value>', methods=['GET'])
def search_vendors(value):
    """Search for a specific vendor, platform, os-type, os-version depending on
    the value sent via API.
            Arguments:
                :param value: (str) path that contains one of the @module_keys and
                    ends with /value searched for
                :return response to the request.
    """
    LOGGER.info('Searching for specific vendors {}'.format(value))
    path = application.protocol + '://' + application.confd_ip + ':' + repr(application.confdPort) + '/api/config/catalog/vendors/' + value + '?deep'
    data = requests.get(path, auth=(application.credentials[0], application.credentials[1]),
                        headers={'Accept': 'application/vnd.yang.data+json'})
    if data.status_code == 200 or data.status_code == 204:
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict) \
            .decode(data.content)
        return Response(json.dumps(data), mimetype='application/json')
    else:
        return not_found()


@application.route('/search/modules/<name>,<revision>,<organization>', methods=['GET'])
def search_module(name, revision, organization):
    """Search for a specific module defined with name, revision and organization
            Arguments:
                :param name: (str) name of the module
                :param revision: (str) revision of the module
                :param organization: (str) organization of the module
                :return response to the request with job_id that user can use to
                    see if the job is still on or Failed or Finished successfully
    """
    active_cache = get_active_cache()
    with active_cache[0]:
        LOGGER.info('Searching for module {}, {}, {}'.format(name, revision,
                                                             organization))
        if uwsgi.cache_exists(name + '@' + revision + '/' + organization,
                              'cache_chunks{}'.format(active_cache[1])):
            chunks = uwsgi.cache_get(name + '@' + revision + '/' + organization,
                                     'cache_chunks{}'.format(active_cache[1]))
            data = ''
            for i in range(0, int(chunks), 1):
                data += uwsgi.cache_get(name + '@' + revision + '/' +
                                        organization + '-' + repr(i),
                                        'cache_modules{}'.format(active_cache[1]))

            return Response(json.dumps({
                'module': [json.JSONDecoder(object_pairs_hook=collections.OrderedDict)\
                    .decode(data)]
            }), mimetype='application/json')
        return not_found()


@application.route('/search/modules', methods=['GET'])
def get_modules():
    """Search for a all the modules populated in confd
            :return response to the request with all the modules
    """
    active_cache = get_active_cache()
    with active_cache[0]:
        LOGGER.info('Searching for modules')
        return Response(json.dumps(modules_data(active_cache[1])), mimetype='application/json')


@application.route('/search/vendors', methods=['GET'])
def get_vendors():
    """Search for a all the vendors populated in confd
            :return response to the request with all the vendors
    """
    active_cache = get_active_cache()
    with active_cache[0]:
        LOGGER.info('Searching for vendors')
        return Response(json.dumps(vendors_data(active_cache[1])), mimetype='application/json')


@application.route('/search/catalog', methods=['GET'])
def get_catalog():
    """Search for a all the data populated in confd
                :return response to the request with all the data
    """
    LOGGER.info('Searching for catalog data')
    active_cache = get_active_cache()
    with active_cache[0]:
        data = catalog_data(active_cache[1])
    if data is None:
        return not_found()
    else:
        return Response(json.dumps(data), mimetype='application/json')


@application.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    """Search for a job_id to see the process of the job
                :return response to the request with the job
    """
    LOGGER.info('Searching for job_id {}'.format(job_id))
    result = application.sender.get_response(job_id)
    split = result.split('#split#')

    reason = None
    if split[0] == 'Failed':
        result = split[0]
        reason = split[1]

    return jsonify({'info': {'job-id': job_id,
                             'result': result,
                             'reason': reason}
                    })


@application.route('/check-platform-metadata', methods=['POST'])
def trigger_populate():
    LOGGER.info('Trigger populate if necessary')
    try:
        commits = request.json['commits']
        paths = []
        new = []
        mod = []
        if commits:
            for commit in commits:
                added = commit.get('added')
                if added:
                    for add in added:
                        if 'platform-metadata.json' in add:
                            paths.append('/'.join(add.split('/')[:-1]))
                            new.append('/'.join(add.split('/')[:-1]))
                modified = commit.get('modified')
                if modified:
                    for m in modified:
                        if 'platform-metadata.json' in m:
                            paths.append('/'.join(m.split('/')[:-1]))
                            mod.append('/'.join(m.split('/')[:-1]))
        if len(paths) > 0:
            mf = messageFactory.MessageFactory()
            mf.send_new_modified_platform_metadata(new, mod)
            LOGGER.info('Forking the repo')
            repo = repoutil.RepoUtil('https://github.com/YangModels/yang.git')
            try:
                repo.clone(application.config_name, application.config_email)
                LOGGER.info('Cloned repo to local directory {}'
                            .format(repo.localdir))
                for path in paths:
                    arguments = ["python", repo.localdir + "/" +
                                 "tools/parseAndPopulate/populate.py", "--port", repr(application.confdPort), "--ip",
                                 application.confd_ip, "--api-protocol", application.api_protocol, "--api-port",
                                 repr(application.api_port), "--api-ip", application.ip,
                                 "--dir", repo.localdir + "/" + path, "--result-html-dir", application.result_dir,
                                 "--credentials", application.credentials[0], application.credentials[1],
                                 "--save-file-dir", application.save_file_dir, "repoLocalDir"]
                    arguments = arguments + paths + [repo.localdir, "github"]
                    application.sender.send("#".join(arguments))
            except:
                LOGGER.error('Could not populate after git push')
                repo.remove()
            return make_response(jsonify({'info': 'Success'}), 200)
        return make_response(jsonify({'info': 'Success'}), 200)
    except Exception as e:
        LOGGER.error('Automated github webhook failure - {}'.format(e.message))
        return make_response(jsonify({'info': 'Success'}), 200)


@application.route('/load-cache', methods=['POST'])
@auth.login_required
def load_to_memory():
    """Load all the data populated to yang-catalog to memory.
            :return response to the request.
    """
    username = request.authorization['username']
    if username != 'admin':
        return unauthorized
    if get_password(username) != hash_pw(request.authorization['password']):
        return unauthorized()
    load(True)
    return make_response(jsonify({'info': 'Success'}), 201)


@application.route('/contributors', methods=['GET'])
def get_organizations():
    orgs = set()
    active_cache = get_active_cache()
    with active_cache[0]:
        data = modules_data(active_cache[1]).get('module')
    for mod in data:
        if mod['organization'] != 'example' and mod['organization'] != 'missing element':
            orgs.add(mod['organization'])
    orgs = list(orgs)
    resp = make_response(jsonify({'contributors': orgs}), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def modules_data(which_cache):
    chunks = int(uwsgi.cache_get('chunks-modules', 'cache_chunks{}'.format(which_cache)))
    data = ''
    for i in range(0, chunks, 1):
        data += uwsgi.cache_get('modules-data{}'.format(i), 'main_cache{}'.format(which_cache))
    json_data = \
        json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(data)
    return json_data


def vendors_data(which_cache):
    chunks = int(uwsgi.cache_get('chunks-vendor', 'cache_chunks{}'.format(which_cache)))
    data = ''
    for i in range(0, chunks, 1):
        data += uwsgi.cache_get('vendors-data{}'.format(i), 'main_cache{}'.format(which_cache))
    json_data = \
        json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(data)
    return json_data


def catalog_data(which_cache):
    chunks = int(uwsgi.cache_get('chunks-data', 'cache_chunks{}'.format(which_cache)))
    if chunks == 0:
        return None
    data = ''
    for i in range(0, chunks, 1):
        data += uwsgi.cache_get('data{}'.format(i), 'main_cache{}'.format(which_cache))
    json_data = \
        json.JSONDecoder(object_pairs_hook=collections.OrderedDict) \
            .decode(data)
    return json_data


def get_active_cache():
    active_cache = uwsgi.cache_get('active_cache', 'cache_chunks1')
    if active_cache is None:
        return None
    else:
        if active_cache == '1':
            return lock_uwsgi_cache1, '1'
        else:
            return lock_uwsgi_cache2, '2'


def load(on_change):
    """Load all the data populated to yang-catalog to memory saved in file in ./cache."""
    active_cache = get_active_cache()
    if active_cache is None or on_change:
        # We should get here only if application was started for the first time (active_cache is None)
        # or if we need to reload cache (on_change == True)

        with lock_for_load:
            with lock_uwsgi_cache1:
                LOGGER.info('Loading cache 1')
                load_uwsgi_cache('cache_chunks1', 'main_cache1', 'cache_modules1', on_change)
                # reset active cache back to 1 since we are done with populating cache 1
                uwsgi.cache_update('active_cache', '1', 0, 'cache_chunks1')
            LOGGER.info('Loading cache 2')
            with lock_uwsgi_cache2:
                load_uwsgi_cache('cache_chunks2', 'main_cache2', 'cache_modules2', on_change)
            LOGGER.info('Both caches are loaded')
    else:
        # if we need to get some data from api
        if active_cache[1] == '1':
            # From cache 1
            with lock_uwsgi_cache1:
                load_uwsgi_cache('cache_chunks1', 'main_cache1', 'cache_modules1', on_change)
                # reset active cache back to 1 since we are done with populating cache 1
                uwsgi.cache_update('active_cache', '1', 0, 'cache_chunks1')
                LOGGER.info('Using cache 1')
        else:
            with lock_uwsgi_cache2:
                initialized = uwsgi.cache_get('initialized', 'cache_chunks2')
                LOGGER.debug('initialized {} on change {}'.format(initialized, on_change))
                if initialized is not None and initialized == 'True':
                    load_uwsgi_cache('cache_chunks2', 'main_cache2', 'cache_modules2', on_change)
                    LOGGER.info('Using cache 2')


def load_uwsgi_cache(cache_chunks, main_cache, cache_modules, on_change):
    response = 'work'
    initialized = uwsgi.cache_get('initialized', cache_chunks)
    LOGGER.debug('initialized {} on change {}'.format(initialized, on_change))
    if initialized is None or initialized == 'False' or on_change:
        uwsgi.cache_clear(cache_chunks)
        uwsgi.cache_clear(main_cache)
        uwsgi.cache_clear(cache_modules)
        if cache_chunks == 'cache_chunks1':
            # set active cache to 2 until we work on cache 1
            uwsgi.cache_set('active_cache', '2', 0, 'cache_chunks1')
        uwsgi.cache_set('initialized', 'False', 0, cache_chunks)
        response, data = make_cache(application.credentials, response, cache_chunks, main_cache, is_uwsgi=application.is_uwsgi)

        cat = \
            json.JSONDecoder(object_pairs_hook=collections.OrderedDict) \
                .decode(data)['yang-catalog:catalog']
        modules = cat['modules']
        if cat.get('vendors'):
            vendors = cat['vendors']
        else:
            vendors = {}
        if len(modules) != 0:
            for i, mod in enumerate(modules['module']):
                key = mod['name'] + '@' + mod['revision'] + '/' + mod[
                    'organization']
                value = json.dumps(mod)
                chunks = int(math.ceil(len(value) / float(20000)))
                uwsgi.cache_set(key, repr(chunks), 0, cache_chunks)
                for j in range(0, chunks, 1):
                    uwsgi.cache_set(key + '-{}'.format(j),
                                    value[j * 20000: (j + 1) * 20000], 0,
                                    cache_modules)

        chunks = int(math.ceil(len(json.dumps(modules)) / float(64000)))
        for i in range(0, chunks, 1):
            uwsgi.cache_set('modules-data{}'.format(i),
                            json.dumps(modules)[i * 64000: (i + 1) * 64000],
                            0, main_cache)
        LOGGER.info(
            'all {} modules chunks are set in uwsgi cache'.format(chunks))
        uwsgi.cache_set('chunks-modules', repr(chunks), 0, cache_chunks)

        chunks = int(math.ceil(len(json.dumps(vendors)) / float(64000)))
        for i in range(0, chunks, 1):
            uwsgi.cache_set('vendors-data{}'.format(i),
                            json.dumps(vendors)[i * 64000: (i + 1) * 64000],
                            0, main_cache)
        LOGGER.info(
            'all {} vendors chunks are set in uwsgi cache'.format(chunks))
        uwsgi.cache_set('chunks-vendor', repr(chunks), 0, cache_chunks)
    if response != 'work':
        LOGGER.error('Could not load or create cache')
        sys.exit(500)
    uwsgi.cache_update('initialized', 'True', 0, cache_chunks)


def process(data, passed_data, value, module, split, count):
    """Iterates recursively through the data to find only modules
    that are searched for
            Arguments:
                :param data: (dict) module that is searched
                :param passed_data: (list) data that contain value searched
                    for are saved in this variable
                :param value: (str) value searched for
                :param module: (dict) module that is searched
                :param split: (str) key value that conatins value searched for
                :param count: (int) if split contains '/' then we need to know
                    which part of the path are we searching.
    """
    if isinstance(data, unicode):
        if data == value:
            passed_data.append(module)
            return True
    elif isinstance(data, list):
        for part in data:
            if process(part, passed_data, value, module, split, count):
                break
    elif isinstance(data, dict):
        if data:
            count += 1
            return process(data.get(split[count]), passed_data, value, module, split, count)
    return False


@auth.hash_password
def hash_pw(password):
    """Hash the password
            Arguments:
                :param password: (str) password provided via API
                :return hashed password
    """
    return hashlib.sha256(password).hexdigest()


@auth.get_password
def get_password(username):
    """Get password out of database
            Arguments:
                :param username: (str) username privided via API
                :return hashed password
    """
    try:
        db = MySQLdb.connect(host=application.dbHost, db=application.dbName, user=application.dbUser, passwd=application.dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM `users`")

        data = cursor.fetchall()

        for row in data:
            if username in row[1]:
                return row[2]
        db.close()
        return None

    except MySQLdb.MySQLError as err:
        LOGGER.error('Cannot connect to database. MySQL error: {}'.format(err))


@auth.error_handler
def unauthorized():
    """Return unathorized error message"""
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


load(False)