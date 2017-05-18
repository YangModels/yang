from __future__ import print_function

import fnmatch
import os
import time

import capability as cap


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


start = time.time()
for filename in find_files('../', '*netconf-capabilit*.xml'):
    print('Found xml source:' + filename)
    capability = cap.Capability(filename)
    capability.parse_and_dump()
# for filename in find_files('../', '*restconf-capabilit*.xml'):
#    print('Found xml source:' + filename)
#    capability = cap.Capability(filename)
#    capability.parse_and_dump()
end = time.time()
print(end - start)
