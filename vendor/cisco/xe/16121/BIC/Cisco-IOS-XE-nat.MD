## Cisco-IOS-XE-nat.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description
Added NAT64 changes made for 16.12 as deprecated

### Reason
Yang cloning had removed 16.11.1 changes.

- /native/ios-nat:nat64/ios-nat:v6v4/ios-nat:list/ios-nat:list/ios-nat:interface/ios-nat:vrf

## XPaths Modified

### Description
Allow multiple NAT cli's to use same ACL

### Reason
Previous code commit had broken this functionality

- /native/ip/ios-nat:inside/ios-nat:source/ios-nat:list/ios-nat:interface

## XPaths Added

### Description
New feature required CLI extension. Deprecated old model and added new leaf.

- /native/ios-nat:nat64/ios-nat:route
- /native/ios-nat:nat64/ios-nat:route/ios-nat:global
- /native/ios-nat:nat64/ios-nat:route/ios-nat:ipv6-prefix
- /native/ios-nat:nat64/ios-nat:route/ios-nat:vrf



