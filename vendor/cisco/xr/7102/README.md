## YANG Models for Cisco IOS-XR 7.10.2

The YANG files in this directory detail the YANG models and deviations supported by IOS-XR 7.10.2 release. The schemas here may also be retrieved from devices running IOS-XR 7.10.2 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

## Cisco NSO Cisco IOS XR NETCONF NED
Release 7.10.2 NSO NETCONF NED for IOS-XR can be downloaded from the [XR NETCONF NED](https://software.cisco.com/download/redirect?config=d92586785e0ce5e7910f96ea1339da1c) site.

### OpenConfig and IETF Model Inclusion

For ease of reference, the IOS-XR 7.10.2 models in this directory also include copies of the revisions of OpenConfig and IETF model files used by IOS-XR 7.10.2. It should be noted that compilation of the OpenConfig models using the [check-models.sh](check-models.sh) script will result in errors being listed. Cisco has chosen **not** to modify these models to allow error-free compilation.

### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

From IOS-XR 5.3.2 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs. These will be noted by running the ```check-models.sh``` script with the ```-b``` option.

### Backwards Compatibility Issues

It should be noted that some of the modules released in IOS-XR 7.10.2 may break the backwards compatibility guidelines defined in RFC 6020 when compared to the same modules released in IOS-XR 7.10.1. This is because the "native" YANG modules for IOS-XR are generated from internal schema files that are an integral part of the implementation, and, as such, these can change in ways that break backwards compatibility per RFC 6020 guidelines when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Cisco cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the [```check-models.sh```](check-models.sh) script, in conjunction with pyang, can be used to determine what technically incompatible changes may have occurred. Please run ```check.sh``` from this directory with pyang 2.0 or greater on your path thus:

```
$ ./check-models.sh -b 7101
```

The script will check basic compilation using pyang (some open modules will be reported missing unless you include them on your pyang module path) and then run backwards compatibility checks against the model in the `../7101` directory. Directories other than 7101 may be specified.

#### The BIC subdirectory

All the model specific backward incompatible changes have been documented in [Backward Incompatible Changes](BIC).

### Unified Models

CLI-based YANG models are generated from the Cisco XR CLI and refined manually.  We continue our journey replacing native device models.  In 7.10.2, 326 UM models are released.  Unified Models have the naming convention with the '-um-' designation: 'Cisco-IOS-XR-um-&lt;feature&gt;.yang'.

### Semantic Version

In the 7.0.1 release, semantic version is included in each model.
Because of processing issues, semantic version updates did not go into release 7.10.2. Methodology and workflow are still undergoing much refinements. We are expecting consolidation in the release 7.11.x timeframe.

Semantic version update method can be found in the following general references:

https://datatracker.ietf.org/doc/draft-verdt-netmod-yang-semver  
https://semver.org

### Known Issues

Earlier versions of IETF models are used in this release.  Updated versions will be used in the future releases.
