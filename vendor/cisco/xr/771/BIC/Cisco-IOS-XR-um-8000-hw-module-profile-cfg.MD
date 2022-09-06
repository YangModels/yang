## Cisco-IOS-XR-um-8000-hw-module-profile-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added leaf pause-threshold-bytes. Updated buffer-extended and buffer-internal nodes.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L688)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id][location-name]/pause-threshold
- (L661)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id][location-name]

## XPaths Removed

- (L560)	/hw-module/profile/stats/acl-permit/no-bvi-ingress

## XPaths Modified

- (L682)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id][location-name]/pause-threshold
- (L740)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id][location-name]/kbytes/headroom
- (L755)	/hw-module/profile/priority-flow-control/locations/location[location-name]/buffer-extended/traffic-class[traffic-class-id][location-name]/mbytes/headroom

