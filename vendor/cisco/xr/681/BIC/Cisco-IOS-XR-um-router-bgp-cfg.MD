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

- (L837)	/{AS-COMMON}/rpki/servers/server[server-id]/transport/tcp/port
- (L852)	/{AS-COMMON}/rpki/servers/server[server-id]/transport/ssh/port
- (L966)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/per-ce
- (L972)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/per-vrf
- (L979)	/{AS-COMMON}/address-families/address-family[af-name]/vrf/all/label/mode/route-policy
- (L1146)	/{AS-COMMON}/address-families/address-family[af-name]/optimal-route-reflection/orr-group[orr-group-name]/tertiary-address
- (L1321)	/{AS-COMMON}/address-families/address-family[af-name]/advertise/best-external/disable
- (L1328)	/{AS-COMMON}/address-families/address-family[af-name]/advertise/local-labeled-route
- (L2011)	/{AS-COMMON}/address-families/address-family[af-name]/retain/local-label
- (L2065)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-ce
- (L2066)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-ce
- (L2072)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-vrf
- (L2073)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-vrf
- (L2079)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/route-policy
- (L2081)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/route-policy
- (L2638)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L2644)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L2650)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L2656)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L2874)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/remove-private-as/entire-aspath
- (L2880)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/remove-private-as/inheritance-disable
- (L2993)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L2999)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L3037)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/advertise/permanent-network
- (L3231)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L3232)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L3224)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/encapsulation-type
- (L4183)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/active-only
- (L4189)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/passive-only
- (L4195)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/session-open-mode/both
- (L4671)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L4677)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L4683)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L4689)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L4907)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/remove-private-as/entire-aspath
- (L4913)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/remove-private-as/inheritance-disable
- (L5026)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L5032)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L5070)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/advertise/permanent-network
- (L5264)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L5265)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L5257)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/encapsulation-type
- (L6197)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/active-only
- (L6203)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/passive-only
- (L6209)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/both
- (L6688)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L6694)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L6700)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L6706)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L6927)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/remove-private-as/entire-aspath
- (L6933)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/remove-private-as/inheritance-disable
- (L7046)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L7052)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L7090)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/advertise/permanent-network
- (L7284)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L7285)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L7277)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/encapsulation-type
- (L6638)	/{AS-COMMON}/af-groups/af-group[af-group-name]
- (L8161)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/active-only
- (L8167)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/passive-only
- (L8173)	/{AS-COMMON}/session-groups/session-group[session-group-name]/session-open-mode/both
- (L8609)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L8615)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L8621)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L8627)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L8845)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/remove-private-as/entire-aspath
- (L8851)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/remove-private-as/inheritance-disable
- (L8964)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L8970)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L9008)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/advertise/permanent-network
- (L9202)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L9203)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/encapsulation-type/vxlan
- (L9195)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/encapsulation-type
- (L10196)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/active-only
- (L10202)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/passive-only
- (L10208)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/session-open-mode/both
- (L10764)	/{AS-COMMON}/socket/bgp-write-buffer-size
- (L10785)	/{AS-COMMON}/socket/bgp-read-buffer-size
- (L11794)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/optimal-route-reflection/orr-group[orr-group-name]/tertiary-address
- (L11764)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/optimal-route-reflection
- (L11996)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/advertise/best-external/disable
- (L12003)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/advertise/local-labeled-route
- (L12606)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-prefix
- (L12607)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-prefix
- (L12613)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-ce
- (L12614)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-ce
- (L12620)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-vrf
- (L12621)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/per-vrf
- (L12627)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/route-policy
- (L12629)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/label/mode/route-policy
- (L12919)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L12925)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L12931)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L12937)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L13150)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/remove-private-as/entire-aspath
- (L13156)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/remove-private-as/inheritance-disable
- (L13269)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L13275)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L14299)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/active-only
- (L14305)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/passive-only
- (L14311)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/session-open-mode/both
- (L14773)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/receive
- (L14779)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/send
- (L14785)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/both
- (L14791)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/capability/orf/prefix/none
- (L15004)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/remove-private-as/entire-aspath
- (L15010)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/remove-private-as/inheritance-disable
- (L15123)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/always
- (L15129)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/soft-reconfiguration/inbound/inheritance-disable
- (L16065)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/active-only
- (L16071)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/passive-only
- (L16077)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/session-open-mode/both
- (L16549)	/{AS-COMMON}/vrfs/vrf[vrf-name]/socket/bgp-write-buffer-size
- (L16570)	/{AS-COMMON}/vrfs/vrf[vrf-name]/socket/bgp-read-buffer-size
- (L17126)	/as-format/asdot
- (L17132)	/as-format/asplain
- (L17522)	/router/bgp/instances/instance[instance-name]

## XPaths Removed

- (L1582)	/{AS-COMMON}/address-families/address-family[af-name]/label/mode/per-prefix
- (L2405)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/local-labeled-route
- (L4095)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/local-labeled-route
- (L5771)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/local-labeled-route
- (L7363)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/local-labeled-route
- (L9577)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/domain-distinguisher
- (L9831)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/permanent-network
- (L10594)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/implicit-import
- (L10640)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/inter-as
- (L10672)	/{AS-COMMON}/vrfs/vrf[vrf-name]/address-families/address-family[af-name]/default-martian-check
- (L11078)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/local-labeled-route
- (L11088)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/encapsulation-type
- (L12794)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/local-labeled-route
- (L12804)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/encapsulation-type

## XPaths Modified

- (L8560)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/neighbor-group-name
- (L17522)	/router/bgp/instances/instance[instance-name]

