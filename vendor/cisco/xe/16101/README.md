## YANG Models and Platform Capabilities for Cisco IOS XE 16.10.1

This directory contains the YANG models supported by IOS XE 16.10.1:

* IOS XE native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms:

* ASR 900, 920 and 1000
* CSR 1000v/ISRv
* Catalyst 9300, 9400, 9500 and 9800
* CBR-8
* IR 1101
* ISR 1000 and 4000
* NCS520 and NCS4200

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:
#### ASR 900 RSP2/RSP3, ASR920, NCS520 and NCS4200
Capability Statement: [capability-asr900.xml](capability-asr900.xml)
#### ASR 1000
Capability Statement: [capability-asr1k.xml](capability-asr1k.xml)
#### Catalyst 9300
Capability Statement: [capability-cat9300.xml](capability-cat9300.xml)
#### Catalyst 9400
Capability Statement: [capability-cat9400.xml](capability-cat9400.xml)
#### Catalyst 9500
Capability Statement: [capability-cat9500.xml](capability-cat9500.xml)
#### Catalyst 9800
Capability Statement: [capability-wireless.xml](capability-wireless.xml)
#### CBR-8
Capability Statement: [capability-cbr.xml](capability-cbr.xml)
#### CSR1000v/ISRv
Capability Statement: [capability-csr1k.xml](capability-csr1k.xml)
#### IR 1101
Capability Statement: [capability-ir1101.xml](capability-ir1101.xml)
#### ISR 1000
Capability Statement: [capability-isr1k.xml](capability-isr1k.xml)
#### ISR 4000
Capability Statement: [capability-isr4k.xml](capability-isr4k.xml)


### Major Namespace and Model Changes In 16.10.1

16.10.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-app-hosting-cfg.yang
* Cisco-IOS-XE-wireless-access-point-oper.yang
* Cisco-IOS-XE-wireless-cts-sxp-cfg.yang
* Cisco-IOS-XE-wireless-cts-sxp-oper.yang
* Cisco-IOS-XE-wireless-fabric-cfg.yang
* Cisco-IOS-XE-wireless-fqdn-oper.yang
* Cisco-IOS-XE-wireless-hyperlocation-oper.yang
* Cisco-IOS-XE-wireless-lisp-agent-oper.yang
* Cisco-IOS-XE-wireless-location-cfg.yang
* Cisco-IOS-XE-wireless-location-oper.yang
* Cisco-IOS-XE-wireless-mcast-oper.yang
* Cisco-IOS-XE-wireless-mobility-cfg.yang
* Cisco-IOS-XE-wireless-mobility-oper.yang
* Cisco-IOS-XE-wireless-mobility-types.yang
* Cisco-IOS-XE-wireless-nmsp-oper.yang
* Cisco-IOS-XE-wireless-rf-cfg.yang
* Cisco-IOS-XE-wireless-rf-profile-oper.yang
* Cisco-IOS-XE-wireless-rogue-cfg.yang
* Cisco-IOS-XE-wireless-rogue-oper.yang
* Cisco-IOS-XE-wireless-rogue-types.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-arp-oper.yang
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp-route-oper.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-bridge-domain.yang
* Cisco-IOS-XE-card.yang
* Cisco-IOS-XE-cef.yang
* Cisco-IOS-XE-cellular.yang
* Cisco-IOS-XE-cellwan-oper.yang
* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-controller-vdsl-oper.yang
* Cisco-IOS-XE-controller.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-device-hardware-oper.yang
* Cisco-IOS-XE-dhcp-oper.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-eta.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-fw-oper.yang
* Cisco-IOS-XE-igmp.yang
* Cisco-IOS-XE-interface-common.yang
* Cisco-IOS-XE-interfaces-oper.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ios-events-oper.yang
* Cisco-IOS-XE-ip-sla-oper.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isis.yang
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
* Cisco-IOS-XE-mpls.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-nd.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-object-group.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-otv.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-ppp.yang
* Cisco-IOS-XE-qos.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-segment-routing.yang
* Cisco-IOS-XE-service-insertion.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-umbrella.yang
* Cisco-IOS-XE-utd-oper.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-voice.yang
* Cisco-IOS-XE-vrrp.yang
* Cisco-IOS-XE-vservice.yang
* Cisco-IOS-XE-zone.yang


