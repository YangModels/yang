## Cisco-IOS-XE-snmp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description


### Reason


## XPaths Deprecated


## XPaths Modified

### Description
Added range for standard-acl leaf

### Reason
Wrong max value was set for standard-acl in snmp users case and range was not added.

- /native/router/ios-isis:isis/ios-isis:snmp/ios-isis:context/ios-isis:user/ios-isis:permisssion/ios-isis:access/ios-isis:standard-acl

## XPaths Added

### Description
Added new leaves added under access container

### Reason
CLI command formed was wrong as ordering of leaves were wrong

- /native/router/ios-isis:isis/ios-isis:snmp/ios-isis:context/ios-isis:community/ios-isis:access/ios-isis:ro
- /native/router/ios-isis:isis/ios-isis:snmp/ios-isis:context/ios-isis:community/ios-isis:access/ios-isis:rw




