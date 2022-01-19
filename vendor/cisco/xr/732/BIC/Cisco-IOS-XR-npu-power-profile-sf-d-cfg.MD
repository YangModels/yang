## Cisco-IOS-XR-npu-power-profile-sf-d-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

External format location string is used and power mode changed to enum instead of uint32.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L77)	/npu-hw-module-profile-config/profile/npu-power-profile/card-type/line-card-locations/line-card-location[location-string]/location-string
- (L82)	/npu-hw-module-profile-config/profile/npu-power-profile/card-type/line-card-locations/line-card-location[location-string]/line-card-node-id[location-id]

## XPaths Modified

- (L92)	/npu-hw-module-profile-config/profile/npu-power-profile/card-type/fabric-card/power-mode
- (L101)	/npu-hw-module-profile-config/profile/npu-power-profile/card-type/line-card-locations/line-card-location[location]

