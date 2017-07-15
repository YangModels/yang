from __future__ import print_function

import argparse
import base64
import errno
import hashlib
import json
import os
import shutil
import subprocess
import unicodedata
import ConfigParser
import urllib2

import MySQLdb
import datetime
import requests
from flask import Flask, jsonify, abort, make_response, request, Response
from flask_httpauth import HTTPBasicAuth

import repoutil
from tools.api import yangParser

url = 'https://github.com/'

github_api_url = 'https://api.github.com'
github_repos_url = github_api_url + '/repos'
yang_models_url = github_repos_url + '/YangModels/yang'

auth = HTTPBasicAuth()
app = Flask(__name__)


def unicode_normalize(variable):
    return unicodedata.normalize('NFKD', variable).encode('ascii', 'ignore')


# Make a http request on path with json_data
def http_request(path, method, json_data, http_credentials):
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(path, data=json_data)
        request.add_header('Content-Type', 'application/vnd.yang.data+json')
        request.add_header('Accept', 'application/vnd.yang.data+json')
        base64string = base64.b64encode('%s:%s' % (http_credentials[0], http_credentials[1]))
        request.add_header("Authorization", "Basic %s" % base64string)
        request.get_method = lambda: method
        return opener.open(request)
    except:
        print('Could not send request with body ' + json_data + ' and path ' + path)
        raise


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


def authorize_for_sdos(request, organizations_sent, organization_parsed):
    username = request.authorization['username']
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
        print("Cannot connect to database. MySQL error: " + str(err))

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
        print("Cannot connect to database. MySQL error: " + str(err))

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


@app.route('/modules', methods=['PUT'])
@auth.login_required
def add_modules():
    if not request.json:
        abort(400)
    body = request.json

    with open('./prepare-sdo.json', "w") as plat:
         json.dump(body, plat)

    repo = {}
    warning = []
    for mod in body['modules']['module']:
        sdo = mod['sdo-file']
        org = mod['organization']

        directory = '/'.join(sdo['path'].split('/')[:-1])

        repo_url = url + sdo['owner'] + '/' + sdo['repo']
        if repo_url not in repo:
            repo[repo_url] = repoutil.RepoUtil(repo_url)
            repo[repo_url].clone()

        for submodule in repo[repo_url].repo.submodules:
            submodule.update(init=True)

        save_to = 'temp/' + sdo['owner'] + '/' + sdo['repo'].split('.')[0] + '/' + directory
        try:
            os.makedirs(save_to)
        except OSError as e:
            # be happy if someone already created the path
            if e.errno != errno.EEXIST:
                raise
        shutil.copy(repo[repo_url].localdir + '/' + sdo['path'], save_to)
        organization = yangParser.parse(os.path.abspath(save_to + '/' + sdo['path'].split('/')[-1])) \
            .search('organization')[0].arg
        resolved_authorization = authorize_for_sdos(request, org, organization)
        if not resolved_authorization:
            shutil.rmtree('temp/')
            for key in repo:
                repo[key].remove()
            return unauthorized()
        if 'organization' in repr(resolved_authorization):
            warning.append(sdo['path'].split('/')[-1] + ' ' + resolved_authorization)

    with open("log.txt", "wr") as f:
        try:
            arguments = ["python", "../parseAndPopulate/populate.py", "--sdo", "--port", repr(confdPort), "--dir",
                          "temp", "--api", "--ip", confd_ip, "--credentials", credentials[0], credentials[1]]
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            shutil.rmtree('temp/')
            for key in repo:
                repo[key].remove()
            return jsonify({'error': 'Was not able to write all or partial yang files'})

    try:
        os.makedirs('../../api/sdo/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise
    subprocess.call(["cp", "-r", "temp/.", "../../api/sdo/"])

    shutil.rmtree('temp')
    for item in os.listdir('./'):
        if 'log' in item and '.txt' in item:
            os.remove(item)
    for key in repo:
        repo[key].remove()
    if len(warning) > 0:
        return jsonify({'info': 'success', 'warnings': [{'warning': val}for val in warning]})
    else:
        return jsonify({'info': 'success'})


@app.route('/platforms', methods=['PUT'])
@auth.login_required
def add_vendors():
    if not request.json:
        abort(400)
    body = request.json
    resolved_authorization = authorize_for_vendors(request, body)
    if 'passed' != resolved_authorization:
        return resolved_authorization

    repo = {}
    for platform in body['platforms']:
        capability = platform['capabilities-file']
        file_name = capability['path'].split('/')[-1]

        repo_url = url + capability['owner'] + '/' + capability['repo']
        if repo_url not in repo:
            repo[repo_url] = repoutil.RepoUtil(repo_url)
            repo[repo_url].clone()

        for submodule in repo[repo_url].repo.submodules:
            submodule.update(init=True)

        directory = '/'.join(capability['path'].split('/')[:-1])
        save_to = 'temp/' + capability['owner'] + '/' + capability['repo'].split('.')[0] + '/' + directory

        try:
            shutil.copytree(repo[repo_url].localdir + '/' + directory, save_to,
                            ignore=shutil.ignore_patterns('*.json', '*.xml', '*.sh', '*.md', '*.txt', '*.bin'))
        except OSError:
            pass
        with open(save_to + '/' + file_name.split('.')[0] + '.json', "w") as plat:
            json.dump(platform, plat)
        shutil.copy(repo[repo_url].localdir + '/' + capability['path'], save_to,)

    with open("log.txt", "wr") as f:
        try:
            arguments = ["python", "../parseAndPopulate/populate.py", "--port", repr(confdPort), "--dir", "temp",
                         "--api", "--ip", confd_ip, "--credentials", credentials[0], credentials[1]]
            subprocess.check_call(arguments, stderr=f)
        except subprocess.CalledProcessError as e:
            shutil.rmtree('temp/')
            for key in repo:
                repo[key].remove()
            return jsonify({'error': 'Was not able to write all or partial yang files'})
    try:
        os.makedirs('../../api/vendor/')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise
    subprocess.call(["cp", "-r", "temp/.", "../../api/vendor/"])

    shutil.rmtree('temp/')
    for item in os.listdir('./'):
        if 'log' in item and '.txt' in item:
            os.remove(item)
    for key in repo:
        repo[key].remove()
    integrity_file_name = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%m:%S.%f")[:-3]+'Z'

    if integrity_file_location != './':
        shutil.move('./integrity.html', integrity_file_location + 'integrity' + integrity_file_name + '.html')
    return jsonify({'result':
                    {
                        'integrity-file': 'www.yangcatalog.org/integrity/integrity' + integrity_file_name + '.html',
                        'info': 'success'
                    }
                })


# Generic read-only get request
@app.route('/search/<key>/<value>', methods=['GET'])
def search(key, value):
    split = key.split('$')
    module_keys = ['ietf$ietf-wg', 'maturity-level', 'document-name', 'author-email', 'compilation-status',
                   'conformance-type', 'module-type', 'organization', 'yang-version']
    for module_key in module_keys:
        if key == module_key:
            path = protocol + '://' + confd_ip + ':' + repr(confdPort) + '/api/config/catalog/modules?deep'
            data = json.loads(http_request(path, 'GET', '', credentials).read())
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
        print("Cannot connect to database. MySQL error: " + str(err))


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
