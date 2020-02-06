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

- (L675)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/version
- (L686)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/basic-trap-types
- (L699)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/advanced-trap-types1
- (L708)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/encrypted-user-communities/encrypted-user-community[community-name]/advanced-trap-types2
- (L742)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/version
- (L753)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/basic-trap-types
- (L766)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/advanced-trap-types1
- (L775)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/type6-encrypted-user-communities/type6-encrypted-user-community[community-name]/advanced-trap-types2
- (L815)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/version
- (L826)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/basic-trap-types
- (L839)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/advanced-trap-types1
- (L848)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-user-communities/inform-user-community[community-name]/advanced-trap-types2
- (L882)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/version
- (L893)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/basic-trap-types
- (L906)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/advanced-trap-types1
- (L915)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-type6-encrypted-user-communities/inform-type6-encrypted-user-community[community-name]/advanced-trap-types2
- (L949)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/version
- (L960)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/basic-trap-types
- (L973)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/advanced-trap-types1
- (L982)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/inform-host/inform-encrypted-user-communities/inform-encrypted-user-community[community-name]/advanced-trap-types2
- (L1019)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/version
- (L1030)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/basic-trap-types
- (L1043)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/advanced-trap-types1
- (L1052)	/{TRAP-HOST-TABLE}/trap-hosts/trap-host[ip-address]/default-user-communities/default-user-community[community-name]/advanced-trap-types2

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

