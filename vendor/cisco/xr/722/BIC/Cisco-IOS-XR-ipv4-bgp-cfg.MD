## Cisco-IOS-XR-ipv4-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Converted some default nodes to mandatory.

## XPaths Obsoleted

- (L4712)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/label-mode-enable

## XPaths Deprecated

N/A

## XPaths Added

- (L4214)	/snmp/notification/bgp/bgp4mib/enable
- (L4221)	/snmp/notification/bgp/bgp4mib/up-down
- (L4238)	/snmp/notification/bgp/cisco-bgp4mib/enable
- (L4244)	/snmp/notification/bgp/cisco-bgp4mib/up-down

## XPaths Removed

- (L4886)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L5057)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L5226)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5392)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L2628)	/{EPE-PEER-NODE-SID}

## XPaths Modified

N/A

