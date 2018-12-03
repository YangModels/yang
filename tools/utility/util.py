# searching for file based on pattern or pattern_with_revision
import fnmatch
import json
import os
import urllib2

from numpy.f2py.auxfuncs import throw_error

import tools.utility.log as lo
from tools.utility import yangParser

LOGGER = lo.get_logger('util')


def get_curr_dir(f):
    LOGGER.debug('{}'.format(os.getcwd()))
    return os.getcwd()


def resolve_results(url):
    failed = True
    html = None
    tries = 10
    results = []
    while failed:
        try:
            html = urllib2.urlopen(url).read()
            failed = False
        except:
            tries -= 1
            if tries == 0:
                failed = False
            pass
    if tries == 0:
        raise throw_error('Couldn`t open a json file from url: ' + url)
    ths = html.split('<TH>')
    for th in ths:
        res = th.split('</TH>')[0]
        if 'Compilation Result' in res:
            results.append(res)

    return results


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


def find_first_file(directory, pattern, pattern_with_revision):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern_with_revision):
                filename = os.path.join(root, basename)
                return filename
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                try:
                    revision = yangParser.parse(filename).search('revision')[0]\
                        .arg
                except:
                    revision = '1970-01-01'
                if '*' not in pattern_with_revision:
                    if revision in pattern_with_revision:
                        return filename
                else:
                    return filename
