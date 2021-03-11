## Cisco-IOS-XR-aaa-protocol-radius-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added Type 6 encryption support for preshared key.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L424)	/{SERVER-KEY}/server-key
- (L488)	/aaa/radius/hosts/host[ordering-index][ip-address][auth-port-number][acct-port-number]/host-key
- (L856)	/aaa/radius/key
- (L954)	/aaa/server-groups/radius-server-groups/radius-server-group[server-group-name]/private-servers/private-server[ordering-index][ip-address][auth-port-number][acct-port-number]/private-key

## XPaths Modified

- (L464)	/{SERVER-KEY}/server-key
- (L525)	/aaa/radius/hosts/host[ordering-index][ip-address][auth-port-number][acct-port-number]/host-key
- (L892)	/aaa/radius/key
- (L1000)	/aaa/server-groups/radius-server-groups/radius-server-group[server-group-name]/private-servers/private-server[ordering-index][ip-address][auth-port-number][acct-port-number]/private-key

