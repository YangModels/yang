## Cisco-IOS-XR-um-multicast-routing-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

[CSCvw68672] Container maximum was removed. It's due to the node that requires cisco-support task and it should not be exposed in yang model. Since it's not something that customers configure for their daiyly operations, it will not impact their operations. [CSCvw53974] Renamed node name inerface to more appropriate interface. Also changed max string legth from 1024 to 800. CLI won't accept lenth 1024 so this will most like not break backward-comaptibility. Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured.

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

N/A

