## Cisco-IOS-XR-ipv4-bgp-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Naming convention changed for ORR groups. The term policy is changed to group to be consistent throughout. Naming convention changes for SR v6 and endpoint. EPE peerset under BGP neighbor is changed from integer to bitfield as multiple peersets can be enabled and single integer is not enough. A common slow peer flag is replaced with granular multiple flags. Extra step added in BGP bestpath algorithm.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L12922)	{BGP-PATH-BAG}/label-oor-version
- (L13705)	{BGP-PROCESS-INFO-AF-GBL}/version-wrap-start-time-spec
- (L13710)	{BGP-PROCESS-INFO-AF-GBL}/version-wrap-done-time-spec
- (L13757)	{BGP-PROCESS-INFO-AF-GBL}/version-wrapped-tid

## XPaths Modified

N/A

