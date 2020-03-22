## Cisco-IOS-XR-um-mpls-ldp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Complex YFED internal support requirements dictated that we need unique list and leaf node names with the same parent for correct JSON data parsing via CSCvr15428. Moved out trap augments into um-traps-mpls-ldp model via via CSCvr62233.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L565)	/mpls/ldp/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address][label-space-id]/password/encrypted
- (L570)	/mpls/ldp/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address][label-space-id]/password/disable
- (L939)	/mpls/ldp/session/protection/for
- (L977)	/mpls/ldp/session/protection/duration
- (L1328)	/mpls/ldp/neighbor/neighbors/neighbor[neighbor-address][label-space-id]/password/encrypted
- (L1333)	/mpls/ldp/neighbor/neighbors/neighbor[neighbor-address][label-space-id]/password/disable

## XPaths Removed

- (L1659)	/mpls/ldp/address-families/address-family[af-name]/label/local/advertise/for/access-list[access-list-name]
- (L50)	traps

## XPaths Modified

- (L641)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv4/label/local/implicit-null-override/for
- (L731)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv4/label/local/advertise/to/neighbor[neighbor-address][label-space-id]/for
- (L793)	/mpls/ldp/vrfs/vrf[vrf-name]/address-family/ipv4/label/remote/accept/from/neighbor[neighbor-address][label-space-id]/for
- (L1546)	/mpls/ldp/address-families/address-family[af-name]/label/local/implicit-null-override/for
- (L1636)	/mpls/ldp/address-families/address-family[af-name]/label/local/advertise/to/neighbor[neighbor-address][label-space-id]/for
- (L1727)	/mpls/ldp/address-families/address-family[af-name]/label/remote/accept/from/neighbor[neighbor-address][label-space-id]/for

