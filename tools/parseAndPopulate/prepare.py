import json


class Prepare:
    def __init__(self, file_name):
        self.file_name = file_name
        self.name_revision = set()
        self.conformance_type = {}
        self.namespace = {}
        self.implementations = {}
        self.reference = {}
        self.prefix = {}
        self.yang_version = {}
        self.organization = {}
        self.description = {}
        self.contact = {}
        self.compilation_status = {}
        self.author_email = {}
        self.schema = {}
        self.feature = {}
        self.maturity_level = {}
        self.compilation_result = {}
        self.deviations = {}
        self.json_submodules = {}

    def add_key(self, key, namespace, conformance_type, vendor, platform, software_version, software_flavor, os_type,
                os_version, feature_set, reference, prefix, yang_version, organization, description, contact,
                compilation_status, author_email, schema, feature, maturity_level, compilation_result, deviations,
                json_submodules):
        self.name_revision.add(key)
        self.namespace[key] = namespace
        self.conformance_type[key] = conformance_type
        self.reference[key] = reference
        self.prefix[key] = prefix
        self.yang_version[key] = yang_version
        self.organization[key] = organization
        self.description[key] = description
        self.contact[key] = contact
        self.compilation_status[key] = compilation_status
        self.author_email[key] = author_email
        self.schema[key] = schema
        self.feature[key] = feature
        self.maturity_level[key] = maturity_level
        self.compilation_result[key] = compilation_result
        self.deviations[key] = deviations
        self.json_submodules[key] = json_submodules

        if key not in self.implementations:
            self.implementations[key] = {}
        self.implementations[key][vendor + platform + software_version + software_flavor] = \
            {'vendor': vendor,
             'platform': platform,
             'software-version': software_version,
             'software-flavor': software_flavor,
             'os-type': os_type,
             'os-version': os_version,
             'feature-set': feature_set
             }
        pass

    def dump(self):
        with open(self.file_name + '.json', "w") as prepare_model:
            json.dump({'module': [{
                'name': key.split('@')[0],
                'revision': key.split('@')[1],
                'namespace': self.namespace[key],
                'conformance-type': self.conformance_type[key],
                'reference': self.reference[key],
                'prefix': self.prefix[key],
                'yang-version': self.yang_version[key],
                'organization': self.organization[key],
                'description': self.description[key],
                'contact': self.contact[key],
                'compilation-status': self.compilation_status[key],
                'author-email': self.author_email[key],
                'schema': self.schema[key],
                'feature': self.feature[key],
                'maturity-level': self.maturity_level[key],
                'compilation-result': self.compilation_result[key],
                'submodule': json.loads(self.json_submodules[key]),
                'implementations': {
                    'implementation': [{
                        'vendor': self.implementations[key][implementation]['vendor'],
                        'platform': self.implementations[key][implementation]['platform'],
                        'software-version': self.implementations[key][implementation]['software-version'],
                        'software-flavor': self.implementations[key][implementation]['software-flavor'],
                        'os-type': self.implementations[key][implementation]['os-type'],
                        'os-version': self.implementations[key][implementation]['os-version'],
                        'feature-set': self.implementations[key][implementation]['feature-set']
                    } for implementation in self.implementations[key]],
                },
                'deviation': [
                    {'name': self.deviations[key]['name'][i],
                     'revision': self.deviations[key]['revision'][i]
                     } for
                    i, val in enumerate(self.deviations[key]['name'])],
            } for key in self.name_revision]}, prepare_model)
