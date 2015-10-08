#!/usr/bin/python
from __future__ import print_function  # Must be at the beginning of the file
import argparse
from collections import Counter
import os.path
import sys
import re
import requests
from requests.packages.urllib3 import disable_warnings

__author__ = 'jmedved@cisco.com, calle@tail-f.com, bclaise@cisco.com'
__copyright__ = "Copyright(c) 2015, Cisco Systems, Inc."
__license__ = "New-style BSD"
__email__ = "jmedved@cisco.com"
__version__ = "0.1.1"

if sys.version_info < (2, 7, 9):
    disable_warnings()

def remove_leading_spaces(mdl):
    """
    Helper function that removes leading spaces from an extracted module;
    depending on the formatting of the draft/rfc text, may have multiple
    spaces prepended to each line.
    :param mdl: YANG model lines from the text string
    :return: YANG model lines with leading spaces removed
    """
    leading_spaces = 1024
    for line in mdl:
        if line.rstrip(' \r\n') != '':
            leading_spaces = min(leading_spaces, len(line) - len(line.lstrip(' ')))
    res = []
    for l in mdl:
        res.append(l[leading_spaces:])
    return res


class YangModuleExtractor:
    """
    Extract yang modules from IETF RFC or draft text string.
    """
    MODULE_STATEMENT = re.compile('''^[ \t]*(sub)?module +(["'])?([-A-Za-z0-9]*(@[0-9-]*)?)(["'])? *\{.*$''')
    PAGE_TAG = re.compile('.*\[Page [0-9]*\].*')
    CODE_ENDS_TAG = re.compile('^[ \t]*<CODE ENDS>.*$')
    CODE_BEGINS_TAG = re.compile('^[ \t]*<CODE BEGINS>( *file( +"(.*)")?)?.*$')

    def __init__(self, src_id, dst_dir, strict, debug_level):
        """
        Initializes class-global variables.
        :param src_id: text string containing the draft or RFC text from which YANG
                      module(s) are to be extracted
        :param dst_dir: Directory where to put the extracted yang module(s)
        :param strict: Mode - if 'True', enforce <CODE BEGINS> / <CODE ENDS>;
                       if 'False', just look for 'module <name> {' and '}'
        :param debug_level: If > 0 print some debug statements to the console
        :return:
        """
        self.src_id = src_id
        self.dst_dir = dst_dir
        self.strict = strict
        self.debug_level = debug_level
        self.model = []
        self.extracted_models = []

    def warning(self, s):
        """
        Prints out a warning message to stderr.
        :param s: The warning string to print
        :return: None
        """
        print("WARNING: '%s', %s" % (self.src_id, s), file=sys.stderr)

    def error(self, s):
        """
        Prints out an error message to stderr.
        :param s: The error string to print
        :return: None
        """
        print("ERROR: '%s', %s" % (self.src_id, s), file=sys.stderr)

    def get_extracted_models(self):
        return self.extracted_models

    def remove_newlines(self, m):
        """
        Removes superfluous newlines from a YANG model that was extracted from
        a draft or RFC text.

        :param m: Original YANG model
        :return: YANG model with superfluous newlines removed
        """
        ncnt = 0
        o = []
        for ln in m:
            # print(':'.join(x.encode('hex') for x in ln))
            # print(ncnt)
            if ln.strip(' \n\r') is '':
                if ncnt is 0:
                    o.append(ln)
                ncnt += 1
            else:
                o.append(ln)
                ncnt = 0
        if self.debug_level > 0:
            print('   Removed %d empty lines' % (len(m) - len(o)))
        return o

    def write_model_to_file(self, mdl, fn):
        """
        Write a yang model that was extracted from a source identifier
        (URL or source .txt file) to a .yang destination file
        :param mdl: YANG model, as a list of lines
        :param fn: Name of the yang model file
        :return:
        """
        # Write the model to file
        output = ''.join(self.remove_newlines(remove_leading_spaces(mdl)))
        if fn:
            fqfn = self.dst_dir + '/' + fn
            if os.path.isfile(fqfn):
                self.error("File '%s' exists" % fqfn)
                return
            with open(fqfn, 'w') as of:
                of.write(output)
                of.close()
                self.extracted_models.append(fn)
        else:
            self.error("Output file name can not be determined; yang file not created")

    def extract_yang_model(self, content):
        """
        Extracts one or more yang models from a RFC/draft text string in which the
        models are specified. The function skips over page formatting (headers
        and footers) and performs basic yang module syntax checking. In strict
        mode, the function also enforces the <CODE BEGINS> / <CODE ENDS> tags
        - a model is not extracted unless the tags are present.
        :return: None
        """
        model = []
        output_file = None
        in_model = False
        i = 0
        level = 0
        while i < len(content):
            line = content[i]
            # Try to match '<CODE ENDS>'
            if self.CODE_ENDS_TAG.match(line):
                if in_model is False:
                    self.warning("Line %d: misplaced <CODE ENDS>" % i)
                in_model = False

            # Try to match '(sub)module <module_name> {'
            match = self.MODULE_STATEMENT.match(line)
            if match:
                # We're already parsing a module
                if level > 0:
                    self.error("Line %d - 'module' statement within another module" % i)
                    return
                # Check if we should enforce <CODE BEGINS> / <CODE ENDS>
                # if we do enforce, we ignore models  not enclosed in <CODE BEGINS> / <CODE ENDS>
                if match.groups()[1] or match.groups()[4]:
                    self.warning('Line %d - Module name should not be enclosed in quotes' % i)
                if self.strict is True:
                    if in_model is True:
                        level = 1
                else:
                    level = 1
                    if in_model is False:
                        self.warning("Line %d - Yang module with no <CODE BEGINS>" % i)
                if not output_file and level == 1:
                    output_file = '%s.yang' % match.groups()[2].strip('"\'')
                    if self.debug_level > 0:
                        print('   Getting yang file name from module name: %s' % output_file)

            if level > 0:
                # Try to match '[Page <page_num>]'
                # If match found, skip over page headers and footers
                if self.PAGE_TAG.match(line):
                    i += 1
                    # Skip over empty lines until the next page header is found
                    while i < len(content):
                        cnt = content[i].strip(' \r\n')
                        # print('%d: cnt - %s ' % (i, ':'.join(x.encode('hex') for x in content[i])))
                        if cnt != '':
                            break
                        i += 1
                    if i < len(content):
                        i += 1
                    else:
                        self.error("<End of File> - EOF encountered while parsing the model")
                        return
                else:
                    if self.debug_level > 1:
                        print('%d %d: %s' % (i, level, line))
                    if self.debug_level > 2:
                        print(':'.join(x.encode('hex') for x in line))
                    model.append(line)
                    counter = Counter(line)
                    level += (counter['{'] - counter['}'])
                    if level == 1:
                        self.write_model_to_file(model, output_file)
                        model = []
                        output_file = None
                        level = 0

            # Try to match '<CODE BEGINS>'
            match = self.CODE_BEGINS_TAG.match(line)
            if match:
                # Found the beginning of the yang module code section; make sure we're not parsing a model already
                if level > 0:
                    self.error("Line %d - <CODE BEGINS> within a model" % i)
                    return
                if in_model is True:
                    self.error("Line %d - Misplaced <CODE BEGINS> or missing <CODE ENDS>" % i)
                in_model = True
                mg = match.groups()
                # Get the yang module's file name
                if mg[2]:
                    output_file = mg[2].strip()
                else:
                    if mg[0] and mg[1] is None:
                        self.warning('Line %d - Missing file name in <CODE BEGINS>' % i)
                    else:
                        self.warning("Line %d - Yang file not specified in <CODE BEGINS>" % i)
            i += 1
        if level > 0:
            self.error("<End of File> - EOF encountered while parsing the model")
            return
        if in_model is True:
            self.error("Line %d - Missing <CODE ENDS>" % i)


