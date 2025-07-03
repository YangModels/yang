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

- (L1626)	/ipv6-rib
- (L1685)	/ipv6-rib-stdby

## XPaths Added

N/A

## XPaths Removed

- (L4231)	{RIB-EDM-ROUTE-SRV6-INFO}/is-srv6-endpoint
- (L3800)	{IPV6-RIB-EDM-PATH}/ipv6-rib-edm-path
- (L632)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/address
- (L637)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L472)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/address
- (L477)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L332)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/address
- (L337)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L375)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/address
- (L380)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L1432)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/address
- (L1437)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L707)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/address
- (L712)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L500)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/address
- (L505)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L513)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/address
- (L518)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/prefix-length
- (L4250)	{RIB-EDM-ALGO-LABEL-SET}
- (L4251)	{RIB-EDM-ALGO-LABEL-SET}/algorithm-id
- (L4256)	{RIB-EDM-ALGO-LABEL-SET}/label
- (L4261)	{RIB-EDM-ALGO-LABEL-SET}/metric
- (L759)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/address
- (L764)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/prefix-length
- (L4649)	{IPV6-RIB-EDM-NH-ADDR}/clients
- (L4654)	{IPV6-RIB-EDM-NH-ADDR}/resolved-route
- (L4744)	{IPV6-RIB-EDM-NH-ADDR}/num-algo-label
- (L730)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/address
- (L735)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L3018)	{IPV6-RIB-EDM-ADVERT}/ipv6-rib-edm-advert
- (L451)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/address
- (L456)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/prefix-length
- (L1238)	{RIB-EDM-STATS-BATCH-SUMMARY}/attribute-arg-rx
- (L910)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/address
- (L915)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/prefix-length
- (L4383)	{IPV6-RIB-EDM-ROUTE}/paths-count
- (L4475)	{IPV6-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4491)	{IPV6-RIB-EDM-ROUTE}/has-aft
- (L4649)	{IPV6-RIB-EDM-NH-ADDR}/clients
- (L4654)	{IPV6-RIB-EDM-NH-ADDR}/resolved-route
- (L4744)	{IPV6-RIB-EDM-NH-ADDR}/num-algo-label
- (L1008)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/address
- (L1013)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/prefix-length
- (L2277)	{IPV6-RIB-EDM-CLIENT-STATS-SUMMARY}/attribute
- (L2516)	{RIB-EDM-STATS-COMPLETE-UPDATE}/bad-args
- (L2521)	{RIB-EDM-STATS-COMPLETE-UPDATE}/success
- (L2396)	{IPV6-RIB-EDM-CLIENT-REDIST-OPAQUE}/opaques
- (L2401)	{IPV6-RIB-EDM-CLIENT-REDIST-OPAQUE}/num-history-opaques
- (L1591)	{IPV6-RIB-EDM-CLIENT-REDIST}/routes
- (L1601)	{IPV6-RIB-EDM-CLIENT-REDIST}/num-history-routes
- (L14)	/
- (L207)	/{Nhid-entry-count-range-v6}
- (L215)	/{Nhid-hist-count-range-v6}
- (L223)	/{Rpf-head-count-range-v6}

## XPaths Modified

- (L406)	{Rib-opaque}
- (L407)	{Rib-opaque}
- (L288)	/{RIB-NH-ID-HISTORY-TABLE}/rib-nh-id-histories/rib-nh-id-history[nh-idi-hist-count]/nh-idi-hist-count
- (L333)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[network]
- (L5378)	{RIB-EDM-ROUTE}/route-path
- (L366)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[network]
- (L390)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-best-routes/dest-best-route[address]/address
- (L401)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[network]
- (L421)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[network-addr][network-prefix]
- (L526)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-next-hop-routes/dest-next-hop-route[address]/address
- (L1571)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[network]
- (L697)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[network]
- (L813)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop[network][table-id][unresolved-nh-tree][exact-match][allow-default][recurse][cross-table][pack-sfs][pack-backup-paths][backup-route][best-metric][algo-label-set][track-cross-table]/algo-label-set
- (L854)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[network][protoid]
- (L897)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[network-addr][network-prefix]
- (L944)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/saf-name
- (L951)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/af-name
- (L1032)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-summary-head-counts/rib-rpf-list-summary-head-count[rpf-head-count]/rpf-head-count
- (L1107)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-table-itf-hndls/rib-table-itf-hndl[handle]/itf-route[address]/address
- (L1180)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix[network][unresolved-nh-tree]/rib-nexthop-routes/rib-nexthop-route[table-id][exact-match][allow-default][recurse][cross-table][pack-sfs][pack-backup-paths][backup-route][best-metric][algo-label-set][track-cross-table]/algo-label-set
- (L1272)	/{RIB-NH-ID-SUMMARY-TABLE}/rib-nh-id-summaries/rib-nh-id-summary[tableid]/rib-nh-ids/rib-nh-id[nh-id-entry-count]/nh-id-entry-count
- (L1474)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-redists/rib-client-redist[table-id]/rib-client-redist-protos/rib-client-redist-proto[proto-id][channel-id]

