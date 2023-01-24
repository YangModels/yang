## Cisco-IOS-XR-um-8000-hw-module-profile-netflow-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed duplicate location key from netflow and sflow-enable containers.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L62)	/hw-module/profile/netflow/ipfix315-enable/locations/location[location-name][location-name2]/location-name2
- (L85)	/hw-module/profile/netflow/sflow-enable/locations/location[location-name][location-name2]/location-name2

## XPaths Modified

- (L64)	/hw-module/profile/netflow/ipfix315-enable/locations/location[location-name]
- (L64)	/hw-module/profile/netflow/ipfix315-enable/locations/location[location-name]
- (L82)	/hw-module/profile/netflow/sflow-enable/locations/location[location-name]
- (L82)	/hw-module/profile/netflow/sflow-enable/locations/location[location-name]

