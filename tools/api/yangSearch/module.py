# Copyright (c) 2017  Joe Clarke <jclarke@cisco.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import urllib


class Module(object):
    __object_dict = {
        'name': True,
        'revision': True,
        'organization': True,
        'ietf': True,
        'namespace': True,
        'schema': True,
        'generated-from': True,
        'maturity-level': True,
        'document-name': True,
        'author-email': True,
        'reference': True,
        'module-classification': True,
        'compilation-status': True,
        'compilation-result': True,
        'prefix': True,
        'yang-version': True,
        'description': True,
        'contact': True,
        'module-type': True,
        'belongs-to': True,
        'tree-type': True,
        'yang-tree': True,
        'expires': True,
        'submodule': True,
        'dependencies': False,
        'dependents': False,
        'semantic-version': True,
        'derived-semantic-version': True,
        'implementations': True
    }

    __seen_modules = {}

    def __init__(self, rest, name, revision, organization, attrs={}):
        self.__rester = rest
        self.__dict = {}

        for key, val in Module.__object_dict.items():
            if key in attrs:
                self.__dict[key] = attrs[key]
            else:
                self.__dict[key] = None

        if len(attrs) > 0:
            self.__initialized = True
        else:
            self.__initialized = False

        self.__dict['name'] = name
        if revision == '':
            revision = '1970-01-01'

        self.__dict['revision'] = revision
        self.__dict['organization'] = organization

    @staticmethod
    def module_factory(rest, name, revision, organization, override=False, attrs={}):
        mod_sig = '{}@{}/{}'.format(name, revision, organization)

        create_new = False
        if mod_sig not in Module.__seen_modules:
            create_new = True
        elif override:
            Module.__seen_modules[mod_sig] = None
            create_new = True

        if create_new:
            Module.__seen_modules[mod_sig] = Module(
                rest, name, revision, organization, attrs)

        return Module.__seen_modules[mod_sig]

    def __fetch(self):
        if self.__initialized:
            return

        result = self.__rester.get('/search/modules/{},{},{}'.format(urllib.quote(
            self.__dict['name']), urllib.quote(self.__dict['revision']), urllib.quote(self.__dict['organization'])))
        for key, value in result['module'][0].items():
            if key in Module.__object_dict:
                self.__dict[key] = value
            else:
                raise Exception(
                    'Failed to set key {}: not defined'.format(key))

        self.__initialized = True

    def get(self, field):
        if field not in Module.__object_dict:
            raise Exception("Field {} does not exist; please specify one of:\n\n{}".format(
                field, "\n".join(list(Module.__object_dict.keys()))))

        if not self.__initialized:
            self.__fetch()

        return self.__dict[field]

    def get_name(self):
        return self.__dict['name']

    def get_revision(self):
        return self.__dict['revision']

    def get_organization(self):
        return self.__dict['organization']

    def get_rester(self):
        return self.__rester

    def get_mod_sig(self):
        return '{}@{}/{}'.format(self.__dict['name'], self.__dict['revision'], self.__dict['organization'])

    def to_dict(self):
        if not self.__initialized:
            self.__fetch()

        arr = {}
        for key, value in Module.__object_dict.items():
            arr[key] = self.__dict[key]

        return arr

    def __del__(self):
        mod_sig = self.get_mod_sig()
        if mod_sig in Module.__seen_modules:
            del Module.__seen_modules[mod_sig]
