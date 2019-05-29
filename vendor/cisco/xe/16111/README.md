## YANG Models and Platform Capabilities for Cisco IOS XE 16.11.1

This directory contains the YANG models supported by IOS XE 16.11.1:

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
| IE 3x00 | [capability-ie3x00.xml](capability-ie4x00.xml) |
| ISR1K | [capability-isr1k.xml](capability-isr1k.xml) |
| ISR4K | [capability-isr4k.xml](capability-isr4k.xml) |


### Major Model Changes In 16.11.1

16.11.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-dapr.yang
* Cisco-IOS-XE-yang-interfaces-cfg.yang
* Cisco-IOS-XE-cable-diag-oper.yang
* Cisco-IOS-XE-wireless-mdns-oper.yang	

#### Native Models Modified 

* Cisco-IOS-XE-aaa-oper.yang 
* Cisco-IOS-XE-aaa.yang 
* Cisco-IOS-XE-acl-oper.yang 
* Cisco-IOS-XE-acl.yang 
* Cisco-IOS-XE-app-hosting-cfg.yang 
* Cisco-IOS-XE-app-hosting-oper.yang 
* Cisco-IOS-XE-atm.yang 
* Cisco-IOS-XE-bfd-oper.yang 
* Cisco-IOS-XE-bfd.yang 
* Cisco-IOS-XE-bgp-oper.yang 
* Cisco-IOS-XE-bgp-route-oper.yang 
* Cisco-IOS-XE-bgp.yang 
* Cisco-IOS-XE-breakout-port-oper.yang 
* Cisco-IOS-XE-bridge-domain.yang 
* Cisco-IOS-XE-bridge-oper.yang 
* Cisco-IOS-XE-call-home.yang 
* Cisco-IOS-XE-cdp.yang 
* Cisco-IOS-XE-cef.yang 
* Cisco-IOS-XE-cellwan-oper.yang 
* Cisco-IOS-XE-cfm-oper.yang 
* Cisco-IOS-XE-checkpoint-archive-oper.yang 
* Cisco-IOS-XE-coap.yang 
* Cisco-IOS-XE-common-types.yang 
* Cisco-IOS-XE-controller-vdsl-oper.yang 
* Cisco-IOS-XE-controller.yang 
* Cisco-IOS-XE-crypto.yang 
* Cisco-IOS-XE-cts.yang 
* Cisco-IOS-XE-device-hardware-oper.yang 
* Cisco-IOS-XE-device-tracking.yang 
* Cisco-IOS-XE-dhcp-oper.yang 
* Cisco-IOS-XE-dhcp.yang 
* Cisco-IOS-XE-diagnostics.yang 
* Cisco-IOS-XE-dot1x.yang 
* Cisco-IOS-XE-eem.yang 
* Cisco-IOS-XE-eigrp.yang 
* Cisco-IOS-XE-environment-oper.yang 
* Cisco-IOS-XE-eta.yang 
* Cisco-IOS-XE-ethernet.yang 
* Cisco-IOS-XE-event-history-types.yang 
* Cisco-IOS-XE-ezpm.yang 
* Cisco-IOS-XE-features.yang 
* Cisco-IOS-XE-fib-oper.yang 
* Cisco-IOS-XE-flow-monitor-oper.yang 
* Cisco-IOS-XE-flow.yang 
* Cisco-IOS-XE-fw-oper.yang 
* Cisco-IOS-XE-gir-oper.yang 
* Cisco-IOS-XE-ha-oper.yang 
* Cisco-IOS-XE-http.yang 
* Cisco-IOS-XE-icmp.yang 
* Cisco-IOS-XE-igmp.yang 
* Cisco-IOS-XE-interface-common.yang 
* Cisco-IOS-XE-interfaces-oper.yang 
* Cisco-IOS-XE-interfaces.yang 
* Cisco-IOS-XE-ios-common-oper.yang 
* Cisco-IOS-XE-ios-events-oper.yang 
* Cisco-IOS-XE-ip-sla-oper.yang 
* Cisco-IOS-XE-ip.yang 
* Cisco-IOS-XE-ipv6-oper.yang 
* Cisco-IOS-XE-ipv6.yang 
* Cisco-IOS-XE-isis.yang 
* Cisco-IOS-XE-iwanfabric.yang 
* Cisco-IOS-XE-l2vpn.yang 
* Cisco-IOS-XE-license.yang 
* Cisco-IOS-XE-line.yang 
* Cisco-IOS-XE-lisp-oper.yang 
* Cisco-IOS-XE-lisp.yang 
* Cisco-IOS-XE-lldp-oper.yang 
* Cisco-IOS-XE-lldp.yang 
* Cisco-IOS-XE-logging.yang 
* Cisco-IOS-XE-mdt-cfg.yang 
* Cisco-IOS-XE-mdt-common-defs.yang 
* Cisco-IOS-XE-mdt-oper.yang 
* Cisco-IOS-XE-mka.yang 
* Cisco-IOS-XE-mlppp-oper.yang 
* Cisco-IOS-XE-mpls-forwarding-oper.yang 
* Cisco-IOS-XE-mpls.yang 
* Cisco-IOS-XE-multicast.yang 
* Cisco-IOS-XE-mvrp.yang 
* Cisco-IOS-XE-nam.yang 
* Cisco-IOS-XE-nat-oper.yang 
* Cisco-IOS-XE-nat.yang 
* Cisco-IOS-XE-native.yang 
* Cisco-IOS-XE-nbar.yang 
* Cisco-IOS-XE-nd.yang 
* Cisco-IOS-XE-ntp-oper.yang 
* Cisco-IOS-XE-ntp.yang 
* Cisco-IOS-XE-object-group.yang 
* Cisco-IOS-XE-ospf-oper.yang 
* Cisco-IOS-XE-ospf.yang 
* Cisco-IOS-XE-ospfv3.yang 
* Cisco-IOS-XE-parser.yang 
* Cisco-IOS-XE-platform-oper.yang 
* Cisco-IOS-XE-platform-software-oper.yang 
* Cisco-IOS-XE-platform.yang 
* Cisco-IOS-XE-poe-oper.yang 
* Cisco-IOS-XE-policy.yang 
* Cisco-IOS-XE-power.yang 
* Cisco-IOS-XE-ppp-oper.yang 
* Cisco-IOS-XE-ppp.yang 
* Cisco-IOS-XE-pppoe.yang 
* Cisco-IOS-XE-process-cpu-oper.yang 
* Cisco-IOS-XE-qos.yang 
* Cisco-IOS-XE-rip.yang 
* Cisco-IOS-XE-route-map.yang 
* Cisco-IOS-XE-rpc.yang 
* Cisco-IOS-XE-rsvp.yang 
* Cisco-IOS-XE-sanet.yang 
* Cisco-IOS-XE-segment-routing.yang 
* Cisco-IOS-XE-serial.yang 
* Cisco-IOS-XE-service-insertion.yang 
* Cisco-IOS-XE-sla.yang 
* Cisco-IOS-XE-snmp.yang 
* Cisco-IOS-XE-spanning-tree.yang 
* Cisco-IOS-XE-switch.yang 
* Cisco-IOS-XE-template.yang 
* Cisco-IOS-XE-track.yang 
* Cisco-IOS-XE-transceiver-oper.yang 
* Cisco-IOS-XE-trustsec-oper.yang 
* Cisco-IOS-XE-tunnel.yang 
* Cisco-IOS-XE-types.yang 
* Cisco-IOS-XE-udld.yang 
* Cisco-IOS-XE-umbrella.yang 
* Cisco-IOS-XE-utd-common-oper.yang 
* Cisco-IOS-XE-utd-oper.yang 
* Cisco-IOS-XE-utd.yang 
* Cisco-IOS-XE-vlan-oper.yang 
* Cisco-IOS-XE-vlan.yang 
* Cisco-IOS-XE-voice-oper.yang 
* Cisco-IOS-XE-voice.yang 
* Cisco-IOS-XE-vrrp.yang 
* Cisco-IOS-XE-vservice.yang 
* Cisco-IOS-XE-vtp.yang 
* Cisco-IOS-XE-wccp.yang 
* Cisco-IOS-XE-wsa-types.yang 
* Cisco-IOS-XE-zone.yang 
* Cisco-IOS-XE-wireless-access-point-oper.yang
* Cisco-IOS-XE-wireless-ap-cfg.yang
* Cisco-IOS-XE-wireless-ap-types.yang
* Cisco-IOS-XE-wireless-apf-cfg.yang
* Cisco-IOS-XE-wireless-client-oper.yang
* Cisco-IOS-XE-wireless-client-types.yang
* Cisco-IOS-XE-wireless-cts-sxp-cfg.yang
* Cisco-IOS-XE-wireless-cts-sxp-oper.yang
* Cisco-IOS-XE-wireless-dot11-cfg.yang
* Cisco-IOS-XE-wireless-enum-types.yang
* Cisco-IOS-XE-wireless-events-oper.yang
* Cisco-IOS-XE-wireless-fabric-cfg.yang
* Cisco-IOS-XE-wireless-flex-cfg.yang
* Cisco-IOS-XE-wireless-general-cfg.yang
* Cisco-IOS-XE-wireless-hyperlocation-oper.yang
* Cisco-IOS-XE-wireless-lisp-agent-oper.yang
* Cisco-IOS-XE-wireless-location-cfg.yang
* Cisco-IOS-XE-wireless-location-oper.yang
* Cisco-IOS-XE-wireless-mcast-oper.yang
* Cisco-IOS-XE-wireless-mdns-oper.yang
* Cisco-IOS-XE-wireless-mesh-cfg.yang
* Cisco-IOS-XE-wireless-mesh-oper.yang
* Cisco-IOS-XE-wireless-mobility-cfg.yang
* Cisco-IOS-XE-wireless-mobility-oper.yang
* Cisco-IOS-XE-wireless-mobility-types.yang
* Cisco-IOS-XE-wireless-mstream-cfg.yang
* Cisco-IOS-XE-wireless-rf-cfg.yang
* Cisco-IOS-XE-wireless-rogue-cfg.yang
* Cisco-IOS-XE-wireless-rogue-oper.yang
* Cisco-IOS-XE-wireless-rogue-types.yang
* Cisco-IOS-XE-wireless-rrm-cfg.yang
* Cisco-IOS-XE-wireless-rrm-oper.yang
* Cisco-IOS-XE-wireless-rrm-types.yang
* Cisco-IOS-XE-wireless-security-cfg.yang
* Cisco-IOS-XE-wireless-site-cfg.yang
* Cisco-IOS-XE-wireless-types.yang
* Cisco-IOS-XE-wireless-wlan-cfg.yang

