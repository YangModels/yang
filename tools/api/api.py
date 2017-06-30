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
import urllib2

import MySQLdb
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth

import repoutil

#url = 'https://api.github.com/repos/'
url = 'https://github.com/'

auth = HTTPBasicAuth()
app = Flask(__name__)


def unicode_normalize(variable):
    return unicodedata.normalize('NFKD', variable).encode('ascii', 'ignore')


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


def authorize(request, response):
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
                break;
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

    for platform in response['platforms']:
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


@app.route('/modules', methods=['PUT'])
@auth.login_required
def add_modules():
    if not request.json:
        abort(400)
    body = request.json
    #TODO authorization

    with open('./prepare-sdo.json', "w") as plat:
         json.dump(body, plat)

    repo = {}
    for mod in body['modules']['module']:
        sdo = mod['sdo-file']

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

    #os.system('python populate.py --sdo --port ' + repr(confdPort) + ' --dir temp --api --ip ' + confd_ip + ' --credentials '
    #                + ' '.join(credentials))
    with open("log.txt", "wr") as f:
        try:
            arguments = ["python", "populate.py", "--sdo", "--port", repr(confdPort), "--dir",
                          "temp", "--api", "--ip", confd_ip, "--credentials", credentials[0], credentials[1]]
            subprocess.check_call(arguments, stderr=f)
            #df = subprocess.Popen(args, stdout=subprocess.PIPE)
            #output, err = df.communicate()
        except subprocess.CalledProcessError as e:
            shutil.rmtree('temp/')
            for key in repo:
                repo[key].remove()
            return jsonify({'error': 'Was not able to write all or partial yang files'})

    subprocess.call(["cp", "-r", "temp/.", "../../api/sdo/"])

    shutil.rmtree('temp')
    for item in os.listdir('./'):
        if 'log' in item:
            os.remove(item)
    for key in repo:
        repo[key].remove()
    return jsonify({'info': 'success'})


@app.route('/platforms', methods=['PUT'])
@auth.login_required
def add_vendors():
    if not request.json:
        abort(400)
    body = request.json
    resolved_authorization = authorize(request, body)
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

    #os.system('python populate.py --port ' + repr(confdPort) + ' --dir temp --api --ip ' + confd_ip + ' --credentials '
    #          + ' '.join(credentials))
    with open("log.txt", "wr") as f:
        try:
            arguments = ["python", "populate.py", "--port", repr(confdPort), "--dir", "temp",
                         "--api", "--ip", confd_ip, "--credentials", credentials[0], credentials[1]]
            subprocess.check_call(arguments, stderr=f)
            #df = subprocess.Popen(args, stdout=subprocess.PIPE)
            #output, err = df.communicate()
        except subprocess.CalledProcessError as e:
            shutil.rmtree('temp/')
            for key in repo:
                repo[key].remove()
            return jsonify({'error': 'Was not able to write all or partial yang files'})

    subprocess.call(["cp", "-r", "temp/.", "../../api/vendor/"])

    shutil.rmtree('temp/')
    for key in repo:
        repo[key].remove()
    return jsonify({'info': 'success'})


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
    parser.add_argument('--dbIp', type=str, default='localhost',
                        help='Set ip where the mysql database is running')
    parser.add_argument('--dbName', type=str, default='yang_catalog',
                        help='Set name of the mysql database is running')
    parser.add_argument('--dbUser', type=str, default='root',
                        help='Set name of the user where the mysql database is running')
    parser.add_argument('--dbPassword', type=str, default='root',
                        help='Set password where the mysql database is running')
    parser.add_argument('--port', default=5000, type=int,
                        help='Set port where the api should be running')
    parser.add_argument('--ssl-cert', type=str, help='path to SSL certification file')
    parser.add_argument('--ssl-key', type=str, help='path to SSL key file')
    parser.add_argument('--confd-port', default=8008, type=int,
                        help='Set port where the confd is running')
    parser.add_argument('--ip', type=str, default='127.0.0.1',
                        help='Set ip address where this api will run default 127.0.0.1')
    parser.add_argument('--debug', action='store_true', default=False, help='debug API')
    parser.add_argument('--confd-ip', default='127.0.0.1', type=str,
                        help='Set ip address where the confd is started. Default -> 127.0.0.1')
    parser.add_argument('--credentials', help='Set authorization parameters username password respectively.'
                                              ' Default parameters are admin admin', nargs=2, default=['admin', 'admin']
                        , type=str)
    args = parser.parse_args()
    global dbHost
    dbHost = args.dbIp
    global dbName
    dbName = args.dbName
    global dbUser
    dbUser = args.dbUser
    global dbPass
    dbPass = args.dbPassword
    global credentials
    credentials =args.credentials
    global confd_ip
    confd_ip =args.confd_ip
    global confdPort
    confdPort = args.confd_port
    ssl_context = None
    if args.ssl_cert:
        ssl_context = (args.ssl_cert, args.ssl_key)
    app.run(host=args.ip, debug=args.debug, port=args.port, ssl_context=ssl_context)
