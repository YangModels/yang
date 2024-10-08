## Cisco-IOS-XR-ip-rib-ipv6-oper.yang

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

- (L1471)	/ipv6-rib
- (L1529)	/ipv6-rib-stdby

## XPaths Added

N/A

## XPaths Removed

- (L2832)	{IPV6-RIB-EDM-NHID-HIST-OBJ}/nh-addr
- (L4264)	{IPV6-RIB-EDM-ROUTE}/prefix
- (L3758)	{IPV6-RIB-EDM-PATH}/ipv6-rib-edm-path
- (L623)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/address
- (L628)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L463)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/address
- (L468)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L323)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/address
- (L328)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L366)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/address
- (L371)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L1423)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/address
- (L1428)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3017)	{IPV6-RIB-EDM-PROTO}/protocol-route-memory
- (L2967)	{IPV6-RIB-EDM-PROTO}/protocol-names
- (L2972)	{IPV6-RIB-EDM-PROTO}/instance
- (L2977)	{IPV6-RIB-EDM-PROTO}/version
- (L2982)	{IPV6-RIB-EDM-PROTO}/redistribution-client-count
- (L2987)	{IPV6-RIB-EDM-PROTO}/protocol-clients-count
- (L2992)	{IPV6-RIB-EDM-PROTO}/routes-counts
- (L3000)	{IPV6-RIB-EDM-PROTO}/active-routes-count
- (L3005)	{IPV6-RIB-EDM-PROTO}/deleted-routes-count
- (L3010)	{IPV6-RIB-EDM-PROTO}/paths-count
- (L698)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/address
- (L703)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L491)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/address
- (L496)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L504)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/address
- (L509)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/prefix-length
- (L4578)	{IPV6-RIB-EDM-NH-ADDR}/prefix
- (L4588)	{IPV6-RIB-EDM-NH-ADDR}/dest-addr
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3492)	{RIB-EDM-NH-PATH}/address
- (L750)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/address
- (L755)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/prefix-length
- (L4567)	{IPV6-RIB-EDM-NH-ADDR}/clients
- (L4582)	{IPV6-RIB-EDM-NH-ADDR}/prefix-len
- (L4677)	{IPV6-RIB-EDM-NH-ADDR}/num-algo-label
- (L721)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/address
- (L726)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3031)	{IPV6-RIB-EDM-ADVERT}/ipv6-rib-edm-advert
- (L442)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/address
- (L447)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/prefix-length
- (L1303)	{RIB-EDM-RPF-NBR-OBJ}/ip-address
- (L901)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/address
- (L906)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/prefix-length
- (L4268)	{IPV6-RIB-EDM-ROUTE}/prefix-length-xr
- (L4363)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4455)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4567)	{IPV6-RIB-EDM-NH-ADDR}/clients
- (L4582)	{IPV6-RIB-EDM-NH-ADDR}/prefix-len
- (L4677)	{IPV6-RIB-EDM-NH-ADDR}/num-algo-label
- (L999)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/address
- (L1004)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/prefix-length
- (L858)	{IPV6-RIB-EDM-NHID-OBJ}/nh-addr
- (L2020)	{EVT-HIST-ENTRY}/evt-data/entry
- (L2345)	{IPV6-RIB-EDM-CLIENT-REDIST-OPAQUE}/opaques
- (L2350)	{IPV6-RIB-EDM-CLIENT-REDIST-OPAQUE}/num-history-opaques
- (L1535)	{IPV6-RIB-EDM-CLIENT-REDIST}/routes
- (L1545)	{IPV6-RIB-EDM-CLIENT-REDIST}/num-history-routes
- (L836)	{IPV6-RIB-EDM-UG-PRUNED-NODES}/pruned-node/entry
- (L198)	/{Nhid-entry-count-range-v6}
- (L206)	/{Nhid-hist-count-range-v6}
- (L214)	/{Rpf-head-count-range-v6}

## XPaths Modified

- (L252)	/{RIB-NH-ID-HISTORY-TABLE}/rib-nh-id-histories/rib-nh-id-history[nh-idi-hist-count]/nh-idi-hist-count
- (L4852)	{RIB-EDM-NHID-HIST-OBJ}/nh-addr
- (L297)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[network]
- (L4532)	{RIB-EDM-ROUTE}/prefix
- (L4749)	{RIB-EDM-ROUTE}/route-path
- (L330)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[network]
- (L354)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-best-routes/dest-best-route[address]/address
- (L365)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[network]
- (L385)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[network-addr][network-prefix]
- (L433)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-next-hop-routes/dest-next-hop-route[address]/address
- (L1416)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[network]
- (L604)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[network]
- (L3509)	{RIB-EDM-NH-ADDR}/prefix
- (L3514)	{RIB-EDM-NH-ADDR}/dest-addr
- (L3403)	{RIB-EDM-NH-PATH}/address
- (L723)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[network][protoid]
- (L766)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[network-addr][network-prefix]
- (L813)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/saf-name
- (L820)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/af-name
- (L2903)	{RIB-EDM-RPF-NBR-OBJ}/ip-address
- (L2909)	{RIB-EDM-RPF-NBR-OBJ}/afi
- (L901)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-summary-head-counts/rib-rpf-list-summary-head-count[rpf-head-count]/rpf-head-count
- (L976)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-table-itf-hndls/rib-table-itf-hndl[handle]/itf-route[address]/address
- (L3130)	{RIB-EDM-TABLE}/afi
- (L3135)	{RIB-EDM-TABLE}/safi
- (L1126)	/{RIB-NH-ID-SUMMARY-TABLE}/rib-nh-id-summaries/rib-nh-id-summary[tableid]/rib-nh-ids/rib-nh-id[nh-id-entry-count]/nh-id-entry-count
- (L2848)	{RIB-EDM-NHID-OBJ}/nh-addr
- (L2051)	{EVT-HIST-ENTRY}/evt-data
- (L1236)	{RIB-EDM-CLIENT-PROTO-TABLE-INFO}/afi
- (L1241)	{RIB-EDM-CLIENT-PROTO-TABLE-INFO}/safi
- (L897)	{RIB-EDM-CLIENT-REDIST-TABLE}/afi
- (L902)	{RIB-EDM-CLIENT-REDIST-TABLE}/safi
- (L4764)	{RIB-EDM-UG-PRUNED-NODES}/pruned-node

