## Cisco-IOS-XE-ethernet.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

More than one access-group is not allowed to be configured

### Reason

The model in its current state will not work for more than one access-group / Traffic filter and the container has to be updated to a List with access-group type (in/out) as key to make this work properly , since multiple instances of the command are possible.

- /native/interface/ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl
- /native/interface/ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl/ios-eth:access-group
- /native/interface/ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl/ios-eth:in
- /native/interface//ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl/ios-eth:out
- /native/interface/GigabitEthernet/ios-eth:service/ios-eth:instance/ios-eth:ipv6/ios-eth:traffic-filter
- /native/interface/GigabitEthernet/ios-eth:service/ios-eth:instance/ios-eth:ipv6/ios-eth:traffic-filter/ios-eth:in
- /native/interface/GigabitEthernet/ios-eth:service/ios-eth:instance/ios-eth:ipv6/ios-eth:traffic-filter/ios-eth:out


### Description

Addressing backward-incompatiblity changes

### Reason

continuity check was a container before so changed to a leaf now to address backward mappings

- /native/ethernet/ios-eth:cfm/ios-eth:domain/ios-eth:service/ios-eth:continuity-check


### Description

Obsoleted the cfm alarm node which ws incorrectly implemented.

### Reason

cfm alarm notification command is modelled as a container with leaves this results in multiple leaves possible in the configuration but it is incorrect

- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:delay
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:notification
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:notification/ios-eth:all
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:notification/ios-eth:error-xcon
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:notification/ios-eth:mac-remote-error-xcon
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:notification/ios-eth:none
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:notification/ios-eth:remote-error-xcon
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:notification/ios-eth:xcon
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:reset
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm/ios-eth:packet


## XPaths Deprecated

N/A

## XPaths Added

### Description
More than one access-group is not allowed to be configured

### Reason

The model in its current state will not work for more than one access-group / Traffic filter and the container has to be updated to a List with access-group type (in/out) as key to make this work properly , since multiple instances of the command are possible.

- /native/interface/ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl-list
- /native/interface/ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl-list/ios-eth:access-group
- /native/interface/ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl-list/ios-eth:in
- /native/interface//ios-eth:service/ios-eth:instance/ios-eth:ip/ios-eth:acl-list/ios-eth:out
- /native/interface/GigabitEthernet/ios-eth:service/ios-eth:instance/ios-eth:ipv6/ios-eth:traffic-filter-list
- /native/interface/GigabitEthernet/ios-eth:service/ios-eth:instance/ios-eth:ipv6/ios-eth:traffic-filter-list/ios-eth:in
- /native/interface/GigabitEthernet/ios-eth:service/ios-eth:instance/ios-eth:ipv6/ios-eth:traffic-filter-list/ios-eth:out


### Description

Addressing backward-incompatiblity changes

### Reason

continuity check was a container before so changed to a leaf now to address backward mappings

-/native/ethernet/ios-eth:cfm/ios-eth:domain/ios-eth:service/ios-eth:cfm-continuity-check


### Description
Added new nodes for the obsoleted ones.

### Reason
Old nodes were incorrectly implemented.

- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm-config
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm-config/ios-eth:delay
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm-config/ios-eth:notification
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm-config/ios-eth:reset
- /native/ios:ethernet/ios-eth:cfm/ios-eth:alarm-config/ios-eth:packet
