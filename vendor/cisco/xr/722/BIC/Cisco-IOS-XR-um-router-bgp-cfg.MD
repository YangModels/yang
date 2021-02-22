## Cisco-IOS-XR-um-router-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated the model based on 7.2.1 CLI set.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L814)	/{AS-COMMON}/rpki/servers/server[server-id]/transport/tcp/port
- (L829)	/{AS-COMMON}/rpki/servers/server[server-id]/transport/ssh/port
- (L943)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/per-ce
- (L949)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/per-vrf
- (L956)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/route-policy
- (L1277)	/{AS-COMMON}/address-families/address-family[af-name]/advertise/local-labeled-route
- (L1961)	/{AS-COMMON}/address-families/address-family[af-name]/retain/local-label
- (L2015)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-ce
- (L2016)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-ce
- (L2022)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-vrf
- (L2023)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-vrf
- (L2029)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/route-policy
- (L2031)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/route-policy
- (L2569)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L2575)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L2581)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L2587)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L4047)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/active-only
- (L4053)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/passive-only
- (L4059)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/both
- (L4535)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L4541)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L4547)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L4553)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L5994)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/active-only
- (L6000)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/passive-only
- (L6006)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/both
- (L6484)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L6490)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L6496)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L6502)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L7885)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/active-only
- (L7891)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/passive-only
- (L7897)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/both
- (L8333)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L8339)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L8345)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L8351)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L9853)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/active-only
- (L9859)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/passive-only
- (L9865)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/both
- (L10421)	/{AS-COMMON}/socket/bgp-write-buffer-size
- (L10442)	/{AS-COMMON}/socket/bgp-read-buffer-size
- (L11501)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/advertise/local-labeled-route
- (L12105)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-prefix
- (L12106)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-prefix
- (L12112)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-ce
- (L12113)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-ce
- (L12119)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-vrf
- (L12120)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-vrf
- (L12126)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/route-policy
- (L12128)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/route-policy
- (L12405)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L12411)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L12417)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L12423)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L13713)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/active-only
- (L13719)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/passive-only
- (L13725)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/both
- (L14187)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L14193)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L14199)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L14205)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L15412)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/active-only
- (L15418)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/passive-only
- (L15424)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/both
- (L15896)	/{AS-COMMON}/vrfs/vrf[vrf-name]/socket/bgp-write-buffer-size
- (L15917)	/{AS-COMMON}/vrfs/vrf[vrf-name]/socket/bgp-read-buffer-size

## XPaths Removed

- (L1974)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-prefix

## XPaths Modified

N/A

