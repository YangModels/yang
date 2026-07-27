## Cisco-IOS-XR-um-mpls-ldp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Redistribute option supported only for ipv4 address-family. So, adjusted when statement under redistribute container.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L571)	/mpls/ldp/vrfs/vrf[vrf-name]/session/downstream-on-demand/with
- (L723)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv4/label/local/allocate/for/ip-access-list
- (L773)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv4/label/local/advertise/explicit-null/for/access-list
- (L788)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv4/label/local/advertise/explicit-null/for/to/access-list
- (L805)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv4/label/local/advertise/explicit-null/to/access-list
- (L997)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv6/label/local/advertise/explicit-null/for/access-list
- (L1012)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv6/label/local/advertise/explicit-null/for/to/access-list
- (L1029)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv6/label/local/advertise/explicit-null/to/access-list
- (L1284)	/mpls/ldp/session/downstream-on-demand/with
- (L1304)	/mpls/ldp/session/protection/for/for-access-list
- (L1802)	/mpls/ldp/address-families/address-family[af-name]/discovery/targeted-hello/accept/from
- (L1921)	/mpls/ldp/address-families/address-family[af-name]/redistribute/bgp/advertise-to
- (L1945)	/mpls/ldp/address-families/address-family[af-name]/label/local/allocate/for/access-list
- (L1995)	/mpls/ldp/address-families/address-family[af-name]/label/local/advertise/explicit-null/for/access-list
- (L2010)	/mpls/ldp/address-families/address-family[af-name]/label/local/advertise/explicit-null/for/to/access-list
- (L2027)	/mpls/ldp/address-families/address-family[af-name]/label/local/advertise/explicit-null/to/access-list
- (L2101)	/mpls/ldp/address-families/address-family[af-name]/label/local/advertise/for/access-lists[access-list-name]/access-list-name
- (L2111)	/mpls/ldp/address-families/address-family[af-name]/label/local/advertise/for/access-lists[access-list-name]/to

