## Cisco-IOS-XR-um-mpls-lsd-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Two sibling hierarchies have the same path. One implicitly has 0 as part of its path, and the other is a list that only accepts 0. YANG engine will always pick the implicit one, so we need to change the hierarch1.Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L103)	/mpls/label/range/table[table-index]

## XPaths Modified

N/A

