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

- (L818)	/{AS-COMMON}/rpki/servers/server[server-id]/transport/tcp/port
- (L833)	/{AS-COMMON}/rpki/servers/server[server-id]/transport/ssh/port
- (L947)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/per-ce
- (L953)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/per-vrf
- (L960)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/route-policy
- (L1127)	/{AS-COMMON}/address-families/address-family[af-name]/optimal-route-reflection/orr-group[orr-group-name]/tertiary-address
- (L1302)	/{AS-COMMON}/address-families/address-family[af-name]/advertise/local-labeled-route
- (L1986)	/{AS-COMMON}/address-families/address-family[af-name]/retain/local-label
- (L2040)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-ce
- (L2041)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-ce
- (L2047)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-vrf
- (L2048)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-vrf
- (L2054)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/route-policy
- (L2056)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/route-policy
- (L2607)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L2613)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L2619)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L2625)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L2962)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L2968)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L4152)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/active-only
- (L4158)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/passive-only
- (L4164)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/both
- (L4640)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L4646)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L4652)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L4658)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L4995)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L5001)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L6166)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/active-only
- (L6172)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/passive-only
- (L6178)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/both
- (L6656)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L6662)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L6668)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L6674)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L7009)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L7015)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L8124)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/active-only
- (L8130)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/passive-only
- (L8136)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/both
- (L8572)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L8578)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L8584)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L8590)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L8927)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L8933)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L10159)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/active-only
- (L10165)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/passive-only
- (L10171)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/both
- (L10727)	/{AS-COMMON}/socket/bgp-write-buffer-size
- (L10748)	/{AS-COMMON}/socket/bgp-read-buffer-size
- (L11716)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/optimal-route-reflection/orr-group[orr-group-name]/tertiary-address
- (L11686)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/optimal-route-reflection
- (L11918)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/advertise/local-labeled-route
- (L12522)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-prefix
- (L12523)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-prefix
- (L12529)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-ce
- (L12530)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-ce
- (L12536)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-vrf
- (L12537)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-vrf
- (L12543)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/route-policy
- (L12545)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/route-policy
- (L12835)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L12841)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L12847)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L12853)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L13185)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L13191)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L14210)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/active-only
- (L14216)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/passive-only
- (L14222)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/both
- (L14684)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L14690)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L14696)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L14702)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L15034)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L15040)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L15976)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/active-only
- (L15982)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/passive-only
- (L15988)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/both
- (L16460)	/{AS-COMMON}/vrfs/vrf[vrf-name]/socket/bgp-write-buffer-size
- (L16481)	/{AS-COMMON}/vrfs/vrf[vrf-name]/socket/bgp-read-buffer-size

## XPaths Removed

- (L1974)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-prefix

## XPaths Modified

N/A

