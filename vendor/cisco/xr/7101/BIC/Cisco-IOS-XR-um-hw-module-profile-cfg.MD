## Cisco-IOS-XR-um-hw-module-profile-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed base-and-micro-segment-f3216 support. Removed second leaf for location in ACL ingress and egress compression. Removed second location leaf for ipv4 and ipv6 ACL TCAM format.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L413)	/hw-module/profile-tcam/format/access-list/ipv4-locations/location[location-name][location-name2]/location-name2
- (L748)	/hw-module/profile-tcam/format/access-list/ipv6-locations/location[location-name][location-name2]/location-name2
- (L1243)	/hw-module/profile-qos/ingress-model/peering-locations/location[location-name][location-name2]/location-name2
- (L1226)	/hw-module/profile-qos/ingress-model/peering
- (L1434)	/hw-module/profile-qos/policer-scale/policer-48000
- (L1440)	/hw-module/profile-qos/policer-scale/policer-64000
- (L1504)	/hw-module/profile-qos/nif-hp-fifo-reserve-locations/location[location-name][location-name2]/location-name2
- (L1146)	/hw-module/profile-qos/max-classmap-size
- (L1177)	/hw-module/profile-qos/max-classmap-size-locations
- (L1447)	/hw-module/profile-qos/policer-scale-locations

## XPaths Modified

- (L427)	/hw-module/profile-tcam/format/access-list/ipv4-locations/location[location-name]
- (L427)	/hw-module/profile-tcam/format/access-list/ipv4-locations/location[location-name]
- (L757)	/hw-module/profile-tcam/format/access-list/ipv6-locations/location[location-name]
- (L757)	/hw-module/profile-tcam/format/access-list/ipv6-locations/location[location-name]
- (L1267)	/hw-module/profile-qos/ingress-model/peering-locations/location[location-name]
- (L1267)	/hw-module/profile-qos/ingress-model/peering-locations/location[location-name]
- (L1517)	/hw-module/profile-qos/nif-hp-fifo-reserve-locations/location[location-name]
- (L1517)	/hw-module/profile-qos/nif-hp-fifo-reserve-locations/location[location-name]

