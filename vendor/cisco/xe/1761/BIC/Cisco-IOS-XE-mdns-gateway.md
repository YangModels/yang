## Cisco-IOS-XE-mdns-gateway


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/interface/Vlan/mdns-sd/gateway/active-query
- native/interface/Vlan/mdns-sd/gateway/active-query/timer
- native/interface/Vlan/mdns-sd/gateway/service-inst-suffix
- native/interface/Vlan/mdns-sd/gateway/service-mdns-query
- native/interface/Vlan/mdns-sd/gateway/transport
- native/mdns-sd/gateway/active-query
- native/mdns-sd/gateway/active-query/timer
- native/mdns-sd/gateway/mode
- native/mdns-sd/gateway/mode/mode-type(choice)
- native/mdns-sd/gateway/mode/mode-type(choice)/sdg-agent(case)/sdg-agent
- native/mdns-sd/gateway/mode/mode-type(choice)/service-peer(case)/service-peer
- native/mdns-sd/gateway/service-announcement-count
- native/mdns-sd/gateway/service-announcement-timer
- native/mdns-sd/gateway/service-announcement-timer/periodicity
- native/mdns-sd/gateway/service-query-count
- native/mdns-sd/gateway/service-query-timer
- native/mdns-sd/gateway/service-query-timer/periodicity
- native/mdns-sd/location-filter/match/loc_grp_all
- native/mdns-sd/location-filter/match/loc_grp_all/all
- native/mdns-sd/location-filter/match/loc_grp_all/location-group
- native/mdns-sd/location-filter/match/loc_grp_all/vlan
- native/mdns-sd/location-filter/match/loc_grp_configured
- native/mdns-sd/location-filter/match/loc_grp_configured/location-group
- native/mdns-sd/location-filter/match/loc_grp_configured/vlan
- native/mdns-sd/location-filter/match/loc_grp_default
- native/mdns-sd/location-filter/match/loc_grp_default/default
- native/mdns-sd/location-filter/match/loc_grp_default/location-group
- native/mdns-sd/location-filter/match/loc_grp_default/vlan
- native/mdns-sd/service-list
- native/mdns-sd/service-list/direction
- native/mdns-sd/service-list/direction/IN
- native/mdns-sd/service-list/direction/IN/match
- native/mdns-sd/service-list/direction/IN/match/message-type
- native/mdns-sd/service-list/direction/IN/match/name
- native/mdns-sd/service-list/direction/OUT
- native/mdns-sd/service-list/direction/OUT/match
- native/mdns-sd/service-list/direction/OUT/match/location-filter
- native/mdns-sd/service-list/direction/OUT/match/name
- native/mdns-sd/service-list/direction/dir
- native/mdns-sd/service-list/service-list-name
- native/mdns-sd/service-policy/service-list
- native/mdns-sd/service-policy/service-list/direction
- native/mdns-sd/service-policy/service-list/name
- native/vlan/configuration/mdns-sd/gateway/active-query
- native/vlan/configuration/mdns-sd/gateway/active-query/timer
- native/vlan/configuration/mdns-sd/gateway/service-inst-suffix
- native/vlan/configuration/mdns-sd/gateway/service-mdns-query
- native/vlan/configuration/mdns-sd/gateway/transport

### Reason

Counts and timers, in their must conditions, were referring back to 'mode' which was obsoleted and split into wired and wireless

## XPaths Deprecated

### Description

## XPaths Modified

- native/interface/Vlan/mdns-sd/gateway
- native/interface/Vlan/mdns-sd/gateway
- native/mdns-sd/location-filter/loc-fil-name
- native/mdns-sd/service-policy/service-policy-name
- native/vlan/configuration/mdns-sd/gateway
- native/vlan/configuration/mdns-sd/gateway
- mdns-sd-gateway-common-global-grouping(grouping)/sdg-agent
- mdns-sd-switch-vlan-config-grouping(grouping)/sdg-agent
- native/mdns-sd/service-peer-conf/service-peer/group/peer-group/service-peer/location-group
- mdns-sd-gateway-intf-vlan-grouping(grouping)/mdns-sd/gateway
- mdns-sd-vlan-config-grouping(grouping)/mdns-sd/gateway
- mdns-sd-switch-global-grouping(grouping)/service-peer-conf/service-peer/group/peer-group/service-peer/ip

### Description

1. A new must expression added
2. The base type has illegally changed from string to union
3. The container 'location-group' is illegally changed to a list
4. The if-feature 'ios-features:mdns-switch' is illegally added in container gateway
5. The member types in the union have changed

### Reason

CLI hardening for 17.6.1 Bonjour.

## XPaths Added

### Description
