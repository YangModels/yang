## Cisco-IOS-XR-ip-rib-ipv4-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

reworked all RIB schemas to union IP addresses.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L1625)	/rib-stdby
- (L1644)	/rib

## XPaths Added

N/A

## XPaths Removed

- (L3895)	{IPV4-RIB-EDM-PATH}/ipv4-rib-edm-path
- (L283)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/address
- (L288)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L304)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/address
- (L309)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L345)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/address
- (L350)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L388)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/address
- (L393)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L1363)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/address
- (L1368)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L579)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/address
- (L584)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L607)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/address
- (L612)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L620)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/address
- (L625)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/prefix-length
- (L4345)	{RIB-EDM-ALGO-LABEL-SET}
- (L4346)	{RIB-EDM-ALGO-LABEL-SET}/algorithm-id
- (L4351)	{RIB-EDM-ALGO-LABEL-SET}/label
- (L4356)	{RIB-EDM-ALGO-LABEL-SET}/metric
- (L640)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/address
- (L645)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/prefix-length
- (L3392)	{IPV4-RIB-EDM-NH-ADDR}/clients
- (L3397)	{IPV4-RIB-EDM-NH-ADDR}/resolved-route
- (L3487)	{IPV4-RIB-EDM-NH-ADDR}/num-algo-label
- (L708)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/address
- (L713)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3224)	{IPV4-RIB-EDM-ADVERT}/ipv4-rib-edm-advert
- (L758)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/address
- (L763)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/prefix-length
- (L848)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/address
- (L853)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/prefix-length
- (L4493)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4585)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3392)	{IPV4-RIB-EDM-NH-ADDR}/clients
- (L3397)	{IPV4-RIB-EDM-NH-ADDR}/resolved-route
- (L3487)	{IPV4-RIB-EDM-NH-ADDR}/num-algo-label
- (L1012)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/address
- (L1017)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/prefix-length
- (L1174)	{IPV4-RIB-EDM-CLIENT-REDIST-OPAQUE}/opaques
- (L1179)	{IPV4-RIB-EDM-CLIENT-REDIST-OPAQUE}/num-history-opaques
- (L1025)	{IPV4-RIB-EDM-CLIENT-REDIST}/routes
- (L1035)	{IPV4-RIB-EDM-CLIENT-REDIST}/num-history-routes
- (L200)	/{Table-id-range-ipv4}

## XPaths Modified

- (L311)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[network]
- (L5480)	{RIB-EDM-ROUTE}/route-path
- (L344)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[network]
- (L368)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-best-routes/dest-best-route[address]/address
- (L379)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[network]
- (L399)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[network-addr][network-prefix]
- (L504)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-next-hop-routes/dest-next-hop-route[address]/address
- (L1549)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[network]
- (L675)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[network]
- (L791)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop[network][table-id][unresolved-nh-tree][exact-match][allow-default][recurse][cross-table][pack-sfs][pack-backup-paths][backup-route][best-metric][algo-label-set][track-cross-table]/algo-label-set
- (L832)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[network][protoid]
- (L875)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[network-addr][network-prefix]
- (L1018)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/table-id
- (L1085)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-table-itf-hndls/rib-table-itf-hndl[handle]/itf-route[address]/address
- (L1158)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix[network][unresolved-nh-tree]/rib-nexthop-routes/rib-nexthop-route[table-id][exact-match][allow-default][recurse][cross-table][pack-sfs][pack-backup-paths][backup-route][best-metric][algo-label-set][track-cross-table]/algo-label-set
- (L1352)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-stats-nexthops/rib-client-stats-nexthop[table-id]/table-id
- (L1423)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-stats-redist-nexthops/rib-client-stats-redist-nexthop[table-id]/table-id
- (L1452)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-redists/rib-client-redist[table-id]/rib-client-redist-protos/rib-client-redist-proto[proto-id][channel-id]
- (L1512)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-stats-redists/rib-client-stats-redist[table-id]/table-id

