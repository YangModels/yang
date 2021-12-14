<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [YANG Models and Platform Capabilities for Cisco IOS XE 17.7.1](#yang-models-and-platform-capabilities-for-cisco-ios-xe-1771)
  - [Major Model Changes In 17.7.1](#major-model-changes-in-1771)
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

## YANG Models and Platform Capabilities for Cisco IOS XE 17.7.1

This directory contains the YANG models supported by IOS XE 17.7.1:

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


### Major Model Changes In 17.7.1

17.7.1 model changes include the addition of IETF models, new native models and existing native model updates.

#### Native Models Added

* Cisco-IOS-XE-endpoint-tracker-events.yang

#### Openconfig Models Added

* openconfig-bfd.yang
* openconfig-lacp.yang

#### Deviation Models Added

* Cisco-IOS-XE-lisp-deviation.yang
* Cisco-IOS-XE-ospf-deviation.yang
* Cisco-IOS-XE-bridge-domain-asr900-deviation.yang

#### Native Models Modified 

* Cisco-IOS-XE-appqoe-sslproxy-oper.yang
* Cisco-IOS-XE-appqoe-tcpproxy-oper.yang
* Cisco-IOS-XE-bfd-oper.yang
* Cisco-IOS-XE-bfd.yang
* Cisco-IOS-XE-bgp.yang
* Cisco-IOS-XE-crypto.yang
* Cisco-IOS-XE-cts.yang
* Cisco-IOS-XE-device-sensor.yang
* Cisco-IOS-XE-dhcp.yang
* Cisco-IOS-XE-dre-oper.yang
* Cisco-IOS-XE-eigrp.yang
* Cisco-IOS-XE-endpoint-tracker-oper.yang
* Cisco-IOS-XE-ethernet-cfm-efp.yang
* Cisco-IOS-XE-ethernet-rpc.yang
* Cisco-IOS-XE-ethernet.yang
* Cisco-IOS-XE-ezpm.yang
* Cisco-IOS-XE-features.yang
* Cisco-IOS-XE-fib-oper.yang
* Cisco-IOS-XE-flow.yang
* Cisco-IOS-XE-http.yang
* Cisco-IOS-XE-install-events.yang
* Cisco-IOS-XE-install-oper.yang
* Cisco-IOS-XE-interface-common.yang
* Cisco-IOS-XE-interfaces.yang
* Cisco-IOS-XE-ios-events-oper.yang
* Cisco-IOS-XE-ip-sla-oper.yang
* Cisco-IOS-XE-ip.yang
* Cisco-IOS-XE-ipv6.yang
* Cisco-IOS-XE-isis.yang
* Cisco-IOS-XE-l2vpn.yang
* Cisco-IOS-XE-lacp-oper.yang
* Cisco-IOS-XE-lisp-oper.yang
* Cisco-IOS-XE-lisp.yang
* Cisco-IOS-XE-mdns-gateway.yang
* Cisco-IOS-XE-mdt-oper-v2.yang
* Cisco-IOS-XE-mroute-oper.yang
* Cisco-IOS-XE-multicast.yang
* Cisco-IOS-XE-nat.yang
* Cisco-IOS-XE-native.yang
* Cisco-IOS-XE-nbar.yang
* Cisco-IOS-XE-nd.yang
* Cisco-IOS-XE-ntp.yang
* Cisco-IOS-XE-nwpi-oper.yang
* Cisco-IOS-XE-object-group.yang
* Cisco-IOS-XE-ospf.yang
* Cisco-IOS-XE-ospfv3-deviation.yang
* Cisco-IOS-XE-platform-oper.yang
* Cisco-IOS-XE-pnp.yang
* Cisco-IOS-XE-poe-oper.yang
* Cisco-IOS-XE-policy.yang
* Cisco-IOS-XE-port-channel-deviation.yang
* Cisco-IOS-XE-power.yang
* Cisco-IOS-XE-ptp-pi.yang
* Cisco-IOS-XE-qfp-stats.yang
* Cisco-IOS-XE-rawsocket.yang
* Cisco-IOS-XE-rip.yang
* Cisco-IOS-XE-route-map.yang
* Cisco-IOS-XE-sanet.yang
* Cisco-IOS-XE-scada-gw.yang
* Cisco-IOS-XE-segment-routing.yang
* Cisco-IOS-XE-sip-ua.yang
* Cisco-IOS-XE-snmp.yang
* Cisco-IOS-XE-switch.yang
* Cisco-IOS-XE-template.yang
* Cisco-IOS-XE-track.yang
* Cisco-IOS-XE-tunnel.yang
* Cisco-IOS-XE-types.yang
* Cisco-IOS-XE-utd.yang
* Cisco-IOS-XE-vlan.yang
* Cisco-IOS-XE-voice-class.yang
* Cisco-IOS-XE-voice-dspfarm.yang
* Cisco-IOS-XE-voice-register.yang
* Cisco-IOS-XE-voice.yang
* Cisco-IOS-XE-vrrp-oper.yang
* Cisco-IOS-XE-vrrp.yang
* Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang
* Cisco-IOS-XE-wireless-access-point-oper.yang
* Cisco-IOS-XE-wireless-ap-types.yang
* Cisco-IOS-XE-wireless-ble-ltx-oper.yang
* Cisco-IOS-XE-wireless-ble-mgmt-cmd-rpc.yang
* Cisco-IOS-XE-wireless-client-global-oper.yang
* Cisco-IOS-XE-wireless-client-oper.yang
* Cisco-IOS-XE-wireless-dot11-cfg.yang
* Cisco-IOS-XE-wireless-enum-types.yang
* Cisco-IOS-XE-wireless-general-cfg.yang
* Cisco-IOS-XE-wireless-mesh-cfg.yang
* Cisco-IOS-XE-wireless-radio-cfg.yang
* Cisco-IOS-XE-wireless-rf-cfg.yang
* Cisco-IOS-XE-wireless-rlan-cfg.yang
* Cisco-IOS-XE-wireless-rogue-oper.yang
* Cisco-IOS-XE-wireless-rrm-cfg.yang
* Cisco-IOS-XE-wireless-rrm-oper.yang
* Cisco-IOS-XE-wireless-site-cfg.yang
* Cisco-IOS-XE-wireless-types.yang
* Cisco-IOS-XE-wireless-wlan-cfg.yang

#### Other Models Modified

* cisco-ia.yang
* cisco-xe-openconfig-network-instance-deviation.yang
* cisco-xe-switching-cat9k-openconfig-system-deviation.yang
* cisco-xe-switching-openconfig-platform-deviation.yang
* ietf-yang-library.yang
* ietf-yang-patch-ann.yang


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
