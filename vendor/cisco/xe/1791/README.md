<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [YANG Models and Platform Capabilities for Cisco IOS XE 17.9.1](#yang-models-and-platform-capabilities-for-cisco-ios-xe-1771)
  - [Major Model Changes In 17.9.1](#major-model-changes-in-1771)
    - [Native Models Added](#native-models-added)
    - [Openconfig Models Added](#openconfig-models-added)
    - [Deviation Models Added](#deviation-models-added)
    - [Native Models Modified](#native-models-modified)
    - [Other Models Modified](#other-models-modified)
    - [Experimental YANG Models](#experimental-yang-models)
  - [Backward Incompatible Changes](#backward-incompatible-changes)
  - [Compliance With "pyang --lint"](#compliance-with-pyang---lint)
  - [Revision Statements](#revision-statements)
  - [YANG Model Version 1.1](#yang-model-version-11)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## YANG Models and Platform Capabilities for Cisco IOS XE 17.9.1

This directory contains the YANG models supported by IOS XE 17.9.1:

* IOS XE native models
* IETF, OpenConfig and tail-f models (and deviations)
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)

The schemas may be retrieved from devices using the NETCONF "get-schema" RPC as detailed in [RFC 6022](https://tools.ietf.org/html/rfc6022) Section 3.1. Schemas may also be retrieved using RESTCONF "get" on ietf-yang-library.yang model schema leaf, which provides the list of URL's from which the schemas can be downloaded. Models listed in this repository are supported by following IOS XE platforms
listed below. As model content may differ based on platform capabilities, samples of the platform "hello" messages are also provided in the files listed against platforms:

| Platform | Capability File |
|----------|-----------------|
| ASR 1000 | [capability-asr1k.xml](capability-asr1k.xml) |
| ASR 900 RSP2/RSP3, ASR 920, NCS 520 and NCS 4200 | [capability-asr900.xml](capability-asr900.xml) |
| Catalyst 9200 | [capability-cat9200.xml](capability-cat9200.xml) |
| Catalyst 9300 | [capability-cat9300.xml](capability-cat9300.xml) |
| Catalyst 9400 | [capability-cat9400.xml](capability-cat9400.xml) |
| Catalyst 9500 | [capability-cat9500.xml](capability-cat9500.xml) |
| Catalyst 9600 | [capability-cat9600.xml](capability-cat9600.xml) |
| Catalyst 9800 | [capability-wireless.xml](capability-wireless.xml) |
| C8000v/ISRv | [capability-c8000v.xml](capability-c8000v.xml) |
| C8500/C8500L | [capability-c8500.xml](capability-c8500.xml) |
| C8200 | [capability-c8200.xml](capability-c8200.xml) |
| C8300 | [capability-c8300.xml](capability-c8300.xml) |
| ESS 3x00 | [capability-ess3x00.xml](capability-ess3x00.xml) |
| IR 1101 | [capability-ir1101.xml](capability-ir1101.xml) |
| IE 3x00 | [capability-ie3x00.xml](capability-ie3x00.xml) |
| ISR 1000 | [capability-isr1k.xml](capability-isr1k.xml) |
| ISR 4000 | [capability-isr4k.xml](capability-isr4k.xml) |


### Major Model Changes In 17.9.1

17.9.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-appqoe-http-oper.yang
* Cisco-IOS-XE-banner-internal.yang
* Cisco-IOS-XE-bgp-actions-rpc.yang
* Cisco-IOS-XE-cli-rpc.yang
* Cisco-IOS-XE-location.yang
* Cisco-IOS-XE-loop-detect.yang
* Cisco-IOS-XE-mrp.yang
* Cisco-IOS-XE-poe-health-oper.yang
* Cisco-IOS-XE-prp-oper.yang
* Cisco-IOS-XE-prp.yang
* Cisco-IOS-XE-qfp-appqoe-dp-oper.yang
* Cisco-IOS-XE-system-integrity-oper.yang
* Cisco-IOS-XE-transceiver-monitor.yang
* Cisco-IOS-XE-uidp-oper.yang
* Cisco-IOS-XE-voice-rpc.yang
* Cisco-IOS-XE-wireless-client-rpc.yang
* Cisco-IOS-XE-wireless-rfid-global-oper.yang
* Cisco-IOS-XE-wireless-rrm-emul-oper.yang
* Cisco-IOS-XE-wireless-rrm-global-oper.yang
* Cisco-IOS-XE-wireless-sisf-global-oper.yang

#### Openconfig Models Added

* openconfig-license.yang
* openconfig-messages.yang
* openconfig-system-grpc.yang

#### Deviation Models Added

* cisco-xe-openconfig-system-grpc-deviation.yang
* cisco-xe-routing-openconfig-system-grpc-deviation.yang

#### Native Models Modified 

* Cisco-IOS-XE-aaa-types.yang
* Cisco-IOS-XE-aaa.yang
* Cisco-IOS-XE-app-hosting-cfg.yang
* Cisco-IOS-XE-app-hosting-oper.yang
* Cisco-IOS-XE-appqoe-oper.yang
* Cisco-IOS-XE-appqoe-serv-oper.yang
* Cisco-IOS-XE-appqoe-sslproxy-oper.yang
* Cisco-IOS-XE-appqoe-types.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-cef-deviation.yang
* Cisco-IOS-XE-cef.yang
* Cisco-IOS-XE-controller.yang
* Cisco-IOS-XE-crypto-actions-rpc.yang
* Cisco-IOS-XE-crypto-rpc.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts-routing-deviation.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-digitalio.yang
* Cisco-IOS-XE-ethernet-cfm-efp.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-features.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-hsrp.yang
* Cisco-IOS-XE-http.yang
* Cisco-IOS-XE-igmp.yang
* Cisco-IOS-XE-install-event-types.yang
* Cisco-IOS-XE-install-oper-types.yang
* Cisco-IOS-XE-install-oper.yang
* Cisco-IOS-XE-install-rpc.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-line-deviation.yang
* Cisco-IOS-XE-line.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-mdns-gateway.yang
* Cisco-IOS-XE-mdt-oper-v2.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-nwpi-oper.yang
* Cisco-IOS-XE-nwpi-rpc.yang
* Cisco-IOS-XE-object-group.yang
* Cisco-IOS-XE-platform-software-oper.yang
* Cisco-IOS-XE-platform.yang
* Cisco-IOS-XE-poch-lb-switch-deviation.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-policy-deviation.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-power-deviation.yang
* Cisco-IOS-XE-qfp-stats.yang
* Cisco-IOS-XE-rawsocket.yang
* Cisco-IOS-XE-rmi-dad.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-sanet.yang
* Cisco-IOS-XE-segment-routing.yang
* Cisco-IOS-XE-sla.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-spanning-tree.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-udld.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-voice-class.yang
* Cisco-IOS-XE-voice-port.yang
* Cisco-IOS-XE-voice.yang
* Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang
* Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang
* Cisco-IOS-XE-wireless-access-point-oper.yang
* Cisco-IOS-XE-wireless-ap-cfg.yang
* Cisco-IOS-XE-wireless-ap-global-oper.yang
* Cisco-IOS-XE-wireless-ap-types.yang
* Cisco-IOS-XE-wireless-apf-cfg.yang
* Cisco-IOS-XE-wireless-ble-ltx-oper.yang
* Cisco-IOS-XE-wireless-client-oper.yang
* Cisco-IOS-XE-wireless-client-types.yang
* Cisco-IOS-XE-wireless-dot11-cfg.yang
* Cisco-IOS-XE-wireless-enum-types.yang
* Cisco-IOS-XE-wireless-events-oper.yang
* Cisco-IOS-XE-wireless-general-cfg.yang
* Cisco-IOS-XE-wireless-hyperlocation-oper.yang
* Cisco-IOS-XE-wireless-location-cfg.yang
* Cisco-IOS-XE-wireless-mesh-cfg.yang
* Cisco-IOS-XE-wireless-mesh-oper.yang
* Cisco-IOS-XE-wireless-mesh-rpc.yang
* Cisco-IOS-XE-wireless-radio-cfg.yang
* Cisco-IOS-XE-wireless-rf-cfg.yang
* Cisco-IOS-XE-wireless-rogue-cfg.yang
* Cisco-IOS-XE-wireless-rogue-oper.yang
* Cisco-IOS-XE-wireless-rrm-oper.yang
* Cisco-IOS-XE-wireless-rrm-rpc.yang
* Cisco-IOS-XE-wireless-rule-cfg.yang
* Cisco-IOS-XE-wireless-types.yang
* Cisco-IOS-XE-wireless-wlan-cfg.yang
* Cisco-IOS-XE-wpan-oper.yang
* Cisco-IOS-XE-xcopy-rpc.yang
* Cisco-IOS-XE-yang-interfaces-cfg.yang
* Cisco-IOS-XE-zone.yang

#### Other Models Modified

* cisco-xe-access-openconfig-system-deviation.yang
* cisco-xe-openconfig-access-points-deviation.yang
* cisco-xe-routing-openconfig-system-deviation.yang
* cisco-xe-switching-cat9k-openconfig-system-deviation.yang
* openconfig-system.yang

#### Experimental YANG Models

* Cisco-IOS-XE-wireless-ble-mgmt-oper.yang
* Cisco-IOS-XE-wireless-tunnel-cfg.yang
* Cisco-IOS-XE-wireless-tunnel-types.yang
* Cisco-IOS-XE-wireless-nmsp-oper.yang
* Cisco-IOS-XE-wireless-rfid-cfg.yang
* Cisco-IOS-XE-wireless-rfid-oper.yang
* Cisco-IOS-XE-wireless-radio-cfg.yang

These experimental YANG models are in the early status of design and are likely to change

### Backward Incompatible Changes

All the model specific backward incompatible changes have been documented in [Backward Incompatible Changes](BIC).

### Compliance With "pyang --lint"

Some models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint```flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

As part of the model validation for this release we are ignoring "LEAFREF_IDENTIFIER_NOT_FOUND" and "STRICT_XPATH_FUNCTIONS" error types. Reason being that the missing leafref reference errors are due to pyang bug which needs to be fixed and some of the XPATH function errors are false positives which are handled in the newer version of pyang (2.3.2)

### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.

### YANG Model Version 1.1

YANG version 1.1 is described by the RFC 7950, The YANG 1.1 Data Modeling Language. YANG version 1.1 is a maintenance release of the YANG language that addresses ambiguities and defects inthe YANG version 1.0 specification. The YANG module in YANG version 1.1 is advertised through the ietf-yang-library instead of the NETCONF hello messages.

The YANG version 1.1 models will be published from 17.10.1 release onwards. However to prepare for the YANG 1.1 release, the 1.1 version YANG models are added under [YANG_1.1](YANG_1.1) directory along with the script "migrate_yang_version.py" that converts NED models from version 1.0 to version 1.1 for reference.

The following example shows how to migrate from YANG version 1.0 to YANG version 1.1 using the script:

migrate_yang_version.py [-h] [--out OUT] path

Use the help command to view the options available with the script:

python migrate_yang_version.py --help

usage: migrate_yang_version.py [-h] [--out OUT] path

positional arguments:
path Path to the YANG files

optional arguments:
-h, --help show this help message and exit
--out OUT Path to the output YANG file

After the YANG model version 1.1 is created, either by downloading it from GitHub or by using the migrate_yang_version.py script and compiled on the client application, end-to-end YANG model tests can be executed and validated against Cisco IOS XE devices.

Support: Please send inquiry related to the ‘migrate_yang_version.py’ script or XE YANG version 1.1 migration process to ‘xe-yang-migration@cisco.com’ mailing list.
