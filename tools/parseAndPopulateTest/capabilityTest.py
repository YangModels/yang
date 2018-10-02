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
    'ietf-yang-types@2013-07-15.yang': {'tree': 'not-applicable', 'type': 'module'},
    'openconfig-catalog-types@2017-03-08.yang': {'tree': 'not-applicable', 'type': 'module'},
    'openconfig-extensions@2017-01-29.yang': {'tree': 'not-applicable', 'type': 'module'},
    'openconfig-module-catalog@2017-03-08.yang': {'tree': 'nmda-compatible', 'type': 'module'},
    'ietf-te-sr-mpls@2017-07-02.yang': {'tree': 'openconfig', 'type': 'module'},
    'ietf-snmp-usm@2014-12-10.yang': {'tree': 'not-applicable', 'type': 'submodule'},
    'ietf-snmp-common@2014-12-10.yang': {'tree': 'not-applicable', 'type': 'submodule'},
    'ietf-routing.yang': {'tree': 'split', 'type': 'module'}
}
TEST_DIR = '../parseAndPopulate/test0/'


class CapabilityTest(unittest.TestCase):

    def tearDown(self):
        shutil.rmtree(TEST_DIR)

    def setUp(self):
        self.maxDiff = None
        os.makedirs(TEST_DIR)

    def testSdo(self):
        prepare_sdo = prepare.Prepare('prepare', TEST_DIR)
        integrity = statistics.Statistics('./testModules')
        capability = cap.Capability('./testModules', 0, prepare_sdo, integrity,
                                    False, True, TEST_DIR, TEST_DIR, TEST_DIR, None)
        capability.parse_and_dump_sdo()
        prepare_sdo.dump_modules('../parseAndPopulate/test0/')
        with open('../parseAndPopulate/test0/prepare.json', 'r') as f:
            output_file = json.load(f)
        with open('./testJson/prepare.json', 'r') as f:
            file_to_comapre = json.load(f)
        self.assertDictEqual(output_file, file_to_comapre)


if __name__ == '__main__':
    unittest.main()
