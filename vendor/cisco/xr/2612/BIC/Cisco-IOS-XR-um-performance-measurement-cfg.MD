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

N/A

## XPaths Added

- (L159)	/performance-measurement/interfaces/interface[interface-name]/delay-measurement/advertise-delay/delay-value

## XPaths Removed

- (L135)	/performance-measurement/interfaces/interface[interface-name]/delay-measurement/advertise-delay
- (L128)	/performance-measurement/interfaces/interface[interface-name]/delay-measurement/fallback
- (L1942)	/performance-measurement/delay-profile/endpoint/default/probe/measurement-mode/timestamp-format
- (L2120)	/performance-measurement/delay-profile/endpoint/default/histogram
- (L2483)	/performance-measurement/delay-profile/names/name[profile-name]/advertisement/ber-threshold
- (L2493)	/performance-measurement/delay-profile/names/name[profile-name]/advertisement/per-threshold
- (L2911)	/performance-measurement/liveness-profile/endpoint/default/liveness-detection/npu-offload

## XPaths Modified

- (L149)	/performance-measurement/interfaces/interface[interface-name]/delay-measurement/advertise-delay

