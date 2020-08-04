## Cisco-IOS-XE-sanet


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/interface/*/authentication/event/server/dead/action/authorize/vlan(leaf)
- native/interface/*/authentication/event/server/dead/action/reinitialize/vlan(leaf)

### Description

1. A new when expression cannot be added
2. default '3600' is removed.

### Reason

Authentication isnt supported on sub interfaces. Hence added when statement
Default 3600 was incorrectly added to deprecated node. So removed it


- native/interface/\*/authentication

### Reason

Must statement is added to make sure that the CLIs are mutually exclusive

## XPaths Added

### Description
