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

- (L654)	/{PM-SRPOLICY-LIVE-PROBE-CFG-PROBE}/probe/measurement-mode
- (L706)	/{PM-ENDPOINT-LIVENESS-DETECTION-PROBE-CFG-PROBE}/probe/measurement-mode

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L753)	/performance-measurement/protocol/twamp-light/delay-measurement/unauthenticated/querier-source-port
- (L783)	/performance-measurement/protocol/twamp-light/delay-measurement/unauthenticated/querier-destination-port

