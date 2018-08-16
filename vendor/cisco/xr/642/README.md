## YANG Models for Cisco IOS-XR 6.4.2

The YANG files in this directory detail the native YANG models and deviations supported by IOS-XR 6.4.2 releases. The schemas here may also be retrieved from devices running IOS-XR 6.4.2 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

### OpenConfig and IETF Model Inclusion

For ease of reference, the IOS-XR 6.4.2 models in this directory also include copies of the revisions of OpenConfig and IETF model files used by IOS-XR 6.4.2. It should be noted that compilation of the OpenConfig models using the [check-models.sh](check-models.sh) script will result in errors being listed. Cisco has chosen **not** to modify these models to allow error-free compilation.


### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

From IOS-XR 5.3.2 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs. These will be noted by running the ```check-models.sh``` script with the ```-b``` option.

### Backwards Compatibility Issues

It should be noted that some of the modules released in IOS-XR 6.4.2 may break the backwards compatibility guidelines defined in RFC 6020 when compared to the same modules released in IOS-XR 6.4.2. This is because the "native" YANG modules for IOS-XR are generated from internal schema files that are an integral part of the implementation, and, as such, these can change in ways that break backwards compatibility per RFC 6020 guidelines when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Cisco cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the [```check-models.sh```](check-models.sh) script, in conjunction with pyang, can be used to determine what technically incompatible changes may have occurred. Please run ```check.sh``` from this directory with pyang 1.5 or greater on your path thus:

```
$ ./check-models.sh -b 631
```

The script will check basic compilation using pyang (some open modules will be reported missing unless you include them on your pyang module path) and then run backwards compatibility checks against the model in the `../631` directory. Directories other than 631 may be specified.

### Cross-Platform Compatibility Issues

Unfortunately, IOS-XR 6.4.2 has some issues with small number of native models that have illegal variations in definition across platforms. The details of the models impacted and the issues can be found in [this document](MODEL-ISSUES.md)

