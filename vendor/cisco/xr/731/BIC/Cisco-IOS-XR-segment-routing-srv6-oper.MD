## Cisco-IOS-XR-segment-routing-srv6-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

'SRV6-SIDMGR-PARAMS-ENCAP-HOPLIMIT' is changed to 'SRV6-SIDMGR-PARAMS-SET-OR-PROPAGATE' as more encap info is added, also depreceating the leaf 'encap-ttl-propagate'.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L747)	{SRV6-SID-INFO}/behavior-type
- (L446)	{MGMT-SRV6-SID-CTX-U-A}/u-a-base-ctx
- (L655)	{MGMT-SRV6-SID-CTX-KEY}/u-a-shift-only
- (L664)	{MGMT-SRV6-SID-CTX-KEY}/u-a-psp-usd
- (L787)	{MGMT-SRV6-PLATFORM-SIG-PARAMS}/max-t-insert
- (L792)	{MGMT-SRV6-PLATFORM-SIG-PARAMS}/max-t-encap
- (L837)	{SRV6-PLATFORM-SUPPORT}/end-func
- (L842)	{SRV6-PLATFORM-SUPPORT}/transit-func
- (L903)	{SRV6-PLATFORM-CAPABILITY}/max-sid
- (L919)	{SRV6-OOR-SUMMARY}/out-of-resources-state

## XPaths Modified

- (L984)	{MGMT-SRV6-SID-CTX-KEY}/u-a-shift-only
- (L993)	{MGMT-SRV6-SID-CTX-KEY}/u-a-psp-usd
- (L1002)	{MGMT-SRV6-SID-CTX-KEY}/u-n-shift-only
- (L1011)	{MGMT-SRV6-SID-CTX-KEY}/u-n-psp-usd
- (L1020)	{MGMT-SRV6-SID-CTX-KEY}/u-dt4
- (L1029)	{MGMT-SRV6-SID-CTX-KEY}/u-dt6
- (L1056)	{MGMT-SRV6-SID-CTX-KEY}/sid-context-type

