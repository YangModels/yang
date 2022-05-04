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

N/A

## XPaths Added

N/A

## XPaths Removed

- (L545)	{PM-LIVENESS-PROFILE-BAG}/multiplier
- (L579)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/liveness-detection-config
- (L834)	{PM-LOSS-WINDOW-BAG}/current-packet-t-xin-window
- (L839)	{PM-LOSS-WINDOW-BAG}/current-packet-r-xin-window
- (L1189)	{PM-DELAY-TRANSPORT-SUMMARY-BAG}/total-delay-sessions
- (L1234)	{PM-SUMMARY-BAG}/rate-limiting-information
- (L1301)	{PM-RSVPTE-LSP-HISTORY-BAG}/lspid
- (L1264)	{PM-RSVPTE-LSP-DELAY-METRICS-BAG}/lspid
- (L1365)	{PM-RSVPTE-LSP-DELAY-BAG}/lspid
- (L1421)	{PM-RSVPTE-LSP-DELAY-COUNTERS-BAG}/lspid
- (L2216)	{PM-SRPOLICY-ATOMIC-PATH-BAG}/liveness-detection-info
- (L2309)	{PM-SRPOLICY-SEGMENT-LIST-BAG}/liveness-detection-info
- (L2458)	{PM-SCB-PROBE-RESULTS-BAG}/numberof-packets-received
- (L2573)	{PM-SRPOLICY-CANDIDATE-PATH-BAG}/liveness-detection-info
- (L126)	{PM-COUNTER-RESP-BAG}/received-packet-error-urotlv-not-present
- (L191)	/performance-measurement/nodes/node[node]/sr-policies/sr-policy-delay/sr-policy-aggregated-histories
- (L206)	/performance-measurement/nodes/node[node]/sr-policies/sr-policy-delay/sr-policy-probe-histories
- (L289)	/performance-measurement/nodes/node[node]/rsvpte-tunnels/rsvpte-delay/rsvpte-aggregated-histories
- (L349)	/performance-measurement/nodes/node[node]/rsvpte-tunnels/rsvpte-delay/rsvpte-probe-histories
- (L440)	/performance-measurement/nodes/node[node]/interfaces/interface-delay/interface-probe-histories
- (L455)	/performance-measurement/nodes/node[node]/interfaces/interface-delay/interface-aggregated-histories

## XPaths Modified

- (L1084)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/tos-traffic-class-value
- (L1090)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/tos-dscp-value
- (L1455)	{PM-INTF-LOSS-SESSION-BAG}/probe-not-running-reason
- (L3892)	{PM-SCB-PROBE-BAG}/probe-not-running-reason

