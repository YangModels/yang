## Cisco-IOS-XR-snmp-agent-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L669)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/version
- (L680)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/basic-trap-types
- (L693)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/advanced-trap-types1
- (L702)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/advanced-trap-types2
- (L731)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/version
- (L742)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/basic-trap-types
- (L755)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/advanced-trap-types1
- (L764)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/advanced-trap-types2
- (L799)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/version
- (L810)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/basic-trap-types
- (L823)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/advanced-trap-types1
- (L832)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/advanced-trap-types2
- (L861)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/version
- (L872)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/basic-trap-types
- (L885)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/advanced-trap-types1
- (L894)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/advanced-trap-types2
- (L923)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/version
- (L934)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/basic-trap-types
- (L947)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/advanced-trap-types1
- (L956)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/advanced-trap-types2
- (L988)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/version
- (L999)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/basic-trap-types
- (L1012)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/advanced-trap-types1
- (L1021)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/advanced-trap-types2

## XPaths Removed

- (L659)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/port
- (L665)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/version
- (L676)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/basic-trap-types
- (L689)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/advanced-trap-types1
- (L698)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/advanced-trap-types2
- (L722)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/port
- (L728)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/version
- (L739)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/basic-trap-types
- (L752)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/advanced-trap-types1
- (L761)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/advanced-trap-types2
- (L791)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/port
- (L797)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/version
- (L808)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/basic-trap-types
- (L821)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/advanced-trap-types1
- (L830)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/advanced-trap-types2
- (L854)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/port
- (L860)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/version
- (L871)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/basic-trap-types
- (L884)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/advanced-trap-types1
- (L893)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/advanced-trap-types2
- (L917)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/port
- (L923)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/version
- (L934)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/basic-trap-types
- (L947)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/advanced-trap-types1
- (L956)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/advanced-trap-types2
- (L983)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/port
- (L989)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/version
- (L1000)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/basic-trap-types
- (L1013)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/advanced-trap-types1
- (L1022)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/advanced-trap-types2

## XPaths Modified

N/A

