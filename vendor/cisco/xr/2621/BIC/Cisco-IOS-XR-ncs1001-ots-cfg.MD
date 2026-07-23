## Cisco-IOS-XR-ncs1001-ots-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

This change reflect the changes made in CLI where the spanloss attribute has been changed from boolean type to a structured type, now the user can set the spanloss delta value in order to trigger an OTDR automatic scan.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L279)	/{NODE-CFG}/slot[slot-id]/otdrs/otdr[port][direction]/periodic-scan/minutes
- (L282)	/{NODE-CFG}/slot[slot-id]/otdrs/otdr[port][direction]/periodic-scan/minutes

## XPaths Modified

- (L428)	/{NODE-CFG}/slot[slot-id]/otdrs/otdr[port][direction]/periodic-scan/minutes

