## Cisco-IOS-XE-bgp.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/bgp/redistribute-internal
- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/bgp/redistribute-internal
- native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-multicast/bgp/redistribute-internal
- native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/bgp/redistribute-internal
- native/router/bgp/bgp/bestpath/med/med-choice
- native/router/bgp/bgp/enforce-first-as

### Reason

xPaths moved from deprecated to obsolete after 2 releases.

## XPaths Deprecated

### Description

## XPaths Modified

- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/template/peer-policy/advertise-map/name
- metric-route-map-grouping-deprecated
- redistribute-include-connected-grouping-deprecated

### Description

1. The grouping 'metric-route-map-grouping-deprecated is removed

3. The grouping 'redistribute-include-connected-grouping-deprecated is removed

4. the range '[(0, 2147483647)]' is added

4. A new must statement added

### Reason

1. 'metric-route-map-grouping-deprecated' is not used in the model. Removing definitions that are not used.
2. 'redistribute-include-connected-grouping-deprecated' is not used in the model. Removing definitions that are not used.
3. Must statement was updated to remove reference to deprecated and obsoleted nodes.
4. Loopback range in yang interface-grouping was 0-4294967295. However, from device side loopback interface can only support range from 0 to 2147483647. Hence loopback range in yang was modified to be inline with device range

## XPaths Added

### Description
