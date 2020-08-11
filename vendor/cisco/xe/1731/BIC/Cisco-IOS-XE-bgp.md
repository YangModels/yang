## Cisco-IOS-XE-bgp


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/router/bgp/address-family/no-vrf/ipv4/ipv4-multicast/redistribute/nat-route
- native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/redistribute/nat-route
- native/router/bgp/address-family/no-vrf/link-state/link-state/domain-distinguisher
- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/redistribute-vrf/nat-route
- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/redistribute-vrf/nat-route
- native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/redistribute/nat-route
- native/router/bgp/scope/global/address-family/no-vrf/link-state/link-state/domain-distinguisher
- native/router/bgp/scope/vrf/address-family/no-vrf/link-state/link-state/domain-distinguisher

### Description

1. The presence 'BGP Domain distinguisher' is illegally added

2. The presence 'NAT Route' is illegally added

### Reason

The containers (domain-distinguisher and nat) are allowed to be configured without any sub-options

## XPaths Added

### Description
