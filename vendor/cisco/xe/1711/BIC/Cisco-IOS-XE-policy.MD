## Cisco-IOS-XE-policy.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description

Hardening - match CLIs within class-map part1

### Reason

Most of the CLIs, only one instance could be created inside class-map while on IOS, multiole such CLIs can be configured with different values.

- /native/policy/ios-policy:class-map/ios-policy:no-match/ios-policy:authorizing-method-priority/ios-policy:eq
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:authorizing-method-priority/ios-policy:gt
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:authorizing-method-priority/ios-policy:lt
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:client-type
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:device-type
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:interface
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:ip-address
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:mac-address
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:ipv6-address
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:oui
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:port-type
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:service-template
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:session-type
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:tag
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:sgt
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:timer
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:ssid
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:username
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:user-role

## XPaths Modified

### Description

Add the range check for cEdge QoS shaper rate.

### Reason

Easier for user to find their out-of-range config.

- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:action-param/ios-policy:shape-case/ios-policy:shape/ios-policy:average/ios-policy:average-choice/ios-policy:a/ios-policy:bit-rate

## XPaths Added

### Description

[YANG] Class-map no-match result-type method listed with wrong values

### Reason

'uses class-map-match-result-type-grouping' was moved from inside the method container to out of it, which fixed the issue.

- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:result-type/ios-policy:aaa-timeout
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:result-type/ios-policy:agent-not-found
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:result-type/ios-policy:agent-not-found
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:result-type/ios-policy:method-timeout
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:result-type/ios-policy:none
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:result-type/ios-policy:success

### Reason

'uses class-map-match-result-type-grouping' was moved from inside the method container to out of it, which fixed the issue.

- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:authorizing-method-priority/ios-policy:equal
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:authorizing-method-priority/ios-policy:greater-than
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:authorizing-method-priority/ios-policy:less-than
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:client-type-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:device-type-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:mac-address-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:ip-address-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:interface
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:ipv6-address-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:port-type-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:oui-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:service-template-name
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:session-type-name
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:tag-name
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:sgt-name
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:timer-name
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:ssid-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:username-list
- /native/policy/ios-policy:class-map/ios-policy:match/ios-policy:user-role-name
