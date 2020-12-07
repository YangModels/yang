## Cisco-IOS-XE-snmp.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- /native/snmp-server/enable/enable-choice/traps/wireless/bsnMobileStation
- /native/snmp-server/enable/enable-choice/traps/wireless/bsnMobileStation/bsnAccessPoint
- /native/snmp-server/enable/enable-choice/traps/wireless/bsnMobileStation/bsnAccessPoint/bsnRogue

### Description

### Reason

The NED model for snmp-server's subconfig of wireless traps did not represent the traps correctly (with wrong hierarchy, which caused some config to never be represented in YANG)

## XPaths Deprecated

### Description

## XPaths Modified

- /config-host-attribute-grouping(grouping)/security-level
- /config-host-attribute-grouping(grouping)/version

### Description

The choice 'informs-traps-choice', leaf 'security-level', leaf 'version' is  removed.

### Reason

NSO was not consuming the snmp annotation changes. Therefore moved the changes from annotation to snmp yang . leaves were part of grouping and group was used in four list. To bring the annotation changes to snmp yang, leaves were removed from group and added to list

## XPaths Added

### Description
