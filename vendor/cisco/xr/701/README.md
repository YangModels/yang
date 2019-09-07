## YANG Models for Cisco IOS-XR 7.0.1

The YANG files in this directory detail the native YANG models and deviations supported by IOS-XR 7.0.1 releases. The schemas here may also be retrieved from devices running IOS-XR 7.0.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

### OpenConfig and IETF Model Inclusion

For ease of reference, the IOS-XR 7.0.1 models in this directory also include copies of the revisions of OpenConfig and IETF model files used by IOS-XR 6.5.1. It should be noted that compilation of the OpenConfig models using the [check-models.sh](check-models.sh) script will result in errors being listed. Cisco has chosen **not** to modify these models to allow error-free compilation.


### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

From IOS-XR 5.3.2 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs. These will be noted by running the ```check-models.sh``` script with the ```-b``` option.

### Backwards Compatibility Issues

It should be noted that some of the modules released in IOS-XR 7.0.1 may break the backwards compatibility guidelines defined in RFC 6020 when compared to the same modules released in IOS-XR 6.6.2. This is because the "native" YANG modules for IOS-XR are generated from internal schema files that are an integral part of the implementation, and, as such, these can change in ways that break backwards compatibility per RFC 6020 guidelines when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Cisco cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the [```check-models.sh```](check-models.sh) script, in conjunction with pyang, can be used to determine what technically incompatible changes may have occurred. Please run ```check.sh``` from this directory with pyang 1.5 or greater on your path thus:

```
$ ./check-models.sh -b 662
```

The script will check basic compilation using pyang (some open modules will be reported missing unless you include them on your pyang module path) and then run backwards compatibility checks against the model in the `../662` directory. Directories other than 662 may be specified.


### Unified Models

In the 7.0.1 release, we introduce the first set of Unified Models. They are CLI-based models, generated from the Cisco XR CLI and refined manually.  The unified models will gradually replace native models.  Below is the list of new unified models, and corresponding native models being replaced. The native models are deprecated.

| Deprecated model                             | Unified model                                   |
|----------------------------------------------|-------------------------------------------------|
|                                              | Cisco-IOS-XR-um-if-ip-address-cfg.yang          |
|                                              | Cisco-IOS-XR-um-if-tunnel-cfg.yang              |
|                                              | Cisco-IOS-XR-um-interface-cfg.yang              |
|                                              | Cisco-IOS-XR-um-lacp-cfg.yang                   |
|                                              | Cisco-IOS-XR-um-snmp-server-cfg.yang            |
| Cisco-IOS-XR-bundlemgr-cfg.yang              | Cisco-IOS-XR-um-if-bundle-cfg.yang              |
| Cisco-IOS-XR-drivers-media-eth-cfg.yang      | Cisco-IOS-XR-um-if-ethernet-cfg.yang            |
| Cisco-IOS-XR-infra-rsi-cfg.yang              | Cisco-IOS-XR-um-vrf-cfg.yang                    |
| Cisco-IOS-XR-ip-rib-cfg.yang                 | Cisco-IOS-XR-um-router-rib-cfg.yang             |
| Cisco-IOS-XR-ip-static-cfg.yang              | Cisco-IOS-XR-um-router-static-cfg.yang          |
| Cisco-IOS-XR-ipv4-arp-cfg.yang               | Cisco-IOS-XR-um-arp-cfg.yang                    |
| Cisco-IOS-XR-man-ems-cfg.yang                | Cisco-IOS-XR-um-grpc-cfg.yang                   |
| Cisco-IOS-XR-man-netconf-cfg.yang            | Cisco-IOS-XR-um-netconf-yang-cfg.yang           |
| Cisco-IOS-XR-mpls-io-cfg.yang                | Cisco-IOS-XR-um-if-mpls-cfg.yang                |
| Cisco-IOS-XR-mpls-ldp-cfg.yang               | Cisco-IOS-XR-um-mpls-ldp-cfg.yang               |
| Cisco-IOS-XR-mpls-lsd-cfg.yang               | Cisco-IOS-XR-um-mpls-lsd-cfg.yang               |
| Cisco-IOS-XR-mpls-vpn-cfg.yang               | Cisco-IOS-XR-um-mpls-l3vpn-cfg.yang             |
| Cisco-IOS-XR-telemetry-model-driven-cfg.yang | Cisco-IOS-XR-um-telemetry-model-driven-cfg.yang |


### Semantic Version

In the 7.0.1 release, semantic version is included in each model.  Subsequent model releases will have semantic version incremented based on the relevant major, minor, patch level changes.

General references:

https://datatracker.ietf.org/doc/draft-verdt-netmod-yang-semver  
https://semver.org


### Known Issues

Earlier versions of IETF models are used in this release.  Updated versions will be used in the future releases.

ietf-netconf-monitoring (2016-08-15)
