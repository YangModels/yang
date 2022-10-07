## Cisco-IOS-XR-um-8000-hw-module-profile-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added new leaf pause-threshold-bytes.Added must constraints to list traffic-class and leaf pause-threshold. Updated buffer-extended and buffer-internal nodes. Removed leaf location name.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L668)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id][location-name]/location-name
- (L776)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class[traffic-class-id][location-name]/location-name

## XPaths Modified

- (L662)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id]
- (L662)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id]
- (L780)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class[traffic-class-id]
- (L780)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class[traffic-class-id]

