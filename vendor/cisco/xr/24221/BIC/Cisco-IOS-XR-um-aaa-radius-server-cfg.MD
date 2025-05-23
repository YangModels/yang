## Cisco-IOS-XR-um-aaa-radius-server-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated xr schema type for leaf six with Type6-password.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L253)	/aaa/group/server/radius/server-groups/server-group[server-group-name]/server-privates/server-private[ordering-index][address][auth-port][acct-port]/key/six
- (L490)	/aaa/server/radius/dynamic-author/server-key/six
- (L537)	/aaa/server/radius/dynamic-author/clients/client[address][vrf]/server-key/six
- (L620)	/aaa/radius-server/hosts/host[ordering-index][address][auth-port][acct-port]/key/six
- (L687)	/aaa/radius-server/key/six

