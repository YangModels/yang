## Cisco-IOS-XE-igmp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
IGMP backward compatibility changes.

### Reason
Obsoleted nodes were functionally broken hence has to be fixed.

- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static/ios-igmp:acl
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static/ios-igmp:source-ip
- /native/interface/<interface>/ip/ios-igmp:igmp/ios-igmp:join-group
- /native/interface/<interface>/ip/ios-igmp:igmp/ios-igmp:join-group/ios-igmp:ip-group-address
- /native/interface/<interface>/ip/ios-igmp:igmp/ios-igmp:join-group/ios-igmp:source


## XPaths Deprecated

### Description
IGMP backward compatibility changes.

### Reason
Obsoleted nodes were functionally broken hence has to be fixed.

- /native/interface/Tunnel/ip/ios-igmp:igmp/ios-igmp:limit

## XPaths Modified
N/A

## XPaths Added

- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static-list
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static-list/ios-igmp:acl
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static-list/ios-igmp:source-ip
- /native/interface/Tunnel/ip/ios-igmp:igmp/ios-igmp:igmp-join-group
- /native/interface/Tunnel/ip/ios-igmp:igmp/ios-igmp:igmp-join-group/ios-igmp:join-group
- /native/interface/Tunnel/ip/ios-igmp:igmp/ios-igmp:igmpv3-join-group
- /native/interface/Tunnel/ip/ios-igmp:igmp/ios-igmp:igmpv3-join-group/ios-igmp:ip-group-address
- /native/interface/Tunnel/ip/ios-igmp:igmp/ios-igmp:igmpv3-join-group/ios-igmp:source
- /native/interface/Tunnel/ip/ios-igmp:igmp/ios-igmp:limit-container/ios-igmp:limit
