## Cisco-IOS-XR-sysadmin-fabric-mgr-fsdb-aggregator-iosxrwbd.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed admin plane config.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L216)	/{fsdb_agg_conf_plane}/plane[plane_id]/b2b
- (L224)	/{fsdb_agg_conf_plane}/plane[plane_id]/instance[instance-id]
- (L238)	/{fsdb_agg_conf_plane}/plane[plane_id]/instance_folded[instance-id]
- (L443)	/{fabric_rack_health}/rack_info_list[rack_id]

## XPaths Modified

- (L84)	/{plane_show}/plane[planeid]/planeid
- (L221)	/{fsdb_agg_conf_plane}/plane[plane_id]/plane_id
- (L238)	/{fsdb_agg_conf_plane}/link/port/location[loc_str]/loc_str
- (L499)	/{fsdb_agg_plane_clear}/plane[planeid]/planeid
- (L750)	/{fsdb_aggr_bundle}/bundle/port/location[loc_str]/loc_str
- (L761)	/{fsdb_aggr_bundle}/bundle/location[loc_str]/loc_str
- (L791)	/{fsdb_aggr}/fsdbagg_link/port[portname]/portname

