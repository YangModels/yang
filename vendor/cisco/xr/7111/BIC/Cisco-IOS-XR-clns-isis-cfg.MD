## Cisco-IOS-XR-clns-isis-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Replace ospf-route-type by route-type since it is now used by protocols other than ospf. Replace boolean flag with an enum type to accommodate more values.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L2740)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/micro-loop-avoidance/enable
- (L3740)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/flex-algo-afs/flex-algo-af[af-name][saf-name]/maximum-paths
- (L3973)	/isis/instances/instance[instance-name]/standard-algos/standard-algo[standard-algo]/standard-algo-afs/standard-algo-af[af-name][saf-name]/maximum-paths

## XPaths Modified

- (L2748)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/micro-loop-avoidance/enable

