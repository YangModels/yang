from __future__ import print_function

import fnmatch
import os
import time

import capability as cap
import prepare


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


start = time.time()
i = 1
prepare = prepare.Prepare("prepare")
for filename in find_files('../../', '*capabilit*.xml'):
    print('Found xml source:' + filename)
    capability = cap.Capability(filename, i, prepare)
    capability.parse_and_dump()
    i += 1

prepare.dump()
# for filename in find_files('../', '*restconf-capabilit*.xml'):
#    print('Found xml source:' + filename)
#    capability = cap.Capability(filename)
#    capability.parse_and_dump()
end = time.time()
print(end - start)
