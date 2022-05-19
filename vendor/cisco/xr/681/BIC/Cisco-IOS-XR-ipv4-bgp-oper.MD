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

- (L311)	/{VRFDBVRF-TABLE}/vrfdbvr-ftableentries
- (L1294)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry/orr-root-address
- (L1299)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry/orr-sec-root-address
- (L1304)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry/orr-ter-root-address
- (L1309)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry
- (L1215)	/{AF-TABLE}/afs/af[af-name]/epes
- (L2088)	{BGP-EDM-RPKI-ROUTE}/refcount
- (L2752)	{BGP-EDM-LOCATOR-ENTRY}/stale
- (L5132)	{BGP-PROCESS-INFO-GBL}/prefix-sids-rv6vpnsid-count
- (L5137)	{BGP-PROCESS-INFO-GBL}/prefix-sids-rv6vpnsid-memory
- (L6465)	{BGP-GLOBAL-PROCESS-INFO-GBL}/gshut-all-nbrs-ts
- (L6470)	{BGP-GLOBAL-PROCESS-INFO-GBL}/gshu-all-nbrs-age
- (L9497)	{BGP-EPE-SET-BAG}/epe-key-length-xr
- (L8266)	{BGP-NBR-AF}/slow-peer
- (L9947)	{BGP-NET-BAG}/has-s-rv6sid-allocated
- (L9952)	{BGP-NET-BAG}/srv6sid-address
- (L9957)	{BGP-NET-BAG}/srv6sid-address-len
- (L9973)	{BGP-NET-BAG}/best-path-orr-bitfield
- (L9978)	{BGP-NET-BAG}/add-path-orr-bitfield
- (L11857)	{BGP-GLOBAL-PROCESS-INFO-AF-VRF}/isvrf-s-rv6-enabled
- (L11872)	{BGP-GLOBAL-PROCESS-INFO-AF-VRF}/isvrfall-s-rv6-enabled
- (L12149)	{BGP-RPC-SET-BAG}/srv6sid-address
- (L12154)	{BGP-RPC-SET-BAG}/srv6sid-address-len
- (L13843)	{BGP-COMMON-ATTR-ENTRY}/prefix-sids-rv6vpnsid
- (L13848)	{BGP-COMMON-ATTR-ENTRY}/prefix-sid-unk-tl-vs
- (L13942)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sid-label-indexpresent
- (L13947)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sid-orig-srg-bpresent
- (L13952)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sids-rv6vpnsi-dpresent
- (L13957)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sid-unk-tl-vspresent
- (L15072)	{BGP-PATH}/best-path-orr-bitfield
- (L15077)	{BGP-PATH}/add-path-orr-bitfield
- (L15615)	{BGP-AF-DEP}/orr-root-address
- (L15636)	{BGP-AF-DEP}/orr-info
- (L16732)	{BGP-AF-INDEP}/suppress4-byte-as

## XPaths Modified

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
- (L1456)	{Bgp-bp-stage}
- (L1457)	{Bgp-bp-stage}
- (L1461)	{Bgp-bp-stage}
- (L1462)	{Bgp-bp-stage}
- (L1466)	{Bgp-bp-stage}
- (L1467)	{Bgp-bp-stage}
- (L1471)	{Bgp-bp-stage}
- (L1472)	{Bgp-bp-stage}
- (L1476)	{Bgp-bp-stage}
- (L1477)	{Bgp-bp-stage}
- (L1481)	{Bgp-bp-stage}
- (L1482)	{Bgp-bp-stage}
- (L1486)	{Bgp-bp-stage}
- (L1487)	{Bgp-bp-stage}
- (L1492)	{Bgp-bp-stage}
- (L1493)	{Bgp-bp-stage}
- (L1339)	/{AF-TABLE}/afs/af[af-name]/orr-group-table-entries/orr-group-table-entry[orr-grp-name]
- (L16464)	{BGP-CONFIG-RELATIVES-BAG}/address-family-identifier
- (L17129)	{BGP-CONFIG-ENTID}/bgp-config-entid/address-family-identifier
- (L18238)	{BGP-CONFIG-ENTITY-BAG}/address-family-identifier

