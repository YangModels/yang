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

- (L21762)	/mpls/traffic-eng/path-selection/ignore/overload

## XPaths Removed

N/A

## XPaths Modified

- (L1999)	/{IF-BODY}/affinity/affinity-attribute-value
- (L2004)	/{IF-BODY}/affinity/mask
- (L5269)	/{IF-BODY}/tunnel-mte/affinity/affinity-attribute-value
- (L5275)	/{IF-BODY}/tunnel-mte/affinity/mask
- (L8186)	/mpls/traffic-eng/named-tunnels/tunnel-tes/tunnel-te[tunnel-name]/affinity/affinity-attribute-value
- (L8191)	/mpls/traffic-eng/named-tunnels/tunnel-tes/tunnel-te[tunnel-name]/affinity/mask
- (L11052)	/mpls/traffic-eng/attribute-set/auto-meshes/auto-mesh[attribute-set-name]/affinity/affinity-attribute
- (L11057)	/mpls/traffic-eng/attribute-set/auto-meshes/auto-mesh[attribute-set-name]/affinity/mask
- (L13103)	/mpls/traffic-eng/attribute-set/auto-backups/auto-backup[attribute-set-name]/affinity/affinity-attribute
- (L13108)	/mpls/traffic-eng/attribute-set/auto-backups/auto-backup[attribute-set-name]/affinity/mask
- (L15088)	/mpls/traffic-eng/attribute-set/path-options/path-option[attribute-set-name]/affinity/affinity-attribute
- (L15093)	/mpls/traffic-eng/attribute-set/path-options/path-option[attribute-set-name]/affinity/mask
- (L17215)	/mpls/traffic-eng/attribute-set/p2mp-tes/p2mp-te[attribute-set-name]/affinity/affinity-attribute
- (L17220)	/mpls/traffic-eng/attribute-set/p2mp-tes/p2mp-te[attribute-set-name]/affinity/mask
- (L19467)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/affinity-attribute
- (L19472)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/mask
- (L21668)	/mpls/traffic-eng/path-selection/loose-expansion/affinity/class-type[type]/affinity-attribute
- (L21673)	/mpls/traffic-eng/path-selection/loose-expansion/affinity/class-type[type]/mask

