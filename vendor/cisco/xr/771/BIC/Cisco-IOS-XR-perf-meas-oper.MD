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

- (L2580)	{PM-DELAY-SUMMARY-BAG}/delay-global-counters
- (L2346)	{PM-LOSS-SUMMARY-BAG}/delay-global-counters

## XPaths Added

N/A

## XPaths Removed

- (L2685)	{PM-CAPABILITY-INFO}/hardware-offload-capability-info
- (L2708)	{PM-CAPABILITY-INFO}/hardware-offload-supported
- (L1049)	{PM-LIVENESS-TRANSPORT-PROFILE-BAG}/tx-interval-effectiv-endpoint
- (L1049)	{PM-LIVENESS-TRANSPORT-PROFILE-BAG}/tx-interval-effectiv-endpoint
- (L923)	{PM-PPS-SUMMARY-BAG}/pps-pool
- (L928)	{PM-PPS-SUMMARY-BAG}/interface-session-info
- (L934)	{PM-PPS-SUMMARY-BAG}/sr-policy-session-info
- (L940)	{PM-PPS-SUMMARY-BAG}/rsvp-te-session-info
- (L946)	{PM-PPS-SUMMARY-BAG}/endpoint-session-info
- (L723)	{PM-DR-INFO}/linecard-name
- (L1049)	{PM-LIVENESS-TRANSPORT-PROFILE-BAG}/tx-interval-effectiv-endpoint

## XPaths Modified

N/A

