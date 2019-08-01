## YANG Models and Platform Capabilities for Cisco IOS XE 16.12.1

This directory contains the YANG models supported by IOS XE 16.12.1:

* IOS XE native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms
listed below. As model content may differ based on platform capabilities, samples of the platform "hello" messages are also provided in the files listed against platforms:

| Platform | Capability File |
|----------|-----------------|
| ASR 1000 | [capability-asr1k.xml](capability-asr1k.xml) |
| ASR 900 RSP2/RSP3, ASR 920, NCS 520 and NCS 4200 | [capability-asr900.xml](capability-asr900.xml) |
| Catalyst 3650/3850 | [capability-cat3k.xml](capability-cat3k.xml) |
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


### Major Model Changes In 16.12.1

16.12.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-matm-oper.yang
* Cisco-IOS-XE-ucse.yang
* Cisco-IOS-XE-aaa-rpc.yang
* Cisco-IOS-XE-arp-rpc.yang
* Cisco-IOS-XE-bgp-rpc.yang
* Cisco-IOS-XE-cellular-rpc.yang
* Cisco-IOS-XE-crypto-rpc.yang
* Cisco-IOS-XE-cts-rpc.yang
* Cisco-IOS-XE-dhcp-rpc.yang
* Cisco-IOS-XE-cable-diag-rpc.yang
* Cisco-IOS-XE-factory-reset-secure-rpc.yang
* Cisco-IOS-XE-flow-rpc.yang
* Cisco-IOS-XE-ospf-rpc.yang
* Cisco-IOS-XE-platform-rpc.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-switch-rpc.yang
* Cisco-IOS-XE-ucse-rpc.yang
* Cisco-IOS-XE-umbrella-rpc.yang
* Cisco-IOS-XE-utd-rpc.yang


#### Native Models Modified 

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl-oper.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-app-hosting-cfg.yang
* Cisco-IOS-XE-app-hosting-oper.yang
* Cisco-IOS-XE-arp-oper.yang
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-avb.yang
* Cisco-IOS-XE-bba-group.yang
* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp-common-oper.yang
* Cisco-IOS-XE-bgp-oper.yang
* Cisco-IOS-XE-bgp-route-oper.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-boot-integrity-oper.yang
* Cisco-IOS-XE-breakout-port-oper.yang
* Cisco-IOS-XE-bridge-domain.yang
* Cisco-IOS-XE-bridge-oper.yang
* Cisco-IOS-XE-cable-diag-oper.yang
* Cisco-IOS-XE-call-home.yang
* Cisco-IOS-XE-card.yang
* Cisco-IOS-XE-cdp-oper.yang
* Cisco-IOS-XE-cdp.yang
* Cisco-IOS-XE-cef.yang
* Cisco-IOS-XE-cellular.yang
* Cisco-IOS-XE-cellwan-oper.yang
* Cisco-IOS-XE-cfm-oper.yang
* Cisco-IOS-XE-checkpoint-archive-oper.yang
* Cisco-IOS-XE-coap.yang
* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-controller-vdsl-oper.yang
* Cisco-IOS-XE-controller.yang
* Cisco-IOS-XE-crypto-oper.yang
* Cisco-IOS-XE-crypto-pki-oper.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-dapr.yang
* Cisco-IOS-XE-device-hardware-oper.yang

#### Openconfig Models Added

* openconfig-alarm-types.yang
* openconfig-isis-lsdb-types.yang   (**Refer to cisco-xe-openconfig-isis-deviation.yang**)
* openconfig-isis-lsp.yang   (**Refer to cisco-xe-openconfig-isis-deviation.yang**)
* openconfig-isis-policy.yang   (**Refer to cisco-xe-openconfig-isis-deviation.yang**)
* openconfig-isis-routing.yang   (**Refer to cisco-xe-openconfig-isis-deviation.yang**)
* openconfig-isis-types.yang   (**Refer to cisco-xe-openconfig-isis-deviation.yang**)
* openconfig-isis.yang   (**Refer to cisco-xe-openconfig-isis-deviation.yang**)
* openconfig-mpls-igp.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-mpls-ldp.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-mpls-rsvp.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-mpls-sr.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-mpls-static.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-mpls-te.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-mpls-types.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-mpls.yang   (**Refer to cisco-xe-openconfig-mpls-deviation.yang**)
* openconfig-platform-cpu.yang
* openconfig-platform-fan.yang
* openconfig-platform-psu.yang
* openconfig-system-wifi-ext.yang
* openconfig-wifi-mac.yang
* openconfig-wifi-phy.yang
* openconfig-wifi-types.yang


