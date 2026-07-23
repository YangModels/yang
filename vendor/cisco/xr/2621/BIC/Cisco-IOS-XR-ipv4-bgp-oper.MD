## Cisco-IOS-XR-ipv4-bgp-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated bgp_updgrp_wdr_types with new enum value for EVPN IMET PMSI Tunnel ID not v4.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L20396)	{BGP-ATTR}/ribrnh-ip
- (L20396)	{BGP-ATTR}/ribrnh-ip
- (L21587)	{BGP-LRNH-ENTRY-INFO}/lrnh-addr
- (L21592)	{BGP-LRNH-ENTRY-INFO}/lrnhv6-addr
- (L21527)	{BGP-RNH-ENTRY-INFO}/lrnh-addr
- (L20396)	{BGP-ATTR}/ribrnh-ip
- (L20396)	{BGP-ATTR}/ribrnh-ip
- (L24254)	{BGP-ADDRTYPE}/l2vpn-vpls-address
- (L24263)	{BGP-ADDRTYPE}/l2vpn-evpn-address
- (L24272)	{BGP-ADDRTYPE}/l2vpn-mspw-address
- (L24281)	{BGP-ADDRTYPE}/ipv4-sr-policy-address
- (L24290)	{BGP-ADDRTYPE}/ipv6-sr-policy-address
- (L24299)	{BGP-ADDRTYPE}/afi
- (L24304)	{BGP-ADDRTYPE}/ipv4-address
- (L24313)	{BGP-ADDRTYPE}/ipv4-mcast-address
- (L24322)	{BGP-ADDRTYPE}/ipv4-label-address
- (L24331)	{BGP-ADDRTYPE}/ipv4-tunnel-address
- (L24340)	{BGP-ADDRTYPE}/ipv4-mdt-address
- (L24349)	{BGP-ADDRTYPE}/ipv4vpn-address
- (L24358)	{BGP-ADDRTYPE}/ipv4vpna-mcastddress
- (L24367)	{BGP-ADDRTYPE}/ipv6-address
- (L24376)	{BGP-ADDRTYPE}/ipv6-mcast-address
- (L24385)	{BGP-ADDRTYPE}/ipv6-label-address
- (L24394)	{BGP-ADDRTYPE}/ipv6vpn-address
- (L24403)	{BGP-ADDRTYPE}/ipv6vpn-mcast-address
- (L24412)	{BGP-ADDRTYPE}/rt-constraint-address
- (L24421)	{BGP-ADDRTYPE}/ipv6mvpn-address
- (L24430)	{BGP-ADDRTYPE}/ipv4mvpn-address
- (L24439)	{BGP-ADDRTYPE}/ls-ls-address
- (L24448)	{BGP-ADDRTYPE}/ipv4-flowspec-address
- (L24457)	{BGP-ADDRTYPE}/ipv6-flowspec-address
- (L24466)	{BGP-ADDRTYPE}/ipv4vpn-flowspec-address
- (L24475)	{BGP-ADDRTYPE}/ipv6vpn-flowspec-address
- (L24254)	{BGP-ADDRTYPE}/l2vpn-vpls-address
- (L24263)	{BGP-ADDRTYPE}/l2vpn-evpn-address
- (L24272)	{BGP-ADDRTYPE}/l2vpn-mspw-address
- (L24281)	{BGP-ADDRTYPE}/ipv4-sr-policy-address
- (L24290)	{BGP-ADDRTYPE}/ipv6-sr-policy-address
- (L24299)	{BGP-ADDRTYPE}/afi
- (L24304)	{BGP-ADDRTYPE}/ipv4-address
- (L24313)	{BGP-ADDRTYPE}/ipv4-mcast-address
- (L24322)	{BGP-ADDRTYPE}/ipv4-label-address
- (L24331)	{BGP-ADDRTYPE}/ipv4-tunnel-address
- (L24340)	{BGP-ADDRTYPE}/ipv4-mdt-address
- (L24349)	{BGP-ADDRTYPE}/ipv4vpn-address
- (L24358)	{BGP-ADDRTYPE}/ipv4vpna-mcastddress
- (L24367)	{BGP-ADDRTYPE}/ipv6-address
- (L24376)	{BGP-ADDRTYPE}/ipv6-mcast-address
- (L24385)	{BGP-ADDRTYPE}/ipv6-label-address
- (L24394)	{BGP-ADDRTYPE}/ipv6vpn-address
- (L24403)	{BGP-ADDRTYPE}/ipv6vpn-mcast-address
- (L24412)	{BGP-ADDRTYPE}/rt-constraint-address
- (L24421)	{BGP-ADDRTYPE}/ipv6mvpn-address
- (L24430)	{BGP-ADDRTYPE}/ipv4mvpn-address
- (L24439)	{BGP-ADDRTYPE}/ls-ls-address
- (L24448)	{BGP-ADDRTYPE}/ipv4-flowspec-address
- (L24457)	{BGP-ADDRTYPE}/ipv6-flowspec-address
- (L24466)	{BGP-ADDRTYPE}/ipv4vpn-flowspec-address
- (L24475)	{BGP-ADDRTYPE}/ipv6vpn-flowspec-address
- (L24254)	{BGP-ADDRTYPE}/l2vpn-vpls-address
- (L24263)	{BGP-ADDRTYPE}/l2vpn-evpn-address
- (L24272)	{BGP-ADDRTYPE}/l2vpn-mspw-address
- (L24281)	{BGP-ADDRTYPE}/ipv4-sr-policy-address
- (L24290)	{BGP-ADDRTYPE}/ipv6-sr-policy-address
- (L24299)	{BGP-ADDRTYPE}/afi
- (L24304)	{BGP-ADDRTYPE}/ipv4-address
- (L24313)	{BGP-ADDRTYPE}/ipv4-mcast-address
- (L24322)	{BGP-ADDRTYPE}/ipv4-label-address
- (L24331)	{BGP-ADDRTYPE}/ipv4-tunnel-address
- (L24340)	{BGP-ADDRTYPE}/ipv4-mdt-address
- (L24349)	{BGP-ADDRTYPE}/ipv4vpn-address
- (L24358)	{BGP-ADDRTYPE}/ipv4vpna-mcastddress
- (L24367)	{BGP-ADDRTYPE}/ipv6-address
- (L24376)	{BGP-ADDRTYPE}/ipv6-mcast-address
- (L24385)	{BGP-ADDRTYPE}/ipv6-label-address
- (L24394)	{BGP-ADDRTYPE}/ipv6vpn-address
- (L24403)	{BGP-ADDRTYPE}/ipv6vpn-mcast-address
- (L24412)	{BGP-ADDRTYPE}/rt-constraint-address
- (L24421)	{BGP-ADDRTYPE}/ipv6mvpn-address
- (L24430)	{BGP-ADDRTYPE}/ipv4mvpn-address
- (L24439)	{BGP-ADDRTYPE}/ls-ls-address
- (L24448)	{BGP-ADDRTYPE}/ipv4-flowspec-address
- (L24457)	{BGP-ADDRTYPE}/ipv6-flowspec-address
- (L24466)	{BGP-ADDRTYPE}/ipv4vpn-flowspec-address
- (L24475)	{BGP-ADDRTYPE}/ipv6vpn-flowspec-address
- (L20396)	{BGP-ATTR}/ribrnh-ip

## XPaths Modified

- (L627)	{Bgp-resource}
- (L628)	{Bgp-resource}
- (L632)	{Bgp-resource}
- (L633)	{Bgp-resource}
- (L569)	/{BMP}/bmp/server-summaries/server-summary[server-id]/server-id
- (L622)	/{BMP}/bmp/server-neighbors/server-neighbor[server-id]/server-id
- (L14426)	{BGP-BMP-CONVERGENCE-BAG}/bmp-per-server-information[bmp-server-name]
- (L2483)	/bgp/instances/instance[instance-name]/instance-active/bmp-server/bmp-server-neighbors/bmp-server-neighbor[server-id]/server-id
- (L2499)	/bgp/instances/instance[instance-name]/instance-active/bmp-server/bmp-server-summaries/bmp-server-summary[server-id]/server-id

