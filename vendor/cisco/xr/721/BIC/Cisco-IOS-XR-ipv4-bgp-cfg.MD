## Cisco-IOS-XR-ipv4-bgp-cfg.yang

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

N/A

## XPaths Added

N/A

## XPaths Removed

- (L4750)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L4751)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L4756)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L4771)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/{VRF-NEIGHBOR-CONTENT}
- (L4920)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L4921)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L4926)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L4941)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/{NEIGHBOR-CONTENT}
- (L5088)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5089)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5094)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5109)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbor-groups/neighbor-group[neighbor-group-name]
- (L5253)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L5254)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L5259)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L5274)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/session-groups/session-group[session-group-name]
- (L819)	/{MSG-LOG-IN}
- (L3142)	/{MSG-LOG-OUT}
- (L3440)	/{SUPPRESS-ALL-CAPABILITIES}
- (L3469)	/{SUPPRESS-FOUR-BYTE-AS-CAPABILITY}

## XPaths Modified

- (L4911)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/vrf-neighbor-prefix-length[neighbor-address][prefix-length]
- (L5082)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/neighbor-prefix-length[neighbor-address][prefix-length]

