## Cisco-IOS-XE-logging


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/logging/host/ipv4-host-vrf-list/vrf
- native/logging/host/ipv4-host-vrf-transport-list/vrf
- native/logging/host/ipv6/ipv6-host-vrf-list/vrf
- native/logging/host/ipv6/ipv6-host-vrf-transport-list/vrf

### Description

Added new must constraint

### Reason

Updated must conditions to handle:

1. vrf configured via "vrf definition <vrf-name>" and " ip vrf <vrf-name>" both.
2. Check if vrf is properly configured (address- family)

## XPaths Added

### Description

