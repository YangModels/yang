## YANG Models and Platform Capabilities for Cisco IOS XE 16.7

This directory contains the [MIBS](MIBS) subdirectory and YANG models supported by IOS XE 16.7:

* Models unique to IOS XE platforms
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)
* IETF,OpenConfig and tailf-f models(and deviations) 

The schemas here may also be retrieved from devices running IOS XE 16.7 by using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. For Restconf we can do a "get" on the schema leaf of ietf-yang-library.yang model,which provides the list of URL's from which the schemas can be dowloaded. Models listed in this repository are supported by following IOS XE platforms:

* ASR1000
* CSR1000V/ISRv
* ISR4000
* ASR900 RSP2/RSP3 and ASR920

#### NOTE: IOS XE is not supported on Catalyst switching platforms.

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:
#### ASR1000
Netconf capability Statement: [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
#### CSR1000
Netconf capability Statement: [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
#### ISR4000
Netconf capability Statement: [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)
#### ASR900/ASR920 RSP2/RSP3 
Netconf capability Statement: [asr920-netconf-capability.xml](asr920-netconf-capability.xml)

### Major namespace and model changes in 16.7

### 16.7 Model Changes

#### 16.7 Model changes includes addition of ietf models, new native models and existing native model updation.

#### ietf models added in 16.7:

* ietf-yang-push.yang
* ietf-event-notifications.yang
 
#### Native models added in 16.7:

* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-iwanfabric.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-mdt-cfg.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper.yang

#### Models that requires ODM configuration in 16.7:

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

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


## Platform Differences

Each supported platform advertises NETCONF capabilities during NETCONF session establishment. 

### Exceptions to capability statement:

Below is the list of operational models advertised in the capability of ASR920/ASR900 RSP2/RSP3, but not supported.

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
