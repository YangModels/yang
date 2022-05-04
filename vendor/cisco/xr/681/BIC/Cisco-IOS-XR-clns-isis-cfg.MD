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

- (L2388)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/redistributions/redistribution[protocol-name]/{REDISTRIBUTION-CONTENT}/ospf-route-type

## XPaths Modified

- (L2137)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/segment-routing/prefix-sid-map/advertise-local
- (L3121)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/single-topology

