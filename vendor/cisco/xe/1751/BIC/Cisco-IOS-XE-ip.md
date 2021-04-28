## Cisco-IOS-XE-ip.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- config-ip-grouping(grouping)/ip/vrf/maximum
- config-vrf-definition-grouping(grouping)/vrf/definition/address-family/ipv4/maximum
- vrf-maximum-grouping(grouping)/maximum
- interface-grouping(grouping)/interface-choice/Loopback/Loopback
- vrf-maximum-grouping(grouping)/maximum/routes

### Description

- A new must expression cannot be added.
- The range '[(0, 2147483647)]' is added
- The range has been illegally restricted)

### Reason

1. allowing value 4294967295 is a bug and would have never worked
2. Loopback range in yang interface-grouping was 0-4294967295. However, from device side loopback interface can only support range from 0 to 2147483647. Hence loopback range in yang was modified to be inline with device range.

## XPaths Added

### Description
