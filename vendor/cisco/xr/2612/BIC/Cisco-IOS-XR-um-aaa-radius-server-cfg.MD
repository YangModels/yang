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

- (L1236)	/aaa/radius-server/attribute/list[list-name]/attribute/vendor-ids/vendor-id[id]/vendor-types

## XPaths Removed

- (L323)	/aaa/group/server/radius/server-groups/server-group[server-group-name]/server-privates/server-private[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/mandate
- (L329)	/aaa/group/server/radius/server-groups/server-group[server-group-name]/server-privates/server-private[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/optional
- (L556)	/aaa/server/radius/dynamic-author/clients/client[address][vrf]/attribute/message-authenticator/mandate
- (L562)	/aaa/server/radius/dynamic-author/clients/client[address][vrf]/attribute/message-authenticator/optional
- (L738)	/aaa/radius-server/hosts/host[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/mandate
- (L744)	/aaa/radius-server/hosts/host[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator/optional

## XPaths Modified

- (L327)	/aaa/group/server/radius/server-groups/server-group[server-group-name]/server-privates/server-private[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator
- (L560)	/aaa/server/radius/dynamic-author/clients/client[address][vrf]/attribute/message-authenticator
- (L742)	/aaa/radius-server/hosts/host[ordering-index][address][auth-port][acct-port]/attribute/message-authenticator