#### Deviation Models Added

* cisco-xe-openconfig-isis-deviation.yang
* cisco-xe-openconfig-mpls-deviation.yang
* cisco-xe-openconfig-segment-routing-deviation.yang

#### OpenConfig Models Modified

* openconfig-extensions.yang
* openconfig-if-aggregate.yang
* openconfig-if-ethernet.yang
* openconfig-network-instance.yang
* openconfig-platform-linecard.yang
* openconfig-platform-port.yang
* openconfig-platform-transceiver.yang
* openconfig-platform-types.yang
* openconfig-platform.yang
* openconfig-rib-bgp.yang
* openconfig-spanning-tree-types.yang
* openconfig-spanning-tree.yang
* openconfig-types.yang
* openconfig-vlan-types.yang
* openconfig-vlan.yang
* openconfig-yang-types.yang

#### Other Models Modified

* cisco-bridge-common.yang
* cisco-bridge-domain.yang
* cisco-ia.yang
* cisco-ospf.yang
* cisco-policy-filters.yang
* cisco-policy-target.yang
* cisco-policy.yang
* cisco-pw.yang
* cisco-routing-ext.yang
* cisco-self-mgmt.yang
* cisco-smart-license-errors.yang
* cisco-smart-license.yang
* cisco-storm-control.yang
* cisco-xe-access-openconfig-platform-deviation.yang
* cisco-xe-ietf-yang-push-deviation.yang
* cisco-xe-ietf-yang-push-ext.yang
* cisco-xe-openconfig-acl-ext.yang
* cisco-xe-openconfig-bgp-deviation.yang
* cisco-xe-openconfig-if-ethernet-ext.yang
* cisco-xe-openconfig-interfaces-deviation.yang
* cisco-xe-openconfig-interfaces-ext.yang
* cisco-xe-openconfig-lldp-deviation.yang
* cisco-xe-openconfig-system-ext.yang
* cisco-xe-routing-csr-openconfig-platform-deviation.yang
* cisco-xe-routing-isr-openconfig-platform-deviation.yang
* cisco-xe-switching-openconfig-platform-deviation.yang
* cisco-xe-switching-openconfig-vlan-deviation.yang
* cisco-xe-wireless-openconfig-vlan-deviation.yang
* common-mpls-static.yang
* common-mpls-types.yang
* nvo.yang
* pim.yang


#### Experimental YANG Models

* Cisco-IOS-XE-voice-register.yang
* Cisco-IOS-XE-wireless-ble-mgmt-oper.yang
* Cisco-IOS-XE-wireless-general-oper.yang
* Cisco-IOS-XE-wireless-rlan-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-types.yang
* Cisco-IOS-XE-wireless-fqdn-cfg.yang
* Cisco-IOS-XE-wireless-nmsp-oper.yang
* Cisco-IOS-XE-wireless-rfid-cfg.yang
* Cisco-IOS-XE-wireless-rfid-oper.yang
* Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang
* Cisco-IOS-XE-wireless-mobility-express-rpc.yang
* Cisco-IOS-XE-wireless-radio-cfg.yang

These experimental YANG models are in the early status of design and are likely to change

### 16.12.1 Errata

The below models, while advertised in the capabilities, are not supported on any platforms

* Cisco-IOS-XE-g8032.yang
* Cisco-IOS-XE-scada-gw-oper.yang
* openconfig-ap-manager.yang
* openconfig-access-points.yang
* openconfig-system-wifi-ext.yang
* openconfig-wifi-mac.yang
* openconfig-wifi-phy.yang
* openconfig-wifi-types.yang

The following two submodules of Cisco-IOS-XE-ethernet.yang are not officially supported until 17.1.1.

* Cisco-IOS-XE-ethernet-cfm-efp.yang
* Cisco-IOS-XE-ethernet-oam.yang

### Backward Incompatible Changes

All the model specific backward incompatible changes have been documented in [Backward Incompatible Changes](BIC).

### "On-Change" support

List of models supporting "On-change" notification are documented under [On-Change-Support](ON_CHANGE_MODELS).

### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint```flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


