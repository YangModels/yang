## Cisco-IOS-XE-cts.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description

Deprecated the list "sgt-map" which has key {ip, sgt}

### Reason

To fix backward incompatible changes

- /native/cts/ios-cts:role-based/ios-cts:sgt-map

## XPaths Modified

N/A

## XPaths Added

### Description

Created two lists "sgt-map-list" which has key {ip} and "sgt-map-vrf-list" which has key {vrf,ip}

- /native/cts/ios-cts:role-based/ios-cts:sgt-map-list

- /native/cts/ios-cts:role-based/ios-cts:sgt-map-vrf-list/ios-cts:sgt-map
