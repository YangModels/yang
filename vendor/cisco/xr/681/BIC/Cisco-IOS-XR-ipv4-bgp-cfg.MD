## Cisco-IOS-XR-ipv4-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed the hidden CLIs.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L4417)	/snmp/notification/bgp/bgp4mib/enable
- (L4424)	/snmp/notification/bgp/bgp4mib/up-down
- (L4441)	/snmp/notification/bgp/cisco-bgp4mib/enable
- (L4447)	/snmp/notification/bgp/cisco-bgp4mib/up-down

## XPaths Removed

- (L2001)	/{BEST-EXTERNAL}/best-external
- (L4581)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]
- (L6120)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]
- (L1720)	/{OPTIMAL-ROUTE-REFLECTOR-GROUP-TABLE}

## XPaths Modified

- (L2219)	/{BEST-EXTERNAL}/best-external
- (L5138)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-neighbors/vrf-neighbor-prefix-length[neighbor-address][prefix-length]
- (L5320)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/bgp-entity/neighbors/neighbor-prefix-length[neighbor-address][prefix-length]

