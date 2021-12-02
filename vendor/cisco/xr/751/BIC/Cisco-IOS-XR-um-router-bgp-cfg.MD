## Cisco-IOS-XR-um-router-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Restrictions were added such that only certain combination of leaves can be used for config container. These include TCP session-mode cfg, RPKI cache server connection mode, AFI label-mode config including per-vrf, per-prefix, per-ce cfgs where permitting only one of them, send/receive ORF capability, socket buffer size.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L14576)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/enforce-first-as-disable
- (L16342)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/enforce-first-as-disable

## XPaths Modified

- (L2674)	/{AS-COMMON}/address-families/address-family[af-name]/segment-routing/srv6/alloc/mode/per-ce
- (L2680)	/{AS-COMMON}/address-families/address-family[af-name]/segment-routing/srv6/alloc/mode/per-vrf
- (L13113)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/segment-routing/srv6/alloc/mode/per-ce
- (L13119)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/segment-routing/srv6/alloc/mode/per-vrf

