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

- (L3862)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/affinity-include-anies/affinity-include-any
- (L3874)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/affinity-exclude-anies/affinity-exclude-any
- (L3886)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/affinity-include-alls/affinity-include-all
- (L3914)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/srlg-exclude-anies/srlg-exclude-any
- (L3983)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/reverse-affinity-include-anies/reverse-affinity-include-any
- (L3995)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/reverse-affinity-exclude-anies/reverse-affinity-exclude-any
- (L4007)	/isis/instances/instance[instance-name]/flex-algos/flex-algo[flex-algo]/reverse-affinity-include-alls/reverse-affinity-include-all
- (L4604)	/isis/instances/instance[instance-name]/interfaces/interface[interface-name]/int-affinity-table/flex-algos/flex-algo
- (L4618)	/isis/instances/instance[instance-name]/interfaces/interface[interface-name]/int-affinity-table/flex-algo-anomalies/flex-algo-anomaly

## XPaths Removed

N/A

## XPaths Modified

N/A

