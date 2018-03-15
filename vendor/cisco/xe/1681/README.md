## YANG Models and Platform Capabilities for Cisco IOS XE 16.8.1

This directory contains the YANG models supported by IOS XE 16.8.1:

* IOS XE native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms:

* ASR 1000
* CSR 1000v/ISRv
* ISR 1000 and ISR 4000
* ASR900 RSP2/RSP3, ASR920 and NCS4200
* Catalyst 3650 and 3850
* Catalyst 9300, 9400 and 9500

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:
#### ASR 1000
Capability Statement: [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
#### CSR 1000v
Capability Statement: [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
#### ISR 1000
Capability Statement: [isr1k-netconf-capability.xml](isr1k-netconf-capability.xml)
#### ISR 4000
Capability Statement: [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)
#### ASR900 RSP2/RSP3, ASR920 and NCS4200
Capability Statement: [asr920-netconf-capability.xml](asr920-netconf-capability.xml)
#### Catalyst 3650 and 3850
Capability Statement: [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)
#### Catalyst 9300
Capability Statement: [cat9300-netconf-capability.xml](cat9300-netconf-capability.xml)
#### Catalyst 9400
Capability Statement: [cat9400-netconf-capability.xml](cat9400-netconf-capability.xml)
#### Catalyst 9500
Capability Statement: [cat9500-netconf-capability.xml](cat9500-netconf-capability.xml)

### 16.8.1 Errata

Please note that the following models, while advertised by Cat9400, are not actually supported.

* openconfig-platform.yang
* openconfig-platform-types.yang

### Major Namespace and Model Changes In 16.8.1

16.8.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-avb.yang
* Cisco-IOS-XE-cellwan-oper.yang
* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-cellular.yang
* Cisco-IOS-XE-device-hardware-oper.yang
* Cisco-IOS-XE-dhcp-oper.yang
* Cisco-IOS-XE-diffserv-target-oper.yang
* Cisco-IOS-XE-eta.yang
* Cisco-IOS-XE-fib-oper.yang
* Cisco-IOS-XE-interfaces-oper.yang
* Cisco-IOS-XE-ipv6-oper.yang
* Cisco-IOS-XE-mvrp.yang
* Cisco-IOS-XE-nat-oper.yang
* Cisco-IOS-XE-ntp-oper.yang
* Cisco-IOS-XE-ospf-oper.yang
* Cisco-IOS-XE-ppp-oper.yang
* Cisco-IOS-XE-ptp.yang
* Cisco-IOS-XE-stackwise-virtual.yang
* Cisco-IOS-XE-spanning-tree-oper.yang
* Cisco-IOS-XE-tcam-oper.yang
* Cisco-IOS-XE-vlan-oper.yang
* Cisco-IOS-XE-vrrp-oper.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-bgp-oper.yang
* Cisco-IOS-XE-bgp-router-oper.yang
* Cisco-IOS-XE-cdp.yang
* Cisco-IOS-XE-cdp-oper.yang
* Cisco-IOS-XE-cfm-oper.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-dot1x.yang
* Cisco-IOS-XE-eem.yang
* Cisco-IOS-XE-eigrp.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-environment-oper.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-flow-monitor-oper.yang
* Cisco-IOS-XE-http.yang
* Cisco-IOS-XE-icmp.yang
* Cisco-IOS-XE-igmp.yang
* Cisco-IOS-XE-iwanfabric.yang
* Cisco-IOS-XE-interface-common.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ip-sla-oper.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-license.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-lldp.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper.yang
* Cisco-IOS-XE-mka.yang
* Cisco-IOS-XE-mmode.yang
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
* Cisco-IOS-XE-parser.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-power.yang
* Cisco-IOS-XE-ppp.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-rsvp.yang
* Cisco-IOS-XE-sanet.yang
* Cisco-IOS-XE-service-routing.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-udld.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-umbrella.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-vservice.yang
* Cisco-IOS-XE-virtual-service-oper.yang
* Cisco-IOS-XE-wccp.yang
* Cisco-IOS-XE-template.yang
* Cisco-IOS-XE-zone.yang

#### IETF Models Added

* ietf-netconf-acm.yang

#### Openconfig Models Added

* openconfig-aaa.yang
* openconfig-rib-bgp-ext.yang
* openconfig-rib-bgp-types.yang
* openconfig-system.yang
* openconfig-system-logging.yang
* openconfig-system-terminal.yang
* openconfig-procmon.yang
* openconfig-spanning-tree.yang
* openconfig-spanning-tree-types.yang
* openconfig-transport-line-common.yang
* openconfig-transport-types.yang

#### OpenConfig Models Modified

* openconfig-acl.yang
* openconfig-packet-match.yang
* openconfig-if-ethernet.yang
* openconfig-network-instance.yang
* openconfig-extensions.yang
* openconfig-types.yang
* openconfig-packet-match-types.yang
* openconfig-inet-types.yang
* openconfig-yang-types.yang
* openconfig-vlan.yang
* openconfig-platform.yang
* openconfig-platform-types.yang

#### OpenConfig Deviations Added

* Cisco-XE-openconfig-bgp-policy-deviation.yang
* Cisco-XE-openconfig-bgp-deviation.yang
* Cisco-XE-openconfig-spanning-tree-deviation.yang
* Cisco-XE-openconfig-openflow-deviation.yang
* Cisco-XE-ietf-event-notifications-deviation.yang
* Cisco-XE-ietf-yang-push-deviation.yang

#### OpenConfig Extensions Added

* cisco-xe-openconfig-rib-bgp-ext.yang
* cisco-xe-openconfig-spanning-tree-ext.yang
* cisco-xe-openconfig-vlan-ext.yang
* cisco-xe-openconfig-platform-ext.yang
* cisco-xe-ietf-yang-push-ext.yang
	 
### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.
