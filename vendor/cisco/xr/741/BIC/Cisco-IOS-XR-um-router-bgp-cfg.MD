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

- (L1321)	/{AS-COMMON}/address-families/address-family[af-name]/advertise/best-external/disable
- (L6638)	/{AS-COMMON}/af-groups/af-group[af-group-name]
- (L11996)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/advertise/best-external/disable
- (L17522)	/router/bgp/instances/instance[instance-name]

## XPaths Removed

N/A

## XPaths Modified

- (L8560)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/neighbor-group-name
- (L17522)	/router/bgp/instances/instance[instance-name]

