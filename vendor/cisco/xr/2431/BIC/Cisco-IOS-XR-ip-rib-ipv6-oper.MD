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

- (L1497)	/ipv6-rib
- (L1556)	/ipv6-rib-stdby

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
- (L2345)	{IPV6-RIB-EDM-CLIENT-REDIST-OPAQUE}/opaques
- (L2350)	{IPV6-RIB-EDM-CLIENT-REDIST-OPAQUE}/num-history-opaques
- (L1535)	{IPV6-RIB-EDM-CLIENT-REDIST}/routes
- (L1545)	{IPV6-RIB-EDM-CLIENT-REDIST}/num-history-routes
- (L198)	/{Nhid-entry-count-range-v6}
- (L206)	/{Nhid-hist-count-range-v6}
- (L214)	/{Rpf-head-count-range-v6}

## XPaths Modified

- (L249)	/{RIB-NH-ID-HISTORY-TABLE}/rib-nh-id-histories/rib-nh-id-history[nh-idi-hist-count]/nh-idi-hist-count
- (L5565)	{RIB-EDM-NHID-HIST-OBJ}/nh-addr
- (L294)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[network]
- (L5236)	{RIB-EDM-ROUTE}/prefix
- (L5458)	{RIB-EDM-ROUTE}/route-path
- (L327)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[network]
- (L351)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-best-routes/dest-best-route[address]/address
- (L362)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[network]
- (L382)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[network-addr][network-prefix]
- (L430)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-next-hop-routes/dest-next-hop-route[address]/address
- (L1422)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[network]
- (L601)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[network]
- (L4149)	{RIB-EDM-NH-ADDR}/prefix
- (L4154)	{RIB-EDM-NH-ADDR}/dest-addr
- (L4043)	{RIB-EDM-NH-PATH}/address
- (L720)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[network][protoid]
- (L763)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[network-addr][network-prefix]
- (L810)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/saf-name
- (L817)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/af-name
- (L3523)	{RIB-EDM-RPF-NBR-OBJ}/ip-address
- (L3529)	{RIB-EDM-RPF-NBR-OBJ}/afi
- (L898)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-summary-head-counts/rib-rpf-list-summary-head-count[rpf-head-count]/rpf-head-count
- (L973)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-table-itf-hndls/rib-table-itf-hndl[handle]/itf-route[address]/address
- (L3770)	{RIB-EDM-TABLE}/afi
- (L3775)	{RIB-EDM-TABLE}/safi
- (L1123)	/{RIB-NH-ID-SUMMARY-TABLE}/rib-nh-id-summaries/rib-nh-id-summary[tableid]/rib-nh-ids/rib-nh-id[nh-id-entry-count]/nh-id-entry-count
- (L3468)	{RIB-EDM-NHID-OBJ}/nh-addr
- (L1852)	{RIB-EDM-CLIENT-PROTO-TABLE-INFO}/afi
- (L1857)	{RIB-EDM-CLIENT-PROTO-TABLE-INFO}/safi
- (L1325)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-redists/rib-client-redist[table-id]/rib-client-redist-protos/rib-client-redist-proto[proto-id][channel-id]
- (L1508)	{RIB-EDM-CLIENT-REDIST-TABLE}/afi
- (L1513)	{RIB-EDM-CLIENT-REDIST-TABLE}/safi

