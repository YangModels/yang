## Cisco-IOS-XR-perf-meas-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Container probe under delay-profile-rsvp-te, delay-profile-interface and delay-profile-sr-policy are replaced by grouping PROBE, PM-PROBE-CFG-PROBE, PM-SRPOLICY-PROBE-CFG-PROBE when adding new list delay-name-profile-rsvp-tes, delay-name-profile-interfaces, delay-name-profile-sr-policies to used it in named profile feature development.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L124)	/{Pm-protocol-and-encap}
- (L336)	/{PROBE}/probe/type-of-service/traffic-class-value
- (L345)	/{PROBE}/probe/protocol
- (L678)	/performance-measurement/protocol/pm-mpls
- (L729)	/performance-measurement/delay-profile-rsvp-te
- (L598)	/performance-measurement/delay-name-profile-rsvp-tes
- (L846)	/performance-measurement/maximum-pps

## XPaths Modified

N/A

