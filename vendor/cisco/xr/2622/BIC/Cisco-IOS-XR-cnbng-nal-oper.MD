## Cisco-IOS-XR-cnbng-nal-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

[CSCwt16287] Replaced disconnect history reason from uint32 to enum [CSCwr62010]Added up-instance-id in subscriber detail and filter cnbng show commands.[CSCwp18613]Added event history and disconnect data history for warm standby subscribers.[CSCwq61202]Updated timestamp data type from uint32 to uint64.[CSCwp83752]New Bag file added for spa warm subscriber.[CSCwo33880]Updated timestamp data type from unit32 to unit64.[CSCwo33074]Control-plane subscriber ID datatype updated to uint64.[CSCwe38809]Reduced failed description string length in cnbng-nal nal_last_failed_data.[CSCwd53063]Updated the data type of node feature-id to String.[CSCwc62211]Removed dynamic route history query from schema.[CSCwc50899]Updated SRG group admin state datatype.[CSCvz70278]Debug improvements in cnbng counters type.[CSCvz42446]Updated nal_main_edm_process_info to include SPIO connection information.[CSCvv94638]Operational data can have duplicated records should justify the leaf-list to list change. [CSCws62508] Removed dynamic-route-summary-tbl container.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L2806)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-node-assoc-applied
- (L2812)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-session-report-applied
- (L2817)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-srg-node-report-applied
- (L2822)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-gtpu-control-pkt-applied
- (L2806)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-node-assoc-applied
- (L2812)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-session-report-applied
- (L2817)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-srg-node-report-applied
- (L2822)	{NAL-MAIN-EDM-CP-CONN-STS-INFO}/dscp-gtpu-control-pkt-applied

## XPaths Modified

N/A

