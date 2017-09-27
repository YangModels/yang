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

import requests

REST_TIMEOUT = 300


class RestException(Exception):

    def __init__(self, msg, rcode):
        super(RestException, self).__init__(msg)
        self._rcode = rcode

    def get_response_code(self):
        return self._rcode


class Rester(Object):
    __timeout = REST_TIMEOUT

    def __init__(self, base, username=None, password=None, timeout=REST_TIMEOUT):
        self.__base = base
        self.__username = username
        self.__password = password
        self.__timeout = timeout

    @staticmethod
    def __assert_response(resp, msg):
        if resp.status_code > 299:
            raise RestException("Failed to {}: {}".format(
                msg, resp.text), resp.status_code)

    def get(self, path, want_json=True):
        url = self.__base

        url += path

        auth = ()
        if self.__username is not None and self.__password is not None:
            auth = (self.__username, self.__password)

        headers = {}
        if want_json:
            headers['Accept'] = 'application/json'

        resp = requests.get(url, auth=auth, headers=headers,
                            timeout=self.__timeout)
        Rester.__assert_response(
            resp, "get {} from {}".format(path, self.__base))

        if want_json:
            return resp.json()
        else:
            return resp.text
