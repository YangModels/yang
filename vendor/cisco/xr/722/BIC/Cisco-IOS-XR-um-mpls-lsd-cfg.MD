## Cisco-IOS-XR-um-mpls-lsd-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Two sibling hierarchies have the same star to their sysdbpath. One implicitly has 0 as part of its path, and the other is a list that only accepts 0. YFW will always pick the implicit one, so we need to change the hierarchy.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L111)	/mpls/label/range/table[table-index]

## XPaths Modified

N/A

