## Cisco-IOS-XR-sysmgr-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Earlier only single instance of process was returned which was bug.Fix needed because process can have multiple instances.As part of new design this issue is addressed and we now return list of all process instances.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L74)	/{NODE}/node[node-name]/name/process-name-run-infos/process-name-run-info[proc-name]
- (L89)	/{NODE}/node[node-name]/name/process-name-infos/process-name-info[proc-name]
- (L104)	/{NODE}/node[node-name]/name/process-name-run-details/process-name-run-detail[proc-name]
- (L119)	/{NODE}/node[node-name]/name/process-name-runverboses/process-name-runverbose[proc-name]
- (L134)	/{NODE}/node[node-name]/name/process-name-details/process-name-detail[proc-name]
- (L149)	/{NODE}/node[node-name]/name/process-name-verboses/process-name-verbose[proc-name]

## XPaths Modified

N/A

