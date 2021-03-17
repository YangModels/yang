## Cisco-IOS-XR-ipv4-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Naming convention changed for ORR table. Capability suppress table container, which included three supress configs is replaced with individual config leaves - all, 4-bytee-as and ENHE. Message log table container under neighbor, which included two logging configs is replaced with individual config leaves - log-in and log-out. EPE peer-node-sid is removed out of nbr-grp and session-grp as they are AFI agnostic. Restriction added for SNMP BGP trap config that lets to configure either updown or enable.

## XPaths Obsoleted

- (L4839)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/label-mode-enable

## XPaths Deprecated

N/A

## XPaths Added

- (L4341)	/snmp/notification/bgp/bgp4mib/enable
- (L4348)	/snmp/notification/bgp/bgp4mib/up-down
- (L4365)	/snmp/notification/bgp/cisco-bgp4mib/enable
- (L4371)	/snmp/notification/bgp/cisco-bgp4mib/up-down

## XPaths Removed

- (L4704)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]
- (L4851)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L4883)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L4886)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L5021)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L5054)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L5057)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L5191)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5223)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5226)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5358)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L5389)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L5392)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L6276)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]
- (L249)	/{Bgp-msg-log-dir}
- (L594)	/{Bgp-cap-sup}
- (L1755)	/{OPTIMAL-ROUTE-REFLECTOR-GROUP-TABLE}
- (L2502)	/{MSG-LOG-TABLE}
- (L2628)	/{EPE-PEER-NODE-SID}
- (L3751)	/{CAPABILITY-SUPPRESS-TABLE}

## XPaths Modified

N/A

