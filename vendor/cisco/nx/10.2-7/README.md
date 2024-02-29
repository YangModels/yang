## YANG Models and Platform Capabilities for Cisco NX-OS 10.2(7)

The YANG files in this directory detail the native and OpenConfig YANG models with deviations supported by NX-OS 10.2(7) release.

As a convenience, a copy of the "hello" message is also provided (netconf-capabilities.xml).

### YANG Syntax Issues With ```Cisco-NX-OS-device.yang```

The core native device model for NX-OS is [```Cisco-NX-OS-device.yang```](Cisco-NX-OS-device.yang). This model currently has a number of problems relating to non-compliant regular expresssion constraints (per RFC 6020) and incorrect default values. These issues will be fixed in a subsequent release.  Developers can examine the script [```check.sh```](../check.sh) for details of how the model is currently compiled to pass CI builds.

### Generating models for a specific agent/controller

For netconf (default): `./prepare.sh` 
     Creates ./netconf_models

For restconf: `./prepare.sh -a restconf` 
     Creates ./restconf_models
     
For gnmi: `./prepare.sh -a gnmi` 
     Creates ./gnmi_models

All your models will be in the created models directory.

### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

From NX-OS 7.0.3 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs. These will be noted by running the ```check-models.sh``` script with the ```-b``` option.


### RPM Download

The RPMs supporting YANG models are available for download at the Cisco Artifactory http://devhub.cisco.com/artifactory/open-nxos-agents/10.2-7/
