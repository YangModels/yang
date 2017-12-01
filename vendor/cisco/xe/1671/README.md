## YANG Models and Platform Capabilities for Cisco IOS XE 16.7.1

This directory contains the [MIBS](MIBS) subdirectory and YANG models supported by IOS XE 16.7.1:

* Models unique to IOS XE platforms
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)
* IETF, OpenConfig and tail-f models (and deviations) 

The schemas here may also be retrieved from devices running IOS XE 16.7.1 by using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. For RESTCONF we can do a "get" on the schema leaf of ietf-yang-library.yang model, which provides the list of URL's from which the schemas can be dowloaded. Models listed in this repository are supported by following IOS XE platforms:

* ASR1000
* CSR1000V/ISRv
* ISR4000
* ASR900, RSP2/RSP3, ASR920 and NCS4200

** NOTE: IOS XE 16.7.1 is not supported on Catalyst switching platforms.**

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:
#### ASR1000
NETCONF capability Statement: [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
#### CSR1000
NETCONF capability Statement: [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
#### ISR4000
NETCONF capability Statement: [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)
#### ASR900, ASR920, RSP2/RSP3 and NCS4200
NETCONF capability Statement: [asr920-netconf-capability.xml](asr920-netconf-capability.xml)

### Major Namespace And Model Changes In 16.7.1

16.7.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### IETF Models Added

* ietf-yang-push.yang
* ietf-event-notifications.yang

#### Native Models Added

* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-iwanfabric.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-mdt-cfg.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper.yang
* Cisco-IOS-XE-stackwise-virtual.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-cdp.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-device-sensor.yang
* Cisco-IOS-XE-device-tracking.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-dot1x.yang
* Cisco-IOS-XE-eem.yang
* Cisco-IOS-XE-eigrp.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-icmp.yang
* Cisco-IOS-XE-igmp.yang
* Cisco-IOS-XE-interface-common.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-license.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-lldp.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mka.yang
* Cisco-IOS-XE-mmode.yang
* Cisco-IOS-XE-mpls.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-nd.yang
* Cisco-IOS-XE-object-group.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-parser.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-power.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-rpc.yang
* Cisco-IOS-XE-rsvp.yang
* Cisco-IOS-XE-sanet.yang
* Cisco-IOS-XE-service-insertion.yang
* Cisco-IOS-XE-service-routing.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-udld.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-vservice.yang
* Cisco-IOS-XE-zone.yang

#### Models Requiring Operational Data manager (ODM) configuration

* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-cfm-oper.yang
* Cisco-IOS-XE-mpls-fwd-oper.yang
* Cisco-IOS-XE-mpls-ldp.yang
* Cisco-IOS-XE-virtual-service-oper.yang
* cisco-bridge-domain.yang
* common-mpls-static.yang
* ietf-ospf.yang
* ietf-routing.yang
	 
### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, the following models have been changed with no corresponding update to the revision statement:

* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-device-tracking.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-parser.yang
* Cisco-IOS-XE-service-insertion.yang
* Cisco-IOS-XE-vlan.yang

## Platform Differences

Each supported platform advertises NETCONF capabilities during NETCONF session establishment. 

### Exceptions to capability statement:

Below is the list of operational models advertised in the capability of ASR920, ASR900, RSP2/RSP3 and NCS4200 but not supported.

* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-cdp-oper.yang
* Cisco-IOS-XE-diffserv-target-oper.yang
* Cisco-IOS-XE-mpls-fwd-oper.yang
* Cisco-IOS-XE-platform-oper.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-virtual-service-oper.yang
* Cisco-bridge-domain.yang
* Cisco-IOS-XE-mpls-ldp.yang
* Cisco-IOS-XE-bridge-domain.yang
* ietf-interfaces.yang
* ietf-routing.yang
* common-mpls-static.yang
* ietf-ospf.yang
* ietf-diffserv-target.yang
