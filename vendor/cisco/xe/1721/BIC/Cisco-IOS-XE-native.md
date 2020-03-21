## Cisco-IOS-XE-native.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

Shutdown model was not working as expected, hence obsoleted.

### Reason

When we create an ERSPAN session, it is shutdown by default. But because the type of  ‘shutdown’ was ‘empty’ before, we were not able to set it’s default value to true. So, new leafs have been created ‘shutdown-destination' and 'shutdown-source' of type boolean.

- /native/monitor/session/type/erspan-destination/shutdown/native/monitor/session/type/erspan-source/shutdown

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

### Description

New node added for the obsoleted xpath.

- /native/monitor/session/type/erspan-destination/shutdown-destination/native/monitor/session/type/erspan-source/shutdown-source
