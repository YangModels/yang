## Cisco-IOS-XR-l2vpn-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Update keys and members of l2fib-mac-learning-mac, l2fib-mac-learning-mac-ipv4 and l2fib-mac-learning-mac-ipv6. Update keys of l2fib-evpn-incl-mcast-ole, l2fib-mroute-port.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L898)	/{L2FIB-EVPN-INCL-MCAST-OLE-TABLE}/l2fib-evpn-incl-mcast-oles/l2fib-evpn-incl-mcast-ole/moi-type
- (L903)	/{L2FIB-EVPN-INCL-MCAST-OLE-TABLE}/l2fib-evpn-incl-mcast-oles/l2fib-evpn-incl-mcast-ole/next-hop-address
- (L908)	/{L2FIB-EVPN-INCL-MCAST-OLE-TABLE}/l2fib-evpn-incl-mcast-oles/l2fib-evpn-incl-mcast-ole/sr-te-interface
- (L913)	/{L2FIB-EVPN-INCL-MCAST-OLE-TABLE}/l2fib-evpn-incl-mcast-oles/l2fib-evpn-incl-mcast-ole/sr-te-bsid
- (L920)	/{L2FIB-EVPN-INCL-MCAST-OLE-TABLE}/l2fib-evpn-incl-mcast-oles/l2fib-evpn-incl-mcast-ole/srv6-te-bsid
- (L3458)	{L2FIB-MAC-DB-NODE-INFO}/interface-handle
- (L1445)	/l2vpn-forwarding/nodes/node[node-id]/l2fib-mac-learning/l2fib-mac-learning-macs/l2fib-mac-learning-mac/interface-name
- (L1450)	/l2vpn-forwarding/nodes/node[node-id]/l2fib-mac-learning/l2fib-mac-learning-macs/l2fib-mac-learning-mac/address
- (L3493)	{L2FIB-MAC-DB-INFO}/addr
- (L3498)	{L2FIB-MAC-DB-INFO}/nhaddr
- (L1485)	/l2vpn-forwarding/nodes/node[node-id]/l2fib-mac-learning/l2fib-mac-learning-mac-ipv4s/l2fib-mac-learning-mac-ipv4/bdid
- (L1490)	/l2vpn-forwarding/nodes/node[node-id]/l2fib-mac-learning/l2fib-mac-learning-mac-ipv4s/l2fib-mac-learning-mac-ipv4/mac-address
- (L3493)	{L2FIB-MAC-DB-INFO}/addr
- (L3498)	{L2FIB-MAC-DB-INFO}/nhaddr
- (L1515)	/l2vpn-forwarding/nodes/node[node-id]/l2fib-mac-learning/l2fib-mac-learning-mac-ipv6s/l2fib-mac-learning-mac-ipv6/bdid
- (L1520)	/l2vpn-forwarding/nodes/node[node-id]/l2fib-mac-learning/l2fib-mac-learning-mac-ipv6s/l2fib-mac-learning-mac-ipv6/mac-address
- (L3493)	{L2FIB-MAC-DB-INFO}/addr
- (L3498)	{L2FIB-MAC-DB-INFO}/nhaddr
- (L2328)	/l2vpn-forwarding/nodes/node[node-id]/l2fib-mroute-ports/l2fib-mroute-port/originating-ip
- (L340)	/{L2fib-evpn-moi}

## XPaths Modified

- (L6122)	{L2VPN-SRV6}/remote-path-buffer[next-hop]

