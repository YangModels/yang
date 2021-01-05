## Cisco-IOS-XE-line.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- /native/line/async-line/privilege/level
- /native/line/async-line/transport/preferred
- /native/line/aux/privilege/level
- /native/line/aux/transport/preferred
- /native/line/console/privilege/level
- /native/line/console/transport/preferred
- /native/line/line-list/privilege/level
- /native/line/line-list/transport/preferred
- /native/line/vty/privilege/level
- /native/line/vty/transport/preferred

### Description

The presence 'true' is removed

### Reason

To align yang model with IOS, presence container has been removed.

Before changes:

1. privilege level (This is not a valid IOS CLI. So, presence container has been removed)
2. privilege level <level>

## XPaths Added

### Description
