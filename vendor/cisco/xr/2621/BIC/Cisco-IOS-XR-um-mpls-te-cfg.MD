## Cisco-IOS-XR-um-mpls-te-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated the model with the latest CLI changes, one of which was to remove a PCE node which is not backwards compatible. Also removed several nodes due to them requiring cisco-support task. Such configuration should not exposed in yang model and since it's not used by customers, it will not impact customer's operations. Updated the mandatory flag for leaf min under overflow, adjustment-threshole and underflow containers which is not backwards compatible. Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L10383)	/mpls/traffic-eng/hw-oor/yellow/recovery-duration
- (L10461)	/mpls/traffic-eng/hw-oor/red/recovery-duration
- (L10710)	/mpls/traffic-eng/pce/stateful-client/timers/redundancy
- (L19535)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/affinity-attribute
- (L19540)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/mask
- (L19545)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/includes
- (L20149)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/include-stricts
- (L21357)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/ignore
- (L21362)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/exclude-all

## XPaths Modified

N/A

