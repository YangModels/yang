## Cisco-IOS-XR-um-router-igmp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added node 'disable' under igmp default and vrf containers. non-backward compatible addition, in 'must not(../disable)' under container enable/disable for mutual exclusivity.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L199)	/router/igmp/vrfs/vrf[vrf-name]/explicit-tracking/access-list
- (L799)	/router/igmp/explicit-tracking/access-list

## XPaths Removed

- (L616)	/router/igmp/vrfs/vrf[vrf-name]/interfaces/interface[interface-name]/join-groups/join-group[group-address]/includes
- (L630)	/router/igmp/vrfs/vrf[vrf-name]/interfaces/interface[interface-name]/join-groups/join-group[group-address]/excludes
- (L1248)	/router/igmp/interfaces/interface[interface-name]/join-groups/join-group[group-address]/includes
- (L1262)	/router/igmp/interfaces/interface[interface-name]/join-groups/join-group[group-address]/excludes

## XPaths Modified

- (L616)	/router/igmp/vrfs/vrf[vrf-name]/interfaces/interface[interface-name]/join-groups/join-group[group-address]
- (L1250)	/router/igmp/interfaces/interface[interface-name]/join-groups/join-group[group-address]

