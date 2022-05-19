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

- (L84)	/{Pm-protocol-and-encap}
- (L254)	/performance-measurement/protocol/pm-mpls
- (L276)	/performance-measurement/delay-profile-rsvp-te/probe/type-of-service/traffic-class-values
- (L288)	/performance-measurement/delay-profile-rsvp-te/probe/type-of-service/dscp-values
- (L341)	/performance-measurement/delay-profile-interface/probe
- (L383)	/performance-measurement/delay-profile-sr-policy/probe
- (L534)	/performance-measurement/maximum-pps

## XPaths Modified

N/A