#### IETF model modified

* ietf-event-notifications.yang

#### OpenConfig Models Modified

* openconfig-if-ethernet.yang
* openconfig-platform.yang

#### Other Models Modified

* Cisco-ia.yang
* Cisco-routing-ext.yang
* Cisco-storm-control.yang
* Cisco-xe-ietf-event-notifications-deviation.yang
* Cisco-xe-ietf-yang-push-deviation.yang
* Cisco-xe-ietf-yang-push-ext.yang
* Cisco-xe-openconfig-if-poe-deviation.yang
* Cisco-xe-openconfig-platform-ext.yang
* Cisco-xe-openconfig-routing-policy-deviation.yang

#### Experimental YANG Models

* Cisco-IOS-XE-crypto-oper.yang
* Cisco-IOS-XE-crypto-pki-oper.yang
* Cisco-IOS-XE-dialer.yang
* Cisco-IOS-XE-eigrp-oper.yang
* Cisco-IOS-XE-ha-oper.yang
* Cisco-IOS-XE-gir-oper.yang
* Cisco-IOS-XE-qfp-stats.yang
* Cisco-IOS-XE-mdns-gateway.yang
* Cisco-IOS-XE-serial.yang
* Cisco-IOS-XE-stacking-oper.yang
* Cisco-IOS-XE-stack-oper
* Cisco-IOS-XE-site-manager.yang
* Cisco-IOS-XE-tunnel-oper.yang
* Cisco-IOS-XE-tunnel-types.yang
* Cisco-IOS-XE-umbrella-oper-dp.yang
* Cisco-IOS-XE-umbrella-oper.yang
* Cisco-IOS-XE-vrf-oper.yang (On Wireless and IOT platforms)
* Cisco-IOS-XE-voice-oper.yang
* Cisco-IOS-XE-vxlan.yang
* Cisco-IOS-XE-wsa-types.yang
* Cisco-IOS-XE-wireless-ble-mgmt-oper.yang
* Cisco-IOS-XE-wireless-general-oper.yang
* Cisco-IOS-XE-wireless-rlan-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-types.yang
* Cisco-IOS-XE-wireless-fqdn-cfg.yang
* Cisco-IOS-XE-wireless-nmsp-oper.yang
* Cisco-IOS-XE-wireless-rfid-cfg.yang
* Cisco-IOS-XE-wireless-rfid-oper.yang

These experimental YANG models are in the early status of design and are likely to change.

 
### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint```flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


