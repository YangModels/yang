<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [YANG Models and Platform Capabilities for Cisco IOS XE 17.3.1](#yang-models-and-platform-capabilities-for-cisco-ios-xe-1731)
  - [Major Model Changes In 17.3.1](#major-model-changes-in-1731)
    - [Native Models Added](#native-models-added)
    - [Native Models Modified](#native-models-modified)
    - [Deviation Models Added](#deviation-models-added)
    - [Openconfig Models Added](#openconfig-models-added)
    - [OpenConfig Models Modified](#openconfig-models-modified)
    - [Other Models Modified](#other-models-modified)
    - [Experimental YANG Models](#experimental-yang-models)
  - [Backward Incompatible Changes](#backward-incompatible-changes)
  - [Compliance With "pyang --lint"](#compliance-with-pyang---lint)
  - [Revision Statements](#revision-statements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## YANG Models and Platform Capabilities for Cisco IOS XE 17.3.1

This directory contains the YANG models supported by IOS XE 17.3.1:

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
| CBR-8 | [capability-cbr.xml](capability-cbr.xml) |
| CSR 1000v/ISRv | [capability-csr1k.xml](capability-csr1k.xml) |
| ESS 3x00 | [capability-ess3x00.xml](capability-ess3x00.xml) |
| IR 1101 | [capability-ir1101.xml](capability-ir1101.xml) |
| IE 3x00 | [capability-ie3x00.xml](capability-ie3x00.xml) |
| ISR 1000 | [capability-isr1k.xml](capability-isr1k.xml) |
| ISR 4000 | [capability-isr4k.xml](capability-isr4k.xml) |


### Major Model Changes In 17.3.1

17.3.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-banner-internal.yang
* Cisco-IOS-XE-digital-io-oper.yang
* Cisco-IOS-XE-digitalio.yang
* Cisco-IOS-XE-eogre-tunnel-oper.yang
* Cisco-IOS-XE-frame-relay.yang
* Cisco-IOS-XE-install-oper.yang
* Cisco-IOS-XE-isdn.yang
* Cisco-IOS-XE-macsec-oper.yang
* Cisco-IOS-XE-mdt-oper-v2.yang
* Cisco-IOS-XE-mobileip.yang
* Cisco-IOS-XE-mroute-oper.yang
* Cisco-IOS-XE-multicast-rpc.yang
* Cisco-IOS-XE-ncch-cfg.yang
* Cisco-IOS-XE-ncch-oper.yang
* Cisco-IOS-XE-ospf-common.yang
* Cisco-IOS-XE-ospf-events.yang
* Cisco-IOS-XE-perf-measure-events.yang
* Cisco-IOS-XE-perf-measure-oper.yang
* Cisco-IOS-XE-pim-oper.yang
* Cisco-IOS-XE-qfp-resource-utilization-oper.yang
* Cisco-IOS-XE-swc.yang
* Cisco-IOS-XE-switch-dp-mac-learning-oper.yang
* Cisco-IOS-XE-switch-dp-punt-inject-oper.yang
* Cisco-IOS-XE-switch-dp-resources-oper.yang
* Cisco-IOS-XE-voice-class.yang
* Cisco-IOS-XE-voice-dspfarm.yang
* Cisco-IOS-XE-wireless-ble-ltx-oper.yang
* Cisco-IOS-XE-wireless-ble-mgmt-cmd-rpc.yang
* Cisco-IOS-XE-wireless-dot15-cfg.yang
* Cisco-IOS-XE-wireless-rule-cfg.yang
* Cisco-IOS-XE-wireless-rule-mdns-oper.yang
* openconfig-macsec-types.yang
* openconfig-macsec.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa-types.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl-oper.yang
* Cisco-IOS-XE-app-hosting-cfg.yang
* Cisco-IOS-XE-app-hosting-oper.yang
* Cisco-IOS-XE-arp-oper.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp-common-oper.yang
* Cisco-IOS-XE-bgp-oper.yang
* Cisco-IOS-XE-bgp-route-oper.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-boot-integrity-oper.yang
* Cisco-IOS-XE-breakout-port-oper.yang
* Cisco-IOS-XE-bridge-oper.yang
* Cisco-IOS-XE-cable-diag-oper.yang
* Cisco-IOS-XE-cdp-oper.yang
* Cisco-IOS-XE-cdp.yang
* Cisco-IOS-XE-cellwan-oper.yang
* Cisco-IOS-XE-cfm-oper.yang
* Cisco-IOS-XE-checkpoint-archive-oper.yang
* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-controller-shdsl-common.yang
* Cisco-IOS-XE-controller-shdsl-events.yang
* Cisco-IOS-XE-controller-shdsl-oper.yang
* Cisco-IOS-XE-controller-t1e1-oper.yang
* Cisco-IOS-XE-controller-vdsl-oper.yang
* Cisco-IOS-XE-controller.yang
* Cisco-IOS-XE-crypto-oper.yang
* Cisco-IOS-XE-crypto-pki-events.yang
* Cisco-IOS-XE-crypto-pki-oper.yang
* Cisco-IOS-XE-crypto-rpc.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-device-hardware-oper.yang
* Cisco-IOS-XE-dhcp-oper.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-docsis-oper.yang
* Cisco-IOS-XE-efp-oper.yang
* Cisco-IOS-XE-eigrp-oper.yang
* Cisco-IOS-XE-environment-oper.yang
* Cisco-IOS-XE-ethernet-cfm-efp.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-event-history-types.yang
* Cisco-IOS-XE-features.yang
* Cisco-IOS-XE-fib-oper.yang
* Cisco-IOS-XE-flow-monitor-oper.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-fw-oper.yang
* Cisco-IOS-XE-gir-oper.yang
* Cisco-IOS-XE-gnss-oper.yang
* Cisco-IOS-XE-ha-oper.yang
* Cisco-IOS-XE-icmp.yang
* Cisco-IOS-XE-identity-oper.yang
* Cisco-IOS-XE-im-events-oper.yang
* Cisco-IOS-XE-install-events.yang
* Cisco-IOS-XE-install-rpc.yang
* Cisco-IOS-XE-interface-common.yang
* Cisco-IOS-XE-interfaces-oper.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ios-common-oper.yang
* Cisco-IOS-XE-ios-events-oper.yang
* Cisco-IOS-XE-ip-sla-events.yang
* Cisco-IOS-XE-ip-sla-oper.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6-oper.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isdn-oper.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-l2tp-oper.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-lacp-oper.yang
* Cisco-IOS-XE-linecard-oper.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-lldp-oper.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-matm-oper.yang
* Cisco-IOS-XE-mdns-gateway.yang
* Cisco-IOS-XE-mdt-cfg.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper.yang
* Cisco-IOS-XE-memory-oper.yang
* Cisco-IOS-XE-mka-oper.yang
* Cisco-IOS-XE-mlppp-oper.yang
* Cisco-IOS-XE-mpls-forwarding-oper.yang
* Cisco-IOS-XE-mpls-ldp-oper.yang
* Cisco-IOS-XE-mpls.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat-oper.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-nd.yang
* Cisco-IOS-XE-ntp-oper.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-ospf-oper.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-platform-common-oper.yang
* Cisco-IOS-XE-platform-events-oper.yang
* Cisco-IOS-XE-platform-oper.yang
* Cisco-IOS-XE-platform-rpc.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-ppp-oper.yang
* Cisco-IOS-XE-ppp.yang
* Cisco-IOS-XE-pppoe.yang
* Cisco-IOS-XE-process-cpu-oper.yang
* Cisco-IOS-XE-process-memory-oper.yang
* Cisco-IOS-XE-ptp-synce-oper.yang
* Cisco-IOS-XE-qfp-classification-oper.yang
* Cisco-IOS-XE-qfp-stats-oper.yang
* Cisco-IOS-XE-qfp-stats.yang
* Cisco-IOS-XE-rawsocket-oper.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-sanet-deviation.yang
* Cisco-IOS-XE-sanet.yang
* Cisco-IOS-XE-scada-gw-oper.yang
* Cisco-IOS-XE-sd-vxlan-oper.yang
* Cisco-IOS-XE-segment-routing.yang
* Cisco-IOS-XE-service-insertion.yang
* Cisco-IOS-XE-site-manager.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-sm-enum-types.yang
* Cisco-IOS-XE-sm-events-oper.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree-oper.yang
* Cisco-IOS-XE-stack-mgr-events-oper.yang
* Cisco-IOS-XE-stack-oper.yang
* Cisco-IOS-XE-stacking-oper.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-synce.yang
* Cisco-IOS-XE-tcam-oper.yang
* Cisco-IOS-XE-template.yang
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-transceiver-oper.yang
* Cisco-IOS-XE-trustsec-oper.yang
* Cisco-IOS-XE-tunnel-oper.yang
* Cisco-IOS-XE-tunnel-types.yang
* Cisco-IOS-XE-ucse-oper.yang
* Cisco-IOS-XE-ucse.yang
* Cisco-IOS-XE-umbrella-oper.yang
* Cisco-IOS-XE-utd-common-oper.yang
* Cisco-IOS-XE-utd-oper.yang
* Cisco-IOS-XE-vlan-oper.yang
* Cisco-IOS-XE-voice-oper.yang
* Cisco-IOS-XE-voice-port.yang
* Cisco-IOS-XE-voice-register.yang
* Cisco-IOS-XE-voice.yang
* Cisco-IOS-XE-vrf-oper.yang
* Cisco-IOS-XE-vrrp-oper.yang
* Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang
* Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang
* Cisco-IOS-XE-wireless-access-point-oper.yang
* Cisco-IOS-XE-wireless-ap-cfg.yang
* Cisco-IOS-XE-wireless-ap-types.yang
* Cisco-IOS-XE-wireless-apf-cfg.yang
* Cisco-IOS-XE-wireless-client-oper.yang
* Cisco-IOS-XE-wireless-dot11-cfg.yang
* Cisco-IOS-XE-wireless-enum-types.yang
* Cisco-IOS-XE-wireless-events-oper.yang
* Cisco-IOS-XE-wireless-fabric-cfg.yang
* Cisco-IOS-XE-wireless-flex-cfg.yang
* Cisco-IOS-XE-wireless-general-cfg.yang
* Cisco-IOS-XE-wireless-hotspot-cfg.yang
* Cisco-IOS-XE-wireless-mesh-cfg.yang
* Cisco-IOS-XE-wireless-mesh-oper.yang
* Cisco-IOS-XE-wireless-rf-cfg.yang
* Cisco-IOS-XE-wireless-rlan-cfg.yang
* Cisco-IOS-XE-wireless-rogue-cfg.yang
* Cisco-IOS-XE-wireless-rrm-cfg.yang
* Cisco-IOS-XE-wireless-security-cfg.yang
* Cisco-IOS-XE-wireless-site-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-types.yang
* Cisco-IOS-XE-wireless-types.yang
* Cisco-IOS-XE-wireless-wlan-cfg.yang
* Cisco-IOS-XE-yang-interfaces-cfg.yang

#### Deviation Models Added

* Cisco-IOS-XE-dialer-deviation.yang
* Cisco-IOS-XE-ethernet-deviation.yang
* Cisco-IOS-XE-nd-deviation.yang
* Cisco-IOS-XE-policy-deviation.yang

#### Openconfig Models Added

* openconfig-macsec-types.yang
* openconfig-macsec.yang

#### OpenConfig Models Modified

* openconfig-lldp.yang
* openconfig-yang-types.yang

#### Other Models Modified

* cisco-xe-ietf-yang-push-ext.yang
* cisco-xe-openconfig-access-points-deviation.yang
* cisco-xe-openconfig-if-ip-deviation.yang
* cisco-xe-openconfig-openflow-deviation.yang

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


