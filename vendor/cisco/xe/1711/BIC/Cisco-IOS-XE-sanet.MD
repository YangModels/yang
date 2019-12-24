## Cisco-IOS-XE-sanet.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsoletion of "access-session tunnel vlan" CLI and its equivalent model

### Reason
The CLI "access-session tunnel vlan" is not used anymore, and has been obsoleted.. 
Hence any equivalent model also needs to be made obsolete.

- /native/ios-sanet:access-session/ios-sanet:tunnel

## XPaths Deprecated

### Description
Backward compatible changes for authentication timer cli's

### Reason
There can be only one instance of authentication timer reauthenticate and inactivity timer. Hence made leaves part of switch

- /native/ios:interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:value/ios-sanet:value
- /native/ios:interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:value/ios-sanet:dynamic
- /native/ios:interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:server
- /native/ios:interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:server/ios-sanet:dynamic
- /native/ios:interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:reauthenticate/ios-sanet:value
- /native/ios:interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:reauthenticate/ios-sanet:server

## XPaths Modified
N/A

## XPaths Added

### Decription
Backward compatible changes for authentication timer cli's

### Reason
There can be only one instance of authentication timer reauthenticate and inactivity timer. Hence made leaves part of switch

- /native/interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:value-config/ios-sanet:value
- /native/interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:value-config/ios-sanet:dynamic
- /native/interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:server-config/ios-sanet:dynamic
- /native/interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:inactivity/ios-sanet:server-config
- /native/interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:reauthenticate/ios-sanet:value-config
- /native/interface/\*/ios-sanet:authentication/ios-sanet:timer/ios-sanet:reauthenticate/ios-sanet:server-config



