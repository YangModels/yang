class StatisticsInCatalog:
    def __init__(self):
        self.sdos = {'standard/bbf/standard': [0, 0], 'standard/bbf/draft': [0, 0], 'standard/ieee/802.1': [0, 0],
                     'experimental/ieee/802.1': [0, 0], 'standard/ieee/802.3': [0, 0],
                     'experimental/ieee/802.3': [0, 0], 'standard/ieee/draft': [0, 0], 'standard/ietf/RFC': [0, 0],
                     'standard/ietf/DRAFT': [0, 0], 'experimental/openconfig': [0, 0], 'experimental/ietf': [0, 0],
                     'experimental/vendor': [0, 0], 'experimental/odp': [0, 0], # this line of dictionaries are not used in code
                     'experimental/ietf-extracted-YANG-modules': [0, 0], 'standard/mef': [0, 0]}


    def add_in_catalog(self, key):
        key = '/'.join(key.split('/')[2:5])
        try:
            self.sdos[key][0] += 1
        except KeyError:
            key = '/'.join(key.split('/')[0:2])
            self.sdos[key][0] += 1

    def set_passed(self, key, status):
        key = '/'.join(key.split('/')[2:5])
        if status == 'PASSED':
            try:
                self.sdos[key][1] += 1
            except KeyError:
                key = '/'.join(key.split('/')[0:2])
                self.sdos[key][1] += 1

    def get_passed(self, key):
        return self.sdos[key][1]

    def get_in_catalog(self, key):
        return self.sdos[key][0]
