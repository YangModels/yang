## YANG Models and Platform Capabilities for Cisco NX-OS 7.0(3)I5(1)

The YANG files in this directory detail the native and OpenConfig YANG models supported by NX-OS 7.0(3)I5(1) release.

As a convenience, a copy of the "hello" message is also provided (netconf-capabilities.xml).  Althought it represents a bare minimum support of the native model, the actual "hello" message with installation of all additional OpenConfig models will list those models also.


### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.
