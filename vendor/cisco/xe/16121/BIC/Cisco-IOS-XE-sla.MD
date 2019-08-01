## Cisco-IOS-XE-sla.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Reason
Obsoleted old nodes to make the model backward compatible

- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:frequency
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:owner
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:tag
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:threshold
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:timeout
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:udp-jitter/ios-sla:data-pattern

"NOTE":
None of the child nodes under ios-sla:get/ios-sla:history are marked obsolete. This issue is being currently addressed and will  be fixed in the upcoming release

## XPaths Deprecated

### Description
Deprecated some of the nodes 

### Reason
To make model backward compatible

- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:udp-jitter/ios-sla:clock-tolerance
- /native/ip/ios-sla:sla/ios-sla:schedule/ios-sla:start-time/ios-sla:after
- /native/ip/ios-sla:sla/ios-sla:schedule/ios-sla:start-time/ios-sla:hour-min
- /native/ip/ios-sla:sla/ios-sla:schedule/ios-sla:start-time/ios-sla:hour-min-sec
- /native/ip/ios-sla:sla/ios-sla:schedule/ios-sla:start-time/ios-sla:now
- /native/ip/ios-sla:sla/ios-sla:schedule/ios-sla:start-time/ios-sla:pending
- /native/ip/ios-sla:sla/ios-sla:schedule/ios-sla:start-time/ios-sla:random

"NOTE":
None of the child nodes under ios-sla:y1731 and ios-sla:clock-tolerance are marked as deprecated. This issue is being currently addressed and will  be fixed in the upcoming release.

## XPaths Modified

###Description
Updated When Clause

### Reason
Filling the existing IPSLA NED model gaps

** /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:modification-configuration/* ( Excluding containers "history" and sla-control" )
** /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:modification-configuration/ios-sla:history/*
** /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:modification-configuration/ios-sla:control/*

### Description
Range restrictions added

### Reason
Given range is incorrect for the request-data-size leaf for udp-echo probe

** /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:udp-echo/ios-sla:request-data-size

## XPaths Added

### Reason
New nodes added under a different container, and the old ones are obsoleted to make model backward compatible.

- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:frequency
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:history
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:history/ios-sla:buckets-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:history/ios-sla:distributions-of-statistics-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:history/ios-sla:filter
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:history/ios-sla:hours-of-statistics-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:history/ios-sla:lives-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:history/ios-sla:statistics-distribution-interval
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:owner
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:tag
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:threshold
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:timeout




