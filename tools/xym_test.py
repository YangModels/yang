#!/usr/bin/python
__author__ = "Jan Medved"
__copyright__ = "Copyright(c) 2015, Cisco Systems, Inc."
__license__ = "New-style BSD"
__email__ = "jmedved@cisco.com"

from xym import xym
from os import listdir
import argparse


if __name__ == "__main__":
    """
    A test utility for xym.py. It is typically run over a directory
    containing multiple RFC and/or draft text files from which the
    yang modules are to be extracted.
    """

    parser = argparse.ArgumentParser(description='Extract model out of an IETF RFC or src_name')
    parser.add_argument("--inpath", default='.', help="Directory where to find the test RFC/draft text files)")
    parser.add_argument("--outpath", default='.', help="Directory where to put the extracted yang module(s)")
    parser.add_argument("--strict", type=bool, default=False, help='Determines strict syntax enforcement - '
                                                                   'requires <CDE BEGINS> / <CODE ENDS>')
    parser.add_argument("--debug", type=int, default=0, help="Debug level")
    args = parser.parse_args()

    files = listdir(args.inpath)
    total_models = 0
    for f in files:
        if '.txt' in f:
            print "*** Extracting models from: %s ***" % f
            extracted_models = xym(f, args.inpath, args.outpath, args.strict, args.debug)
            if len(extracted_models) > 0:
                print "Created the following models:"
                for em in extracted_models:
                    print '   %s' % em
                total_models += len(extracted_models)
            else:
                print 'No models created.'
    print '\n**** Total models created: % d' % total_models


