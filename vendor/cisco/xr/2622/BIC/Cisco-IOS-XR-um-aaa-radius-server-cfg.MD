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

- (L325)	/aaa/group/server/radius/server-groups/server-group[server-group-name]/server-privates/server-private[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/mandate
- (L331)	/aaa/group/server/radius/server-groups/server-group[server-group-name]/server-privates/server-private[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/optional
- (L558)	/aaa/server/radius/dynamic-author/clients/client[address][vrf]/attribute/message-authenticator/mandate
- (L564)	/aaa/server/radius/dynamic-author/clients/client[address][vrf]/attribute/message-authenticator/optional
- (L740)	/aaa/radius-server/hosts/host[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/mandate
- (L746)	/aaa/radius-server/hosts/host[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/optional

## XPaths Modified

- (L327)	/aaa/group/server/radius/server-groups/server-group[server-group-name]/server-privates/server-private[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator
- (L560)	/aaa/server/radius/dynamic-author/clients/client[address][vrf]/attribute/message-authenticator
- (L742)	/aaa/radius-server/hosts/host[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator

