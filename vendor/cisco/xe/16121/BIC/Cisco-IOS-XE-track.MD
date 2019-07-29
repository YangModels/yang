## Cisco-IOS-XE-track.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsoleted old paths and created new nodes for the same

### Reason
To Handle negative test cases

- /native/track/ios-track:timer/ios-track:interface/ios-track:ms
- /native/track/ios-track:timer/ios-track:interface/ios-track:seconds
- /native/track/ios-track:timer/ios-track:ip/ios-track:route/ios-track:ms
- /native/track/ios-track:timer/ios-track:ip/ios-track:route/ios-track:seconds
- /native/track/ios-track:timer/ios-track:ip/ios-track:sla/ios-track:ms
- /native/track/ios-track:timer/ios-track:ip/ios-track:sla/ios-track:seconds
- /native/track/ios-track:timer/ios-track:ipv6/ios-track:route/ios-track:ms
- /native/track/ios-track:timer/ios-track:list/ios-track:ms
- /native/track/ios-track:timer/ios-track:list/ios-track:seconds
- /native/track/ios-track:timer/ios-track:stub-object/ios-track:ms
- /native/track/ios-track:timer/ios-track:stub-object/ios-track:seconds
- /native/track/ios-track:tracked-object/ios-track:ip/ios-track:route/ios-track:metric
- /native/track/ios-track:tracked-object/ios-track:ip/ios-track:route/ios-track:reachability
- /native/track/ios-track:tracked-object/ios-track:ip/ios-track:sla/ios-track:reachability
- /native/track/ios-track:tracked-object/ios-track:ip/ios-track:sla/ios-track:state
- /native/track/ios-track:tracked-object/ios-track:ipv6/ios-track:route/ios-track:metric
- /native/track/ios-track:tracked-object/ios-track:ipv6/ios-track:route/ios-track:reachability
- /native/track/ios-track:tracked-object/ios-track:list/ios-track:boolean
- /native/track/ios-track:tracked-object/ios-track:list/ios-track:threshold

## XPaths Deprecated

N/A

## XPaths Modified

### Description
Added When constraints

### Reason
To handle negative test cases

- /native/track/ios-track:tracked-object/ios-track:threshold/\*
- /native/track/ios-track:tracked-object/ios-track:carrier-delay
- /native/track/ios-track:tracked-object/ios-track:default-state
- /native/track/ios-track:tracked-object/ios-track:object/ios-track:not
- /native/track/ios-track:tracked-object/ios-track:object/ios-track:weight

## XPaths Added

### Description
XPaths added for the obsoleted nodes above

- /native/track/ios-track:tracked-object/ios-track:ip/ios-track:route/ios-track:option/ios-track:reachability-case/ios-track:reachability-ip
- /native/track/ios-track:tracked-object/ios-track:ip/ios-track:route/ios-track:option/ios-track:metric-case/ios-track:metric-ip
- /native/track/ios-track:tracked-object/ios-track:ipv6/ios-track:route/ios-track:option/ios-track:reachability-case/ios-track:reachability-ipv6
- /native/track/ios-track:tracked-object/ios-track:ipv6/ios-track:route/ios-track:option/ios-track:metric-case/ios-track:metric-ipv6
- /native/track/ios-track:tracked-object/ios-track:list/ios-track:option/ios-track:boolean-case/ios-track:boolean-config
- /native/track/ios-track:tracked-object/ios-track:list/ios-track:option/ios-track:threshold-case/ios-track:threshold-config
- /native/track/ios-track:timer/ios-track:interface/ios-track:timer-val/ios-track:time-sec/ios-track:sec
- /native/track/ios-track:timer/ios-track:interface/ios-track:timer-val/ios-track:time-msec/ios-track:msec
- /native/track/ios-track:timer/ios-track:ip/ios-track:route/ios-track:timer-val/ios-track:time-sec/ios-track:sec
- /native/track/ios-track:timer/ios-track:ip/ios-track:route/ios-track:timer-val/ios-track:time-msec/ios-track:msec
- /native/track/ios-track:timer/ios-track:ipv6/ios-track:route/ios-track:timer-val/ios-track:time-sec/ios-track:sec
- /native/track/ios-track:timer/ios-track:ipv6/ios-track:route/ios-track:timer-val/ios-track:time-msec/ios-track:msec
- /native/track/ios-track:timer/ios-track:list/ios-track:timer-val/ios-track:time-sec/ios-track:sec
- /native/track/ios-track:timer/ios-track:list/ios-track:timer-val/ios-track:time-msec/ios-track:msec
- /native/track/ios-track:timer/ios-track:stub-object/ios-track:timer-val/ios-track:time-sec/ios-track:sec
- /native/track/ios-track:timer/ios-track:stub-object/ios-track:timer-val/ios-track:time-msec/ios-track:msec




