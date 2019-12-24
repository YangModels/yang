## Cisco-IOS-XE-zone.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Modified

### Description/Reason

Type change from leafref to string of source/destination zone in zone-pair. Source/destination zone can be internal self zone which cannot be configured - therefore cannot be a leafref as it is rejected

- /native/zone-pair/ios-zone:security/ios-zone:source
- /native/zone-pair/ios-zone:security/ios-zone:destination

## XPaths Added

N/A
