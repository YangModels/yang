## Cisco-IOS-XR-ipv4-bgp-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Changed the leaf name from label-o-or-version to label-oor-version.

## XPaths Obsoleted

- (L1137)	/{AF-TABLE}/afs/af[af-name]/bmp-path-table-generic
- (L1319)	/{AF-TABLE}/afs/af[af-name]/bmp-paths/bmp-path[network]

## XPaths Deprecated

- (L1314)	/{AF-TABLE}/afs/af[af-name]/bmp-paths

## XPaths Added

N/A

## XPaths Removed

- (L12568)	{BGP-UPDGRP-BAG}/contains-slow-peer
- (L8374)	{BGP-PERF-NBR-AF}/refresh-mismatch-update-blocked
- (L8380)	{BGP-PERF-NBR-AF}/refresh-mismatch-withdraw-spurious
- (L9166)	{BGP-NBR-AF}/slow-peer-flags
- (L9171)	{BGP-NBR-AF}/slow-peer-static
- (L9176)	{BGP-NBR-AF}/slow-peer-dynamic
- (L9181)	{BGP-NBR-AF}/slow-peer-permanent
- (L9186)	{BGP-NBR-AF}/slow-peer-count
- (L7033)	{BGP-GLOBAL-PROCESS-INFO-VRF}/slow-peer-detection-enabled
- (L17632)	{BGP-AF-DEP}/slow-peer-detection-enable
- (L17642)	{BGP-AF-DEP}/slow-peer-update-group-split-type

## XPaths Modified

- (L9803)	{BGP-NBR-BAG}/previous-connection-state

