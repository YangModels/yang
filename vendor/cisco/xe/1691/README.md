## YANG Models and Platform Capabilities for Cisco IOS XE 16.9.1

This directory contains the YANG models supported by IOS XE 16.9.1:

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
* CBR-8

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
#### CBR-8
Capability Statement: [cbr-netconf-capability.xml](cbr-netconf-capability.xml)

### Major Namespace and Model Changes In 16.9.1

16.9.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-arp-oper.yang
* Cisco-IOS-XE-boot-integrity-oper.yang
* Cisco-IOS-XE-breakout-port-oper.yang
* Cisco-IOS-XE-bridge-oper.yang
* Cisco-IOS-XE-controller-vdsl-oper.yang
* Cisco-IOS-XE-event-history-types.yang
* Cisco-IOS-XE-fw-oper.yang
* Cisco-IOS-XE-ios-common-oper.yang
* Cisco-IOS-XE-ios-events-oper.yang
* Cisco-IOS-XE-linecard-oper.yang
* Cisco-IOS-XE-mpls-forwarding-oper.yang
* Cisco-IOS-XE-nam.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-transceiver-oper.yang
* Cisco-IOS-XE-utd-common-oper.yang
* Cisco-IOS-XE-utd-oper.yang
* Cisco-IOS-XE-virtual-service-cfg.yang
* Cisco-IOS-XE-vrrp.yang



#### Native Models Modified 

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-card.yang
* Cisco-IOS-XE-cellwan-oper.yang
* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-controller.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-device-tracking.yang
* Cisco-IOS-XE-dhcp-oper.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-dot1x.yang
* Cisco-IOS-XE-eem.yang
* Cisco-IOS-XE-eigrp.yang
* Cisco-IOS-XE-eta.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-fib-oper.yang
* Cisco-IOS-XE-http.yang
* Cisco-IOS-XE-interface-common.yang
* Cisco-IOS-XE-interfaces-oper.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-mdt-cfg.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper.yang
* Cisco-IOS-XE-mld.yang
* Cisco-IOS-XE-mmode.yang
* Cisco-IOS-XE-mpls.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat-oper.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-ntp-oper.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-ospf-oper.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-parser.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-ppp-oper.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-umbrella.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-virtual-service-oper.yang
* Cisco-IOS-XE-vlan-oper.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-vrrp-oper.yang
* Cisco-IOS-XE-zone.yang

#### IETF Models Added

* ietf-yang-patch.yang

#### Openconfig Models Added

* openconfig-alarms.yang
* openconfig-if-poe.yang
* openconfig-platform-linecard.yang
* openconfig-platform-port.yang
* openconfig-platform-transceiver.yang


#### OpenConfig Models Modified

* openconfig-aaa-tacacs.yang
* openconfig-aaa-types.yang
* openconfig-if-aggregate.yang
* openconfig-if-ethernet.yang
* openconfig-if-ip-ext.yang
* openconfig-if-ip.yang
* openconfig-inet-types.yang
* openconfig-interfaces.yang
* openconfig-system.yang
* openconfig-transport-types.yang
* openconfig-types.yang

#### OpenConfig Deviations Added

* cisco-xe-openconfig-if-poe-deviation.yang
* cisco-xe-openconfig-interfaces-switching-deviation.yang
	 
### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.

### Known Issues

Below are some of the issues captured after running backward compatibility check with the previous release (16.8.1). These issues are being tracked and will be resolved in the upcoming release.

* Cisco-IOS-XE-ospf.yang:2001: error: XPath function "compare" is not defined in the XPath context.
* Cisco-IOS-XE-atm.yang:1: error: new revision 2017-02-07 is not newer than old revision 2017-02-07 (RFC 6020: 10, p2)
* Cisco-IOS-XE-common-types.yang:1: error: new revision 2017-12-01 is not newer than old revision 2017-12-01 (RFC 6020: 10, p2)
* Cisco-IOS-XE-device-tracking.yang:1: error: new revision 2017-06-07 is not newer than old revision 2017-06-07 (RFC 6020: 10, p2)
* Cisco-IOS-XE-dot1x.yang:1: error: new revision 2017-11-27 is not newer than old revision 2017-11-27 (RFC 6020: 10, p2)
* Cisco-IOS-XE-http.yang:1: error: new revision 2018-01-24 is not newer than old revision 2018-01-24 (RFC 6020: 10, p2)
* openconfig-aaa-tacacs.yang:1: error: new revision 2017-09-18 is not newer than old revision 2017-09-18 (RFC 6020: 10, p2)
* openconfig-aaa-types.yang:1: error: new revision 2017-09-18 is not newer than old revision 2017-09-18 (RFC 6020: 10, p2)
* openconfig-inet-types.yang:1: error: new revision 2017-08-24 is not newer than old revision 2017-08-24 (RFC 6020: 10, p2)
* cisco-routing-ext.yang:1: error: new revision 2016-07-09 is not newer than old revision 2016-07-09 (RFC 6020: 10, p2)
* cisco-xe-openconfig-bgp-deviation.yang:1: error: new revision 2017-05-24 is not newer than old revision 2017-05-24 (RFC 6020: 10, p2)
* cisco-xe-openconfig-bgp-policy-deviation.yang:1: error: new revision 2017-07-24 is not newer than old revision 2017-07-24 (RFC 6020: 10, p2)
* cisco-xe-openconfig-routing-policy-deviation.yang:1: error: new revision 2017-03-30 is not newer than old revision 2017-03-30 (RFC 6020: 10, p2)


