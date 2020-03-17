## Cisco-IOS-XE-wireless-general-cfg.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Modified

### Description

Changed to non presence container

### Reason

A new gRPC channel provisioning from AP to DNA-Spaces has been introduced in 17.2.1. However, we need to make sure a single remote server (DNA-C  /DNA-Spaces) is allowed to be up at any point in time

- /general-cfg-data/ap-dna-global-config

### Description

Added new Must constraint

### Reason

Added must constraint in both WSA gRPC and Cisco-DNA channel provisioning

- /general-cfg-data/ap-dna-global-config/token/general-cfg-data/wsa-config/enable

## XPaths Added

N/A
