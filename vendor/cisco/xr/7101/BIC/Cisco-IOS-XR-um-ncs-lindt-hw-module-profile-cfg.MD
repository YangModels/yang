## Cisco-IOS-XR-um-ncs-lindt-hw-module-profile-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

IPv6 Packet Length Support for BGP Flowspec. Removed the second location for ipv4 and ipv6 ACL tcam format.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L382)	/hw-module/profile-tcam/format/access-list/ipv4-locations/location[location-name][location-name2]/location-name2
- (L717)	/hw-module/profile-tcam/format/access-list/ipv6-locations/location[location-name][location-name2]/location-name2
- (L1194)	/hw-module/profile-qos/ingress-model/peering-locations/location[location-name][location-name2]/location-name2
- (L1177)	/hw-module/profile-qos/ingress-model/peering
- (L1097)	/hw-module/profile-qos/max-classmap-size
- (L1128)	/hw-module/profile-qos/max-classmap-size-locations

## XPaths Modified

- (L382)	/hw-module/profile-tcam/format/access-list/ipv4-locations/location[location-name]
- (L382)	/hw-module/profile-tcam/format/access-list/ipv4-locations/location[location-name]
- (L712)	/hw-module/profile-tcam/format/access-list/ipv6-locations/location[location-name]
- (L712)	/hw-module/profile-tcam/format/access-list/ipv6-locations/location[location-name]
- (L1204)	/hw-module/profile-qos/ingress-model/peering-locations/location[location-name]
- (L1204)	/hw-module/profile-qos/ingress-model/peering-locations/location[location-name]

