<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [YANG Models and Platform Capabilities for Cisco IOS XE 17.4.1](#yang-models-and-platform-capabilities-for-cisco-ios-xe-1741)
  - [Major Model Changes In 17.4.1](#major-model-changes-in-1741)
    - [Native Models Added](#native-models-added)
    - [Other Models Added](#other-models-added)
    - [Native Models Modified](#native-models-modified)
    - [Other Models Modified](#other-models-modified)
    - [Experimental YANG Models](#experimental-yang-models)
  - [Backward Incompatible Changes](#backward-incompatible-changes)
  - [Compliance With "pyang --lint"](#compliance-with-pyang---lint)
  - [Revision Statements](#revision-statements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## YANG Models and Platform Capabilities for Cisco IOS XE 17.4.1

This directory contains the YANG models supported by IOS XE 17.4.1:

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
| CSR 1000v/ISRv | [capability-csr1k.xml](capability-csr1k.xml) |
| ESS 3x00 | [capability-ess3x00.xml](capability-ess3x00.xml) |
| IR 1101 | [capability-ir1101.xml](capability-ir1101.xml) |
| IE 3x00 | [capability-ie3x00.xml](capability-ie3x00.xml) |
| ISR 1000 | [capability-isr1k.xml](capability-isr1k.xml) |
| ISR 4000 | [capability-isr4k.xml](capability-isr4k.xml) |


### Major Model Changes In 17.4.1

17.4.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-geo.yang
* Cisco-IOS-XE-isis-oper.yang
* Cisco-IOS-XE-stack-member-oper.yang
* Cisco-IOS-XE-app-hosting.yang
* Cisco-IOS-XE-ethinternal-subslot.yang
* Cisco-IOS-XE-hsrp-events.yang
* Cisco-IOS-XE-hsrp-oper.yang
* Cisco-IOS-XE-wireless-rrm-rpc.yang

#### Other Models Added

* cisco-xe-access-openconfig-system-ext.yang
* cisco-xe-routing-openconfig-system-ext.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa-types.yang 
* Cisco-IOS-XE-aaa.yang 
* Cisco-IOS-XE-acl-oper.yang 
* Cisco-IOS-XE-acl.yang 
* Cisco-IOS-XE-app-hosting-cfg.yang 
* Cisco-IOS-XE-app-hosting-oper.yang 
* Cisco-IOS-XE-atm.yang 
* Cisco-IOS-XE-bfd.yang 
* Cisco-IOS-XE-bgp-oper.yang 
* Cisco-IOS-XE-bgp-route-oper.yang 
* Cisco-IOS-XE-bgp.yang 
* Cisco-IOS-XE-bridge-domain.yang 
* Cisco-IOS-XE-cable-diag-oper.yang 
* Cisco-IOS-XE-cable-diag-rpc.yang 
* Cisco-IOS-XE-call-home.yang 
* Cisco-IOS-XE-cdp.yang 
* Cisco-IOS-XE-common-types.yang 
* Cisco-IOS-XE-controller.yang 
* Cisco-IOS-XE-crypto-pki-events.yang 
* Cisco-IOS-XE-crypto-rpc.yang 
* Cisco-IOS-XE-crypto.yang 
* Cisco-IOS-XE-cts.yang 
* Cisco-IOS-XE-device-hardware-oper.yang 
* Cisco-IOS-XE-device-tracking.yang 
* Cisco-IOS-XE-dhcp.yang 
* Cisco-IOS-XE-dialer.yang 
* Cisco-IOS-XE-dot1x.yang 
* Cisco-IOS-XE-eem.yang 
* Cisco-IOS-XE-eigrp.yang 
* Cisco-IOS-XE-ethernet-cfm-efp.yang 
* Cisco-IOS-XE-ethernet-deviation.yang 
* Cisco-IOS-XE-ethernet-oam.yang 
* Cisco-IOS-XE-ethernet.yang 
* Cisco-IOS-XE-ezpm.yang 
* Cisco-IOS-XE-features.yang 
* Cisco-IOS-XE-flow.yang 
* Cisco-IOS-XE-fw-oper.yang 
* Cisco-IOS-XE-icmp.yang 
* Cisco-IOS-XE-identity-oper.yang 
* Cisco-IOS-XE-igmp.yang 
* Cisco-IOS-XE-install-events.yang 
* Cisco-IOS-XE-install-rpc.yang 
* Cisco-IOS-XE-interface-common.yang 
* Cisco-IOS-XE-interfaces.yang 
* Cisco-IOS-XE-ios-common-oper.yang 
* Cisco-IOS-XE-ios-events-oper.yang 
* Cisco-IOS-XE-ip-sla-events.yang 
* Cisco-IOS-XE-ip-sla-oper.yang 
* Cisco-IOS-XE-ip.yang 
* Cisco-IOS-XE-ipv6.yang 
* Cisco-IOS-XE-isis.yang 
* Cisco-IOS-XE-l2vpn.yang 
* Cisco-IOS-XE-license.yang 
* Cisco-IOS-XE-line.yang 
* Cisco-IOS-XE-lisp-oper.yang 
* Cisco-IOS-XE-lisp.yang 
* Cisco-IOS-XE-logging.yang 
* Cisco-IOS-XE-mdns-gateway.yang 
* Cisco-IOS-XE-mdt-cfg.yang 
* Cisco-IOS-XE-mdt-common-defs.yang 
* Cisco-IOS-XE-mdt-oper-v2.yang 
* Cisco-IOS-XE-mld.yang 
* Cisco-IOS-XE-mobileip.yang 
* Cisco-IOS-XE-mpls.yang 
* Cisco-IOS-XE-multicast.yang 
* Cisco-IOS-XE-nat.yang 
* Cisco-IOS-XE-native.yang 
* Cisco-IOS-XE-nbar.yang 
* Cisco-IOS-XE-nd.yang 
* Cisco-IOS-XE-nhrp.yang 
* Cisco-IOS-XE-ntp.yang 
* Cisco-IOS-XE-object-group.yang 
* Cisco-IOS-XE-ospf-obsolete.yang 
* Cisco-IOS-XE-ospf.yang 
* Cisco-IOS-XE-ospfv3.yang 
* Cisco-IOS-XE-perf-measure.yang 
* Cisco-IOS-XE-platform.yang 
* Cisco-IOS-XE-policy.yang 
* Cisco-IOS-XE-ppp.yang 
* Cisco-IOS-XE-pppoe.yang 
* Cisco-IOS-XE-ptp.yang 
* Cisco-IOS-XE-qfp-stats.yang 
* Cisco-IOS-XE-rmi-dad.yang 
* Cisco-IOS-XE-route-map.yang 
* Cisco-IOS-XE-rpc.yang 
* Cisco-IOS-XE-sanet.yang 
* Cisco-IOS-XE-scada-gw.yang 
* Cisco-IOS-XE-segment-routing.yang 
* Cisco-IOS-XE-service-insertion.yang 
* Cisco-IOS-XE-site-manager.yang 
* Cisco-IOS-XE-sla.yang 
* Cisco-IOS-XE-snmp.yang 
* Cisco-IOS-XE-stack-oper.yang 
* Cisco-IOS-XE-switch-deviation.yang 
* Cisco-IOS-XE-switch-rpc.yang 
* Cisco-IOS-XE-switch.yang 
* Cisco-IOS-XE-synce.yang 
* Cisco-IOS-XE-template.yang 
* Cisco-IOS-XE-track.yang 
* Cisco-IOS-XE-trustsec-oper.yang 
* Cisco-IOS-XE-tunnel.yang 
* Cisco-IOS-XE-types.yang 
* Cisco-IOS-XE-ucse.yang 
* Cisco-IOS-XE-umbrella.yang 
* Cisco-IOS-XE-utd.yang 
* Cisco-IOS-XE-vlan.yang 
* Cisco-IOS-XE-voice-dspfarm.yang 
* Cisco-IOS-XE-voice-oper.yang 
* Cisco-IOS-XE-voice-port.yang 
* Cisco-IOS-XE-voice-register.yang 
* Cisco-IOS-XE-voice.yang 
* Cisco-IOS-XE-vxlan.yang 
* Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang 
* Cisco-IOS-XE-wireless-access-point-oper.yang 
* Cisco-IOS-XE-wireless-ap-types.yang 
* Cisco-IOS-XE-wireless-apf-cfg.yang 
* Cisco-IOS-XE-wireless-awips-oper.yang 
* Cisco-IOS-XE-wireless-client-oper.yang 
* Cisco-IOS-XE-wireless-enum-types.yang 
* Cisco-IOS-XE-wireless-flex-cfg.yang 
* Cisco-IOS-XE-wireless-general-cfg.yang 
* Cisco-IOS-XE-wireless-hotspot-cfg.yang 
* Cisco-IOS-XE-wireless-me-general-cfg.yang 
* Cisco-IOS-XE-wireless-mobility-oper.yang 
* Cisco-IOS-XE-wireless-rf-cfg.yang 
* Cisco-IOS-XE-wireless-rfid-oper.yang 
* Cisco-IOS-XE-wireless-rogue-cfg.yang 
* Cisco-IOS-XE-wireless-rogue-oper.yang 
* Cisco-IOS-XE-wireless-rogue-types.yang 
* Cisco-IOS-XE-wireless-rrm-oper.yang 
* Cisco-IOS-XE-wireless-site-cfg.yang 
* Cisco-IOS-XE-wireless-tunnel-cfg.yang 
* Cisco-IOS-XE-wireless-tunnel-types.yang 
* Cisco-IOS-XE-wireless-types.yang 
* Cisco-IOS-XE-wireless-wlan-cfg.yang 
* Cisco-IOS-XE-zone.yang

#### Other Models Modified

* cisco-ia.yang 
* cisco-routing-ext.yang 
* cisco-smart-license-errors.yang 
* cisco-smart-license.yang 
* cisco-xe-openconfig-access-points-deviation.yang 
* cisco-xe-openconfig-bgp-deviation.yang 
* cisco-xe-openconfig-network-instance-deviation.yang 

#### Experimental YANG Models

* Cisco-IOS-XE-wireless-ble-mgmt-oper.yang
* Cisco-IOS-XE-wireless-tunnel-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-types.yang
* Cisco-IOS-XE-wireless-nmsp-oper.yang
* Cisco-IOS-XE-wireless-rfid-cfg.yang
* Cisco-IOS-XE-wireless-rfid-oper.yang
* Cisco-IOS-XE-wireless-radio-cfg.yang

These experimental YANG models are in the early status of design and are likely to change

### Backward Incompatible Changes

All the model specific backward incompatible changes have been documented in [Backward Incompatible Changes](BIC).

### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint```flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

As part of the model validation for this release we are ignoring "LEAFREF_IDENTIFIER_NOT_FOUND" and "STRICT_XPATH_FUNCTIONS" error types. Reason being that the missing leafref reference errors are due to pyang bug which needs to be fixed and some of the XPATH function errors are false positives which are handled in the newer version of pyang (2.3.2)

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


