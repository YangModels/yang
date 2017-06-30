import errno
import json
import os
import urllib2

from numpy.f2py.auxfuncs import throw_error

#from ..api import repoutil
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
    ietf_draft_json = load_json_from_url('http://www.claise.be/IETFYANGDraft.json')
    repo = repoutil.RepoUtil('https://github.com/YangModels/yang.git')
    repo.clone()
    try:
        os.makedirs('ietf/DRAFT')
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != errno.EEXIST:
            raise
    for key in ietf_draft_json:
        yang_file = open('ietf/DRAFT/' + key, 'w+')
        yang_download_link = ietf_draft_json[key][2].split('href="')[1].split('">Download')[0]
        try:
            yang_raw = urllib2.urlopen(yang_download_link).read()
            yang_file.write(yang_raw)
        except:
            print(key + ' - ' + yang_download_link)
            yang_file.write('')
        yang_file.close()
    repo.add_all_untracked()
    repo.commit_all('Crone job every day pull of ietf draft yang files.')
    # repo.push()
    repo.remove()
