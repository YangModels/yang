## Cisco-IOS-XE-rip.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/router/rip/address-family/ipv4/unicast/distribute-list/accesslist-ifname/interface-routing-id
- native/router/rip/address-family/ipv4/unicast/distribute-list/accesslist-ifname/isis-tag
- native/router/rip/address-family/ipv4/unicast/distribute-list/accesslist-ifname/vrf
- native/router/rip/address-family/ipv4/unicast/distribute-list/accesslist-prefix-gateway-ifname/interface-routing-id
- native/router/rip/address-family/ipv4/unicast/distribute-list/accesslist-prefix-gateway-ifname/isis-tag
- native/router/rip/address-family/ipv4/unicast/distribute-list/accesslist-prefix-gateway-ifname/vrf
- native/router/rip/address-family/ipv4/vrf/distribute-list/accesslist-ifname/interface-routing-id
- native/router/rip/address-family/ipv4/vrf/distribute-list/accesslist-ifname/isis-tag
- native/router/rip/address-family/ipv4/vrf/distribute-list/accesslist-ifname/vrf
- native/router/rip/address-family/ipv4/vrf/distribute-list/accesslist-prefix-gateway-ifname/interface-routing-id
- native/router/rip/address-family/ipv4/vrf/distribute-list/accesslist-prefix-gateway-ifname/isis-tag
- native/router/rip/address-family/ipv4/vrf/distribute-list/accesslist-prefix-gateway-ifname/vrf
- native/router/rip/default/distribute-list/accesslist-ifname/interface-routing-id
- native/router/rip/default/distribute-list/accesslist-ifname/isis-tag
- native/router/rip/default/distribute-list/accesslist-ifname/vrf
- native/router/rip/default/distribute-list/accesslist-prefix-gateway-ifname/interface-routing-id
- native/router/rip/default/distribute-list/accesslist-prefix-gateway-ifname/isis-tag
- native/router/rip/default/distribute-list/accesslist-prefix-gateway-ifname/vrf
- native/router/rip/distribute-list/accesslist-ifname/interface-routing-id
- native/router/rip/distribute-list/accesslist-ifname/isis-tag
- native/router/rip/distribute-list/accesslist-ifname/vrf
- native/router/rip/distribute-list/accesslist-prefix-gateway-ifname/interface-routing-id
- native/router/rip/distribute-list/accesslist-prefix-gateway-ifname/isis-tag
- native/router/rip/distribute-list/accesslist-prefix-gateway-ifname/vrf

### Reason

Distribute-list under router rip has few invalid nodes in the yang module

## XPaths Deprecated

### Description

## XPaths Modified

- address-family-vrf-grouping(grouping)/timers/basic/flush
- address-family-vrf-grouping(grouping)/timers/basic/holddown
- address-family-vrf-grouping(grouping)/timers/basic/invalid
- address-family-vrf-grouping(grouping)/timers/basic/sleep
- address-family-vrf-grouping(grouping)/timers/basic/updates

### Description

The range has been illegally restricted

### Reason

Ranges are wrong and default values are missing for RIP timers

## XPaths Added

### Description