def xym(source_id, srcdir, dstdir, strict, debug_level):
    """
    Extracts yang model from an IETF RFC or draft text file.
    This is the main (external) API entry for the module.
    :param source_id: identifier (file name or URL) of a draft or RFC file containing
           one or more yang models
    :param srcdir: If source_id points to a file, the optional parameter identifies
           the directory where the file is located
    :param dstdir: Directory where to put the extracted yang models
    :param strict: Strict syntax enforcement
    :param debug_level: Determines how much debug output is printed to the console
    :return: None
    """
    url = re.compile(r'^(?:http|ftp)s?://'  # http:// or https://
                     r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
                     r'localhost|'  # localhost...
                     r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                     r'(?::\d+)?'  # optional port
                     r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    rqst_hdrs = {'Accept': 'text/plain', 'Accept-Charset': 'utf-8'}

    ye = YangModuleExtractor(source_id, dstdir, strict, debug_level)
    is_url = url.match(source_id)
    if is_url:
        r = requests.get(source_id, headers=rqst_hdrs)
        if r.status_code == 200:
            content = r.text.encode('utf8').splitlines(True)
            ye.extract_yang_model(content)
        else:
            print("Failed to fetch file from URL '%s', error '%d'" % (source_id, r.status_code), file=sys.stderr)
    else:
        try:
            with open(os.path.join(srcdir, source_id)) as sf:
                ye.extract_yang_model(sf.readlines())
        except IOError as ioe:
            print(ioe)
    return ye.get_extracted_models()


if __name__ == "__main__":
    """
    Command line utility / test
    """
    parser = argparse.ArgumentParser(description='Extracts one or more yang models from an IETF RFC/draft text file')
    parser.add_argument("source", help="The URL or file name of the RFC/draft text from which to get the model")
    parser.add_argument("--srcdir", default='.', help="Optional: directory where to find the source text; "
                                                      "default is './'")
    parser.add_argument("--dstdir", default='.', help="Optional: directory where to put the extracted yang module(s); "
                                                      "default is './'")
    parser.add_argument("--strict", type=bool, default=False, help='Optional flag that determines syntax enforcement; '
                                                                   "'If set to 'True', the <CODE BEGINS> / <CODE ENDS> "
                                                                   "tags are required; default is 'False'")
    parser.add_argument("--debug", type=int, default=0, help="Optional: debug level - determines the amount of debug "
                                                             "info printed to console; default is 0 (no debug info "
                                                             "printed)")
    args = parser.parse_args()

    extracted_models = xym(args.source, args.srcdir, args.dstdir, args.strict, args.debug)
    if len(extracted_models) > 0:
        print("Created the following models::")
        for em in extracted_models:
            print('   %s' % em)
    else:
        print('No models created.')
