<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [YANG Models and Platform Capabilities for Cisco Cedge 17.2.1](#yang-models-and-platform-capabilities-for-cisco-cedge-1721)
    - [Native Models Added](#native-models-added)
    - [Openconfig Models Added](#openconfig-models-added)
    - [Other Models Added](#other-models-added)
  - [Compliance With "pyang --lint"](#compliance-with-pyang---lint)
  - [Revision Statements](#revision-statements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## YANG Models and Platform Capabilities for Cisco Cedge 17.2.1

This directory contains the YANG models supported by Cedge 17.2.1:

* Cedge native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms
listed below. As model content may differ based on platform capabilities, samples of the platform "hello" messages are also provided in the files listed against platforms:

| Platform | Capability File |
|----------|-----------------|
| ASR 1000 | [capability-asr1k.xml](capability-asr1k.xml) |
| CSR 1000v/ISRv | [capability-csr1k.xml](capability-csr1k.xml) |
| ISR 4000 | [capability-isr4k.xml](capability-isr4k.xml) |
| SPARROW | [capability-IOT.xml](capability-IOT.xml) |


#### Native Models Added

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa-rpc.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl-oper.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-app-hosting-cfg.yang
* Cisco-IOS-XE-app-hosting-oper.yang
* Cisco-IOS-XE-arp-oper.yang
* Cisco-IOS-XE-arp-rpc.yang
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-bba-group.yang
* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp-common-oper.yang
* Cisco-IOS-XE-bgp-oper.yang
* Cisco-IOS-XE-bgp-route-oper.yang
* Cisco-IOS-XE-bgp-rpc.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-breakout-port-oper.yang
* Cisco-IOS-XE-bridge-domain.yang
* Cisco-IOS-XE-bridge-oper.yang
* Cisco-IOS-XE-call-home.yang
* Cisco-IOS-XE-card.yang
* Cisco-IOS-XE-cdp-deviation.yang
* Cisco-IOS-XE-cdp-oper.yang
* Cisco-IOS-XE-cdp.yang
* Cisco-IOS-XE-cef.yang
* Cisco-IOS-XE-cellular-rpc.yang
* Cisco-IOS-XE-cellular.yang
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
* Cisco-IOS-XE-cts-rpc.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-dapr.yang
* Cisco-IOS-XE-device-hardware-oper.yang
* Cisco-IOS-XE-device-tracking.yang
* Cisco-IOS-XE-dhcp-oper.yang
* Cisco-IOS-XE-dhcp-rpc.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-diagnostics.yang
* Cisco-IOS-XE-dialer.yang
* Cisco-IOS-XE-diffserv-target-oper.yang
* Cisco-IOS-XE-dot1x.yang
* Cisco-IOS-XE-eem.yang
* Cisco-IOS-XE-efp-oper.yang
* Cisco-IOS-XE-eigrp-obsolete.yang
* Cisco-IOS-XE-eigrp-oper.yang
* Cisco-IOS-XE-eigrp.yang
* Cisco-IOS-XE-environment-oper.yang
* Cisco-IOS-XE-eta.yang
* Cisco-IOS-XE-ethernet-cfm-efp.yang
* Cisco-IOS-XE-ethernet-oam.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-event-history-types.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-factory-reset-secure-rpc.yang
* Cisco-IOS-XE-features.yang
* Cisco-IOS-XE-fib-oper.yang
* Cisco-IOS-XE-flow-monitor-oper.yang
* Cisco-IOS-XE-flow-rpc.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-fw-oper.yang
* Cisco-IOS-XE-gir-oper.yang
* Cisco-IOS-XE-gnss-oper.yang
* Cisco-IOS-XE-http.yang
* Cisco-IOS-XE-icmp.yang
* Cisco-IOS-XE-igmp.yang
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
* Cisco-IOS-XE-ipmux.yang
* Cisco-IOS-XE-ipv6-oper.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isdn-oper.yang
* Cisco-IOS-XE-isg.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-iwanfabric.yang
* Cisco-IOS-XE-l2tp-oper.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-l3vpn.yang
* Cisco-IOS-XE-lacp-oper.yang
* Cisco-IOS-XE-license.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-linecard-oper.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-lldp-oper.yang
* Cisco-IOS-XE-lldp.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-mdns-gateway.yang
* Cisco-IOS-XE-mdt-cfg.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper.yang
* Cisco-IOS-XE-memory-oper.yang
* Cisco-IOS-XE-mka-oper.yang
* Cisco-IOS-XE-mka.yang
* Cisco-IOS-XE-mld.yang
* Cisco-IOS-XE-mlppp-oper.yang
* Cisco-IOS-XE-mpls-forwarding-oper.yang
* Cisco-IOS-XE-mpls-ldp-oper.yang
* Cisco-IOS-XE-mpls.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nam.yang
* Cisco-IOS-XE-nat-oper.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-nd.yang
* Cisco-IOS-XE-nhrp.yang
* Cisco-IOS-XE-ntp-oper.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-object-group.yang
* Cisco-IOS-XE-ospf-obsolete.yang
* Cisco-IOS-XE-ospf-oper.yang
* Cisco-IOS-XE-ospf-rpc.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-otv.yang
* Cisco-IOS-XE-parser.yang
* Cisco-IOS-XE-pathmgr.yang
* Cisco-IOS-XE-perf-measure.yang
* Cisco-IOS-XE-pfr.yang
* Cisco-IOS-XE-platform-oper.yang
* Cisco-IOS-XE-platform-rpc.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-pnp.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-power-deviation.yang
* Cisco-IOS-XE-power.yang
* Cisco-IOS-XE-ppp-oper.yang
* Cisco-IOS-XE-ppp.yang
* Cisco-IOS-XE-pppoe.yang
* Cisco-IOS-XE-process-cpu-oper.yang
* Cisco-IOS-XE-process-memory-oper.yang
* Cisco-IOS-XE-qfp-classification-oper.yang
* Cisco-IOS-XE-qfp-stats-oper.yang
* Cisco-IOS-XE-qfp-stats.yang
* Cisco-IOS-XE-qos.yang
* Cisco-IOS-XE-rawsocket-oper.yang
* Cisco-IOS-XE-rawsocket.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-rmi-dad.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-rsvp.yang
* Cisco-IOS-XE-sanet-deviation.yang
* Cisco-IOS-XE-sanet.yang
* Cisco-IOS-XE-scada-gw-oper.yang
* Cisco-IOS-XE-scada-gw.yang
* Cisco-IOS-XE-sd-vxlan-oper.yang
* Cisco-IOS-XE-segment-routing.yang
* Cisco-IOS-XE-serial.yang
* Cisco-IOS-XE-service-chain.yang
* Cisco-IOS-XE-service-discovery.yang
* Cisco-IOS-XE-service-insertion.yang
* Cisco-IOS-XE-service-routing.yang
* Cisco-IOS-XE-site-manager.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-sm-enum-types.yang
* Cisco-IOS-XE-sm-events-oper.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree-oper.yang
* Cisco-IOS-XE-spanning-tree.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-synce.yang
* Cisco-IOS-XE-template.yang
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-transceiver-oper.yang
* Cisco-IOS-XE-trustsec-oper.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-ucse-oper.yang
* Cisco-IOS-XE-ucse-rpc.yang
* Cisco-IOS-XE-ucse.yang
* Cisco-IOS-XE-umbrella-oper-dp.yang
* Cisco-IOS-XE-umbrella-oper.yang
* Cisco-IOS-XE-umbrella-rpc.yang
* Cisco-IOS-XE-umbrella.yang
* Cisco-IOS-XE-utd-common-oper.yang
* Cisco-IOS-XE-utd-oper.yang
* Cisco-IOS-XE-utd-rpc.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-vlan-oper.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-voice-oper.yang
* Cisco-IOS-XE-voice-port.yang
* Cisco-IOS-XE-voice-register.yang
* Cisco-IOS-XE-voice.yang
* Cisco-IOS-XE-vpdn.yang
* Cisco-IOS-XE-vrf-oper.yang
* Cisco-IOS-XE-vrrp-oper.yang
* Cisco-IOS-XE-vrrp.yang
* Cisco-IOS-XE-vservice.yang
* Cisco-IOS-XE-vtp.yang
* Cisco-IOS-XE-vxlan.yang
* Cisco-IOS-XE-wccp.yang
* Cisco-IOS-XE-wsma.yang
* Cisco-IOS-XE-yang-interfaces-cfg.yang
* Cisco-IOS-XE-zone-rpc.yang
* Cisco-IOS-XE-zone.yang

#### Openconfig Models Added

* openconfig-aaa-radius.yang
* openconfig-aaa-tacacs.yang
* openconfig-aaa-types.yang
* openconfig-aaa.yang
* openconfig-acl.yang
* openconfig-aft-network-instance.yang
* openconfig-aft-types.yang
* openconfig-aft.yang
* openconfig-alarm-types.yang
* openconfig-alarms.yang
* openconfig-bgp-common-multiprotocol.yang
* openconfig-bgp-common-structure.yang
* openconfig-bgp-common.yang
* openconfig-bgp-global.yang
* openconfig-bgp-neighbor.yang
* openconfig-bgp-peer-group.yang
* openconfig-bgp-policy.yang
* openconfig-bgp-types.yang
* openconfig-bgp.yang
* openconfig-extensions.yang
* openconfig-if-aggregate.yang
* openconfig-if-ethernet.yang
* openconfig-if-ip-ext.yang
* openconfig-if-ip.yang
* openconfig-if-poe.yang
* openconfig-inet-types.yang
* openconfig-interfaces.yang
* openconfig-isis-lsdb-types.yang
* openconfig-isis-lsp.yang
* openconfig-isis-policy.yang
* openconfig-isis-routing.yang
* openconfig-isis-types.yang
* openconfig-isis.yang
* openconfig-lacp.yang
* openconfig-lldp-types.yang
* openconfig-lldp.yang
* openconfig-local-routing.yang
* openconfig-mpls-igp.yang
* openconfig-mpls-ldp.yang
* openconfig-mpls-rsvp.yang
* openconfig-mpls-sr.yang
* openconfig-mpls-static.yang
* openconfig-mpls-te.yang
* openconfig-mpls-types.yang
* openconfig-mpls.yang
* openconfig-network-instance-l2.yang
* openconfig-network-instance-l3.yang
* openconfig-network-instance-types.yang
* openconfig-network-instance.yang
* openconfig-packet-match-types.yang
* openconfig-packet-match.yang
* openconfig-platform-cpu.yang
* openconfig-platform-fan.yang
* openconfig-platform-linecard.yang
* openconfig-platform-port.yang
* openconfig-platform-psu.yang
* openconfig-platform-transceiver.yang
* openconfig-platform-types.yang
* openconfig-platform.yang
* openconfig-policy-types.yang
* openconfig-procmon.yang
* openconfig-rib-bgp-ext.yang
* openconfig-rib-bgp-types.yang
* openconfig-rib-bgp.yang
* openconfig-routing-policy.yang
* openconfig-segment-routing.yang
* openconfig-spanning-tree-types.yang
* openconfig-spanning-tree.yang
* openconfig-system-logging.yang
* openconfig-system-management.yang
* openconfig-system-terminal.yang
* openconfig-system.yang
* openconfig-transport-types.yang
* openconfig-types.yang
* openconfig-vlan-types.yang
* openconfig-vlan.yang
* openconfig-yang-types.yang

#### Other Models Added

* CISCO-CEF-TC.yang
* CISCO-FIREWALL-TC.yang
* CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN.yang
* CISCO-SMI.yang
* CISCO-ST-TC.yang
* CISCO-TC.yang
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
* cisco-self-mgmt.yang
* cisco-semver-internal.yang
* cisco-semver.yang
* cisco-smart-license-errors.yang
* cisco-smart-license.yang
* cisco-storm-control.yang
* cisco-xe-ietf-event-notifications-deviation.yang
* cisco-xe-ietf-ip-deviation.yang
* cisco-xe-ietf-ipv4-unicast-routing-deviation.yang
* cisco-xe-ietf-ipv6-unicast-routing-deviation.yang
* cisco-xe-ietf-ospf-deviation.yang
* cisco-xe-ietf-routing-deviation.yang
* cisco-xe-ietf-yang-push-deviation.yang
* cisco-xe-ietf-yang-push-ext.yang
* cisco-xe-openconfig-acl-deviation.yang
* cisco-xe-openconfig-acl-ext.yang
* cisco-xe-openconfig-aft-deviation.yang
* cisco-xe-openconfig-bgp-deviation.yang
* cisco-xe-openconfig-bgp-policy-deviation.yang
* cisco-xe-openconfig-if-ethernet-ext.yang
* cisco-xe-openconfig-if-ip-deviation.yang
* cisco-xe-openconfig-if-poe-deviation.yang
* cisco-xe-openconfig-interfaces-deviation.yang
* cisco-xe-openconfig-interfaces-ext.yang
* cisco-xe-openconfig-isis-deviation.yang
* cisco-xe-openconfig-lldp-deviation.yang
* cisco-xe-openconfig-mpls-deviation.yang
* cisco-xe-openconfig-network-instance-deviation.yang
* cisco-xe-openconfig-platform-ext.yang
* cisco-xe-openconfig-rib-bgp-ext.yang
* cisco-xe-openconfig-routing-policy-deviation.yang
* cisco-xe-openconfig-segment-routing-deviation.yang
* cisco-xe-openconfig-spanning-tree-deviation.yang
* cisco-xe-openconfig-spanning-tree-ext.yang
* cisco-xe-openconfig-system-ext.yang
* cisco-xe-openconfig-system-management-deviation.yang
* cisco-xe-openconfig-vlan-ext.yang
* cisco-xe-routing-asr-openconfig-if-ethernet-deviation.yang
* cisco-xe-routing-csr-openconfig-platform-deviation.yang
* cisco-xe-routing-isr-openconfig-if-ethernet-deviation.yang
* cisco-xe-routing-openconfig-system-deviation.yang
* cisco-xe-routing-openconfig-system-management-deviation.yang
* cisco-xe-routing-openconfig-vlan-deviation.yang
* cisco-xe-switching-openconfig-vlan-deviation.yang
* ietf-diffserv-action.yang
* ietf-diffserv-classifier.yang
* ietf-diffserv-policy.yang
* ietf-diffserv-target.yang
* ietf-event-notifications.yang
* ietf-inet-types.yang
* ietf-interfaces-ext.yang
* ietf-interfaces.yang
* ietf-ip.yang
* ietf-ipv4-unicast-routing.yang
* ietf-ipv6-unicast-routing.yang
* ietf-key-chain.yang
* ietf-netconf-acm.yang
* ietf-netconf-monitoring.yang
* ietf-netconf-notifications.yang
* ietf-netconf-with-defaults.yang
* ietf-netconf.yang
* ietf-ospf.yang
* ietf-restconf-monitoring-ann.yang
* ietf-restconf-monitoring.yang
* ietf-restconf.yang
* ietf-routing.yang
* ietf-yang-library.yang
* ietf-yang-patch-ann.yang
* ietf-yang-patch.yang
* ietf-yang-push.yang
* ietf-yang-smiv2.yang
* ietf-yang-types.yang
* tailf-cli-extensions.yang
* tailf-common-monitoring.yang
* tailf-common-query.yang
* tailf-common.yang
* tailf-confd-monitoring.yang
* tailf-meta-extensions.yang
* tailf-netconf-inactive.yang
* tailf-netconf-monitoring.yang
* tailf-netconf-query.yang
* tailf-netconf-transactions.yang
* tailf-rest-error.yang
* tailf-rest-query.yang
* tailf-xsd-types.yang
* DIFFSERV-DSCP-TC.yang
* ETHER-WIS.yang
* HCNUM-TC.yang
* RFC-1212.yang
* RFC-1215.yang
* RFC1155-SMI.yang
* SNMPv2-TC.yang
* common-mpls-static-devs.yang
* common-mpls-static.yang
* common-mpls-types.yang
* confd_dyncfg.yang
* iana-crypt-hash.yang
* iana-if-type.yang
* nvo-devs.yang
* nvo.yang
* pim.yang
* policy-attr.yang
* policy-types.yang

### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint```flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


