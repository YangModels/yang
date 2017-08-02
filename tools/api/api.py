import ConfigParser
import argparse
import base64
import errno
import hashlib
import json
import logging
import os
import shutil
import unicodedata
import urllib2
from urllib2 import URLError

import MySQLdb
import requests
from flask import Flask, jsonify, abort, make_response, request, Response
from flask_httpauth import HTTPBasicAuth

import repoutil
from tools.api.sender import Sender
from tools.parseAndPopulate import yangParser

LOGGER = logging.getLogger('api')
url = 'https://github.com/'

github_api_url = 'https://api.github.com'
github_repos_url = github_api_url + '/repos'
yang_models_url = github_repos_url + '/YangModels/yang'

auth = HTTPBasicAuth()
app = Flask(__name__)

NS_MAP = {
    "http://cisco.com/ns/yang/": "cisco",
    "http://www.huawei.com/netconf": "huawei",
    "http://openconfig.net/yang/": "openconfig",
    "http://tail-f.com/": "tail-f"
}


def unicode_normalize(variable):
    return unicodedata.normalize('NFKD', variable).encode('ascii', 'ignore')


# Make a http request on path with json_data
def http_request(path, method, json_data, http_credentials, header):
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


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


def authorize_for_sdos(request, organizations_sent, organization_parsed):
    username = request.authorization['username']
    LOGGER.info('Checking sdo authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=dbHost, db=dbName, user=dbUser, passwd=dbPass)
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
    username = request.authorization['username']
    LOGGER.info('Checking vendor authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=dbHost, db=dbName, user=dbUser, passwd=dbPass)
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

    for platform in body['platforms']:
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


@app.route('/checkComplete', methods=['POST'])
@auth.login_required
def check_local():
    global yang_models_url

    body = request.json
    if body['repository']['owner_name'] == 'yang-catalog':
        if body['result_message'] == 'Passed':
            if body['type'] == 'push':
                # After build was successful only locally
                json_body = jsonify({
                    "title": "Cron job - every day pull of ietf draft yang files.",
                    "body": "ietf extracted yang modules",
                    "head": "yang-catalog:master",
                    "base": "master"
                })
                requests.post(yang_models_url + '/pulls', json=json_body,
                              headers={'Authorization': 'token ' + token})

            if body['type'] == 'pull_request':
                # If build was successful on pull request
                pull_number = body['pull_request_number']
                log.write('pull request was successful %s' % repr(pull_number))
                #requests.put('https://api.github.com/repos/YangModels/yang/pulls/' + pull_number +
                #             '/merge', headers={'Authorization': 'token ' + token})
                requests.delete(yang_models_url,
                                headers={'Authorization': 'token ' + token})


@app.route('/modules/module/<name>,<revision>,<organization>', methods=['DELETE'])
@auth.login_required
def delete_modules(name, revision, organization):
    LOGGER.info('deleting module with name, revision and organization {} {} {}'.format(name, revision, organization))
    username = request.authorization['username']
    LOGGER.debug('Checking authorization for user {}'.format(username))
    accessRigths = None
    try:
        db = MySQLdb.connect(host=dbHost, db=dbName, user=dbUser, passwd=dbPass)
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
            protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/modules/module/' + name +
            ',' + revision + ',' + organization, 'GET', None, credentials, 'application/vnd.yang.data+json')
    except urllib2.HTTPError as e:
        return not_found()
    read = json.loads(response.read())
    if read['yang-catalog:module']['organization'] != accessRigths:
        return unauthorized()
    try:
        http_request(
            protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/modules/module/' + name +
            ',' + revision + ',' + organization, 'DELETE', None, credentials, 'application/vnd.yang.data+json')
    except urllib2.HTTPError as e:
        make_response(jsonify({'error': e.msg}), 401)
    return jsonify({'info': 'success'})


@app.route('/modules', methods=['PUT', 'POST'])
@auth.login_required
def add_modules():
    if not request.json:
        abort(400)
    body = request.json
    LOGGER.info('Adding modules with body {}'.format(body))
    tree_created = False

    with open('./prepare-sdo.json', "w") as plat:
        json.dump(body, plat)

    try:
        http_request(protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/modules/',
                     'DELETE', None, credentials, 'application/vnd.yang.collection+json')
    except:
        pass
    path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/modules'
    try:
        http_request(path, 'PUT', json.dumps(body), credentials, 'application/vnd.yang.data+json')
    except urllib2.HTTPError as e:
        abort(e.code)
    repo = {}
    warning = []

    direc = 0
    while True:
        if os.path.isdir('../parseAndPopulate/' + repr(direc)):
            direc += 1
        else:
            break
    direc = '../parseAndPopulate/' + repr(direc)
    for mod in body['modules']['module']:
        sdo = mod['source-file']
        orgz = mod['organization']
        if request.method == 'POST':
            try:
                path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/modules/module/' + \
                       mod['name'] + ',' + mod['revision']
                http_request(path, 'GET', None, credentials, 'application/vnd.yang.data+json')
                continue
            except urllib2.HTTPError as e:
                pass
        directory = '/'.join(sdo['path'].split('/')[:-1])

        repo_url = url + sdo['owner'] + '/' + sdo['repository']
        LOGGER.debug('Cloning repository')
        if repo_url not in repo:
            repo[repo_url] = repoutil.RepoUtil(repo_url)
            repo[repo_url].clone()

        for submodule in repo[repo_url].repo.submodules:
            submodule.update(init=True)

        if sdo.get('branch'):
            branch = sdo.get('branch')
        else:
            branch = 'master'
        save_to = direc + '/temp/' + sdo['owner'] + '/' + sdo['repository'].split('.')[0]\
                  + '/' + branch + '/' + directory
        try:
            os.makedirs(save_to)
        except OSError as e:
            # be happy if someone already created the path
            if e.errno != errno.EEXIST:
                raise
        shutil.copy(repo[repo_url].localdir + '/' + sdo['path'], save_to)
        if os.path.isfile('./prepare-sdo.json'):
            shutil.move('./prepare-sdo.json', direc)
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

    for key in repo:
        repo[key].remove()
    LOGGER.debug('Sending a new job')
    arguments = ["python", "../parseAndPopulate/populate.py", "--sdo", "--port", repr(confdPort), "--dir",
                 direc + "/temp", "--api", "--ip", confd_ip, "--credentials", credentials[0], credentials[1],
                 repr(tree_created)]
    job_id = sender.send('#'.join(arguments))
    LOGGER.info('job_id {}'.format(job_id))
    if len(warning) > 0:
        return jsonify({'info': 'Verification successful', 'job-id': job_id, 'warnings': [{'warning': val}
                                                                                          for val in warning]})
    else:
        return jsonify({'info': 'Verification successful', 'job-id': job_id})


@app.route('/platforms', methods=['PUT', 'POST'])
@auth.login_required
def add_vendors():
    if not request.json:
        abort(400)
    body = request.json
    LOGGER.info('Adding vendor with body {}'.format(body))
    tree_created = False
    resolved_authorization = authorize_for_vendors(request, body)
    if 'passed' != resolved_authorization:
        return resolved_authorization
    try:
        http_request(protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/platforms/',
                     'DELETE', None, credentials, 'application/vnd.yang.collection+json')
    except:
        pass
    path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/'
    try:
        http_request(path, 'POST', json.dumps(body), credentials, 'application/vnd.yang.data+json')
    except urllib2.HTTPError as e:
        abort(e.code)
    repo = {}

    direc = 0
    while True:
        if os.path.isdir('../parseAndPopulate/' + repr(direc)):
            direc += 1
        else:
            break
    direc = '../parseAndPopulate/' + repr(direc)

    for platform in body['platforms']:
        capability = platform['module-list-file']
        file_name = capability['path'].split('/')[-1]
        if request.method == 'POST':
            repo_split = capability['repository'].split('.')[0]
            if os.path.isfile('../../api/vendor/' + capability['owner'] + '/' + repo_split + '/' + capability['path']):
                continue

        repo_url = url + capability['owner'] + '/' + capability['repository']

        if repo_url not in repo:
            repo[repo_url] = repoutil.RepoUtil(repo_url)
            repo[repo_url].clone()

        for submodule in repo[repo_url].repo.submodules:
            submodule.update(init=True)

        if capability.get('branch'):
            branch = capability.get('branch')
        else:
            branch = 'master'
        directory = '/'.join(capability['path'].split('/')[:-1])
        save_to = direc + '/temp/' + capability['owner'] + '/'\
            + capability['repository'].split('.')[0] + '/' + branch + '/' + directory

        try:
            shutil.copytree(repo[repo_url].localdir + '/' + directory, save_to,
                            ignore=shutil.ignore_patterns('*.json', '*.xml', '*.sh', '*.md', '*.txt', '*.bin'))
        except OSError:
            pass
        with open(save_to + '/' + file_name.split('.')[0] + '.json', "w") as plat:
            json.dump(platform, plat)
        shutil.copy(repo[repo_url].localdir + '/' + capability['path'], save_to)
        tree_created = True

    for key in repo:
        repo[key].remove()
    arguments = ["python", "../parseAndPopulate/populate.py", "--port", repr(confdPort), "--dir", direc + "/temp",
                 "--api", "--ip", confd_ip, "--credentials", credentials[0], credentials[1], repr(tree_created),
                 integrity_file_location]
    job_id = sender.send('#'.join(arguments))
    LOGGER.info('job_id {}'.format(job_id))
    return jsonify({'info': 'Verification successful', 'job-id': job_id})


# Generic read-only get request
@app.route('/search/<path:value>', methods=['GET'])
def search(value):
    LOGGER.info('Searching for {}'.format(value))
    split = value.split('/')[:-1]
    key = '/'.join(value.split('/')[:-1])
    value = value.split('/')[-1]
    module_keys = ['ietf/ietf-wg', 'maturity-level', 'document-name', 'author-email', 'compilation-status',
                   'conformance-type', 'module-type', 'organization', 'yang-version', 'name', 'revision']
    for module_key in module_keys:
        if key == module_key:
            path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/modules?deep'
            try:
                data = json.loads(http_request(path, 'GET', '', credentials, 'application/vnd.yang.data+json').read())
            except:
                return not_found()
            passed_data = []
            data = data['yang-catalog:modules']['module']
            for module in data:
                count = -1
                process(module, passed_data, value, module, split, count)

            if len(passed_data) > 0:
                return Response(json.dumps({
                    'yang-catalog:modules': {
                        'module': json.loads(json.dumps(passed_data))
                    }
                }), mimetype='application/json')
            else:
                return Response(mimetype='application/json', status=204)


@app.route('/search/modules/<name>,<revision>,<organization>', methods=['GET'])
def search_module(name, revision, organization):
    LOGGER.info('Searching for module {}, {}, {}'.format(name, revision, organization))
    path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/modules/module/' + name + ',' +\
        revision + ',' + organization + '?deep'
    try:
        data = json.loads(http_request(path, 'GET', '', credentials, 'application/vnd.yang.data+json').read())
    except:
        return not_found()
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/search/modules', methods=['GET'])
def get_modules():
    LOGGER.info('Searching for modules')
    path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/vendors?deep'
    try:
        data = json.loads(http_request(path, 'GET', '', credentials, 'application/vnd.yang.data+json').read())
    except:
        return not_found()
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/search/vendors', methods=['GET'])
def get_vendors():
    LOGGER.info('Searching for vendors')
    path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/vendors/?deep'
    try:
        data = json.loads(http_request(path, 'GET', '', credentials, 'application/vnd.yang.data+json').read())
    except:
        return not_found()
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/search/catalog', methods=['GET'])
def get_catalog():
    LOGGER.info('Searching for catalog data')
    path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog?deep'
    try:
        data = json.loads(http_request(path, 'GET', '', credentials, 'application/vnd.yang.data+json').read())
    except:
        return not_found()
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    LOGGER.info('Searching for job_id {}'.format(job_id))
    result = sender.get(job_id)
    return jsonify({'info': {'job-id': job_id,
                             'result': result}
                    })


def process(data, passed_data, value, module, split, count):
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
    return hashlib.sha256(password).hexdigest()

@auth.get_password
def get_password(username):
    #    if username in users:
    #        return users.get(username)
    #    return None
    try:
        db = MySQLdb.connect(host=dbHost, db=dbName, user=dbUser, passwd=dbPass)
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
    # print row

    except MySQLdb.MySQLError as err:
        LOGGER.error('Cannot connect to database. MySQL error: {}'.format(err))


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-path', type=str, default='./config.ini',
                        help='Set path to config file')
    args = parser.parse_args()
    config = ConfigParser.ConfigParser()
    config.read(args.config_path)
    global sender
    sender = Sender()
    global dbHost
    dbHost = config.get('SectionOne', 'dbIp')
    global dbName
    dbName = config.get('SectionOne', 'dbName')
    global dbUser
    dbUser = config.get('SectionOne', 'dbUser')
    global dbPass
    dbPass = config.get('SectionOne', 'dbPassword')
    global credentials
    credentials = config.get('SectionOne', 'credentials').split(' ')
    global confd_ip
    confd_ip = config.get('SectionOne', 'confd-ip')
    global confdPort
    confdPort = int(config.get('SectionOne', 'confd-port'))
    global protocol
    protocol = config.get('SectionOne', 'protocol')
    global token
    token = config.get('SectionOne', 'yang-catalog-token')
    ssl_context = None
    global integrity_file_location
    integrity_file_location = config.get('SectionOne', 'integrity-file-location')
    global log
    ip = config.get('SectionOne', 'ip')
    port = int(config.get('SectionOne', 'port'))
    debug = config.get('SectionOne', 'debug')
    key = config.get('SectionOne', 'ssl-key')
    cert = config.get('SectionOne', 'ssl-cert')
    log = open('api_log_file.txt', 'w')
    if cert:
        ssl_context = (cert, key)
    app.run(host=ip, debug=debug, port=port, ssl_context=ssl_context)
