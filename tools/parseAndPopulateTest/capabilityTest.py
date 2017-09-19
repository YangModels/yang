import json
import os
import shutil
import unittest

import tools.parseAndPopulate.capability as cap
import tools.parseAndPopulate.statistics as statistics
from tools.parseAndPopulate import prepare

TREE_TYPE_MAP = {
    'ietf-interfaces@2014-05-08.yang': {'tree': 'split', 'type': 'module'},
    'ietf-ip@2014-06-16.yang': {'tree': 'split', 'type': 'module'},
    'ietf-ip@2017-08-21.yang': {'tree': 'nmda-compatible', 'type': 'module'},
    'ietf-yang-types@2013-07-15.yang': {'tree': 'unclassified', 'type': 'module'},
    'openconfig-catalog-types@2017-03-08.yang': {'tree': 'unclassified', 'type': 'module'},
    'openconfig-extensions@2017-01-29.yang': {'tree': 'unclassified', 'type': 'module'},
    'openconfig-module-catalog@2017-03-08.yang': {'tree': 'nmda-compatible', 'type': 'module'},
    'ietf-te-sr-mpls@2017-07-02.yang': {'tree': 'openconfig', 'type': 'module'},
    'ietf-snmp-usm@2014-12-10.yang': {'tree': 'not-applicable', 'type': 'submodule'},
    'ietf-snmp-common@2014-12-10.yang': {'tree': 'not-applicable', 'type': 'submodule'}
}


class CapabilityTest(unittest.TestCase):
    def testOutput(self):
        os.makedirs('../parseAndPopulate/test0/')
        prepare_sdo = prepare.Prepare('prepare', '../parseAndPopulate/test0/')
        integrity = statistics.Statistics('./testModules')
        capability = cap.Capability('./testModules', 0, prepare_sdo, integrity, False, True, '../parseAndPopulate/test0/')
        capability.parse_and_dump_sdo()
        prepare_sdo.dump_sdo('../parseAndPopulate/test0/')
        with open('../parseAndPopulate/test0/prepare.json', 'r') as f:
            output_file = json.load(f)
        with open('./testJson/prepare.json', 'r') as f:
            file_to_comapre = json.load(f)
        self.assertDictEqual(output_file, file_to_comapre)
        shutil.rmtree('../parseAndPopulate/test0/')

    def test_module_submodule(self):
        for root, dirs, files in os.walk('./testModules'):
            for basename in files:
                type = cap.module_or_submodule('./testModules/{}'.format(basename))
                self.assertEqual(type, TREE_TYPE_MAP[basename]['type'])

    def test_tree_type(self):
        for root, dirs, files in os.walk('./testModules'):
            for basename in files:
                type = cap.get_tree_type('./testModules/{}'.format(basename),
                                         cap.module_or_submodule('./testModules/{}'.format(basename)))
                self.assertEqual(type, TREE_TYPE_MAP[basename]['tree'])


if __name__ == '__main__':
    unittest.main()
