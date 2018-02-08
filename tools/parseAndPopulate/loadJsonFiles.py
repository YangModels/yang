from tools.utility import log
from tools.utility.util import load_json_from_url, resolve_results

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
        self.mef_experimental_json = {}
        self.openconfig_json = {}
        self.ietf_rfc_standard_json['json'] = load_json_from_url(
            'http://www.claise.be/RFCStandard.json')
        self.ietf_rfc_standard_json['ths'] = resolve_results(
            'http://www.claise.be/RFCStandardYANGPageCompilation.html')

        self.ietf_rfc_json['json'] = load_json_from_url(
            'http://www.claise.be/IETFYANGRFC.json')
        self.ietf_rfc_json['ths'] = resolve_results(
            'http://www.claise.be/IETFYANGOutOfRFC.html')

        self.bbf_json['json'] = load_json_from_url(
            'http://www.claise.be/BBF.json')
        self.bbf_json['ths'] = resolve_results(
            'http://claise.be/BBFYANGPageCompilation.html')

        self.ieee_standard_json['json'] = load_json_from_url(
            'http://www.claise.be/IEEEStandard.json')
        self.ieee_standard_json['ths'] = resolve_results(
            'http://claise.be/IEEEStandardYANGPageCompilation.html ')

        self.ieee_experimental_json['json'] = load_json_from_url(
            'http://www.claise.be/IEEEExperimental.json')
        self.ieee_experimental_json['ths'] = resolve_results(
            'http://claise.be/IEEEExperimentalYANGPageCompilation.html')

        self.ietf_draft_json['json'] = load_json_from_url(
            'http://www.claise.be/IETFYANGDraft.json')
        self.ietf_draft_json['ths'] = resolve_results(
            'http://www.claise.be/IETFYANGPageCompilation.html')

        self.mef_experimental_json['json'] = load_json_from_url(
            'http://www.claise.be/MEFExperimental.json')
        self.mef_experimental_json['ths'] = resolve_results(
            'http://claise.be/MEFExperimentalYANGPageCompilation.html')

        self.openconfig_json['json'] = load_json_from_url(
            'http://www.claise.be/Openconfig.json')
        self.openconfig_json['ths'] = resolve_results(
            'http://claise.be/OpenconfigYANGPageCompilation.html')

        self.xe1631 = ''
        if '1631' in path:
            self.xe1631 = {}
            self.xe1631['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXE1631.json')
            self.xe1631['ths'] = resolve_results(
                'http://www.claise.be/CiscoXE1631YANGPageCompilation.html')
        self.xe1632 = ''
        if '1632' in path:
            self.xe1632 = {}
            self.xe1632['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXE1632.json')
            self.xe1632['ths'] = resolve_results(
                'http://www.claise.be/CiscoXE1632YANGPageCompilation.html')
        self.xe1641 = ''
        if '1641' in path:
            self.xe1641 = {}
            self.xe1641['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXE1641.json')
            self.xe1641['ths'] = resolve_results(
                'http://www.claise.be/CiscoXE1641YANGPageCompilation.html')
        self.xe1651 = ''
        if '1651' in path:
            self.xe1651 = {}
            self.xe1651['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXE1651.json')
            self.xe1651['ths'] = resolve_results(
                'http://www.claise.be/CiscoXE1651YANGPageCompilation.html')
        self.xe1661 = ''
        if '1661' in path:
            self.xe1661 = {}
            self.xe1661['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXE1661.json')
            self.xe1661['ths'] = resolve_results(
                'http://www.claise.be/CiscoXE1661YANGPageCompilation.html')
        self.xe1662 = ''
        if '1662' in path:
            self.xe1662 = {}
            self.xe1662['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXE1662.json')
            self.xe1662['ths'] = resolve_results(
                'http://www.claise.be/CiscoXE1662YANGPageCompilation.html')
        self.xe1671 = ''
        if '1671' in path:
            self.xe1671 = {}
            self.xe1671['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXE1671.json')
            self.xe1671['ths'] = resolve_results(
                'http://www.claise.be/CiscoXE1671YANGPageCompilation.html')

        self.xr611 = ''
        if '611' in path:
            self.xr611 = {}
            self.xr611['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXR611.json')
            self.xr611['ths'] = resolve_results(
                'http://www.claise.be/CiscoXR611YANGPageCompilation.html')
        self.xr612 = ''
        if '612' in path:
            self.xr612 = {}
            self.xr612['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXR612.json')
            self.xr612['ths'] = resolve_results(
                'http://www.claise.be/CiscoXR612YANGPageCompilation.html')
        self.xr613 = ''
        if '613' in path:
            self.xr613 = {}
            self.xr613['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXR613.json')
            self.xr613['ths'] = resolve_results(
                'http://www.claise.be/CiscoXR613YANGPageCompilation.html')
        self.xr621 = ''
        if '621' in path:
            self.xr621 = {}
            self.xr621['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXR621.json')
            self.xr621['ths'] = resolve_results(
                'http://www.claise.be/CiscoXR621YANGPageCompilation.html')
        self.xr622 = ''
        if '622' in path:
            self.xr622 = {}
            self.xr622['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXR622.json')
            self.xr622['ths'] = resolve_results(
                'http://www.claise.be/CiscoXR622YANGPageCompilation.html')
        self.xr631 = ''
        if '631' in path:
            self.xr631 = {}
            self.xr631['json'] = load_json_from_url(
                'http://www.claise.be/CiscoXR631.json')
            self.xr631['ths'] = resolve_results(
                'http://www.claise.be/CiscoXR631YANGPageCompilation.html')

        self.nx703f11 = ''
        if '7.0-3-F1-1' in path:
            self.nx703f11 = {}
            self.nx703f11['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703F11.json')
            self.nx703f11['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703F11YANGPageCompilation.html')
        self.nx703f21 = ''
        if '7.0-3-F2-1':
            self.nx703f21 = {}
            self.nx703f21['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703F21.json')
            self.nx703f21['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703F21YANGPageCompilation.html')
        self.nx703f22 = ''
        if '7.0-3-F2-2':
            self.nx703f22 = {}
            self.nx703f22['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703F22.json')
            self.nx703f22['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703F22YANGPageCompilation.html')
        self.nx703f31 = ''
        if '7.0-3-F3-1':
            self.nx703f31 = {}
            self.nx703f31['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703F31.json')
            self.nx703f31['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703F31YANGPageCompilation.html')
        self.nx703i51 = ''
        if '7.0-3-I5-1' in path:
            self.nx703i51 = {}
            self.nx703i51['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703I51.json')
            self.nx703i51['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703I51YANGPageCompilation.html')
        self.nx703i52 = ''
        if '7.0-3-I5-2' in path:
            self.nx703i52 = {}
            self.nx703i52['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703I52.json')
            self.nx703i52['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703I52YANGPageCompilation.html')
        self.nx703i61 = ''
        if '7.0-3-I6-1' in path:
            self.nx703i61 = {}
            self.nx703i61['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703I61.json')
            self.nx703i61['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703I61YANGPageCompilation.html')
        self.nx703i71 = ''
        if '7.0-3-I7-1' in path:
            self.nx703i71 = {}
            self.nx703i71['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703I71.json')
            self.nx703i71['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703I71YANGPageCompilation.html')
        self.nx703i72 = ''
        if '7.0-3-I7-2' in path:
            self.nx703i72 = {}
            self.nx703i72['json'] = load_json_from_url(
                'http://www.claise.be/CiscoNX703I72.json')
            self.nx703i72['ths'] = resolve_results(
                'http://www.claise.be/CiscoNX703I72YANGPageCompilation.html')

        self.huawei8910 = {}
        self.huawei8910['json'] = load_json_from_url(
            'http://www.claise.be/NETWORKROUTER8910.json')
        self.huawei8910['ths'] = resolve_results(
            'http://www.claise.be/NETWORKROUTER8910YANGPageCompilation.html')
