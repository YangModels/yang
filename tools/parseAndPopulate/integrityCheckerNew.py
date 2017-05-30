import glob

import fnmatch
import json
import os
import unicodedata
import urllib2
import xml.etree.ElementTree as ET

from numpy.f2py.auxfuncs import throw_error

import yangParser

class Integrity:

    def __init__(self, path, *capabilities):

        self.useless_modules = []
        self.missing_modules = set()
        self.missing_submodules = set()
        self.missing_wrong_namespaces = set()
        self.missing_revision = set()
        folder = path.split('/')
        folder.remove(path.split('/')[-1])
        folder = '/'.join(folder)
        self.useless_modules = glob.glob(folder + '/*.yang')
        for caps in capabilities:
            self.root = ET.parse(folder + '/' + caps).getroot()
            tag = self.root.tag
            for cap in self.root.iter(tag.split('hello')[0] + 'capability'):
                if 'module=' in cap.text:
                    module_and_more = cap.text.split('module=')[1]
                    module_name = module_and_more.split('&')[0]
                    self.useless_modules.remove(folder + '/' + module_name + '.yang')

