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

- (L359)	/performance-measurement

## XPaths Added

N/A

## XPaths Removed

- (L281)	/{PM-LIVENESS-DETECTION}
- (L253)	/{NPU-OFFLOAD}
- (L660)	/{PM-SRPOLICY-LIVE-PROBE-CFG-PROBE}
- (L242)	/{THRESHOLD-CROSSING-CHECK-MINIMUM-DELAY}
- (L213)	/{LIVENESS-DETECTION}
- (L743)	/{PM-ENDPOINT-LIVENESS-DETECTION-PROBE-CFG-PROBE}
- (L582)	/{PM-PROBE-CFG-PROBE}
- (L242)	/{THRESHOLD-CROSSING-CHECK-MINIMUM-DELAY}
- (L797)	/performance-measurement/liveness-name-profile-endpoints
- (L975)	/performance-measurement/delay-name-profile-sr-policies
- (L1069)	/performance-measurement/delay-name-profile-endpoints
- (L1207)	/performance-measurement/delay-name-profile-interfaces
- (L1364)	/performance-measurement/liveness-name-profile-sr-policies

## XPaths Modified

N/A

