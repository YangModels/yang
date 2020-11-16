## Cisco-IOS-XR-perf-meas-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

The pm liveness state info grouping used by a container was removed as the grouping was renamed.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1189)	{PM-DELAY-TRANSPORT-SUMMARY-BAG}/total-delay-sessions
- (L2216)	{PM-SRPOLICY-ATOMIC-PATH-BAG}/liveness-detection-info
- (L2309)	{PM-SRPOLICY-SEGMENT-LIST-BAG}/liveness-detection-info
- (L2573)	{PM-SRPOLICY-CANDIDATE-PATH-BAG}/liveness-detection-info
- (L191)	/performance-measurement/nodes/node[node]/sr-policies/sr-policy-delay/sr-policy-aggregated-histories
- (L206)	/performance-measurement/nodes/node[node]/sr-policies/sr-policy-delay/sr-policy-probe-histories
- (L289)	/performance-measurement/nodes/node[node]/rsvpte-tunnels/rsvpte-delay/rsvpte-aggregated-histories
- (L349)	/performance-measurement/nodes/node[node]/rsvpte-tunnels/rsvpte-delay/rsvpte-probe-histories
- (L440)	/performance-measurement/nodes/node[node]/interfaces/interface-delay/interface-probe-histories
- (L455)	/performance-measurement/nodes/node[node]/interfaces/interface-delay/interface-aggregated-histories
- (L508)	/performance-measurement/nodes/node[node]/distribution-records

## XPaths Modified

- (L626)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/tos-traffic-class-value
- (L632)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/tos-dscp-value
- (L966)	{PM-INTF-LOSS-SESSION-BAG}/probe-not-running-reason
- (L2598)	{PM-SCB-PROBE-BAG}/probe-not-running-reason

