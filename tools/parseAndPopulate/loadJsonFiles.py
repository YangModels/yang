import requests

from tools.utility import log

LOGGER = log.get_logger('modules', '/home/miroslav/log/populate/yang.log')


class LoadFiles:
    __prefix = 'https://new.yangcatalog.org/private/'

    def __init__(self, credentials):
        LOGGER.debug('Loading Benoit\'s compilation statuses and results')
        response = requests.get('https://new.yangcatalog.org/private/json_links', auth=(credentials[0], credentials[1]))
        self.names = []
        if response.status_code == 200:
            self.names = response.text.replace('.json', '').split('\n')
            if self.names.count(''):
                self.names.remove('')
        self.status = {}
        self.headers = {}
        for name in self.names:
            self.status[name] = requests.get('{}{}.json'.format(self.__prefix, name)
                                             , auth=(credentials[0], credentials[1])).json()
            html = requests.get('{}{}YANGPageCompilation.html'.format(self.__prefix, name)
                                , auth=(credentials[0], credentials[1])).text

            ths = html.split('<TH>')
            results = []
            for th in ths:
                res = th.split('</TH>')[0]
                if 'Compilation Result' in res:
                    results.append(res)
            self.headers[name] = results