#### IETF model modified

* cisco-xe-ietf-yang-push-ext.yang


#### OpenConfig Models Modified

* cisco-xe-openconfig-bgp-deviation.yang
* cisco-xe-openconfig-bgp-policy-deviation.yang
* cisco-xe-openconfig-if-ethernet-deviation.yang
* cisco-xe-openconfig-interfaces-deviation.yang
* cisco-xe-openconfig-interfaces-ext.yang
* cisco-xe-openconfig-platform-deviation.yang
* cisco-xe-openconfig-routing-policy-deviation.yang
* cisco-xe-openconfig-vlan-deviation.yang

#### OpenConfig Deviations Added

* cisco-xe-openconfig-lldp-deviation.yang

#### Experimental YANG Models

Pay special attention to the following YANG models, which we expect to finalize soon:

* Cisco-IOS-XE-app-hosting-oper.yang
* Cisco-IOS-XE-dialer.yang
* Cisco-IOS-XE-gir-oper.yang
* Cisco-IOS-XE-ha-oper.yang
* Cisco-IOS-XE-mlppp-oper.yang
* Cisco-IOS-XE-pnp.yang
* Cisco-IOS-XE-pppoe.yang
* Cisco-IOS-XE-serial.yang
* Cisco-IOS-XE-stack-oper.yang
* Cisco-IOS-XE-voice-oper.yang
* Cisco-IOS-XE-wsa-types.yang
* Cisco-IOS-XE-wireless-ap-cfg.yang
* Cisco-IOS-XE-wireless-ap-types.yang
* Cisco-IOS-XE-wireless-apf-cfg.yang
* Cisco-IOS-XE-wireless-client-oper.yang
* Cisco-IOS-XE-wireless-client-types.yang
* Cisco-IOS-XE-wireless-dot11-cfg.yang
* Cisco-IOS-XE-wireless-enum-types.yang
* Cisco-IOS-XE-wireless-events-oper.yang
* Cisco-IOS-XE-wireless-flex-cfg.yang
* Cisco-IOS-XE-wireless-fqdn-cfg.yang
* Cisco-IOS-XE-wireless-general-cfg.yang
* Cisco-IOS-XE-wireless-mesh-cfg.yang
* Cisco-IOS-XE-wireless-mesh-oper.yang
* Cisco-IOS-XE-wireless-mstream-cfg.yang
* Cisco-IOS-XE-wireless-rfid-cfg.yang
* Cisco-IOS-XE-wireless-rfid-oper.yang
* Cisco-IOS-XE-wireless-rrm-cfg.yang
* Cisco-IOS-XE-wireless-rrm-oper.yang
* Cisco-IOS-XE-wireless-rrm-types.yang
* Cisco-IOS-XE-wireless-security-cfg.yang
* Cisco-IOS-XE-wireless-site-cfg.yang
* Cisco-IOS-XE-wireless-types.yang
* Cisco-IOS-XE-wireless-wlan-cfg.yang

These experimental YANG models are in the early status of design and are likely to change.

#### 16.10.1 Errata

The below models, while advertised in the capabilities, are not supported on ASR900 RSP2/RSP3, ASR920, NCS520 and NCS4200.

* Cisco-IOS-XE-cellwan-oper.yang
* Cisco-IOS-XE-flow-monitor-oper.yang
* Cisco-IOS-XE-iwanfabric.yang
* Cisco-IOS-XE-utd-common-oper
* Cisco-IOS-XE-utd-oper

"Cisco-IOS-XE-atm.yang" model, while advertised in the capability, is not supported on CSR1000v/ISRv

"Cisco-IOS-XE-im-events-oper.yang" model is not supported on any of the platforms.

 
### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint```flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.

### Cross-Platform Compatibility Issues

IOS-XE 16.10.1 has small number of models that have variations in definition across platforms. The details of the models and platforms impacted can be found in [this document](MODEL_ISSUES.md)
