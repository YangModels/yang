## YANG Models and Platform Capabilities for Cisco IOS XE 16.11.1

This directory contains the YANG models supported by IOS XE 16.11.1:

* IOS XE native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms:

* ASR 900, 920 and 1000
* CSR 1000v/ISRv
* Catalyst 9200, 9300, 9400, 9500 and 9800
* CBR-8
* IR 1101 and IE3x00
* ISR 1000 and 4000
* NCS520 and NCS4200

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:
#### ASR 900 RSP2/RSP3, ASR920, NCS520 and NCS4200
Capability Statement: [capability-asr900.xml](capability-asr900.xml)
#### ASR 1000
Capability Statement: [capability-asr1k.xml](capability-asr1k.xml)
#### Catalyst 9200
Capability Statement: [capability-cat9200.xml](capability-cat9200.xml)
#### Catalyst 9300
Capability Statement: [capability-cat9300.xml](capability-cat9300.xml)
#### Catalyst 9400
Capability Statement: [capability-cat9400.xml](capability-cat9400.xml)
#### Catalyst 9500
Capability Statement: [capability-cat9500.xml](capability-cat9500.xml)
#### Catalyst 9600
capability Statement: [capability-cat9600.xml](capability-cat9600.xml)
#### Catalyst 9800
Capability Statement: [capability-wireless.xml](capability-wireless.xml)
#### CBR-8
Capability Statement: [capability-cbr.xml](capability-cbr.xml)
#### CSR1000v/ISRv
Capability Statement: [capability-csr1k.xml](capability-csr1k.xml)
#### IR 1101
Capability Statement: [capability-ir1101.xml](capability-ir1101.xml)
#### IE 3x00
Capability Statement: [capability-ie3x00.xml](capability-ie3x00.xml)
#### ISR 1000
Capability Statement: [capability-isr1k.xml](capability-isr1k.xml)
#### ISR 4000
Capability Statement: [capability-isr4k.xml](capability-isr4k.xml)


### Major Model Changes In 16.11.1

16.11.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added


#### Native Models Modified 



#### IETF model modified



#### OpenConfig Models Modified


#### OpenConfig Deviations Added


#### Experimental YANG Models


These experimental YANG models are in the early status of design and are likely to change.

 
### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint```flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


