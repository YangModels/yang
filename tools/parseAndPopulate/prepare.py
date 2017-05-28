import json


class Prepare:
    def __init__(self, file_name):
        self.file_name = file_name
        self.keys = set()

    def add_key(self, key):
        self.keys.add(key)

    def dump(self):
        with open(self.file_name + '.json', "w") as prepare_model:
            json.dump({'module': [{
                'name': key.split('@')[0],
                'revision': key.split('@')[1],
                'namespace': key.split('@')[2],
                'conformance-type': key.split('@')[3]
            }for key in self.keys]}, prepare_model)
