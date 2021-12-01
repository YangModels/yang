## Cisco-IOS-XR-aaa-protocol-radius-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added Type 6 encryption support for preshared key, changed leaf type of key from string to tuple.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L474)	/{SERVER-KEY}/server-key/encrypt-type
- (L467)	/{SERVER-KEY}/server-key/text
- (L535)	/aaa/radius/hosts/host[ordering-index][ip-address][auth-port-number][acct-port-number]/host-key/encrypt-type
- (L528)	/aaa/radius/hosts/host[ordering-index][ip-address][auth-port-number][acct-port-number]/host-key/text
- (L902)	/aaa/radius/key/encrypt-type
- (L895)	/aaa/radius/key/text
- (L1010)	/aaa/server-groups/radius-server-groups/radius-server-group[server-group-name]/private-servers/private-server[ordering-index][ip-address][auth-port-number][acct-port-number]/private-key/encrypt-type
- (L1003)	/aaa/server-groups/radius-server-groups/radius-server-group[server-group-name]/private-servers/private-server[ordering-index][ip-address][auth-port-number][acct-port-number]/private-key/text

## XPaths Modified

N/A

