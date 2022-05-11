## Cisco-IOS-XR-lpts-pre-ifib-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

LPTS ACL nodes in YANG model. acl-name,vrf-name,afi-family-type,acl-rate should be mandatory.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L1019)	/lpts/ipolicer/acls/acl[acl-name][afi-family-type][vrf-name]/acl-rate

## XPaths Removed

- (L870)	/lpts/ipolicer/acls/acl[acl-name]/afi-types

## XPaths Modified

- (L1016)	/lpts/ipolicer/acls/acl[acl-name][afi-family-type][vrf-name]

