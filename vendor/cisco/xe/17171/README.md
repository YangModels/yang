<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [YANG Models and Platform Capabilities for Cisco IOS XE 17.17.1](#yang-models-and-platform-capabilities-for-cisco-ios-xe-17131)
  - [Major Model Changes In 17.17.1](#major-model-changes-in-17131)
    - [Native Models Added](#native-models-added)
    - [Native Models Modified](#native-models-modified)
    - [Other Models Modified](#other-models-modified)
    - [Native Models Removed](#native-models-removed)
  - [Backward Incompatible Changes](#backward-incompatible-changes)
  - [Compliance With "pyang --lint"](#compliance-with-pyang---lint)
  - [Revision Statements](#revision-statements)
  - [YANG Model Version 1.1](#yang-model-version-11)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## YANG Models and Platform Capabilities for Cisco IOS XE 17.17.1

This directory contains the YANG models supported by IOS XE 17.17.1:

* IOS XE native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms
listed below. As model content may differ based on platform capabilities, samples of the platform "hello" messages are also provided in the files listed against platforms:

| Platform | Capability File |
|----------|-----------------|
| ASR 1000 | [capability-asr1k.xml](capability-asr1k.xml) |
| ASR 900 RSP2/RSP3, ASR 920, NCS 520 and NCS 4200 | [capability-asr900.xml](capability-asr900.xml) |
| Catalyst 9K_Lite | [capability-cat9200.xml](capability-cat9200.xml) |
| Catalyst 9K | [capability-cat9k.xml](capability-cat9k.xml) |
| Catalyst 9800 | [capability-wireless.xml](capability-wireless.xml) |
| C8000v/ISRv | [capability-c8000v.xml](capability-c8000v.xml) |
| C8500/C8500L | [capability-c8500.xml](capability-c8500.xml) |
| ESS 3x00 | [capability-ess3x00.xml](capability-ess3x00.xml) |
| IR 1101 | [capability-ir1101.xml](capability-ir1101.xml) |
| IE 3x00 | [capability-ie3x00.xml](capability-ie3x00.xml) |
| ISR 1000 | [capability-isr1k.xml](capability-isr1k.xml) |


### Major Model Changes In 17.17.1

17.17.1 model changes include adding new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-evpn-oper.yang
* Cisco-IOS-XE-group-policy-oper.yang
* Cisco-IOS-XE-interfaces-cat9k-deviation.yang
* Cisco-IOS-XE-ngfw-events.yang
* Cisco-IOS-XE-policy-cat9k-deviation.yang
* Cisco-IOS-XE-policy-pegasus-deviation.yang
* Cisco-IOS-XE-policy-wlc-deviation.yang
* Cisco-IOS-XE-sdwan-aaa-oper.yang
* Cisco-IOS-XE-steering-policy-oper.yang
* Cisco-IOS-XE-vdsp-oper.yang
* Cisco-IOS-XE-wireless-rogue-authz-rpc.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa-rpc.yang 
* Cisco-IOS-XE-aaa.yang 
* Cisco-IOS-XE-acl.yang 
* Cisco-IOS-XE-bgp.yang 
* Cisco-IOS-XE-cdp.yang 
* Cisco-IOS-XE-controller.yang 
* Cisco-IOS-XE-crypto.yang 
* Cisco-IOS-XE-ctrl-mng-cfg.yang 
* Cisco-IOS-XE-cts.yang 
* Cisco-IOS-XE-device-hardware-oper.yang 
* Cisco-IOS-XE-dhcp.yang 
* Cisco-IOS-XE-dialer.yang 
* Cisco-IOS-XE-environment-oper.yang 
* Cisco-IOS-XE-eta.yang 
* Cisco-IOS-XE-ethernet-cfm-efp.yang 
* Cisco-IOS-XE-ethernet.yang 
* Cisco-IOS-XE-features.yang 
* Cisco-IOS-XE-flow.yang 
* Cisco-IOS-XE-g8032.yang 
* Cisco-IOS-XE-gnmi-cfg.yang 
* Cisco-IOS-XE-gnss.yang 
* Cisco-IOS-XE-grpc-tunnel-cfg.yang 
* Cisco-IOS-XE-hsrp.yang 
* Cisco-IOS-XE-install-event-types.yang 
* Cisco-IOS-XE-install-rpc.yang 
* Cisco-IOS-XE-interface-common.yang 
* Cisco-IOS-XE-interfaces-deviation.yang 
* Cisco-IOS-XE-interfaces-oper.yang 
* Cisco-IOS-XE-interfaces.yang 
* Cisco-IOS-XE-ip.yang 
* Cisco-IOS-XE-l2vpn.yang 
* Cisco-IOS-XE-license.yang 
* Cisco-IOS-XE-line.yang 
* Cisco-IOS-XE-lisp.yang 
* Cisco-IOS-XE-livetools-actions-rpc.yang 
* Cisco-IOS-XE-livetools-common-types.yang 
* Cisco-IOS-XE-livetools-oper.yang 
* Cisco-IOS-XE-lldp.yang 
* Cisco-IOS-XE-mdns-gateway.yang 
* Cisco-IOS-XE-mdt-cfg.yang 
* Cisco-IOS-XE-mdt-oper.yang 
* Cisco-IOS-XE-meraki-connect-oper.yang 
* Cisco-IOS-XE-native.yang 
* Cisco-IOS-XE-nbar.yang 
* Cisco-IOS-XE-ncch-cfg.yang 
* Cisco-IOS-XE-nhrp.yang 
* Cisco-IOS-XE-nwpi-oper.yang 
* Cisco-IOS-XE-nwpi-rpc.yang 
* Cisco-IOS-XE-object-group.yang 
* Cisco-IOS-XE-ospf.yang 
* Cisco-IOS-XE-parser.yang 
* Cisco-IOS-XE-pim-oper.yang 
* Cisco-IOS-XE-platform-oper.yang 
* Cisco-IOS-XE-platform.yang 
* Cisco-IOS-XE-poe-oper.yang 
* Cisco-IOS-XE-port-bounce-rpc.yang 
* Cisco-IOS-XE-ptp.yang 
* Cisco-IOS-XE-qfp-resource-events.yang 
* Cisco-IOS-XE-qfp-stats.yang 
* Cisco-IOS-XE-rawsocket.yang 
* Cisco-IOS-XE-rip.yang 
* Cisco-IOS-XE-route-map.yang 
* Cisco-IOS-XE-segment-routing.yang 
* Cisco-IOS-XE-service-insertion.yang 
* Cisco-IOS-XE-snmp.yang 
* Cisco-IOS-XE-sslproxy-cfg.yang 
* Cisco-IOS-XE-stack-member-oper.yang 
* Cisco-IOS-XE-stack-mgr-events-oper.yang 
* Cisco-IOS-XE-stack-oper.yang 
* Cisco-IOS-XE-stackwise-virtual.yang 
* Cisco-IOS-XE-system-integrity-oper.yang 
* Cisco-IOS-XE-transceiver-oper.yang 
* Cisco-IOS-XE-tunnel-types.yang 
* Cisco-IOS-XE-tunnel.yang 
* Cisco-IOS-XE-types.yang 
* Cisco-IOS-XE-utd.yang 
* Cisco-IOS-XE-voice.yang 
* Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang 
* Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang 
* Cisco-IOS-XE-wireless-access-point-oper.yang 
* Cisco-IOS-XE-wireless-ap-cfg.yang 
* Cisco-IOS-XE-wireless-ap-types.yang 
* Cisco-IOS-XE-wireless-apf-cfg.yang 
* Cisco-IOS-XE-wireless-client-global-oper.yang 
* Cisco-IOS-XE-wireless-client-oper.yang 
* Cisco-IOS-XE-wireless-client-types.yang 
* Cisco-IOS-XE-wireless-cts-sxp-cfg.yang 
* Cisco-IOS-XE-wireless-dot11-cfg.yang 
* Cisco-IOS-XE-wireless-enum-types.yang 
* Cisco-IOS-XE-wireless-flex-cfg.yang 
* Cisco-IOS-XE-wireless-general-cfg.yang 
* Cisco-IOS-XE-wireless-mobility-cfg.yang 
* Cisco-IOS-XE-wireless-radio-cfg.yang 
* Cisco-IOS-XE-wireless-rf-cfg.yang 
* Cisco-IOS-XE-wireless-rlan-cfg.yang 
* Cisco-IOS-XE-wireless-rogue-cfg.yang 
* Cisco-IOS-XE-wireless-rogue-oper.yang 
* Cisco-IOS-XE-wireless-rrm-cfg.yang 
* Cisco-IOS-XE-wireless-security-cfg.yang 
* Cisco-IOS-XE-wireless-site-cfg.yang 
* Cisco-IOS-XE-wireless-types.yang 
* Cisco-IOS-XE-wireless-wlan-cfg.yang 
* Cisco-IOS-XE-yang-interfaces-cfg.yang 

#### Other Models Modified
 
* cisco-xe-openconfig-evpn-deviation.yang
* openconfig-alarms.yang
* openconfig-network-instance.yang

### Backward Incompatible Changes

All the model specific backward incompatible changes have been documented in [Backward Incompatible Changes](BIC).

### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

As part of the model validation for this release we are ignoring "LEAFREF_IDENTIFIER_NOT_FOUND" and "STRICT_XPATH_FUNCTIONS" error types. Reason being that the missing leafref reference errors are due to pyang bug which needs to be fixed and some of the XPATH function errors are false positives which are handled in the newer version of pyang (2.3.2)

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.

### YANG Model Version 1.1

All native models are in YANG version 1.1 from 17.10.1 release.

YANG version 1.1 is described by the RFC 7950, The YANG 1.1 Data Modeling Language. YANG version 1.1 is a maintenance release of the YANG language that addresses ambiguities and defects in the YANG version 1.0 specification. Per RFC 7950, the YANG module in YANG version 1.1 is advertised through the ietf-yang-library instead of the NETCONF hello messages. As model content may differ based on platform support, samples of the platform 'ietf-yang-library' <rpc-reply> messages listing all implemented modules in the "/modules-state/module" list are also provided in the files listed against platforms:

| Platform | YANG Set File |
|----------|-----------------|
| ASR 1000 | [yang-set-asr1k.xml](yang-set-asr1k.xml) |
| ASR 900 RSP2/RSP3, ASR 920, NCS 520 and NCS 4200 | [yang-set-asr900.xml](yang-set-asr900.xml) |
| Catalyst 9K_Lite | [yang-set-cat9200.xml](yang-set-cat9200.xml) |
| Catalyst 9K | [yang-set-cat9k.xml](yang-set-cat9k.xml) |
| Catalyst 9800| [yang-set-wireless.xml](yang-set-wireless.xml) |
| C8000v/ISRv | [yang-set-c8000v.xml](yang-set-c8000v.xml) |
| C8500/C8500L | [yang-set-c8500.xml](yang-set-c8500.xml) |
| ESS 3x00 | [yang-set-ess3x00.xml](yang-set-ess3x00.xml) |
| IR 1101 | [yang-set-ir1101.xml](yang-set-ir1101.xml) |
| IE 3x00 | [yang-set-ie3x00.xml](yang-set-ie3x00.xml) |
| ISR 1000 | [yang-set-isr1k.xml](yang-set-isr1k.xml) |

### OID to xpath Mapping

SNMP OID MIB to xpath mapping is documented under [iosxe-snmp-OID-xpath-mapping.csv](iosxe-snmp-OID-xpath-mapping.csv) file. 
