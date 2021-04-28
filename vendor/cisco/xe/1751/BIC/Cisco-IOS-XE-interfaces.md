## Cisco-IOS-XE-interfaces


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- interface-common-grouping(grouping)/bandwidth/kilobits
- interface-common-grouping(grouping)/bandwidth/qos-reference
- interface-grouping(grouping)/interface-choice/Loopback/Loopback

### Description

1. The range '[(1, 200000000)]' is  added
2. The range '[(1, 10000000)]' is  added
3. The range '[(0, 2147483647)]' is  added

### Reason

Loopback range in yang interface-grouping was 0-4294967295. However, from device side loopback interface can only support range from 0 to 2147483647. Hence loopback range in yang was modified to be inline with device range

## XPaths Added

### Description
