## Cisco-IOS-XE-lisp.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- interface-grouping(grouping)/interface-choice/Loopback/Loopback

### Reason

Loopback range in yang interface-grouping was 0-4294967295. However, from device side loopback interface can only support range from 0 to 2147483647. Hence loopback range in yang was modified to be inline with device range.

### Description

The range '[(0, 2147483647)]' is added

## XPaths Added

### Description
