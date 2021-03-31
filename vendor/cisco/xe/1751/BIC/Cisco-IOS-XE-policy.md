## Cisco-IOS-XE-policy


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/policy/policy-map/class/action-list/action-param/police-case/police-choice/police-target-bitrate-case/police-target-bitrate/police/actions
- interface-grouping(grouping)/interface-choice/Loopback/Loopback

### Description

- A new when expression cannot be added

- The range '[(0, 2147483647)]' is illegally added

### Reason

Loopback range in yang interface-grouping was 0-4294967295. However, from device side loopback interface can only support range from 0 to 2147483647. Hence loopback range in yang was modified to be inline with device range.

## XPaths Added

### Description
