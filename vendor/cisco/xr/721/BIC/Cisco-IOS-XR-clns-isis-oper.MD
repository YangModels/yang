## Cisco-IOS-XR-clns-isis-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

The type of the leaf nodes max-mettric-status-change-time, max-metric-startup-expiry-time and max-metric-bgp-expiry-time in the groupong ISIS-SH-MXM has been changed from uint32 to ISIS-SH-TIMESTAMP-TYPE via CSCvs61854. The enums of end-tn, end-t-with-psp,end-t-with-usp, end-t-with-psp-usp, end-b6, end-dx2u and end-dx2m have been changed to end-tbl, end-tbl-with-psp, end-tbl-with-usp, end-tbl-with-psp-usp,end-b6-insert, end-dt2u and end-dt2m respectively in the enumeration Srv6-end-function via CSCvs85453. The leaf function-opcode have been removed from the grouping ISIS-SRV6-RSVD-OPCODE. .

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1168)	{Srv6-end-function}
- (L1172)	{Srv6-end-function}
- (L1176)	{Srv6-end-function}
- (L1180)	{Srv6-end-function}
- (L1184)	{Srv6-end-function}
- (L1224)	{Srv6-end-function}
- (L1228)	{Srv6-end-function}
- (L2388)	{ISIS-SH-MXM}/max-metric-status-change-time
- (L2393)	{ISIS-SH-MXM}/max-metric-startup-epiry-time
- (L2398)	{ISIS-SH-MXM}/max-metric-bgp-expiry-time
- (L6491)	{ISIS-SRV6-RSVD-OPCODE}/function-opcode
- (L6554)	{ISIS-SH-SRV6-LOCATOR}/number-of-reserved-opcodes
- (L6559)	{ISIS-SH-SRV6-LOCATOR}/active
- (L6564)	{ISIS-SH-SRV6-LOCATOR}/out-of-resources
- (L6574)	{ISIS-SH-SRV6-LOCATOR}/opcode

## XPaths Modified

- (L2595)	{ISIS-SH-MXM}/max-metric-status-change-time
- (L2600)	{ISIS-SH-MXM}/max-metric-startup-epiry-time
- (L2605)	{ISIS-SH-MXM}/max-metric-bgp-expiry-time

