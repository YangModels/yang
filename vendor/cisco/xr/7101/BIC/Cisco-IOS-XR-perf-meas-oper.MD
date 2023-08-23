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

- (L889)	/performance-measurement/nodes/node[node]/name-profile/delay-profile-rsvptes
- (L919)	/performance-measurement/nodes/node[node]/name-profile/delay-profile-endpoints
- (L934)	/performance-measurement/nodes/node[node]/name-profile/liveness-profile-endpoints
- (L964)	/performance-measurement/nodes/node[node]/name-profile/delay-profile-sr-policies
- (L979)	/performance-measurement/nodes/node[node]/name-profile/delay-profile-interfaces
- (L994)	/performance-measurement/nodes/node[node]/name-profile/liveness-profile-sr-policies

## XPaths Modified

- (L3338)	{PM-ENDPOINT-DETAIL-SEGMENT-LIST-BAG}/delay-measurement-session[session-id]
- (L2338)	{PM-INTF-BAG}/delay-measurement-session[session-id]

