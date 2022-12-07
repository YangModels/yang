## Cisco-IOS-XR-um-8000-hw-module-profile-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Corrected BD flush convergence mode value. Updated buffer-extended and buffer-internal nodes. Removed leaf location name.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L717)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id][location-name]/location-name
- (L821)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class-default[traffic-class-id][location-name]/location-name
- (L845)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class[traffic-class-id][location-name]/location-name
- (L897)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class-default[traffic-class-id][location-name]/location-name

## XPaths Modified

- (L709)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id]
- (L709)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id]
- (L752)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id]/ms/headroom
- (L767)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id]/us/headroom
- (L808)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class-default[traffic-class-id]
- (L808)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class-default[traffic-class-id]
- (L827)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class[traffic-class-id]
- (L827)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class[traffic-class-id]
- (L894)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class-default[traffic-class-id]
- (L894)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-internal/traffic-class-default[traffic-class-id]

