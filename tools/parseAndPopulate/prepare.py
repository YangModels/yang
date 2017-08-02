import json
import logging

LOGGER = logging.getLogger(__name__)


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
        self.module_or_submodule = {}
        self.document_name = {}
        self.generated_from = {}
        self.working_group = {}
        self.tree_type = {}
        self.module_classification = {}

    def add_key_sdo(self, key, namespace, conformance_type, reference, prefix, yang_version, organization, description,
                    contact, schema, feature, json_submodules, compilation_status, author_email, maturity_level,
                    compilation_result, module_or_submodule, document_name, generated_from, working_group, tree_type,
                    module_classification):
        LOGGER.debug('Adding sdo information to prepare.json file with key {} for modules branch'.format(key))
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
        self.json_submodules[key] = json_submodules
        self.module_or_submodule[key] = module_or_submodule
        self.document_name[key] = document_name
        self.generated_from[key] = generated_from
        self.working_group[key] = working_group
        self.tree_type[key] = tree_type
        self.module_classification[key] = module_classification

    def add_key(self, key, namespace, conformance_type, vendor, platform, software_version, software_flavor, os_type,
                os_version, feature_set, reference, prefix, yang_version, organization, description, contact,
                compilation_status, author_email, schema, feature, maturity_level, compilation_result, deviations,
                json_submodules, module_or_submodule, document_name, generated_from, working_group, tree_type,
                module_classification):
        LOGGER.debug('Adding vendor information to prepare.json file with key {} for modules branch'.format(key))
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
        self.module_or_submodule[key] = module_or_submodule
        self.document_name[key] = document_name
        self.generated_from[key] = generated_from
        self.working_group[key] = working_group
        self.tree_type[key] = tree_type
        self.module_classification[key] = module_classification

        if key not in self.implementations:
            self.implementations[key] = {}
        if deviations is None:
            devs = None
        else:
            devs = [
                {'name': deviations['name'][i],
                 'revision': deviations['revision'][i]
                 } for i, val in enumerate(deviations['name'])]
        self.implementations[key][vendor + platform + software_version + software_flavor] = \
            {'vendor': vendor,
             'platform': platform,
             'software-version': software_version,
             'software-flavor': software_flavor,
             'os-type': os_type,
             'os-version': os_version,
             'feature-set': feature_set,
             'conformance-type': conformance_type,
             'feature': feature,
             'deviation': devs
             }

    def dump_sdo(self, directory):
        LOGGER.debug('Creating prepare.json file from sdo information')
        with open('../parseAndPopulate/' + directory + '/' + self.file_name + '.json', "w") as prepare_model:
            json.dump({'module': [{
                'name': key.split('@')[0],
                'revision': key.split('@')[1].split('.')[0].split(',')[0],
                'namespace': self.namespace[key],
                'reference': self.reference[key],
                'prefix': self.prefix[key],
                'yang-version': self.yang_version[key],
                'organization': self.organization[key],
                'description': self.description[key],
                'contact': self.contact[key],
                'compilation-status': self.compilation_status[key],
                'schema': self.schema[key],
                'ietf': {
                    'ietf-wg': self.working_group.get(key)
                },
                'maturity-level': self.maturity_level[key],
                'compilation-result': self.compilation_result[key],
                'author-email': self.author_email[key],
                'submodule': json.loads(self.json_submodules[key]),
                'module-type': self.module_or_submodule[key],
                'document-name': self.document_name[key],
                'generated-from': self.generated_from[key],
                'tree-type': self.tree_type[key],
                'module-classification': self.module_classification[key],
            } for key in self.name_revision]}, prepare_model)

    def dump(self, directory):
        LOGGER.debug('Creating prepare.json file from sdo information')
        with open('../parseAndPopulate/' + directory + '/' + self.file_name + '.json', "w") as prepare_model:
            json.dump({'module': [{
                'name': key.split('@')[0],
                'revision': key.split('@')[1].split('.')[0].split(',')[0],
                'namespace': self.namespace[key],
                'reference': self.reference[key],
                'prefix': self.prefix[key],
                'yang-version': self.yang_version[key],
                'organization': self.organization[key],
                'description': self.description[key],
                'contact': self.contact[key],
                'compilation-status': self.compilation_status[key],
                'author-email': self.author_email[key],
                'schema': self.schema[key],
                'ietf': {
                   'ietf-wg': self.working_group[key]
                },
                'maturity-level': self.maturity_level[key],
                'compilation-result': self.compilation_result[key],
                'submodule': json.loads(self.json_submodules[key]),
                'module-type': self.module_or_submodule[key],
                'generated-from': self.generated_from[key],
                'tree-type': self.tree_type[key],
                'module-classification': self.module_classification[key],
                'implementations': {
                    'implementation': [{
                        'vendor': self.implementations[key][implementation]['vendor'],
                        'platform': self.implementations[key][implementation]['platform'],
                        'software-version': self.implementations[key][implementation]['software-version'],
                        'software-flavor': self.implementations[key][implementation]['software-flavor'],
                        'os-type': self.implementations[key][implementation]['os-type'],
                        'os-version': self.implementations[key][implementation]['os-version'],
                        'feature-set': self.implementations[key][implementation]['feature-set'],
                        'conformance-type': self.implementations[key][implementation]['conformance-type'],
                        'deviation': self.implementations[key][implementation]['deviation'],
                        'feature': self.implementations[key][implementation]['feature']
                    } for implementation in self.implementations[key]],
                }
            } for key in self.name_revision]}, prepare_model)
