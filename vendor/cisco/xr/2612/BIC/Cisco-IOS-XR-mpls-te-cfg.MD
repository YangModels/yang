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

- (L4694)	/mpls-te/named-tunnels/tunnels/tunnel[tunnel-name][tunnel-type]/tunnel-attributes/path-setups/path-setup[path-setup-name]/path-computation/explicit-path-name
- (L5432)	/mpls-te/global-attributes/attribute-set/auto-backup-attributes/auto-backup-attribute[attribute-set-name]/signalled-name/name
- (L7067)	/mpls-te/interfaces/interface[interface-name]/lcac/attribute-name-xr/attribute-name
- (L7090)	/mpls-te/interfaces/interface[interface-name]/lcac/attribute-names/attribute-name[affinity-index]/value
- (L7578)	/mpls-te/gmpls-nni/tunnel-heads/tunnel-head[tunnel-id]/path-options/path-option[preference-level]/path-name

## XPaths Removed

- (L4684)	/mpls-te/named-tunnels/tunnels/tunnel[tunnel-name][tunnel-type]/tunnel-attributes/path-setups/path-setup[path-setup-name]/path-computation/path-computation-server
- (L7051)	/mpls-te/interfaces/interface[interface-name]/lcac/flood-area
- (L880)	/{Mpls-lcac-flooding-igp}

## XPaths Modified

- (L7083)	/mpls-te/interfaces/interface[interface-name]/lcac/attribute-names/attribute-name[affinity-index]/affinity-index

