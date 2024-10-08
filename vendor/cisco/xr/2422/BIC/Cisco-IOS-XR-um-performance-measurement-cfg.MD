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

- (L2400)	/performance-measurement/liveness-profile/sr-policy/default/npu-offload/enable
- (L2719)	/performance-measurement/liveness-profile/names/name[profile-name]/npu-offload/enable

## XPaths Added

- (L1145)	/performance-measurement/delay-profile/rsvp-te/default/probe/measurement-mode/one-way
- (L1644)	/performance-measurement/delay-profile/endpoint/default/probe/flow-label/explicits
- (L2304)	/performance-measurement/liveness-profile/sr-policy/default/probe/flow-label/explicits
- (L2441)	/performance-measurement/liveness-profile/endpoint/default/probe/flow-label/explicits
- (L2623)	/performance-measurement/liveness-profile/names/name[profile-name]/probe/flow-label/explicits
- (L3064)	/performance-measurement/probe-profile/names/name[profile-name]/flow-label/explicits

## XPaths Removed

- (L2832)	/performance-measurement/distribute-sessions
- (L2848)	/performance-measurement/hardware-offload

## XPaths Modified

- (L1010)	/performance-measurement/delay-profile/interfaces/default/advertisement/anomaly-check/upper-bound
- (L1021)	/performance-measurement/delay-profile/interfaces/default/advertisement/anomaly-check/lower-bound
- (L1549)	/performance-measurement/delay-profile/sr-policy/default/advertisement/anomaly-check/upper-bound
- (L1560)	/performance-measurement/delay-profile/sr-policy/default/advertisement/anomaly-check/lower-bound
- (L2201)	/performance-measurement/delay-profile/names/name[profile-name]/advertisement/anomaly-check/upper-bound
- (L2212)	/performance-measurement/delay-profile/names/name[profile-name]/advertisement/anomaly-check/lower-bound

