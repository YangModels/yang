## Cisco-IOS-XR-ipv4-dhcpd-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Fixed GET-OPER to display interface name in standard format.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L616)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-dns
- (L622)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-default-router
- (L628)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-netbious-name-server
- (L634)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-time-server
- (L1285)	{IPV4-DHCPD-PROXY-BINDING}/event-history
- (L1701)	{IPV4-DHCPD-SNOOP-BINDING}/snoop-binding-client-id
- (L1706)	{IPV4-DHCPD-SNOOP-BINDING}/snoop-binding-client-id-len
- (L539)	/ipv4-dhcpd/nodes/node[nodeid]/nodeid

## XPaths Modified

- (L727)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-dns
- (L737)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-default-router
- (L747)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-netbious-name-server
- (L757)	{IPV4-DHCPD-SERVER-PROFILE}/server-profile-time-server
- (L1061)	{IPV4-DHCPD-PROXY-INTERFACE}/intf-mode
- (L1419)	{IPV4-DHCPD-PROXY-BINDING}/event-history
- (L1841)	{IPV4-DHCPD-SNOOP-BINDING}/snoop-binding-state
- (L197)	/ipv4-dhcpd/nodes/node[node-name]
- (L259)	/ipv4-dhcpd/nodes/node[node-name]/proxy/stats/stat/interface-name
- (L314)	/ipv4-dhcpd/nodes/node[node-name]/interfaces/interface[interface-name]/interface-name
- (L390)	/ipv4-dhcpd/nodes/node[node-name]/base/stats/stat/interface-name
- (L433)	/ipv4-dhcpd/nodes/node[node-name]/server/stats/stat/interface-name

