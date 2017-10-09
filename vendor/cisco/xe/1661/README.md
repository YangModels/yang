## YANG Models and Platform Capabilities for Cisco IOS-XE 16.6.1

This directory contains the [MIBS](MIBS) subdirectory and YANG models supported by IOS-XE 16.6.1:

* Native models, unique to IOS-XE platforms
* Common Cisco models
* Platform deviations to models
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)
* Copies of **draft** IETF models implemented by IOS-XE 16.6.1 (some with modifications)
* All IETF, OpenConfig and tail-f models (without modification) that are supported by IOS-XE platforms 

The schemas here may also be retrieved from devices running IOS-XE 16.6.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of [RFC 6022](https://tools.ietf.org/html/rfc6022). Models listed in this repository are supported by following IOS-XE platforms:

* Catalyst 3850 
* Catalyst 3650
* ASR1000
* CSR1000V/ISRv
* ISR4000
* Catalyst 9300
* Catalyst 9500

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:

* [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)
* [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
* [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
* [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)
* [cat9300-netconf-capability.xml](cat9300-netconf-capability.xml)
* [cat9500-netconf-capability.xml](cat9500-netconf-capability.xml)

### 16.6.1 Errata

Please note that the following models, while advertised by several devices, are not actually supported:

* `cisco-qos-common.yang`
* `openconfig-lacp`
* `openconfig-lldp`
* `openconfig-optical-amplifier`
* `openconfig-platform-transceiver.yang`
* `openconfig-terminal-device.yang`
* `openconfig-wavelength-router`

The XML capability files exhibiting errors are:

* [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)
* [cat9300-netconf-capability.xml](cat9300-netconf-capability.xml)
* [cat9500-netconf-capability.xml](cat9500-netconf-capability.xml)


### 16.6.1 Major Model Changes

#### 16.6.1 Model changes includes addition of Openconfig Models, new native models and existing native model updation.

#### List of Openconfig models added in 16.6.1:

* openconfig-interfaces
* openconfig-routing-policy
* openconfig-acl
* openconfig-vlan
* openconfig-network-instance
* openconfig-platform
 
#### List of Native models updated in 16.6.1:

* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-acl.yang 
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-cef.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-eem.yang
* Cisco-IOS-XE-eigrp.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-lldp.yang
* Cisco-IOS-XE-logging.yang
* Cisco-IOS-XE-mmode.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-nd.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-service-routing.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-template.yang
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-vlan.yang

#### List of new native models added in 16.6.1:

* Cisco-IOS-XE-mmode.yang
* Cisco-IOS-XE-template.yang

#### List of models that requires ODM configuration in 16.6.1:

* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-cfm-oper.yang
* Cisco-IOS-XE-mpls-fwd-oper.yang
* Cisco-IOS-XE-mpls-ldp.yang
* Cisco-IOS-XE-virtual-service-oper.yang
* cisco-bridge-domain.yang
* common-mpls-static.yang
* ietf-diffserv-target.yang
* ietf-ospf.yang
* ietf-routing.yang
	 
### Compliance With "pyang --lint"

The native and some common YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


## Platform Differences

Each supported platform advertises NETCONF capabilities during NETCONF session establishment. 

#### Catalyst 3850, 3650

NETCONF capability statement: [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)

Exceptions to capability statement:

1. Common models not supported by cat3k platforms:

  - [nvo.yang](nvo.yang)
  - [nvo-devs.yang](nvo-devs.yang)

#### Catalyst 9300
NETCONF capability statement: [cat9300-netconf-capability.xml](cat9300-netconf-capability.xml)
#### Catalyst 9500
NETCONF capability statement: [cat9500-netconf-capability.xml](cat9500-netconf-capability.xml)
#### ASR1000
NETCONF capability statement: [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
#### CSR1000V
NETCONF capability statement: [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
#### ISR4000
NETCONF capability statement: [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)

