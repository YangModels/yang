## Cisco-IOS-XR-healthcheck-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed redundant leaves plane-up, plane-dn and plane-mcast-dn under health-check/metric-info/fabric-health/mdata/rack-mdata/ due to updates in the native model Cisco-IOS-XR-fabric-plane-health-oper revision 2019-04-05.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L98)	/{SUMMARY}/summary
- (L122)	/{NODE-TABLE}/node-entries/node-entry[node-name]/npus/npu[npu-id]
- (L228)	/health-check/report-info
- (L238)	/health-check/use-case/asic-reset
- (L265)	/health-check/use-case/packet-drop/history/history-nodes/history-node[node-name]/history-npus/history-npu[npu-id]
- (L246)	/health-check/use-case/packet-drop
- (L297)	/health-check/status/status-use-cases/status-use-case[use-case]
- (L312)	/health-check/status-info
- (L326)	/health-check/report/use-cases/use-case[use-case]
- (L130)	/health-check/metric-info/fpd
- (L161)	/health-check/metric-info/platform
- (L233)	/health-check/metric-info/free-memory
- (L321)	/health-check/metric-info/filesystem
- (L333)	/health-check/metric-info/shared-memory
- (L355)	/health-check/metric-info/cpu

## XPaths Added

N/A

## XPaths Removed

- (L130)	/health-check/metric-info/fpd
- (L161)	/health-check/metric-info/platform
- (L233)	/health-check/metric-info/free-memory
- (L321)	/health-check/metric-info/filesystem
- (L333)	/health-check/metric-info/shared-memory
- (L355)	/health-check/metric-info/cpu
- (L141)	/health-check/metric-info/redundancy
- (L148)	/health-check/metric-info/fabric-health
- (L167)	/health-check/metric-info/interface-counters
- (L197)	/health-check/metric-info/asic-errors
- (L244)	/health-check/metric-info/custom-metric
- (L285)	/health-check/metric-info/fabric-stats
- (L419)	/health-check/status/metric
- (L312)	{HCMGR-STATUS-DATA}/collector-pid
- (L317)	{HCMGR-STATUS-DATA}/plat-collector-pid
- (L342)	{HCMGR-STATUS-DATA}/cpu-avg-util
- (L352)	{HCMGR-STATUS-DATA}/sys-resource
- (L357)	{HCMGR-STATUS-DATA}/infra-service
- (L362)	{HCMGR-STATUS-DATA}/platform-stat
- (L367)	{HCMGR-STATUS-DATA}/custom-metric
- (L450)	/health-check/report/metrics

## XPaths Modified

N/A

