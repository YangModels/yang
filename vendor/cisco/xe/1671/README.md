## YANG Models and Platform Capabilities for Cisco IOS-XE 16.7

This directory contains the [MIBS](MIBS) subdirectory and YANG models supported by IOS-XE 16.7:

* Native models, unique to IOS-XE platforms
* Common Cisco models
* Platform deviations to models
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)
* Copies of **draft** IETF models implemented by IOS-XE 16.7 (some with modifications)
* All IETF, OpenConfig and tail-f models (without modification) that are supported by IOS-XE platforms 

The schemas here may also be retrieved from devices running IOS-XE 16.7 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of [RFC 6022](https://tools.ietf.org/html/rfc6022). Models listed in this repository are supported by following IOS-XE platforms:

* ASR1000
* CSR1000V/ISRv
* ISR4000
* ASR920/SPAG

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:

* [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
* [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
* [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)
* [asr920-netconf-capability.xml](asr920-netconf-capability.xml)

### Major namespace and model changes in 16.7

### 16.7 Model Changes

#### 16.7 Model changes includes addition of ietf models, new native models and existing native model updation.

#### List of ietf models added in 16.7:

* ietf-yang-push.yang
* ietf-event-notifications.yang
 
#### List of new native models added in 16.7:

* Cisco-IOS-XE-common-types.yang
* Cisco-IOS-XE-iwanfabric.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-mdt-cfg.yang
* Cisco-IOS-XE-mdt-common-defs.yang
* Cisco-IOS-XE-mdt-oper.yang

#### Other new models added:

* Cisco-xe-ietf-event-notifications-deviation.yang
* Cisco-xe-ietf-yang-push-deviation.yang
* Cisco-xe-ietf-yang-push-ext.yang

#### List of models that requires ODM configuration in 16.7:

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

The native and some common YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


## Platform Differences

Each supported platform advertises NETCONF capabilities during NETCONF session establishment. 

### Exceptions to capability statement:

Below are the list of CODM models advertised in the capability of ASR920, but not supported.

* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-cdp-oper.yang
* Cisco-IOS-XE-diffserv-target-oper.yang
* Cisco-IOS-XE-mpls-fwd-oper.yang
* Cisco-IOS-XE-platform-oper.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-virtual-service-oper.yang
* Cisco-IOS-XE-bridge-domain.yang
* Cisco-IOS-XE-mpls-ldp.yang
* ietf-interfaces.yang
* ietf-routing.yang
* Common-mpls-static.yang
* ietf-diffserv-target.yang
* ietf-ospf.yang

#### ASR1000
NETCONF capability statement: [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
#### CSR1000V
NETCONF capability statement: [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
#### ISR4000
NETCONF capability statement: [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)
#### ASR920
NETCONF capability statement: [asr920-netconf-capability.xml](asr920-etconf-capability.xml)
