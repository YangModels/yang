#!/usr/bin/env python
#
# migrate_yang_version.py
#
# Add 'yang-version 1.1;' statement to a YANG model  
#
# July 2021, Edward Pham 
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.
#

import sys
import os
import shutil 
import argparse

def add_yang_version(dir, file, outdir=None):
    """Write the model text to the outdir location, use default if none is
    provided
    """
    if not file.startswith('Cisco-IOS-XE'):
        return

    if file.find('-ann') > 0:
        return

    if file.find('-deviation') > 0:
        return

    if not file.endswith('.yang'):
        return

    outfile = 'out.yang'
    with open(os.path.join(dir, file)) as f, open(outfile,'w') as of:
        module = 0
        for line in f.readlines():
            if module == 0 and line.find('module ') >= 0:
                of.write(line)
                of.write('  yang-version 1.1;')
                of.write('\n')
                module = 1
            elif module == 1 and line.find('yang-version 1') >= 0:
                continue
            else:
                of.write(line)
        f.close()
        of.close()

    if not outdir:
        out = "{}/{}".format(dir, file)
    else:
        if not os.path.isdir(outdir):
            os.makedirs(outdir)
        out = "{}/{}".format(outdir, file)

    shutil.move(outfile, out)

def parse_args(opts=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to the YANG files")
    parser.add_argument("--out", help="Path to the output YANG file", default=None)
    return parser.parse_args(opts) if opts is not None else parser.parse_args()

def main(opts=None):
    """Main driver for this module"""
    args = parse_args(opts)

    if not os.path.exists(args.path):
        print('Directory %s does not exist'%(args.path))
        sys.exit(1)

    for dir, subdir, files in os.walk(args.path):
        for fname in files:
            add_yang_version(dir, fname, args.out)
        break

if __name__ == '__main__':
    main()
