## YANG Models and Platform Capabilities for Cisco IOS XE 16.9.3

This directory contains the YANG models supported by IOS XE 16.9.3:

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
Capability Statement: [capability-asr1k.xml](capability-asr1k.xml)
#### CSR 1000v
Capability Statement: [capability-csr1k.xml](capability-csr1k.xml)
#### ISR 1000
Capability Statement: [capability-isr1k.xml](capability-isr1k.xml)
#### ISR 4000
Capability Statement: [capability-isr4k.xml](capability-isr4k.xml)
#### ASR900 RSP2/RSP3, ASR920 and NCS4200
Capability Statement: [capability-asr900.xml](capability-asr900.xml)
#### Catalyst 3650 and 3850
Capability Statement: [capability-cat3k.xml](capability-cat3k.xml)
#### Catalyst 9300
Capability Statement: [capability-cat9300.xml](capability-cat9300.xml)
#### Catalyst 9400
Capability Statement: [capability-cat9400.xml](capability-cat9400.xml)
#### Catalyst 9500
Capability Statement: [capability-cat9500.xml](capability-cat9500.xml)
#### CBR-8
Capability Statement: [capability-cbr.xml](capability-cbr.xml)

### Major Model Changes In 16.9.3

16.9.3 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-pnp.yang

#### Native Models Modified

* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-aaa-oper.yang
* Cisco-IOS-XE-aaa.yang 
* Cisco-IOS-XE-acl.yang 
* Cisco-IOS-XE-arp.yang
* Cisco-IOS-XE-atm.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang 
* Cisco-IOS-XE-call-home.yang 
* Cisco-IOS-XE-cellwan-oper.yang 
* Cisco-IOS-XE-controller.yang 
* Cisco-IOS-XE-crypto.yang 
* Cisco-IOS-XE-device-tracking.yang 
* Cisco-IOS-XE-dhcp.yang 
* Cisco-IOS-XE-dot1x.yang 
* Cisco-IOS-XE-ethernet.yang 
* Cisco-IOS-XE-interfaces-oper.yang 
* Cisco-IOS-XE-interfaces.yang 
* Cisco-IOS-XE-ip.yang 
* Cisco-IOS-XE-ipv6.yang 
* Cisco-IOS-XE-lisp-oper.yang 
* Cisco-IOS-XE-logging.yang 
* Cisco-IOS-XE-nat.yang 
* Cisco-IOS-XE-native.yang 
* Cisco-IOS-XE-ospf.yang 
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-rip.yang 
* Cisco-IOS-XE-route-map.yang 
* Cisco-IOS-XE-switch.yang 
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-types.yang 
* Cisco-IOS-XE-utd.yang 
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-vrrp.yang 

#### Openconfig Models Modified

* cisco-xe-openconfig-bgp-deviation.yang 
* cisco-xe-openconfig-bgp-policy-deviation.yang 
* cisco-xe-openconfig-routing-policy-deviation.yang 
* cisco-xe-openconfig-vlan-deviation.yang 

#### Other Models Modified

* cisco-ia.yang 
* cisco-routing-ext.yang 

#### Errata

The Cisco-IOS-XE-pnp.yang model is advertised in all the capabilities but should be considered experimental until IOS XE 17.1.
 
### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.





