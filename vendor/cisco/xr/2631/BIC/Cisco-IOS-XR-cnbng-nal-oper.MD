## Cisco-IOS-XR-cnbng-nal-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Replaced disconnect history reason from uint32 to enum. Added up-instance-id in subscriber detail and filter cnbng show commands. Added event history and disconnect data history for warm standby subscribers. Updated timestamp data type from uint32 to uint64. New schema file added for spa warm subscriber. Updated timestamp data type from unit32 to unit64. Control-plane subscriber ID datatype updated to uint64. Reduced failed description string length in cnbng-nal nal_last_failed_data. Updated the data type of node feature-id to String. Removed dynamic route history query from schema. Updated SRG group admin state datatype. Debug improvements in cnbng counters type. Updated nal_main_edm_process_info to include SPIO connection information. Operational data can have duplicated records should justify the leaf-list to list change. Removed dynamic-route-summary-tbl container. Removed dynamic-route-summary-tbl and related cnBNG NAL operational containers and changed disconnect cause to Nal-disc-cause enum.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L4937)	{NAL-SUBS-INFO}/pppflags
- (L4937)	{NAL-SUBS-INFO}/pppflags
- (L4937)	{NAL-SUBS-INFO}/pppflags
- (L4937)	{NAL-SUBS-INFO}/pppflags

## XPaths Modified

N/A

