## YANG Models and Platform Capabilities for Cisco IOS-XE 16.4.1

This directory contains the [MIBS](MIBS) subdirectory contain YANG models supported by IOS-XE 16.4.1:

* Native models, unique to IOS-XE platforms
* Common Cisco models
* Platform deviations to models
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)
* Copies of **draft** IETF models implemented by IOS-XE 16.4.1 (some with modifications)

The schemas here may also be retrieved from devices running IOS-XE 16.4.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of [RFC 6022](https://tools.ietf.org/html/rfc6022). Models listed in this repository are supported by following IOS-XE platforms:

* Catalyst 3850 
* Catalyst 3650
* ASR1000
* CSR1000V
* ISR4000

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:

* [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)
* [router-netconf-capability.xml](router-netconf-capability.xml)

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

#### ASR1000, CSR1000V, ISR4000

NETCONF capability statement: [router-netconf-capability.xml](router-netconf-capability.xml)


