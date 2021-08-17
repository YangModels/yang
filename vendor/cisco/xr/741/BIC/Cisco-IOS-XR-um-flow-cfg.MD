## Cisco-IOS-XR-um-flow-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Add a new container gtp and updated must statements to correctly define constraints with the new container as all the sibling containers are mutually exclusive, which does not break backward-compatibility. No impact on existing operations.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L1855)	/sampler-maps/sampler-map[sampler-map-name]/random
- (L1866)	/sampler-maps/sampler-map[sampler-map-name]/out-of

## XPaths Removed

N/A

## XPaths Modified

- (L1283)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4
- (L1297)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/destination
- (L1312)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/destination-tos
- (L1327)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/as
- (L1342)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/protocol-port
- (L1357)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/prefix
- (L1372)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/source-prefix
- (L1387)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/destination-prefix
- (L1402)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/as-tos
- (L1417)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/protocol-port-tos
- (L1432)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/prefix-tos
- (L1447)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/source-prefix-tos
- (L1462)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/destination-prefix-tos
- (L1477)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/prefix-port
- (L1492)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/bgp-nexthop-tos
- (L1506)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv4/peer-as
- (L1532)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/datalinksectiondump
- (L1543)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv6
- (L1549)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv6/destination
- (L1555)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/ipv6/peer-as
- (L1574)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/mpls
- (L1613)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/map-t
- (L1624)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/sflow
- (L1645)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/default-rtp
- (L1655)	/flow/monitor-map/monitor-maps/monitor-map[monitor-map-name]/record/default-mdi

