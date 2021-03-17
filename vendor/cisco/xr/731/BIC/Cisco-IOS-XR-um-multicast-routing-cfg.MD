## Cisco-IOS-XR-um-multicast-routing-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Container maximum was removed. It's due to the node that requires cisco-support task and it should not be exposed in yang model. Since it's not something that customers configure for their daiyly operations, it will not impact their operations.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L1037)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/static-rpf/address-range[prefix-address][prefix-length]/interface
- (L1861)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/static-rpf/address-range[prefix-address][prefix-length]/interface
- (L2816)	/multicast-routing/address-family/ipv4/static-rpf/address-range[prefix-address][prefix-length]/interface
- (L3617)	/multicast-routing/address-family/ipv6/static-rpf/address-range[prefix-address][prefix-length]/interface

## XPaths Removed

- (L864)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/static-rpf/address-range[prefix-address][prefix-length]/inerface
- (L1684)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/static-rpf/address-range[prefix-address][prefix-length]/inerface
- (L2496)	/multicast-routing/address-family/ipv4/static-rpf/address-range[prefix-address][prefix-length]/inerface
- (L2338)	/multicast-routing/address-family/ipv4/maximum
- (L3306)	/multicast-routing/address-family/ipv6/static-rpf/address-range[prefix-address][prefix-length]/inerface
- (L3154)	/multicast-routing/address-family/ipv6/maximum

## XPaths Modified

- (L73)	/multicast-routing/vrfs/vrf[vrf-name]/vrf-name
- (L438)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/mdt/default/p2mp-te/attribute-set
- (L446)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/mdt/default/p2mp-te/attribute-set
- (L456)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/mdt/default/p2mp-te/static
- (L521)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/mdt/partitioned/p2mp-te/attribute-set
- (L1009)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv4/bgp/auto-discovery/inherit-vrf-ri/vrf
- (L1365)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/mdt/default/p2mp-te/attribute-set
- (L1373)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/mdt/default/p2mp-te/attribute-set
- (L1383)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/mdt/default/p2mp-te/static
- (L1409)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/mdt/partitioned/p2mp-te/attribute-set
- (L1833)	/multicast-routing/vrfs/vrf[vrf-name]/address-family/ipv6/bgp/auto-discovery/inherit-vrf-ri/vrf
- (L2133)	/multicast-routing/address-family/ipv4/mdt/default/p2mp-te/attribute-set
- (L2139)	/multicast-routing/address-family/ipv4/mdt/default/p2mp-te/attribute-set
- (L2266)	/multicast-routing/address-family/ipv4/mdt/partitioned/p2mp-te/attribute-set
- (L2788)	/multicast-routing/address-family/ipv4/bgp/auto-discovery/inherit-vrf-ri/vrf
- (L3044)	/multicast-routing/address-family/ipv6/mdt/default/p2mp-te/attribute-set
- (L3122)	/multicast-routing/address-family/ipv6/mdt/partitioned/p2mp-te/attribute-set
- (L3589)	/multicast-routing/address-family/ipv6/bgp/auto-discovery/inherit-vrf-ri/vrf

