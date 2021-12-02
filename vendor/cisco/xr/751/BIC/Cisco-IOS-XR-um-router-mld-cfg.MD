## Cisco-IOS-XR-um-router-mld-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed nsf container and its child nodes. It's due to the node that requires cisco-support task and it should not be exposed in yang model. Since it's not something that customers configure for their daiyly operations, it will not impact their operations. Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L590)	/router/mld/vrfs/vrf[vrf-name]/interfaces/interface[interface-name]/join-groups/join-group[group-address]/includes
- (L604)	/router/mld/vrfs/vrf[vrf-name]/interfaces/interface[interface-name]/join-groups/join-group[group-address]/excludes
- (L1158)	/router/mld/interfaces/interface[interface-name]/join-groups/join-group[group-address]/includes
- (L1172)	/router/mld/interfaces/interface[interface-name]/join-groups/join-group[group-address]/excludes

## XPaths Modified

- (L588)	/router/mld/vrfs/vrf[vrf-name]/interfaces/interface[interface-name]/join-groups/join-group[group-address]
- (L1156)	/router/mld/interfaces/interface[interface-name]/join-groups/join-group[group-address]

