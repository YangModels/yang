## YANG Models for Cisco IOS 16.3.1 

The YANG files in this directory contains native, common, deviation and MIB-based YANG models supported by IOS 16.3.1 releases. The schemas here may also be retrieved from devices running IOS 16.3.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022. Models listed in this repository are supported by following IOS XE platforms:

	- Catalyst 3850 
	- Catalyst 3650
	- ASR1000
	- CSR1000V
	- ISR4000

Model content may differ based on platform capability.


### Compliance With "pyang --lint"

The native and some common YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


## Platform Differences:

Each supported platform advertises netconf capability during netconf session establishment. 

#### Catalyst 3850, 3650

Netconf capability statement for cat3k devices: [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)

Excpetions to capability statement:

1. Common models not supported by cat3k platforms:

	- nvo.yang
	- nvo-devs.yang

2. Additional deviation module for cat3k platform

	- cisco-xe-native-cat3k-deviation.yang

#### ASR1000, CSR1000V, ISR4000

Netconf capability statement for cat3k devices: [router-netconf-capability.xml](router-netconf-capability.xml)

Excpetions to capability statement:

1. Additional deviation module for routing platforms:

	- cisco-xe-native-router-deviation.yang

## Provisional Content

TBD

