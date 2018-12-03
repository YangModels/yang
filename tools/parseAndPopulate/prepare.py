import json

import tools.utility.log as log

LOGGER = log.get_logger(__name__, '/home/miroslav/log/populate/yang.log')


class Prepare:
    def __init__(self, file_name, yangcatalog_api_prefix):
        self.file_name = file_name
        self.name_revision_organization = set()
        self.yang_modules = {}
        self.yangcatalog_api_prefix = yangcatalog_api_prefix

    def add_key_sdo_module(self, yang):
        key = '{}@{}/{}'.format(yang.name, yang.revision, yang.organization)
        LOGGER.debug('Module {} parsed'.format(key))
        if key in self.name_revision_organization:
            self.yang_modules[key].implementation.extend(yang.implementation)
        else:
            if yang.tree is not None:
                yang.tree = '{}{}'.format(self.yangcatalog_api_prefix,
                                          yang.tree)

            self.name_revision_organization.add(key)
            self.yang_modules[key] = yang

    def dump_modules(self, directory):
        LOGGER.debug('Creating prepare.json file from sdo information')

        with open('../parseAndPopulate/' + directory + '/' + self.file_name +
                          '.json', "w") as prepare_model:
            json.dump({'module': [{
                'name': self.yang_modules[key].name,
                'revision': self.yang_modules[key].revision,
                'organization': self.yang_modules[key].organization,
                'schema': self.yang_modules[key].schema,
                'generated-from': self.yang_modules[key].generated_from,
                'maturity-level': self.yang_modules[key].maturity_level,
                'document-name': self.yang_modules[key].document_name,
                'author-email': self.yang_modules[key].author_email,
                'reference': self.yang_modules[key].reference,
                'module-classification': self.yang_modules[
                    key].module_classification,
                'compilation-status': self.yang_modules[key].compilation_status,
                'compilation-result': self.yang_modules[key].compilation_result,
                'expires': self.yang_modules[key].expiration_date,
                'expired': self.yang_modules[key].expired,
                'prefix': self.yang_modules[key].prefix,
                'yang-version': self.yang_modules[key].yang_version,
                'description': self.yang_modules[key].description,
                'contact': self.yang_modules[key].contact,
                'module-type': self.yang_modules[key].module_type,
                'belongs-to': self.yang_modules[key].belongs_to,
                'tree-type': self.yang_modules[key].tree_type,
                'yang-tree': self.yang_modules[key].tree,
                'ietf': {
                    'ietf-wg': self.yang_modules[key].ietf_wg
                },
                'namespace': self.yang_modules[key].namespace,
                'submodule': json.loads(self.yang_modules[key].json_submodules),
                'dependencies': self.__get_dependencies(self.yang_modules[key]
                                                        .dependencies),
                'semantic-version': self.yang_modules[key].semver,
                'derived-semantic-version': self.yang_modules[key].derived_semver,
                'implementations': {
                    'implementation': [{
                        'vendor': implementation.vendor,
                        'platform': implementation.platform,
                        'software-version': implementation.software_version,
                        'software-flavor': implementation.software_flavor,
                        'os-version': implementation.os_version,
                        'feature-set': implementation.feature_set,
                        'os-type': implementation.os_type,
                        'feature': implementation.feature,
                        'deviation': self.__get_deviations(
                            implementation.deviations),
                        'conformance-type': implementation.conformance_type
                    } for implementation in
                        self.yang_modules[key].implementation],
                }
            } for key in self.name_revision_organization]}, prepare_model)

    def dump_vendors(self, directory):
        with open('../parseAndPopulate/' + directory + '/normal.json',
                  "w") as ietf_model:
            json.dump({
                'vendors': {
                    'vendor': [{
                        'name': impl.vendor,
                        'platforms': {
                            'platform': [{
                                'name': impl.platform,
                                'software-versions': {
                                    'software-version': [{
                                        'name': impl.software_version,
                                        'software-flavors': {
                                            'software-flavor': [{
                                                'name': impl.software_flavor,
                                                'protocols': {
                                                    'protocol': [{
                                                        'name': 'netconf',
                                                        'capabilities': impl.capability,
                                                        'protocol-version': impl.netconf_version,
                                                    }]
                                                },
                                                'modules': {
                                                    'module': [{
                                                        'name':
                                                            self.yang_modules[
                                                                key].name,
                                                        'revision':
                                                            self.yang_modules[
                                                                key].revision,
                                                        'organization':
                                                            self.yang_modules[
                                                                key].organization,
                                                        'os-version': impl.os_version,
                                                        'feature-set': impl.feature_set,
                                                        'os-type': impl.os_type,
                                                        'feature': impl.feature,
                                                        'deviation': self.__get_deviations(
                                                            impl.deviations),
                                                        'conformance-type': impl.conformance_type
                                                    }],
                                                }
                                            }]
                                        }
                                    }]
                                }
                            }]
                        }
                    } for key in self.name_revision_organization for impl in
                        self.yang_modules[key].implementation]
                }
            }, ietf_model)

    @staticmethod
    def __get_deviations(deviations):
        if deviations is None:
            return None
        else:
            return [
                {'name': dev.name,
                 'revision': dev.revision
                 } for dev in deviations]

    @staticmethod
    def __get_dependencies(dependencies):
        if dependencies is None:
            return None
        else:
            return [
                {'name': dep.name,
                 'revision': dep.revision,
                 'schema': dep.schema
                 } for dep in dependencies]
