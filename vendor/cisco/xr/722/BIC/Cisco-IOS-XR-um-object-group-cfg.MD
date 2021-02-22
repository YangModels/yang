## Cisco-IOS-XR-um-object-group-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Changed the datatype from enum to union of same enum and integer range, which does not really break backward-compatibility. No impact on existing operations.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L536)	/object-group/ports/port[port-object-group-name]/ranges/range[starting-port][ending-port]/starting-port
- (L541)	/object-group/ports/port[port-object-group-name]/ranges/range[starting-port][ending-port]/ending-port

