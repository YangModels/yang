## Cisco-IOS-XR-mpls-te-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed flood-area from lcac. Restricted LCAC attribute-name leaf-list values to 32 characters. Removal of leaf 'oor-recovery-duration' and add back as grouping 'OOR-RECOVERY-DURATION', the grouping is used by multiple parents. Restricted named-tunnel computation explicit path names to 99 characters and removed the unused path-computation-server leaf. Restricted auto-backup attribute-set signalled-name values to 64 characters.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L7063)	/mpls-te/interfaces/interface[interface-name]/lcac/flood-area
- (L893)	/{Mpls-lcac-flooding-igp}

## XPaths Modified

N/A

