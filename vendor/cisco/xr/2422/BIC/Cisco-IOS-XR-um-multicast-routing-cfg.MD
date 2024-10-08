## Cisco-IOS-XR-um-multicast-routing-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Changed the next-hop address type in static rpf to ip from ipv6.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L954)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/interface
- (L1901)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/interface
- (L2988)	/multicast-routing/address-family/ipv4/interface
- (L3927)	/multicast-routing/address-family/ipv6/interface

## XPaths Modified

- (L2205)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/static-rpf/address-range[prefix-address][prefix-length]/next-hop-address
- (L4322)	/multicast-routing/address-family/ipv6/static-rpf/address-range[prefix-address][prefix-length]/next-hop-address

