## YANG Models for Cisco IOS-XR 24.1.1

The YANG files in this directory detail the YANG models and deviations supported by IOS-XR 24.1.1 releases. The schemas here may also be retrieved from devices running IOS-XR 24.1.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

## Cisco NSO Cisco IOS XR NETCONF NED
Release 24.1.1 NSO NETCONF NED for IOS-XR can be downloaded from the [XR NETCONF NED](https://software.cisco.com/download/redirect?config=d92586785e0ce5e7910f96ea1339da1c) site.

### OpenConfig and IETF Model Inclusion

For ease of reference, the IOS-XR 24.1.1 models in this directory also include copies of the revisions of OpenConfig and IETF model files used by IOS-XR 24.1.1. It should be noted that compilation of the OpenConfig models using the [check-models.sh](check-models.sh) script will result in errors being listed. Cisco has chosen **not** to modify these models to allow error-free compilation.

### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

From IOS-XR 5.3.2 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs. These will be noted by running the ```check-models.sh``` script with the ```-b``` option.

### Backwards Compatibility Issues

It should be noted that some of the modules released in IOS-XR 24.1.1 may break the backwards compatibility guidelines defined in RFC 6020 when compared to the same modules released in IOS-XR 7.3.1. This is because the "native" YANG modules for IOS-XR are generated from internal schema files that are an integral part of the implementation, and, as such, these can change in ways that break backwards compatibility per RFC 6020 guidelines when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Cisco cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the [```check-models.sh```](check-models.sh) script, in conjunction with pyang, can be used to determine what technically incompatible changes may have occurred. Please run ```check.sh``` from this directory with pyang 2.1.1 or greater on your path thus:

```
$ ./check-models.sh -b 731
```

The script will check basic compilation using pyang (some open modules will be reported missing unless you include them on your pyang module path) and then run backwards compatibility checks against the model in the `../731` directory. Directories other than 731 may be specified.

#### The BIC subdirectory

All the model specific backward incompatible changes have been documented in [Backward Incompatible Changes](BIC).

### Unified Models

CLI-based YANG models are generated from the Cisco XR CLI and refined manually.  The unified models will gradually replace native models.  Below is the list of new unified models, and corresponding native models being replaced. The native models are deprecated.

24.1.1 Unified models

| Unified models                                         |  
|--------------------------------------------------------|  
|Cisco-IOS-XR-um-access-list-datatypes.yang              |  
|Cisco-IOS-XR-um-arp-cfg.yang                            |  
|Cisco-IOS-XR-um-conflict-policy-cfg.yang                |  
|Cisco-IOS-XR-um-event-manager-cfg.yang                  |  
|Cisco-IOS-XR-um-event-manager-policy-map-cfg.yang       |  
|Cisco-IOS-XR-um-ethernet-services-access-list-cfg.yang  |  
|Cisco-IOS-XR-um-flow-cfg.yang                           |  
|Cisco-IOS-XR-um-grpc-cfg.yang                           |  
|Cisco-IOS-XR-um-hw-module-profile-cfg.yang              |  
|Cisco-IOS-XR-um-if-access-group-cfg.yang                |  
|Cisco-IOS-XR-um-if-arp-cfg.yang                         |  
|Cisco-IOS-XR-um-if-bundle-cfg.yang                      |  
|Cisco-IOS-XR-um-if-ethernet-cfg.yang                    |  
|Cisco-IOS-XR-um-if-ip-address-cfg.yang                  |  
|Cisco-IOS-XR-um-if-ipv4-cfg.yang                        |  
|Cisco-IOS-XR-um-if-ipv6-cfg.yang                        |  
|Cisco-IOS-XR-um-if-l2transport-cfg.yang                 |  
|Cisco-IOS-XR-um-if-mpls-cfg.yang                        |  
|Cisco-IOS-XR-um-if-service-policy-qos-cfg.yang          |  
|Cisco-IOS-XR-um-if-tunnel-cfg.yang                      |  
|Cisco-IOS-XR-um-if-vrf-cfg.yang                         |  
|Cisco-IOS-XR-um-interface-cfg.yang                      |  
|Cisco-IOS-XR-um-ipv4-access-list-cfg.yang               |  
|Cisco-IOS-XR-um-ipv4-prefix-list-cfg.yang               |  
|Cisco-IOS-XR-um-ipv6-access-list-cfg.yang               |  
|Cisco-IOS-XR-um-ipv6-prefix-list-cfg.yang               |  
|Cisco-IOS-XR-um-l2-ethernet-cfg.yang                    |  
|Cisco-IOS-XR-um-lacp-cfg.yang                           |  
|Cisco-IOS-XR-um-mpls-l3vpn-cfg.yang                     |  
|Cisco-IOS-XR-um-mpls-ldp-cfg.yang                       |  
|Cisco-IOS-XR-um-mpls-lsd-cfg.yang                       |  
|Cisco-IOS-XR-um-mpls-te-cfg.yang                        |  
|Cisco-IOS-XR-um-multicast-routing-cfg.yang              |  
|Cisco-IOS-XR-um-netconf-yang-cfg.yang                   |  
|Cisco-IOS-XR-um-object-group-cfg.yang                   |  
|Cisco-IOS-XR-um-policymap-classmap-cfg.yang             |  
|Cisco-IOS-XR-um-router-amt-cfg.yang                     |  
|Cisco-IOS-XR-um-router-bgp-cfg.yang                     |  
|Cisco-IOS-XR-um-router-igmp-cfg.yang                    |  
|Cisco-IOS-XR-um-router-isis-cfg.yang                    |  
|Cisco-IOS-XR-um-router-mld-cfg.yang                     |  
|Cisco-IOS-XR-um-router-msdp-cfg.yang                    |  
|Cisco-IOS-XR-um-router-ospf-cfg.yang                    |  
|Cisco-IOS-XR-um-router-ospfv3-cfg.yang                  |  
|Cisco-IOS-XR-um-router-pim-cfg.yang                     |  
|Cisco-IOS-XR-um-router-rib-cfg.yang                     |  
|Cisco-IOS-XR-um-router-static-cfg.yang                  |  
|Cisco-IOS-XR-um-rsvp-cfg.yang                           |  
|Cisco-IOS-XR-um-snmp-server-cfg.yang                    |  
|Cisco-IOS-XR-um-statistics-cfg.yang                     |  
|Cisco-IOS-XR-um-telemetry-model-driven-cfg.yang         |  
|Cisco-IOS-XR-um-traps-mpls-ldp-cfg.yang                 |  
|Cisco-IOS-XR-um-vrf-cfg.yang                            |  

### Semantic Version

In the 7.0.1 release, semantic version is included in each model.
Semantic version updates can be found in the release 24.1.1. This is in final development stage. Methodology and workflow are still undergoing much refinements. We are expecting consolidation in the release 7.7.1 timeframe.

Semantic version update method can be found in the following general references:

https://datatracker.ietf.org/doc/draft-verdt-netmod-yang-semver  
https://semver.org

### Known Issues

Earlier versions of IETF models are used in this release.  Updated versions will be used in the future releases.

ietf-netconf-monitoring (2016-08-15)
