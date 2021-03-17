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

- (L5310)	{ISIS-SH-IF-ENABLED}/avg-dela-rawy
- (L6834)	{ISIS-SRV6-RSVD-OPCODE}/function-type
- (L6913)	{ISIS-SH-SRV6-LOCATOR}/locator-format
- (L7260)	{ISIS-SH-IPV6-FRR-BACKUP}/num-sid
- (L7321)	{ISIS-SH-IPV6-FRR-BACKUP}/is-s-rv6
- (L7417)	{ISIS-SH-IPV6-PATH}/is-s-rv6
- (L7894)	{ISIS-SH-REP-EL}/repair-s-rv6sid
- (L7899)	{ISIS-SH-REP-EL}/repair-s-rv6-end-func
- (L7904)	{ISIS-SH-REP-EL}/repair-s-rv6-strict-spfsid
- (L7909)	{ISIS-SH-REP-EL}/repair-s-rv6-strict-spf-end-func
- (L7975)	{ISIS-SH-IPV4-FRR-BACKUP}/num-sid
- (L9336)	{ISIS-IPV6-ENDX-SID}/end-xsid
- (L9341)	{ISIS-IPV6-ENDX-SID}/end-xsid-backup
- (L9346)	{ISIS-IPV6-ENDX-SID}/end-xsid-function
- (L9381)	{ISIS-SH-ADJ-PER-LOCATOR}/end-xsid
- (L9386)	{ISIS-SH-ADJ-PER-LOCATOR}/non-frr-end-xsid
- (L9493)	{ISIS-SH-ADJ-IPV6}/end-xsid

## XPaths Modified

- (L7125)	{ISIS-SH-SRV6-LOCATOR}/locator-format

