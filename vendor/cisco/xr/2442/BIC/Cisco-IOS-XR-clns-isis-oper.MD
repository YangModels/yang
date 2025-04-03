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

- (L2352)	{Isis-sh-lsp-db-install-reason}
- (L3815)	{ISIS-SH-ERR-LOG-ENT}/error-log-level
- (L3820)	{ISIS-SH-ERR-LOG-ENT}/error-code
- (L3825)	{ISIS-SH-ERR-LOG-ENT}/error-reason
- (L8300)	{ISIS-IP-PREFIX-TYPE}/ipv4
- (L8309)	{ISIS-IP-PREFIX-TYPE}/ipv6
- (L8318)	{ISIS-IP-PREFIX-TYPE}/af-name
- (L3635)	{ISIS-TRAFFIC-INTF-P2P-TYPE}/lsp-retransmit-count
- (L3587)	{ISIS-TRAFFIC-INTF-AREA-TYPE}/lsp-drop-count
- (L3593)	{ISIS-TRAFFIC-INTF-AREA-TYPE}/lsp-flooding-dup-count
- (L3074)	{ISIS-SH-GLOBAL-STATS}
- (L3075)	{ISIS-SH-GLOBAL-STATS}/statistics
- (L899)	/{INSTANCE}/instance[instance-name]/summary

## XPaths Modified

N/A

