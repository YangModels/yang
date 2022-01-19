## Cisco-IOS-XR-fib-common-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

changes related to treat SRv6 and SID as well-known when parsing XML for yang.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L5063)	{FIB-SH-PFX-MASKLEN-DISTRIB}/unicast-prefixe
- (L5068)	{FIB-SH-PFX-MASKLEN-DISTRIB}/broadcast-prefixe
- (L5242)	{FIB-SH-SUM}/old-unresolve-entries
- (L5247)	{FIB-SH-SUM}/new-unresolve-entries
- (L5252)	{FIB-SH-SUM}/unresolve-entries
- (L452)	{FIB-BAG-SUM-OBJ-ATTR}/fsum-attr-cnt
- (L511)	{FIB-GLOBAL-SUMMARY-COUNTS}/num-retry-ojbects
- (L1093)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-egress/nh-info-special-detail-hardware-egress/nh-info-special-null-detail-hardware-egress
- (L1099)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-egress/nh-info-special-detail-hardware-egress/nh-info-special-punt-detail-hardware-egress
- (L1105)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-egress/nh-info-special-detail-hardware-egress/nh-info-special-discard-detail-hardware-egress
- (L1111)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-egress/nh-info-special-detail-hardware-egress/nh-info-special-drop-detail-hardware-egress
- (L1214)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail/nh-info-special-detail/nh-info-special-punt-detail
- (L1219)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail/nh-info-special-detail/nh-info-special-drop-detail
- (L1224)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail/nh-info-special-detail/nh-info-special-null-detail
- (L1229)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail/nh-info-special-detail/nh-info-special-discard-detail
- (L1331)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-ingress/nh-info-special-detail-hardware-ingress/nh-info-special-punt-detail-hardware-ingress
- (L1337)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-ingress/nh-info-special-detail-hardware-ingress/nh-info-special-null-detail-hardware-ingress
- (L1343)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-ingress/nh-info-special-detail-hardware-ingress/nh-info-special-drop-detail-hardware-ingress
- (L1349)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-detail-hardware-ingress/nh-info-special-detail-hardware-ingress/nh-info-special-discard-detail-hardware-ingress
- (L1364)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-brief/nh-info-special-brief/nh-info-special-discard-brief
- (L1369)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-brief/nh-info-special-brief/nh-info-special-null-brief
- (L1374)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-brief/nh-info-special-brief/nh-info-special-punt-brief
- (L1379)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/vrfs/vrf[vrf-name]/nh-info/nh-info-brief/nh-info-special-brief/nh-info-special-drop-brief

## XPaths Modified

- (L153)	{Fib-bag-object}
- (L154)	{Fib-bag-object}
- (L464)	{FIB-BAG-SUM-OBJ-ATTR}/fsum-attr-cnt

