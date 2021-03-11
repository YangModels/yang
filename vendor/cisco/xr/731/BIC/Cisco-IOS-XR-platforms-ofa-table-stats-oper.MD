## Cisco-IOS-XR-platforms-ofa-table-stats-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Previously, in order to query stats for a particular table, the user would need to input the table's unique id. This id could change from release to release. With this change, we have introduced the capability for the user to query stats using the table name (static).

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L62)	/{Max-re-source-s-table}

## XPaths Modified

- (L1556)	/ofa/stats/nodes/node[node-name]/table-datas/table-data[resource]/resource

