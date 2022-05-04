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

- (L442)	/{PROBE}/probe/burst-interval
- (L544)	/{PM-SRPOLICY-PROBE-CFG-PROBE}/probe/burst-interval
- (L611)	/{PM-PROBE-CFG-PROBE}/probe/burst-interval
- (L685)	/{PM-SRPOLICY-LIVE-PROBE-CFG-PROBE}/probe/measurement-mode
- (L693)	/{PM-SRPOLICY-LIVE-PROBE-CFG-PROBE}/probe/burst-interval
- (L749)	/{PM-ENDPOINT-LIVENESS-DETECTION-PROBE-CFG-PROBE}/probe/burst-interval
- (L757)	/{PM-ENDPOINT-LIVENESS-DETECTION-PROBE-CFG-PROBE}/probe/measurement-mode
- (L775)	/performance-measurement/liveness-name-profile-endpoints
- (L953)	/performance-measurement/delay-name-profile-sr-policies
- (L1020)	/performance-measurement/delay-profile-rsvp-te/probe/burst-interval
- (L1047)	/performance-measurement/delay-name-profile-endpoints
- (L1185)	/performance-measurement/delay-name-profile-interfaces
- (L1342)	/performance-measurement/liveness-name-profile-sr-policies

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

N/A

