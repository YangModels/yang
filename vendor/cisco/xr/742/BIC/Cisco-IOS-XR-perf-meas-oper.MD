## Cisco-IOS-XR-perf-meas-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

PM profiles are split into Liveness and delay profiles, removing liveness parameters from the delay profile grouping. Liveness parameters will only be associated with the liveness profile grouping.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L4164)	{PM-SCB-PROBE-BAG}/burst-interval
- (L4171)	{PM-SCB-PROBE-BAG}/burst-interval-is-stretched
- (L1216)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/probe-computation-interval-effective
- (L1259)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/burst-interval
- (L1266)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/burst-interval-effective
- (L1299)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/burst-count
- (L1330)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/delay-measurement-mode
- (L1393)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/periodic-advertisement-interval-effective
- (L1455)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/advertisement-threshold-check-average-delay
- (L1463)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/advertisement-threshold-check-minimum-delay
- (L1471)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/advertisement-threshold-check-maximum-delay
- (L1002)	{PM-LIVENESS-TRANSPORT-PROFILE-BAG}/liveness-detection-config
- (L1021)	{PM-LIVENESS-TRANSPORT-PROFILE-BAG}/burst-interval
- (L1028)	{PM-LIVENESS-TRANSPORT-PROFILE-BAG}/burst-interval-effective
- (L763)	{PM-PPS-TRANSPORT-INFO}/current-multi-hop-burst-interval-stretch-factor
- (L773)	{PM-PPS-TRANSPORT-INFO}/dampened-multi-hop-burst-interval-stretch-factor
- (L783)	{PM-PPS-TRANSPORT-INFO}/inuse-multi-hop-burst-interval-stretch-factor

## XPaths Added

N/A

## XPaths Removed

- (L4058)	{PM-SRPOLICY-CANDIDATE-PATH-BAG}/reverse-path-label

## XPaths Modified

N/A

