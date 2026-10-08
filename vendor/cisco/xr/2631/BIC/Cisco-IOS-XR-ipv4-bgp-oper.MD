## Cisco-IOS-XR-ipv4-bgp-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated the internal structure and fields of update-generation-neighbor to add more statistics and other update-generation related information. Updated the internal structure and fields of update-generation-sub-group to add more statistics and other update-generation related information. Updated the internal structure and fields of update-generation-update-group to add more statistics and other update-generation related information. Updated the internal structure and fields of update-generation-address-family to add more statistics and other update-generation related information. Changed several bags/structures for BMP Outbound Post-Policy support. Reduced the number of BMP servers from 8 to 4. Converted BMPServerName/bmp-server-name to a key in bgp_bmp_convergence_per_server_t. Obsoleted BMP related nodes deprecated in 24.4.1.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L8146)	{BGP-BMP-SRVR-BAG}/bmp-update-modes-bitmap
- (L8340)	{BGP-BMP-SRVR-BAG}/bmp-rmon-local-rib-advertisement-interval-msec
- (L17747)	{BGP-BMP-TBL-GBL-BAG}/update-modes-bitmap
- (L24408)	{BGP-ADDRTYPE}/l2vpn-vpls-address
- (L24417)	{BGP-ADDRTYPE}/l2vpn-evpn-address
- (L24426)	{BGP-ADDRTYPE}/l2vpn-mspw-address
- (L24435)	{BGP-ADDRTYPE}/ipv4-sr-policy-address
- (L24444)	{BGP-ADDRTYPE}/ipv6-sr-policy-address
- (L24453)	{BGP-ADDRTYPE}/afi
- (L24458)	{BGP-ADDRTYPE}/ipv4-address
- (L24467)	{BGP-ADDRTYPE}/ipv4-mcast-address
- (L24476)	{BGP-ADDRTYPE}/ipv4-label-address
- (L24485)	{BGP-ADDRTYPE}/ipv4-tunnel-address
- (L24494)	{BGP-ADDRTYPE}/ipv4-mdt-address
- (L24503)	{BGP-ADDRTYPE}/ipv4vpn-address
- (L24512)	{BGP-ADDRTYPE}/ipv4vpna-mcastddress
- (L24521)	{BGP-ADDRTYPE}/ipv6-address
- (L24530)	{BGP-ADDRTYPE}/ipv6-mcast-address
- (L24539)	{BGP-ADDRTYPE}/ipv6-label-address
- (L24548)	{BGP-ADDRTYPE}/ipv6vpn-address
- (L24557)	{BGP-ADDRTYPE}/ipv6vpn-mcast-address
- (L24566)	{BGP-ADDRTYPE}/rt-constraint-address
- (L24575)	{BGP-ADDRTYPE}/ipv6mvpn-address
- (L24584)	{BGP-ADDRTYPE}/ipv4mvpn-address
- (L24593)	{BGP-ADDRTYPE}/ls-ls-address
- (L24602)	{BGP-ADDRTYPE}/ipv4-flowspec-address
- (L24611)	{BGP-ADDRTYPE}/ipv6-flowspec-address
- (L24620)	{BGP-ADDRTYPE}/ipv4vpn-flowspec-address
- (L24629)	{BGP-ADDRTYPE}/ipv6vpn-flowspec-address
- (L24408)	{BGP-ADDRTYPE}/l2vpn-vpls-address
- (L24417)	{BGP-ADDRTYPE}/l2vpn-evpn-address
- (L24426)	{BGP-ADDRTYPE}/l2vpn-mspw-address
- (L24435)	{BGP-ADDRTYPE}/ipv4-sr-policy-address
- (L24444)	{BGP-ADDRTYPE}/ipv6-sr-policy-address
- (L24453)	{BGP-ADDRTYPE}/afi
- (L24458)	{BGP-ADDRTYPE}/ipv4-address
- (L24467)	{BGP-ADDRTYPE}/ipv4-mcast-address
- (L24476)	{BGP-ADDRTYPE}/ipv4-label-address
- (L24485)	{BGP-ADDRTYPE}/ipv4-tunnel-address
- (L24494)	{BGP-ADDRTYPE}/ipv4-mdt-address
- (L24503)	{BGP-ADDRTYPE}/ipv4vpn-address
- (L24512)	{BGP-ADDRTYPE}/ipv4vpna-mcastddress
- (L24521)	{BGP-ADDRTYPE}/ipv6-address
- (L24530)	{BGP-ADDRTYPE}/ipv6-mcast-address
- (L24539)	{BGP-ADDRTYPE}/ipv6-label-address
- (L24548)	{BGP-ADDRTYPE}/ipv6vpn-address
- (L24557)	{BGP-ADDRTYPE}/ipv6vpn-mcast-address
- (L24566)	{BGP-ADDRTYPE}/rt-constraint-address
- (L24575)	{BGP-ADDRTYPE}/ipv6mvpn-address
- (L24584)	{BGP-ADDRTYPE}/ipv4mvpn-address
- (L24593)	{BGP-ADDRTYPE}/ls-ls-address
- (L24602)	{BGP-ADDRTYPE}/ipv4-flowspec-address
- (L24611)	{BGP-ADDRTYPE}/ipv6-flowspec-address
- (L24620)	{BGP-ADDRTYPE}/ipv4vpn-flowspec-address
- (L24629)	{BGP-ADDRTYPE}/ipv6vpn-flowspec-address
- (L24408)	{BGP-ADDRTYPE}/l2vpn-vpls-address
- (L24417)	{BGP-ADDRTYPE}/l2vpn-evpn-address
- (L24426)	{BGP-ADDRTYPE}/l2vpn-mspw-address
- (L24435)	{BGP-ADDRTYPE}/ipv4-sr-policy-address
- (L24444)	{BGP-ADDRTYPE}/ipv6-sr-policy-address
- (L24453)	{BGP-ADDRTYPE}/afi
- (L24458)	{BGP-ADDRTYPE}/ipv4-address
- (L24467)	{BGP-ADDRTYPE}/ipv4-mcast-address
- (L24476)	{BGP-ADDRTYPE}/ipv4-label-address
- (L24485)	{BGP-ADDRTYPE}/ipv4-tunnel-address
- (L24494)	{BGP-ADDRTYPE}/ipv4-mdt-address
- (L24503)	{BGP-ADDRTYPE}/ipv4vpn-address
- (L24512)	{BGP-ADDRTYPE}/ipv4vpna-mcastddress
- (L24521)	{BGP-ADDRTYPE}/ipv6-address
- (L24530)	{BGP-ADDRTYPE}/ipv6-mcast-address
- (L24539)	{BGP-ADDRTYPE}/ipv6-label-address
- (L24548)	{BGP-ADDRTYPE}/ipv6vpn-address
- (L24557)	{BGP-ADDRTYPE}/ipv6vpn-mcast-address
- (L24566)	{BGP-ADDRTYPE}/rt-constraint-address
- (L24575)	{BGP-ADDRTYPE}/ipv6mvpn-address
- (L24584)	{BGP-ADDRTYPE}/ipv4mvpn-address
- (L24593)	{BGP-ADDRTYPE}/ls-ls-address
- (L24602)	{BGP-ADDRTYPE}/ipv4-flowspec-address
- (L24611)	{BGP-ADDRTYPE}/ipv6-flowspec-address
- (L24620)	{BGP-ADDRTYPE}/ipv4vpn-flowspec-address
- (L24629)	{BGP-ADDRTYPE}/ipv6vpn-flowspec-address
- (L17747)	{BGP-BMP-TBL-GBL-BAG}/update-modes-bitmap
- (L8146)	{BGP-BMP-SRVR-BAG}/bmp-update-modes-bitmap
- (L8340)	{BGP-BMP-SRVR-BAG}/bmp-rmon-local-rib-advertisement-interval-msec

## XPaths Modified

- (L1145)	{Bgp-bmp-state}
- (L1146)	{Bgp-bmp-state}
- (L1150)	{Bgp-bmp-state}
- (L1151)	{Bgp-bmp-state}
- (L1155)	{Bgp-bmp-state}
- (L1156)	{Bgp-bmp-state}
- (L584)	/{BMP}/bmp/server-summaries/server-summary[server-id]/server-id
- (L637)	/{BMP}/bmp/server-neighbors/server-neighbor[server-id]/server-id
- (L14508)	{BGP-BMP-CONVERGENCE-BAG}/bmp-per-server-information[bmp-server-name]
- (L2498)	/bgp/instances/instance[instance-name]/instance-active/bmp-server/bmp-server-neighbors/bmp-server-neighbor[server-id]/server-id
- (L2514)	/bgp/instances/instance[instance-name]/instance-active/bmp-server/bmp-server-summaries/bmp-server-summary[server-id]/server-id

