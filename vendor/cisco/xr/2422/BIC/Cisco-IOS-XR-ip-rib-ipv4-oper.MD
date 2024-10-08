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

- (L1469)	/rib-stdby
- (L1488)	/rib

## XPaths Added

N/A

## XPaths Removed

- (L4658)	{IPV4-RIB-EDM-NHID-HIST-OBJ}/nh-addr
- (L4364)	{IPV4-RIB-EDM-ROUTE}/prefix
- (L3858)	{IPV4-RIB-EDM-PATH}/ipv4-rib-edm-path
- (L274)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/address
- (L279)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[address][prefix-length]/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L295)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/address
- (L300)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[address][prefix-length]/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L336)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/address
- (L341)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[address][prefix-length]/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L379)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/address
- (L384)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[address][prefix-length]/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L1354)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/address
- (L1359)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[address][prefix-length]/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3607)	{IPV4-RIB-EDM-PROTO}/protocol-route-memory
- (L3557)	{IPV4-RIB-EDM-PROTO}/protocol-names
- (L3562)	{IPV4-RIB-EDM-PROTO}/instance
- (L3567)	{IPV4-RIB-EDM-PROTO}/version
- (L3572)	{IPV4-RIB-EDM-PROTO}/redistribution-client-count
- (L3577)	{IPV4-RIB-EDM-PROTO}/protocol-clients-count
- (L3582)	{IPV4-RIB-EDM-PROTO}/routes-counts
- (L3590)	{IPV4-RIB-EDM-PROTO}/active-routes-count
- (L3595)	{IPV4-RIB-EDM-PROTO}/deleted-routes-count
- (L3600)	{IPV4-RIB-EDM-PROTO}/paths-count
- (L570)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/address
- (L575)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[address][prefix-length]/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L598)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/address
- (L603)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/longer-route-last-prefixes/longer-route-last-prefix/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L611)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/address
- (L616)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/longer-route-prefixes/longer-route-prefix/prefix-length
- (L3342)	{IPV4-RIB-EDM-NH-ADDR}/prefix
- (L3352)	{IPV4-RIB-EDM-NH-ADDR}/dest-addr
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3232)	{RIB-EDM-NH-PATH}/address
- (L631)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/address
- (L636)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/nexthops/nexthop/prefix-length
- (L3331)	{IPV4-RIB-EDM-NH-ADDR}/clients
- (L3346)	{IPV4-RIB-EDM-NH-ADDR}/prefix-len
- (L3441)	{IPV4-RIB-EDM-NH-ADDR}/num-algo-label
- (L699)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/address
- (L704)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[address][prefix-length][protoid]/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3173)	{IPV4-RIB-EDM-ADVERT}/ipv4-rib-edm-advert
- (L749)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/address
- (L754)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[address][prefix-length]/prefix-length
- (L2748)	{RIB-EDM-RPF-NBR-OBJ}/ip-address
- (L839)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/address
- (L844)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/rib-rpf-list-routes/rib-rpf-list-route/prefix-length
- (L4368)	{IPV4-RIB-EDM-ROUTE}/prefix-length-xr
- (L4463)	{IPV4-RIB-EDM-ROUTE}/paths-count
- (L4555)	{IPV4-RIB-EDM-ROUTE}/number-of-algorithm-labels
- (L3331)	{IPV4-RIB-EDM-NH-ADDR}/clients
- (L3346)	{IPV4-RIB-EDM-NH-ADDR}/prefix-len
- (L3441)	{IPV4-RIB-EDM-NH-ADDR}/num-algo-label
- (L1003)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/address
- (L1008)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-nexthop-prefixes/rib-nexthop-prefix/prefix-length
- (L2698)	{IPV4-RIB-EDM-NHID-OBJ}/nh-addr
- (L1904)	{EVT-HIST-ENTRY}/evt-data/entry
- (L1118)	{IPV4-RIB-EDM-CLIENT-REDIST-OPAQUE}/opaques
- (L1123)	{IPV4-RIB-EDM-CLIENT-REDIST-OPAQUE}/num-history-opaques
- (L969)	{IPV4-RIB-EDM-CLIENT-REDIST}/routes
- (L979)	{IPV4-RIB-EDM-CLIENT-REDIST}/num-history-routes
- (L4596)	{IPV4-RIB-EDM-UG-PRUNED-NODES}/pruned-node/entry
- (L191)	/{Table-id-range-ipv4}

## XPaths Modified

- (L4830)	{RIB-EDM-NHID-HIST-OBJ}/nh-addr
- (L275)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/routes/route[network]
- (L4510)	{RIB-EDM-ROUTE}/prefix
- (L4727)	{RIB-EDM-ROUTE}/route-path
- (L308)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/deleted-routes/deleted-route[network]
- (L332)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-best-routes/dest-best-route[address]/address
- (L343)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-q-routes/dest-q-route[network]
- (L363)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-backup-kw/dest-backup-prefixes/dest-backup-prefix[network-addr][network-prefix]
- (L411)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/destination-kw/dest-next-hop-routes/dest-next-hop-route[address]/address
- (L1394)	/{PROTOCOL-ROUTE-TABLE}/protocol-routes/protocol-route[network]
- (L582)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/q-routes/q-route[network]
- (L3487)	{RIB-EDM-NH-ADDR}/prefix
- (L3492)	{RIB-EDM-NH-ADDR}/dest-addr
- (L3381)	{RIB-EDM-NH-PATH}/address
- (L701)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/backup-routes/backup-route[network][protoid]
- (L744)	/{VRF-TABLE}/vrfs/vrf[vrf-name]/afs/af[af-name]/safs/saf[saf-name]/ip-rib-route-table-names/ip-rib-route-table-name[route-table-name]/adverts-list/advert-prefixes/advert-prefix[network-addr][network-prefix]
- (L2881)	{RIB-EDM-RPF-NBR-OBJ}/ip-address
- (L2887)	{RIB-EDM-RPF-NBR-OBJ}/afi
- (L887)	/{RIB-RPF-LIST-TABLE}/rib-rpfs/rib-rpf[table-id]/table-id
- (L954)	/{RIB-TABLE}/rib-table-ids/rib-table-id[tableid]/rib-table-itf-hndls/rib-table-itf-hndl[handle]/itf-route[address]/address
- (L3108)	{RIB-EDM-TABLE}/afi
- (L3113)	{RIB-EDM-TABLE}/safi
- (L2826)	{RIB-EDM-NHID-OBJ}/nh-addr
- (L2029)	{EVT-HIST-ENTRY}/evt-data
- (L1206)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-stats-nexthops/rib-client-stats-nexthop[table-id]/table-id
- (L1214)	{RIB-EDM-CLIENT-PROTO-TABLE-INFO}/afi
- (L1219)	{RIB-EDM-CLIENT-PROTO-TABLE-INFO}/safi
- (L1277)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-stats-redist-nexthops/rib-client-stats-redist-nexthop[table-id]/table-id
- (L875)	{RIB-EDM-CLIENT-REDIST-TABLE}/afi
- (L880)	{RIB-EDM-CLIENT-REDIST-TABLE}/safi
- (L1357)	/{RIB-CLIENT-TABLE}/rib-clients/rib-client[clientid]/rib-client-stats-redists/rib-client-stats-redist[table-id]/table-id
- (L4742)	{RIB-EDM-UG-PRUNED-NODES}/pruned-node

