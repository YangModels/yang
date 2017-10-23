from tools.utility import log
from tools.utility.util import load_json_from_url

LOGGER = log.get_logger('modules')


class LoadFiles:
    def __init__(self, path):
        LOGGER.debug('Loading Benoit\'s compilation statuses and results')
        self.ietf_rfc_json = {}
        self.ietf_draft_json = {}
        self.ietf_draft_example_json = {}
        self.bbf_json = {}
        self.ieee_standard_json = {}
        self.ieee_experimental_json = {}
        self.ietf_rfc_standard_json = {}
        self.ietf_rfc_standard_json = load_json_from_url(
            'http://www.claise.be/RFCStandard.json')
        self.ietf_rfc_json = load_json_from_url(
            'http://www.claise.be/IETFYANGRFC.json')
        self.bbf_json = load_json_from_url('http://www.claise.be/BBF.json')
        self.ieee_standard_json = load_json_from_url(
            'http://www.claise.be/IEEEStandard.json')
        self.ieee_experimental_json = load_json_from_url(
            'http://www.claise.be/IEEEExperimental.json')
        self.ietf_draft_json = load_json_from_url(
            'http://www.claise.be/IETFYANGDraft.json')
        self.mef_experimental_json = load_json_from_url(
            'http://www.claise.be/MEFExperimental.json')
        self.openconfig_json = load_json_from_url(
            'http://www.claise.be/Openconfig.json')

        self.xe1631 = ''
        if '1631' in path:
            self.xe1631 = load_json_from_url(
                'http://www.claise.be/CiscoXE1631.json')
        self.xe1632 = ''
        if '1632' in path:
            self.xe1632 = load_json_from_url(
                'http://www.claise.be/CiscoXE1632.json')
        self.xe1641 = ''
        if '1641' in path:
            self.xe1641 = load_json_from_url(
                'http://www.claise.be/CiscoXE1641.json')
        self.xe1651 = ''
        if '1651' in path:
            self.xe1651 = load_json_from_url(
                'http://www.claise.be/CiscoXE1651.json')
        self.xe1661 = ''
        if '1661' in path:
            self.xe1661 = load_json_from_url(
                'http://www.claise.be/CiscoXE1661.json')

        self.xr611 = ''
        if '611' in path:
            self.xr611 = load_json_from_url(
                'http://www.claise.be/CiscoXR611.json')
        self.xr612 = ''
        if '612' in path:
            self.xr612 = load_json_from_url(
                'http://www.claise.be/CiscoXR612.json')
        self.xr613 = ''
        if '613' in path:
            self.xr613 = load_json_from_url(
                'http://www.claise.be/CiscoXR613.json')
        self.xr621 = ''
        if '621' in path:
            self.xr621 = load_json_from_url(
                'http://www.claise.be/CiscoXR621.json')
        self.xr622 = ''
        if '622' in path:
            self.xr622 = load_json_from_url(
                'http://www.claise.be/CiscoXR622.json')
        self.xr631 = ''
        if '631' in path:
            self.xr631 = load_json_from_url(
                'http://www.claise.be/CiscoXR631.json')

        self.nx703f11 = ''
        if '7.0-3-F1-1' in path:
            self.nx703f11 = load_json_from_url(
                'http://www.claise.be/CiscoNX703F11.json')
        self.nx703f21 = ''
        if '7.0-3-F2-1' in path or '7.0-3-F2-2' in path:
            self.nx703f21 = load_json_from_url(
                'http://www.claise.be/CiscoNX703F21.json')
        self.nx703i51 = ''
        if '7.0-3-I5-1' in path:
            self.nx703i51 = load_json_from_url(
                'http://www.claise.be/CiscoNX703I51.json')
        self.nx703i52 = ''
        if '7.0-3-I5-2' in path:
            self.nx703i52 = load_json_from_url(
                'http://www.claise.be/CiscoNX703I52.json')
        self.nx703i61 = ''
        if '7.0-3-I6-1' in path:
            self.nx703i61 = load_json_from_url(
                'http://www.claise.be/CiscoNX703I61.json')
        self.nx703i71 = ''
        if '7.0-3-I7-1' in path:
            self.nx703i71 = load_json_from_url(
                'http://www.claise.be/CiscoNX703I71.json')
        self.huawei8910 = load_json_from_url(
            'http://www.claise.be/NETWORKROUTER8910.json')
