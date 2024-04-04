<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [YANG Models and Platform Capabilities for Cisco IOS XE 17.14.1](#yang-models-and-platform-capabilities-for-cisco-ios-xe-17131)
  - [Major Model Changes In 17.14.1](#major-model-changes-in-17131)
    - [Native Models Added](#native-models-added)
    - [Native Models Modified](#native-models-modified)
    - [Other Models Modified](#other-models-modified)
    - [Native Models Removed](#native-models-removed)
  - [Backward Incompatible Changes](#backward-incompatible-changes)
  - [Compliance With "pyang --lint"](#compliance-with-pyang---lint)
  - [Revision Statements](#revision-statements)
  - [YANG Model Version 1.1](#yang-model-version-11)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## YANG Models and Platform Capabilities for Cisco IOS XE 17.14.1

This directory contains the YANG models supported by IOS XE 17.14.1:

* IOS XE native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms
listed below. As model content may differ based on platform capabilities, samples of the platform "hello" messages are also provided in the files listed against platforms:

| Platform | Capability File |
|----------|-----------------|
| ASR 1000 | [capability-asr1k.xml](capability-asr1k.xml) |
| ASR 900 RSP2/RSP3, ASR 920, NCS 520 and NCS 4200 | [capability-asr900.xml](capability-asr900.xml) |
| Catalyst 9200 | [capability-cat9200.xml](capability-cat9200.xml) |
| Catalyst 9300 | [capability-cat9300.xml](capability-cat9300.xml) |
| Catalyst 9400 | [capability-cat9400.xml](capability-cat9400.xml) |
| Catalyst 9500 | [capability-cat9500.xml](capability-cat9500.xml) |
| Catalyst 9600 | [capability-cat9600.xml](capability-cat9600.xml) |
| Catalyst 9800 | [capability-wireless.xml](capability-wireless.xml) |
| C8000v/ISRv | [capability-c8000v.xml](capability-c8000v.xml) |
| C8500/C8500L | [capability-c8500.xml](capability-c8500.xml) |
| C8200 | [capability-c8200.xml](capability-c8200.xml) |
| C8300 | [capability-c8300.xml](capability-c8300.xml) |
| ESS 3x00 | [capability-ess3x00.xml](capability-ess3x00.xml) |
| IR 1101 | [capability-ir1101.xml](capability-ir1101.xml) |
| IE 3x00 | [capability-ie3x00.xml](capability-ie3x00.xml) |
| ISR 1000 | [capability-isr1k.xml](capability-isr1k.xml) |
| ISR 4000 | [capability-isr4k.xml](capability-isr4k.xml) |


### Major Model Changes In 17.14.1

17.14.1 model changes include adding new native models and existing native model updates. Starting from this release, all native models are in yang-version 1.1

#### Native Models Added

* Cisco-IOS-XE-cwan-fw-rpc.yang
* Cisco-IOS-XE-embedded-ap-actions-rpc.yang
* Cisco-IOS-XE-ida.yang
* Cisco-IOS-XE-l2nat.yang
* Cisco-IOS-XE-l3nat-iox.yang
* Cisco-IOS-XE-loop-detect-events.yang
* Cisco-IOS-XE-matm-events.yang
* Cisco-IOS-XE-meraki-leds-actions-rpc.yang
* Cisco-IOS-XE-mpls-asr900-deviation.yang
* Cisco-IOS-XE-mrp-oper.yang
* Cisco-IOS-XE-pnp-deviation.yang
* Cisco-IOS-XE-service-chain.yang
* Cisco-IOS-XE-sslproxy-cfg.yang
* Cisco-IOS-XE-sslproxy-rpc.yang
* Cisco-IOS-XE-switchport-deviation.yang
* Cisco-IOS-XE-switchport-oper.yang
* Cisco-IOS-XE-udld-events.yang
* Cisco-IOS-XE-udld-oper.yang
* Cisco-IOS-XE-utd-events.yang

#### OpenConfig Model added

* openconfig-aft-common.yang
* openconfig-aft-ethernet.yang
* openconfig-aft-ipv4.yang
* openconfig-aft-ipv6.yang
* openconfig-aft-mpls.yang
* openconfig-aft-network-instance.yang
* openconfig-aft-pf.yang
* openconfig-aft-state-synced.yang
* openconfig-bgp-errors.yang
* openconfig-keychain-types.yang
* openconfig-keychain.yang
* openconfig-pcep.yang
* openconfig-programming-errors.yang
* openconfig-rib-bgp-attributes.yang
* openconfig-rib-bgp-shared-attributes.yang
* openconfig-rib-bgp-table-attributes.yang
* openconfig-rib-bgp-tables.yang
* openconfig-route-summary.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa-rpc.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-bridge-domain-asr900-deviation.yang
* Cisco-IOS-XE-bridge-domain.yang
* Cisco-IOS-XE-cdp-deviation.yang
* Cisco-IOS-XE-cef-deviation.yang
* Cisco-IOS-XE-cef.yang
* Cisco-IOS-XE-cellwan-oper.yang
* Cisco-IOS-XE-controller.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts-routing-deviation.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-device-hardware-oper.yang
* Cisco-IOS-XE-device-sensor.yang
* Cisco-IOS-XE-device-tracking.yang
* Cisco-IOS-XE-dhcp-deviation.yang
* Cisco-IOS-XE-dhcp-oper.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-diagnostics.yang
* Cisco-IOS-XE-dialer-deviation.yang
* Cisco-IOS-XE-diffserv-target-oper.yang
* Cisco-IOS-XE-eem.yang
* Cisco-IOS-XE-embedded-ap-oper.yang
* Cisco-IOS-XE-environment-oper.yang
* Cisco-IOS-XE-ethernet-cfm-efp.yang
* Cisco-IOS-XE-ethernet-deviation.yang
* Cisco-IOS-XE-ethernet-oam.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-features.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-http.yang
* Cisco-IOS-XE-install-oper.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ios-events-oper.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-lacp-oper.yang
* Cisco-IOS-XE-line-common-deviation.yang
* Cisco-IOS-XE-line-deviation.yang
* Cisco-IOS-XE-line-nonquake-deviation.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-lisp-deviation.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-meraki-connect-oper.yang
* Cisco-IOS-XE-mpls.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-nd-deviation.yang
* Cisco-IOS-XE-nhrp.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-nwpi-oper.yang
* Cisco-IOS-XE-nwpi-rpc.yang
* Cisco-IOS-XE-nwpi-types.yang
* Cisco-IOS-XE-object-group.yang
* Cisco-IOS-XE-ospf-deviation.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3-deviation.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-parser.yang
* Cisco-IOS-XE-perf-measure-events.yang
* Cisco-IOS-XE-perf-measure-oper.yang
* Cisco-IOS-XE-perf-measure.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-poch-lb-switch-deviation.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-policy-deviation.yang
* Cisco-IOS-XE-policy-mcp-deviation.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-power-deviation.yang
* Cisco-IOS-XE-pppoe.yang
* Cisco-IOS-XE-qfp-stats.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-sanet-deviation.yang
* Cisco-IOS-XE-segment-routing.yang
* Cisco-IOS-XE-service-insertion.yang
* Cisco-IOS-XE-sip-ua.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree-events.yang
* Cisco-IOS-XE-spanning-tree.yang
* Cisco-IOS-XE-switch-deviation.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-synce.yang
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-transceiver-oper.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-utd-common-oper.yang
* Cisco-IOS-XE-utd-oper.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-voice-class.yang
* Cisco-IOS-XE-voice-dspfarm.yang
* Cisco-IOS-XE-voice-port.yang
* Cisco-IOS-XE-voice-register.yang
* Cisco-IOS-XE-voice.yang
* Cisco-IOS-XE-vrrp.yang
* Cisco-IOS-XE-vtp.yang
* Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang
* Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang
* Cisco-IOS-XE-wireless-access-point-oper.yang
* Cisco-IOS-XE-wireless-afc-oper.yang
* Cisco-IOS-XE-wireless-ap-types.yang
* Cisco-IOS-XE-wireless-client-global-oper.yang
* Cisco-IOS-XE-wireless-client-rpc.yang
* Cisco-IOS-XE-wireless-client-types.yang
* Cisco-IOS-XE-wireless-enum-types.yang
* Cisco-IOS-XE-wireless-fabric-cfg.yang
* Cisco-IOS-XE-wireless-mesh-cfg.yang
* Cisco-IOS-XE-wireless-mesh-oper.yang
* Cisco-IOS-XE-wireless-mobility-cfg.yang
* Cisco-IOS-XE-wireless-rogue-oper.yang
* Cisco-IOS-XE-wireless-rrm-cfg.yang
* Cisco-IOS-XE-wireless-site-cfg.yang
* Cisco-IOS-XE-wireless-types.yang
* Cisco-IOS-XE-wireless-wlan-cfg.yang

#### Other Models Modified

* cisco-xe-ietf-routing-ext.yang
* cisco-xe-openconfig-evpn-deviation.yang
* cisco-xe-openconfig-network-instance-l2-deviation.yang

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
| Catalyst 9200 | [yang-set-cat9200.xml](yang-set-cat9200.xml) |
| Catalyst 9300 | [yang-set-cat9300.xml](yang-set-cat9300.xml) |
| Catalyst 9400 | [yang-set-cat9400.xml](yang-set-cat9400.xml) |
| Catalyst 9500 | [yang-set-cat9500.xml](yang-set-cat9500.xml) |
| Catalyst 9600 | [yang-set-cat9600.xml](yang-set-cat9600.xml) |
| Catalyst 9800 | [yang-set-wireless.xml](yang-set-wireless.xml) |
| C8000v/ISRv | [yang-set-c8000v.xml](yang-set-c8000v.xml) |
| C8500/C8500L | [yang-set-c8500.xml](yang-set-c8500.xml) |
| C8200 | [yang-set-c8200.xml](yang-set-c8200.xml) |
| C8300 | [yang-set-c8300.xml](yang-set-c8300.xml) |
| ESS 3x00 | [yang-set-ess3x00.xml](yang-set-ess3x00.xml) |
| IR 1101 | [yang-set-ir1101.xml](yang-set-ir1101.xml) |
| IE 3x00 | [yang-set-ie3x00.xml](yang-set-ie3x00.xml) |
| ISR 1000 | [yang-set-isr1k.xml](yang-set-isr1k.xml) |
| ISR 4000 | [yang-set-isr4k.xml](yang-set-isr4k.xml) |

### OID to xpath Mapping

SNMP OID MIB to xpath mapping is documented under [iosxe.csv](iosxe.csv) file. 
