## Cisco-IOS-XR-um-performance-measurement-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed container distribute-sessions and updated range for tx-interval.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L2440)	/performance-measurement/liveness-profile/sr-policy/default/npu-offload/enable
- (L2759)	/performance-measurement/liveness-profile/names/name[profile-name]/npu-offload/enable

## XPaths Added

- (L1185)	/performance-measurement/delay-profile/rsvp-te/default/probe/measurement-mode/one-way
- (L1684)	/performance-measurement/delay-profile/endpoint/default/probe/flow-label/explicits
- (L2344)	/performance-measurement/liveness-profile/sr-policy/default/probe/flow-label/explicits
- (L2481)	/performance-measurement/liveness-profile/endpoint/default/probe/flow-label/explicits
- (L2663)	/performance-measurement/liveness-profile/names/name[profile-name]/probe/flow-label/explicits
- (L3104)	/performance-measurement/probe-profile/names/name[profile-name]/flow-label/explicits

## XPaths Removed

- (L2832)	/performance-measurement/distribute-sessions
- (L2848)	/performance-measurement/hardware-offload

## XPaths Modified

- (L1050)	/performance-measurement/delay-profile/interfaces/default/advertisement/anomaly-check/upper-bound
- (L1061)	/performance-measurement/delay-profile/interfaces/default/advertisement/anomaly-check/lower-bound
- (L1589)	/performance-measurement/delay-profile/sr-policy/default/advertisement/anomaly-check/upper-bound
- (L1600)	/performance-measurement/delay-profile/sr-policy/default/advertisement/anomaly-check/lower-bound
- (L2241)	/performance-measurement/delay-profile/names/name[profile-name]/advertisement/anomaly-check/upper-bound
- (L2252)	/performance-measurement/delay-profile/names/name[profile-name]/advertisement/anomaly-check/lower-bound

