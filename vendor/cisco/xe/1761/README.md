<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [YANG Models and Platform Capabilities for Cisco IOS XE 17.6.1](#yang-models-and-platform-capabilities-for-cisco-ios-xe-1761)
  - [Major Model Changes In 17.6.1](#major-model-changes-in-1761)
    - [Native Models Added](#native-models-added)
    - [Deviation Models Added](#deviation-models-added)
    - [Native Models Modified](#native-models-modified)
    - [Other Models Modified](#other-models-modified)
    - [Experimental YANG Models](#experimental-yang-models)
  - [Backward Incompatible Changes](#backward-incompatible-changes)
  - [Compliance With "pyang --lint"](#compliance-with-pyang---lint)
  - [Revision Statements](#revision-statements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## YANG Models and Platform Capabilities for Cisco IOS XE 17.6.1

This directory contains the YANG models supported by IOS XE 17.6.1:

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


### Major Model Changes In 17.6.1

17.6.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-aaa-actions-rpc.yang
* Cisco-IOS-XE-aaa-events.yang
* Cisco-IOS-XE-alarm-profile.yang
* Cisco-IOS-XE-appqoe-serv-oper.yang
* Cisco-IOS-XE-appqoe-sslproxy-oper.yang
* Cisco-IOS-XE-appqoe-tcpproxy-oper.yang
* Cisco-IOS-XE-bridge.yang
* Cisco-IOS-XE-dmi-common-types.yang
* Cisco-IOS-XE-embedded-ap-oper.yang
* Cisco-IOS-XE-ethernet-rpc.yang
* Cisco-IOS-XE-gnmi-cfg.yang
* Cisco-IOS-XE-group-policy.yang
* Cisco-IOS-XE-ignition-oper.yang
* Cisco-IOS-XE-mdt-capabilities-oper.yang
* Cisco-IOS-XE-mpls-te-oper.yang
* Cisco-IOS-XE-ospfv3-deviation.yang
* Cisco-IOS-XE-sisf.yang
* Cisco-IOS-XE-teyes-oper.yang
* Cisco-IOS-XE-trace-events.yang
* Cisco-IOS-XE-trace-rpc.yang
* Cisco-IOS-XE-verify-events.yang
* Cisco-IOS-XE-verify-rpc.yang
* Cisco-IOS-XE-wireless-actions-rpc.yang
* Cisco-IOS-XE-wireless-client-global-oper.yang
* Cisco-IOS-XE-wireless-mesh-rpc.yang
* Cisco-IOS-XE-yang-interfaces-oper.yang

#### Deviation Models Added

* Cisco-IOS-XE-cts-switching-deviation.yang
* Cisco-IOS-XE-group-policy-deviation.yang
* Cisco-IOS-XE-poch-lb-switch-deviation.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa-types.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-adsl.yang
* Cisco-IOS-XE-app-hosting-cfg.yang
* Cisco-IOS-XE-app-hosting-oper.yang
* Cisco-IOS-XE-app-hosting.yang
* Cisco-IOS-XE-appqoe-events.yang
* Cisco-IOS-XE-appqoe-oper.yang
* Cisco-IOS-XE-appqoe-types.yang
* Cisco-IOS-XE-arp-oper.yang
* Cisco-IOS-XE-arp-rpc.yang
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-avb.yang
* Cisco-IOS-XE-banner-internal.yang
* Cisco-IOS-XE-bba-group.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-bridge-domain.yang
* Cisco-IOS-XE-call-home.yang
* Cisco-IOS-XE-card.yang
* Cisco-IOS-XE-cdp-deviation.yang
* Cisco-IOS-XE-cdp.yang
* Cisco-IOS-XE-cef.yang
* Cisco-IOS-XE-cellular.yang
* Cisco-IOS-XE-cfm-oper.yang
* Cisco-IOS-XE-coap.yang
* Cisco-IOS-XE-controller.yang
* Cisco-IOS-XE-crypto-rpc.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts-routing-deviation.yang
* Cisco-IOS-XE-cts-rpc.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-dapr.yang
* Cisco-IOS-XE-device-sensor.yang
* Cisco-IOS-XE-device-tracking.yang
* Cisco-IOS-XE-dhcp-oper.yang
* Cisco-IOS-XE-dhcp-rpc.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-diagnostics.yang
* Cisco-IOS-XE-dialer.yang
* Cisco-IOS-XE-digitalio.yang
* Cisco-IOS-XE-dot1x.yang
* Cisco-IOS-XE-dre-oper.yang
* Cisco-IOS-XE-eem.yang
* Cisco-IOS-XE-eigrp-obsolete.yang
* Cisco-IOS-XE-eigrp.yang
* Cisco-IOS-XE-eta.yang
* Cisco-IOS-XE-ethernet-cfm-efp.yang
* Cisco-IOS-XE-ethernet-deviation.yang
* Cisco-IOS-XE-ethernet-oam.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-ethinternal-subslot.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-factory-reset-secure-rpc.yang
* Cisco-IOS-XE-features.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-fqdn.yang
* Cisco-IOS-XE-frame-relay.yang
* Cisco-IOS-XE-g8032.yang
* Cisco-IOS-XE-geo.yang
* Cisco-IOS-XE-gnss-dr-oper.yang
* Cisco-IOS-XE-http.yang
* Cisco-IOS-XE-icmp.yang
* Cisco-IOS-XE-identity-oper.yang
* Cisco-IOS-XE-igmp.yang
* Cisco-IOS-XE-install-events.yang
* Cisco-IOS-XE-install-oper.yang
* Cisco-IOS-XE-install-rpc.yang
* Cisco-IOS-XE-interface-common.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ios-events-oper.yang
* Cisco-IOS-XE-ip-sla-oper.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipmux.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isdn.yang
* Cisco-IOS-XE-isg.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-iwanfabric.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-l3vpn.yang
* Cisco-IOS-XE-license.yang
* Cisco-IOS-XE-line-deviation.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-lldp.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-mdns-gateway.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper-v2.yang
* Cisco-IOS-XE-mka.yang
* Cisco-IOS-XE-mld.yang
* Cisco-IOS-XE-mmode.yang
* Cisco-IOS-XE-mobileip.yang
* Cisco-IOS-XE-mpls.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-mvrp.yang
* Cisco-IOS-XE-nam.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-nd-deviation.yang
* Cisco-IOS-XE-nd.yang
* Cisco-IOS-XE-nhrp.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-nwpi-oper.yang
* Cisco-IOS-XE-nwpi-rpc.yang
* Cisco-IOS-XE-nwpi-types.yang
* Cisco-IOS-XE-object-group.yang
* Cisco-IOS-XE-ospf-obsolete.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-otv.yang
* Cisco-IOS-XE-parser.yang
* Cisco-IOS-XE-pathmgr.yang
* Cisco-IOS-XE-perf-measure.yang
* Cisco-IOS-XE-pfr.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-pnp.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-policy-deviation.yang
* Cisco-IOS-XE-policy-mcp-deviation.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-port-channel-deviation.yang
* Cisco-IOS-XE-power-deviation.yang
* Cisco-IOS-XE-power.yang
* Cisco-IOS-XE-ppp.yang
* Cisco-IOS-XE-pppoe.yang
* Cisco-IOS-XE-ptp-pi.yang
* Cisco-IOS-XE-ptp.yang
* Cisco-IOS-XE-qfp-stats.yang
* Cisco-IOS-XE-qos.yang
* Cisco-IOS-XE-rawsocket.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-rmi-dad.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-rsvp.yang
* Cisco-IOS-XE-sanet-deviation.yang
* Cisco-IOS-XE-sanet.yang
* Cisco-IOS-XE-scada-gw.yang
* Cisco-IOS-XE-segment-routing.yang
* Cisco-IOS-XE-serial.yang
* Cisco-IOS-XE-service-discovery.yang
* Cisco-IOS-XE-service-insertion-oper.yang
* Cisco-IOS-XE-service-insertion.yang
* Cisco-IOS-XE-service-routing.yang
* Cisco-IOS-XE-sip-ua.yang
* Cisco-IOS-XE-site-manager.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree.yang
* Cisco-IOS-XE-stackwise-virtual.yang
* Cisco-IOS-XE-switch-deviation.yang
* Cisco-IOS-XE-switch-rpc.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-synce.yang
* Cisco-IOS-XE-template.yang
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-tunnel-types.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-ucse-rpc.yang
* Cisco-IOS-XE-ucse.yang
* Cisco-IOS-XE-udld.yang
* Cisco-IOS-XE-umbrella-oper-dp.yang
* Cisco-IOS-XE-umbrella.yang
* Cisco-IOS-XE-utd-rpc.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-voice-class.yang
* Cisco-IOS-XE-voice-dspfarm.yang
* Cisco-IOS-XE-voice-port.yang
* Cisco-IOS-XE-voice-register.yang
* Cisco-IOS-XE-voice.yang
* Cisco-IOS-XE-vpdn.yang
* Cisco-IOS-XE-vrrp-deviation.yang
* Cisco-IOS-XE-vrrp.yang
* Cisco-IOS-XE-vservice.yang
* Cisco-IOS-XE-vstack.yang
* Cisco-IOS-XE-vtp.yang
* Cisco-IOS-XE-vxlan.yang
* Cisco-IOS-XE-wccp.yang
* Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang
* Cisco-IOS-XE-wireless-access-point-oper.yang
* Cisco-IOS-XE-wireless-ap-global-oper.yang
* Cisco-IOS-XE-wireless-ap-types.yang
* Cisco-IOS-XE-wireless-apf-cfg.yang
* Cisco-IOS-XE-wireless-client-oper.yang
* Cisco-IOS-XE-wireless-client-types.yang
* Cisco-IOS-XE-wireless-dot11-cfg.yang
* Cisco-IOS-XE-wireless-enum-types.yang
* Cisco-IOS-XE-wireless-events-oper.yang
* Cisco-IOS-XE-wireless-flex-cfg.yang
* Cisco-IOS-XE-wireless-general-cfg.yang
* Cisco-IOS-XE-wireless-location-oper.yang
* Cisco-IOS-XE-wireless-mesh-cfg.yang
* Cisco-IOS-XE-wireless-radio-cfg.yang
* Cisco-IOS-XE-wireless-rf-cfg.yang
* Cisco-IOS-XE-wireless-rogue-oper.yang
* Cisco-IOS-XE-wireless-rrm-cfg.yang
* Cisco-IOS-XE-wireless-rrm-oper.yang
* Cisco-IOS-XE-wireless-rrm-types.yang
* Cisco-IOS-XE-wireless-site-cfg.yang
* Cisco-IOS-XE-wireless-types.yang
* Cisco-IOS-XE-wireless-wlan-cfg.yang
* Cisco-IOS-XE-wsma.yang
* Cisco-IOS-XE-yang-interfaces-cfg.yang
* Cisco-IOS-XE-zone-rpc.yang
* Cisco-IOS-XE-zone.yang


#### Other Models Modified

* cisco-bridge-common.yang
* cisco-bridge-domain.yang
* cisco-ethernet.yang
* cisco-ia.yang
* cisco-ospf.yang
* cisco-policy-filters.yang
* cisco-policy-target.yang
* cisco-policy.yang
* cisco-pw.yang
* cisco-routing-ext.yang
* cisco-semver.yang
* cisco-smart-license-errors.yang
* cisco-smart-license.yang
* cisco-storm-control.yang
* cisco-xe-access-openconfig-if-ethernet-deviation.yang
* cisco-xe-access-openconfig-platform-deviation.yang
* cisco-xe-access-openconfig-system-deviation.yang
* cisco-xe-access-openconfig-vlan-deviation.yang
* cisco-xe-cbr-openconfig-if-ethernet-deviation.yang
* cisco-xe-cbr-openconfig-system-deviation.yang
* cisco-xe-cbr-openconfig-vlan-deviation.yang
* cisco-xe-ietf-ip-deviation.yang
* cisco-xe-ietf-ipv4-unicast-routing-deviation.yang
* cisco-xe-ietf-ipv6-unicast-routing-deviation.yang
* cisco-xe-ietf-ospf-deviation.yang
* cisco-xe-ietf-routing-deviation.yang
* cisco-xe-openconfig-access-points-deviation.yang
* cisco-xe-openconfig-acl-deviation.yang
* cisco-xe-openconfig-aft-deviation.yang
* cisco-xe-openconfig-bgp-deviation.yang
* cisco-xe-openconfig-bgp-policy-deviation.yang
* cisco-xe-openconfig-if-ethernet-ext.yang
* cisco-xe-openconfig-if-ip-deviation.yang
* cisco-xe-openconfig-if-poe-deviation.yang
* cisco-xe-openconfig-interfaces-deviation.yang
* cisco-xe-openconfig-interfaces-ext.yang
* cisco-xe-openconfig-isis-deviation.yang
* cisco-xe-openconfig-isis-policy-deviation.yang
* cisco-xe-openconfig-lldp-deviation.yang
* cisco-xe-openconfig-local-routing-deviation.yang
* cisco-xe-openconfig-mpls-deviation.yang
* cisco-xe-openconfig-network-instance-deviation.yang
* cisco-xe-openconfig-openflow-deviation.yang
* cisco-xe-openconfig-routing-policy-deviation.yang
* cisco-xe-openconfig-segment-routing-deviation.yang
* cisco-xe-openconfig-spanning-tree-deviation.yang
* cisco-xe-openconfig-system-management-deviation.yang
* cisco-xe-routing-asr-openconfig-if-ethernet-deviation.yang
* cisco-xe-routing-csr-openconfig-platform-deviation.yang
* cisco-xe-routing-isr-openconfig-if-ethernet-deviation.yang
* cisco-xe-routing-isr-openconfig-platform-deviation.yang
* cisco-xe-routing-openconfig-system-deviation.yang
* cisco-xe-routing-openconfig-system-management-deviation.yang
* cisco-xe-routing-openconfig-vlan-deviation.yang
* cisco-xe-switching-cat9k-openconfig-system-deviation.yang
* cisco-xe-switching-openconfig-if-ethernet-deviation.yang
* cisco-xe-switching-openconfig-interfaces-deviation.yang
* cisco-xe-switching-openconfig-platform-deviation.yang
* cisco-xe-switching-openconfig-vlan-deviation.yang
* cisco-xe-wireless-openconfig-if-ethernet-deviation.yang
* cisco-xe-wireless-openconfig-vlan-deviation.yang
* common-mpls-static.yang
* common-mpls-types.yang
* nvo.yang
* openconfig-if-ethernet.yang
* pim.yang
* policy-attr.yang
* policy-types.yang

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


