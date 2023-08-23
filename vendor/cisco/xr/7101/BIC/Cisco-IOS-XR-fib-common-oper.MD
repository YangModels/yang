## Cisco-IOS-XR-fib-common-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added new field to ltep-nve-tunnels in order keep track of destination address protocol.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L286)	{FIB-OC-AFT-PRFX-STATE-V2}/grp-id
- (L666)	{FIB-BAG-SUM-OBJ-ATTR}/fsum-attr-cnt/entry
- (L440)	{MPLS-FWD-INFO}/label-stack/entry
- (L6582)	{FIB-COMMON-LTEP-ENTRY}/destination-address
- (L6582)	{FIB-COMMON-LTEP-ENTRY}/destination-address
- (L6539)	{FIB-IP-ADDR-T-UNION}
- (L6540)	{FIB-IP-ADDR-T-UNION}/afi
- (L6545)	{FIB-IP-ADDR-T-UNION}/none
- (L6554)	{FIB-IP-ADDR-T-UNION}/ipv4
- (L6563)	{FIB-IP-ADDR-T-UNION}/ipv6
- (L6582)	{FIB-COMMON-LTEP-ENTRY}/destination-address
- (L1221)	/fib/nodes/node[node-name]/global/tunnel-database/evni-tunnel-internal-rteps
- (L1242)	/fib/nodes/node[node-name]/global/tunnel-database/evni-tunnel-internal-bgps
- (L1296)	/fib/nodes/node[node-name]/global/tunnel-database/evni-tunnel-rteps
- (L1344)	/fib/nodes/node[node-name]/global/tunnel-database/evni-tunnel-bgps
- (L6539)	{FIB-IP-ADDR-T-UNION}
- (L6540)	{FIB-IP-ADDR-T-UNION}/afi
- (L6545)	{FIB-IP-ADDR-T-UNION}/none
- (L6554)	{FIB-IP-ADDR-T-UNION}/ipv4
- (L6563)	{FIB-IP-ADDR-T-UNION}/ipv6
- (L277)	{FIB-OC-AFT-COND-GRP-STATE-V2}/interface-name
- (L251)	{FIB-OC-AFT-NH-GROUP-STATE-V2}/nhid
- (L256)	{FIB-OC-AFT-NH-GROUP-STATE-V2}/wt-of-nh
- (L261)	{FIB-OC-AFT-NH-GROUP-STATE-V2}/fwd-class
- (L231)	{FIB-OC-AFT-NEXTHOP-V2}/pushed-label-stack

## XPaths Modified

- (L706)	{FIB-BAG-SUM-OBJ-ATTR}/fsum-attr-cnt
- (L481)	{MPLS-FWD-INFO}/label-stack
- (L1614)	/fib/nodes/node[node-name]/global/tunnel-database/ltep-nve-tunnel-hardware-egresses/ltep-nve-tunnel-hardware-egress/dest-address
- (L1620)	/fib/nodes/node[node-name]/global/tunnel-database/ltep-nve-tunnel-hardware-egresses/ltep-nve-tunnel-hardware-egress/underlay-table-id
- (L1837)	/fib/nodes/node[node-name]/global/tunnel-database/ltep-nve-tunnels/ltep-nve-tunnel/dest-address
- (L1843)	/fib/nodes/node[node-name]/global/tunnel-database/ltep-nve-tunnels/ltep-nve-tunnel/underlay-table-id
- (L1876)	/fib/nodes/node[node-name]/global/tunnel-database/ltep-nve-tunnel-hardware-ingresses/ltep-nve-tunnel-hardware-ingress/dest-address
- (L1882)	/fib/nodes/node[node-name]/global/tunnel-database/ltep-nve-tunnel-hardware-ingresses/ltep-nve-tunnel-hardware-ingress/underlay-table-id
- (L2269)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnel-hardware-egresses/ltep-tunnel-hardware-egress/source-address
- (L2283)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnel-hardware-egresses/ltep-tunnel-hardware-egress/destination-address
- (L2303)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/rtep-tunnel-hardware-egresses/rtep-tunnel-hardware-egress/destination-address
- (L2357)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/rtep-tunnel-internals/rtep-tunnel-internal/destination-address
- (L2411)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/rtep-tunnels/rtep-tunnel/destination-address
- (L2465)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnel-hardware-ingresses/ltep-tunnel-hardware-ingress/source-address
- (L2479)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnel-hardware-ingresses/ltep-tunnel-hardware-ingress/destination-address
- (L2499)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnel-internals/ltep-tunnel-internal/source-address
- (L2513)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnel-internals/ltep-tunnel-internal/destination-address
- (L2533)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/rtep-tunnel-hardware-ingresses/rtep-tunnel-hardware-ingress/destination-address
- (L2587)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnels/ltep-tunnel/source-address
- (L2601)	/fib/nodes/node[node-name]/protocols/protocol[protocol-name]/protocol-tunnel-database/ltep-tunnels/ltep-tunnel/destination-address
- (L341)	{FIB-OC-AFT-COND-GRP-STATE-V2}/interface-name
- (L303)	{FIB-OC-AFT-NH-GROUP-STATE-V2}/nhid
- (L312)	{FIB-OC-AFT-NH-GROUP-STATE-V2}/wt-of-nh
- (L321)	{FIB-OC-AFT-NH-GROUP-STATE-V2}/fwd-class
- (L279)	{FIB-OC-AFT-NEXTHOP-V2}/pushed-label-stack

