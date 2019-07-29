## Cisco-IOS-XE-igmp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsoleted few nodes that were functionally broken

### Reason
For the model changes to be backward compatible and to disable igmp-ssm-map query dns via YANG

- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static/ios-igmp:acl
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static/ios-igmp:source-ip
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:join-group
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:join-group/ios-igmp:ip-group-address
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:join-group/ios-igmp:source


## XPaths Deprecated

### Description/Reason
Deprecated some of the nodes for backward compatibility

- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:limit

## XPaths Modified

N/A

## XPaths Added

### Description/Reason

New xpaths added for deprecated and obsoleted nodes for backward compatibility

- /native/ip/ios-igmp:igmp/ios-igmp:vrf/ios-igmp:immediate-leave
- /native/ip/ios-igmp:igmp/ios-igmp:vrf/ios-igmp:immediate-leave/ios-igmp:group-list
- /native/ip/ios-igmp:igmp/ios-igmp:vrf/ios-igmp:limit
- /native/ip/ios-igmp:igmp/ios-igmp:vrf/ios-igmp:query
- /native/ip/ios-igmp:igmp/ios-igmp:vrf/ios-igmp:query/ios-igmp:disperse
- /native/ip/ios-igmp:igmp/ios-igmp:vrf/ios-igmp:ssm-map/ios-igmp:query
- /native/ip/ios-igmp:igmp/ios-igmp:vrf/ios-igmp:ssm-map/ios-igmp:query/ios-igmp:dns
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static-list
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static-list/ios-igmp:acl
- /native/ip/ios-igmp:igmp/ios-igmp:ssm-map/ios-igmp:static-list/ios-igmp:source-ip
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:igmp-join-group
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:igmp-join-group/ios-igmp:join-group
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:igmpv3-join-group
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:igmpv3-join-group/ios-igmp:ip-group-address
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:igmpv3-join-group/ios-igmp:source
- /native/interface/\*/ip/ios-igmp:igmp/ios-igmp:limit-container/\*
