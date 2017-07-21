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
        self.module_or_submodule = {}
        self.document_name = {}
        self.owner = {}
        self.repo = {}
        self.repo_file_path = {}
        self.local_file_path = {}
        self.generated_from = {}
        self.working_group = {}

    def add_key_sdo(self, key, namespace, conformance_type, reference, prefix, yang_version, organization, description,
                    contact, schema, feature, json_submodules, compilation_status, author_email, maturity_level,
                    compilation_result, module_or_submodule, document_name, owner, repo, repo_file_path,
                    local_file_path, generated_from, working_group):
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
        # self.deviations[key] = deviations
        self.json_submodules[key] = json_submodules
        self.module_or_submodule[key] = module_or_submodule
        self.document_name[key] = document_name
        self.repo_file_path[key] = repo_file_path
        self.repo[key] = repo
        self.owner[key] = owner
        self.local_file_path[key] = local_file_path
        self.generated_from[key] = generated_from
        self.working_group[key] = working_group

    def add_key(self, key, namespace, conformance_type, vendor, platform, software_version, software_flavor, os_type,
                os_version, feature_set, reference, prefix, yang_version, organization, description, contact,
                compilation_status, author_email, schema, feature, maturity_level, compilation_result, deviations,
                json_submodules,module_or_submodule, document_name, owner, repo, repo_file_path,
                local_file_path, generated_from, working_group):
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
        self.repo_file_path[key] = repo_file_path
        self.repo[key] = repo
        self.owner[key] = owner
        self.local_file_path[key] = local_file_path
        self.generated_from[key] = generated_from
        self.working_group[key] = working_group

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
             #'conformance-type': conformance_type
             }

    # - deviations, implementations
    def dump_sdo(self):
        with open(self.file_name + '.json', "w") as prepare_model:
            json.dump({'module': [{
                'name': key.split('@')[0],
                'revision': key.split('@')[1].split('.')[0],
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
                #'feature': self.feature[key],
                'maturity-level': self.maturity_level[key],
                'compilation-result': self.compilation_result[key],
                'author-email': self.author_email[key],
                'submodule': json.loads(self.json_submodules[key]),
                'module-type': self.module_or_submodule[key],
                'document-name': self.document_name[key],
                'generated-from': self.generated_from[key],
                'source-file': {
                    'online': {
                        'owner': self.owner[key],
                        'repository': self.repo[key],
                        'path': self.repo_file_path[key]
                    },
                    'local': {
                        'path': self.local_file_path[key]
                    }
                }
            } for key in self.name_revision]}, prepare_model)

    def dump(self):
        with open(self.file_name + '.json', "w") as prepare_model:
            json.dump({'module': [{
                'name': key.split('@')[0],
                'revision': key.split('@')[1],
                'namespace': self.namespace[key],
   #             'conformance-type': self.conformance_type[key],
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
                #'feature': self.feature[key],
                'maturity-level': self.maturity_level[key],
                'compilation-result': self.compilation_result[key],
                'submodule': json.loads(self.json_submodules[key]),
                'module-type': self.module_or_submodule[key],
                'generated-from': self.generated_from[key],
                'source-file': {
                    'online': {
                        'owner': self.owner[key],
                        'repository': self.repo[key],
                        'path': self.repo_file_path[key]
                    },
                    'local': {
                        'path': self.local_file_path[key]
                    }
                },
                'implementations': {
                    'implementation': [{
                        'vendor': self.implementations[key][implementation]['vendor'],
                        'platform': self.implementations[key][implementation]['platform'],
                        'software-version': self.implementations[key][implementation]['software-version'],
                        'software-flavor': self.implementations[key][implementation]['software-flavor'],
                        'os-type': self.implementations[key][implementation]['os-type'],
                        'os-version': self.implementations[key][implementation]['os-version'],
                        'feature-set': self.implementations[key][implementation]['feature-set'],
                     #   'conformance-type': self.implementations[key][implementation]['conformance-type'],
                    } for implementation in self.implementations[key]],
                }#,
               # 'deviation': [
               #     {'name': self.deviations[key]['name'][i],
               #      'revision': self.deviations[key]['revision'][i]
               #      } for
               #     i, val in enumerate(self.deviations[key]['name'])],
            } for key in self.name_revision]}, prepare_model)
