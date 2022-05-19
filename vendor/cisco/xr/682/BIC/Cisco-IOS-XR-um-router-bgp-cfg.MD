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

- (L1235)	/{AS-COMMON}/address-families/address-family[af-name]/maximum-paths/ebgp/order/igp-metric
- (L1230)	/{AS-COMMON}/address-families/address-family[af-name]/maximum-paths/ebgp/order
- (L1267)	/{AS-COMMON}/address-families/address-family[af-name]/maximum-paths/eibgp/order/igp-metric
- (L1262)	/{AS-COMMON}/address-families/address-family[af-name]/maximum-paths/eibgp/order
- (L1299)	/{AS-COMMON}/address-families/address-family[af-name]/maximum-paths/ibgp/order/igp-metric
- (L1294)	/{AS-COMMON}/address-families/address-family[af-name]/maximum-paths/ibgp/order
- (L11909)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/maximum-paths/ebgp/order/igp-metric
- (L11904)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/maximum-paths/ebgp/order
- (L11941)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/maximum-paths/eibgp/order/igp-metric
- (L11936)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/maximum-paths/eibgp/order
- (L11973)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/maximum-paths/ibgp/order/igp-metric
- (L11968)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/maximum-paths/ibgp/order

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

N/A

