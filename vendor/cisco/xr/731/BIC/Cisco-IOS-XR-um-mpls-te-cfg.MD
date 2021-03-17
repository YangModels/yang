## Cisco-IOS-XR-um-mpls-te-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated the model with the latest CLI changes, one of which was to remove a PCE node which is not backwards compatible. Also CSCvw68645 removed several nodes due to them requiring cisco-support task. Such configuration should not exposed in yang model and since it's not used by customers, it will not impact customer's operations. Updated the mandatory flag for leaf min under overflow, adjustment-threshole and underflow containers via CSCvw97652 which is not backwards compatible.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L2617)	/{IF-BODY}/auto-bw/adjustment-threshold/min
- (L2644)	/{IF-BODY}/auto-bw/overflow/min
- (L2682)	/{IF-BODY}/auto-bw/underflow/min

## XPaths Removed

- (L6355)	/mpls/traffic-eng/fast-reroute/timers/hold-backup
- (L7469)	/mpls/traffic-eng/maxabs
- (L19043)	/mpls/traffic-eng/ltrace-buffer

## XPaths Modified

- (L6303)	/mpls/traffic-eng/affinity-maps/affinity-map[attribute-name]/attribute-name

