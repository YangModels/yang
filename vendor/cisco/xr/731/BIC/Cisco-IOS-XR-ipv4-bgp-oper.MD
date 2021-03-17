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

- (L345)	/{VRFDBVRF-TABLE}/vrfdbvr-ftableentries
- (L1307)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry/orr-root-address
- (L1312)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry/orr-sec-root-address
- (L1317)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry/orr-ter-root-address
- (L1322)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry
- (L3249)	{BGP-NBR-RANGE-AF}/max-prefix-exceed-discard-paths
- (L8125)	{BGP-NBR-AF}/max-prefix-exceed-discard-paths
- (L8608)	{BGP-NBR-AF}/slow-peer
- (L10237)	{BGP-NET-BAG}/best-path-orr-bitfield
- (L10242)	{BGP-NET-BAG}/add-path-orr-bitfield
- (L12133)	{BGP-GLOBAL-PROCESS-INFO-AF-VRF}/isvrf-s-rv6-enabled
- (L12153)	{BGP-GLOBAL-PROCESS-INFO-AF-VRF}/isvrfall-s-rv6-enabled
- (L14117)	{BGP-BAG-PSID-SRV6-SVC-SUBSUBTLV-INFO}/endpoint-behavior
- (L15522)	{BGP-PATH}/best-path-orr-bitfield
- (L15527)	{BGP-PATH}/add-path-orr-bitfield
- (L16065)	{BGP-AF-DEP}/orr-root-address
- (L16086)	{BGP-AF-DEP}/orr-info
- (L17335)	{BGP-AF-INDEP}/epe-peer-set-identity

## XPaths Modified

- (L1391)	{Bgp-bp-stage}
- (L1392)	{Bgp-bp-stage}
- (L1396)	{Bgp-bp-stage}
- (L1397)	{Bgp-bp-stage}
- (L1401)	{Bgp-bp-stage}
- (L1402)	{Bgp-bp-stage}
- (L1406)	{Bgp-bp-stage}
- (L1407)	{Bgp-bp-stage}
- (L1411)	{Bgp-bp-stage}
- (L1412)	{Bgp-bp-stage}
- (L1416)	{Bgp-bp-stage}
- (L1417)	{Bgp-bp-stage}
- (L1421)	{Bgp-bp-stage}
- (L1422)	{Bgp-bp-stage}
- (L1426)	{Bgp-bp-stage}
- (L1427)	{Bgp-bp-stage}
- (L1431)	{Bgp-bp-stage}
- (L1432)	{Bgp-bp-stage}
- (L1436)	{Bgp-bp-stage}
- (L1437)	{Bgp-bp-stage}
- (L1441)	{Bgp-bp-stage}
- (L1442)	{Bgp-bp-stage}
- (L1446)	{Bgp-bp-stage}
- (L1447)	{Bgp-bp-stage}
- (L1451)	{Bgp-bp-stage}
- (L1452)	{Bgp-bp-stage}
- (L1456)	{Bgp-bp-stage}
- (L1457)	{Bgp-bp-stage}
- (L1461)	{Bgp-bp-stage}
- (L1462)	{Bgp-bp-stage}
- (L1466)	{Bgp-bp-stage}
- (L1467)	{Bgp-bp-stage}
- (L1471)	{Bgp-bp-stage}
- (L1472)	{Bgp-bp-stage}
- (L1477)	{Bgp-bp-stage}
- (L1478)	{Bgp-bp-stage}
- (L1329)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry[orr-grp-name]

