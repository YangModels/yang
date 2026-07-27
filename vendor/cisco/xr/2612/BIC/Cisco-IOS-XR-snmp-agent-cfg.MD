## Cisco-IOS-XR-snmp-agent-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Converted some default nodes to mandatory.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L676)	/{TRAP-HOST-TABLE}/trap-hosts
- (L1161)	/snmp/encrypted-community-maps/encrypted-community-map[community-name]
- (L1154)	/snmp/encrypted-community-maps
- (L1271)	/snmp/administration/default-communities/default-community[community-name]
- (L1264)	/snmp/administration/default-communities
- (L1330)	/snmp/administration/type6-encrypted-communities/type6-encrypted-community[community-name]
- (L1323)	/snmp/administration/type6-encrypted-communities
- (L1387)	/snmp/administration/encrypted-communities/encrypted-community[community-name]
- (L1380)	/snmp/administration/encrypted-communities
- (L1517)	/snmp/type6-encrypted-community-maps/type6-encrypted-community-map[community-name]
- (L1510)	/snmp/type6-encrypted-community-maps
- (L2092)	/snmp/default-community-maps/default-community-map[community-name]
- (L2086)	/snmp/default-community-maps
- (L2200)	/snmp/users
- (L2340)	/snmp/groups

## XPaths Added

- (L1126)	/{CONTEXT-MAPPING-TABLE}/context-mappings/context-mapping[context-mapping-name]/instance-name
- (L1133)	/{CONTEXT-MAPPING-TABLE}/context-mappings/context-mapping[context-mapping-name]/vrf-name
- (L1140)	/{CONTEXT-MAPPING-TABLE}/context-mappings/context-mapping[context-mapping-name]/topology-name
- (L1172)	/snmp/encrypted-community-maps/encrypted-community-map[community-name]/context
- (L1179)	/snmp/encrypted-community-maps/encrypted-community-map[community-name]/security
- (L1290)	/snmp/administration/default-communities/default-community[community-name]/view-name
- (L1347)	/snmp/administration/type6-encrypted-communities/type6-encrypted-community[community-name]/view-name
- (L1404)	/snmp/administration/encrypted-communities/encrypted-community[community-name]/view-name
- (L1529)	/snmp/type6-encrypted-community-maps/type6-encrypted-community-map[community-name]/context
- (L1536)	/snmp/type6-encrypted-community-maps/type6-encrypted-community-map[community-name]/security
- (L1692)	/snmp/target/targets/target[target-list-name]/vrf-names/vrf-name[name]/name
- (L2105)	/snmp/default-community-maps/default-community-map[community-name]/context
- (L2112)	/snmp/default-community-maps/default-community-map[community-name]/security
- (L2369)	/snmp/groups/group[name]/notify-view
- (L2376)	/snmp/groups/group[name]/read-view
- (L2383)	/snmp/groups/group[name]/write-view
- (L2410)	/snmp/groups/group[name]/context-name

## XPaths Removed

N/A

## XPaths Modified

N/A

