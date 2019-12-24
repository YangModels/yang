## Cisco-IOS-XE-bridge-domain.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Previously deprecated nodes are marked as obsolete

### Reason
This list of nodes were not correctly implemented originally and could have never worked. There were marked as deprecated but should have been obsolete.

- /native/bridge-domain/brd-id/ip/igmp/snooping/explicit-tracking/limit
- /native/bridge-domain/brd-id/ip/igmp/snooping/mrouter/interface
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/address
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/max-response-time
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/query-interval
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/tcn
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/timer
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/version
- /native/bridge-domain/brd-id/ip/igmp/snooping/static
- /native/bridge-domain/brd-id/member/member-interface/interface-id

## XPaths Deprecated

### Description
Backward incompatible change in "ip igmp snooping".

### Reason
"ip igmp snooping check" leaf nodes are not implemented correctly

- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:ip/ios-bd:igmp/ios-bd:snooping/ios-bd:check/ios-bd:ttl;
- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:ip/ios-bd:igmp/ios-bd:snooping/ios-bd:check/ios-bd:rtr-option;
- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:ip/ios-bd:igmp/ios-bd:snooping/ios-bd:report-suppression;
- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:mac/ios-bd:learning

## XPaths Modified

N/A

## XPaths Added

### Description
Added new nodes for the deprecated nodes

### Reason
"ip igmp snooping check" leaf nodes are not implemented correctly

- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:ip/ios-bd:igmp/ios-bd:snooping/ios-bd:check/ios-bd:ttl-boolean;
- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:ip/ios-bd:igmp/ios-bd:snooping/ios-bd:check/ios-bd:rtr-option-boolean;
- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:ip/ios-bd:igmp/ios-bd:snooping/ios-bd:report-suppression-boolean;
- /native/ios:bridge-domain/ios-bd:brd-id/ios-bd:mac/ios-bd:learning-boolean

### Description
Added new nodes for the obsoleted ones

### Reason
The old nodes were not correctly implemented

- /native/bridge-domain/brd-id/ip/igmp/snooping/explicit-tracking/limit-value
- /native/bridge-domain/brd-id/ip/igmp/snooping/mrouter/interface-cfg
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/address-value
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/max-response-time-value
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/query-interval-value
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/tcn-parameters
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/timer-expiry
- /native/bridge-domain/brd-id/ip/igmp/snooping/querier/version-value
- /native/bridge-domain/brd-id/ip/igmp/snooping/static-cfg
