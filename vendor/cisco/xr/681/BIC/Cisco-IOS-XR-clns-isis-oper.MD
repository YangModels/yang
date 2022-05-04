## Cisco-IOS-XR-clns-isis-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Change in Yang tool corrected strings repair-s-rv6* to repair-srv6*, end-xsid* to end-x-sid*, and is-s-rv6 to is-srv6. Changed avg-dela-rawy to avg-delay-raw to fix misspelling. Changed SRv6 function-type to sid-behavior, uint32_t to mgmt_srv6_sid_fmt, and num-sid to num-sids for consistency and to comply with current IETF ISIS SRv6 draft.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L2388)	{ISIS-SH-MXM}/max-metric-status-change-time
- (L2393)	{ISIS-SH-MXM}/max-metric-startup-epiry-time
- (L2398)	{ISIS-SH-MXM}/max-metric-bgp-expiry-time
- (L5032)	{ISIS-SH-IF-ENABLED}/avg-dela-rawy
- (L6486)	{ISIS-SRV6-RSVD-OPCODE}/function-type
- (L6491)	{ISIS-SRV6-RSVD-OPCODE}/function-opcode
- (L6545)	{ISIS-SH-SRV6-LOCATOR}/locator-format
- (L6554)	{ISIS-SH-SRV6-LOCATOR}/number-of-reserved-opcodes
- (L6559)	{ISIS-SH-SRV6-LOCATOR}/active
- (L6564)	{ISIS-SH-SRV6-LOCATOR}/out-of-resources
- (L6574)	{ISIS-SH-SRV6-LOCATOR}/opcode
- (L6882)	{ISIS-SH-IPV6-FRR-BACKUP}/num-sid
- (L6943)	{ISIS-SH-IPV6-FRR-BACKUP}/is-s-rv6
- (L7039)	{ISIS-SH-IPV6-PATH}/is-s-rv6
- (L7496)	{ISIS-SH-REP-EL}/repair-s-rv6sid
- (L7501)	{ISIS-SH-REP-EL}/repair-s-rv6-end-func
- (L7506)	{ISIS-SH-REP-EL}/repair-s-rv6-strict-spfsid
- (L7511)	{ISIS-SH-REP-EL}/repair-s-rv6-strict-spf-end-func
- (L7577)	{ISIS-SH-IPV4-FRR-BACKUP}/num-sid
- (L8938)	{ISIS-IPV6-ENDX-SID}/end-xsid
- (L8943)	{ISIS-IPV6-ENDX-SID}/end-xsid-backup
- (L8948)	{ISIS-IPV6-ENDX-SID}/end-xsid-function
- (L8963)	{ISIS-SH-ADJ-PER-LOCATOR}/end-xsid
- (L8968)	{ISIS-SH-ADJ-PER-LOCATOR}/non-frr-end-xsid
- (L9075)	{ISIS-SH-ADJ-IPV6}/end-xsid

## XPaths Modified

- (L2730)	{ISIS-SH-MXM}/max-metric-status-change-time
- (L2735)	{ISIS-SH-MXM}/max-metric-startup-epiry-time
- (L2740)	{ISIS-SH-MXM}/max-metric-bgp-expiry-time
- (L7167)	{ISIS-SH-SRV6-LOCATOR}/locator-format

