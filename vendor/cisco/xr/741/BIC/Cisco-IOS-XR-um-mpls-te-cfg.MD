## Cisco-IOS-XR-um-mpls-te-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated the model with the latest CLI changes, one of which was to remove a PCE node which is not backwards compatible. Alsoremoved several nodes due to them requiring cisco-support task. Such configuration should not exposed in yang model and since it's not used by customers, it will not impact customer's operations. Updated the mandatory flag for leaf min under overflow, adjustment-threshole and underflow containers which is not backwards compatible. Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L2992)	/{IF-BODY}/destination

## XPaths Removed

N/A

## XPaths Modified

- (L144)	/{IF-BODY}/affinity
- (L1993)	/{IF-BODY}/autoroute
- (L2067)	/{IF-BODY}/backup-bw
- (L2137)	/{IF-BODY}/signalled-bandwidth
- (L2173)	/{IF-BODY}/fast-reroute
- (L2195)	/{IF-BODY}/forward-class
- (L2208)	/{IF-BODY}/forwarding-adjacency
- (L2231)	/{IF-BODY}/load-share
- (L2244)	/{IF-BODY}/logging
- (L2314)	/{IF-BODY}/signalled-name
- (L2327)	/{IF-BODY}/path-options
- (L2483)	/{IF-BODY}/priority
- (L2513)	/{IF-BODY}/record-route
- (L2521)	/{IF-BODY}/binding-sid
- (L2543)	/{IF-BODY}/policy-class
- (L2560)	/{IF-BODY}/auto-bw
- (L2728)	/{IF-BODY}/path-protection
- (L2750)	/{IF-BODY}/soft-preemption
- (L2758)	/{IF-BODY}/delay-measurement
- (L2766)	/{IF-BODY}/pce
- (L2784)	/{IF-BODY}/path-selection
- (L2863)	/{IF-BODY}/bidirectional

