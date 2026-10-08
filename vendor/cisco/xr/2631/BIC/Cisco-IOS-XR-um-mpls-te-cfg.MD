## Cisco-IOS-XR-um-mpls-te-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated affinity-name length handling, removed PCE and cisco-support-only nodes, updated mandatory flags under overflow thresholds, and added cisco-support task yang nodes for latest CLI alignment. Restricted named-tunnel computation explicit path names to 99 characters and removed the unused path-computation-server leaf.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L10388)	/mpls/traffic-eng/hw-oor/yellow/recovery-duration
- (L10466)	/mpls/traffic-eng/hw-oor/red/recovery-duration
- (L10715)	/mpls/traffic-eng/pce/stateful-client/timers/redundancy
- (L19540)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/affinity-attribute
- (L19545)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/mask
- (L19550)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/includes
- (L20154)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/include-stricts
- (L21362)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/ignore
- (L21367)	/mpls/traffic-eng/attribute-set/p2p-tes/p2p-te[attribute-set-name]/affinity/exclude-all

## XPaths Modified

N/A

