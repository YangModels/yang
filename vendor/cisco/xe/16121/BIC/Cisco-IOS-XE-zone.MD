 Cisco-IOS-XE-zone.yang

- [XPaths Modified](#xpaths-modified)

## XPaths Modified

- Type change from leafref to string of source/destination zone in zone-pair. Source/destination zone can be internal self zone which cannot be configured - therefore cannot be a leafref as it is rejected

- /native/zone-pair/ios-zone:security/ios-zone:source
-/native/zone-pair/ios-zone:security/ios-zone:destination
