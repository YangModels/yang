## Cisco-IOS-XR-clns-isis-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Replace ospf-route-type by route-type since it is now used by protocols other than ospf. Replace boolean flag with an enum type to accommodate more values.

## XPaths Obsoleted

- (L3066)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]
- (L3060)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals

## XPaths Deprecated

N/A

## XPaths Added

- (L2960)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]/maximum-wait
- (L2982)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]/secondary-wait

## XPaths Removed

- (L3066)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]
- (L3102)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]/unused1
- (L3109)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]/unused2
- (L3116)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]/unused3
- (L3123)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]/unused4
- (L3060)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals
- (L2675)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-backoffs
- (L2675)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-backoffs
- (L2675)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-backoffs

## XPaths Modified

- (L3047)	/isis/instances/instance[instance-name]/afs/af[af-name][saf-name]/{AF-CONTENT}/spf-intervals/spf-interval[level]/backoff-algorithm

