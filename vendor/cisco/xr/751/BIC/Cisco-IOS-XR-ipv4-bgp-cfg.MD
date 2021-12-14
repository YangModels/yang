## Cisco-IOS-XR-ipv4-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Changes involves segment routing alloc mode to be configured as a policy as well along with per-ce/per-vrf.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1373)	/{SEGMENT-ROUTING}/segment-routing/srv6/srv6sid-allocation-mode
- (L4503)	/vrfs/vrf[vrf-name]/afs/af[af-name][saf-name][topology-name]/bgp/export-vrf-options/import-stitching-rt
- (L4547)	/vrfs/vrf[vrf-name]/afs/af[af-name][saf-name][topology-name]/bgp/import-vrf-options
- (L4611)	/global-af/afs/af[af-name][saf-name][topology-name]/bgp/export-vrf-options/import-stitching-rt
- (L4655)	/global-af/afs/af[af-name][saf-name][topology-name]/bgp/import-vrf-options
- (L4807)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/unequal-cost
- (L4820)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/order-by-igp-metric
- (L4840)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/unequal-cost
- (L4853)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/order-by-igp-metric
- (L4887)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/order-by-igp-metric
- (L6260)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/unequal-cost
- (L6273)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/order-by-igp-metric
- (L6292)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/unequal-cost
- (L6305)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/order-by-igp-metric
- (L6354)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/order-by-igp-metric
- (L6162)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/export-vrf-allow

## XPaths Modified

- (L1397)	/{SEGMENT-ROUTING}/segment-routing/srv6/srv6sid-allocation-mode
- (L4607)	/vrfs/vrf[vrf-name]/afs/af[af-name][saf-name][topology-name]/bgp/import-vrf-options
- (L4737)	/global-af/afs/af[af-name][saf-name][topology-name]/bgp/import-vrf-options

