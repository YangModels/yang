## Cisco-IOS-XE-power.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description

Changed leaf redundancy-mode to container redundancy-mode-config

### Reason

Redundancy mode is not an enum, but its a container with combined, N+1 & N+N combinations

- /native/power/redundancy-mode

## XPaths Modified

N/A

## XPaths Added

### Reason

New leaf added for the deprecated leaf

- /native/power/redundancy-mode-config


