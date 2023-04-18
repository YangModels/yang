## Cisco-IOS-XR-mpls-te-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removal of leaf 'oor-recovery-duration' and add back as grouping 'OOR-RECOVERY-DURATION', the grouping is used by multiple parents.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L5087)	/mpls-te/global-attributes/srlg/names/name[srlg-name]/static-srlg-members
- (L5958)	/mpls-te/global-attributes/pce-attributes/timer

## XPaths Modified

- (L4673)	/mpls-te/named-tunnels/tunnels/tunnel[tunnel-name][tunnel-type]/tunnel-attributes/self-ping/max-count

