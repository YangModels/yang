## Cisco-IOS-XR-ipv4-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L4017)	/vrfs/vrf[vrf-name]/bgp-global
- (L4084)	/snmp/notification/bgp
- (L4139)	/vrfs/vrf[vrf-name]/afs/af[af-name][saf-name][topology-name]/bgp
- (L4240)	/global-af/afs/af[af-name][saf-name][topology-name]/bgp
- (L4343)	/bgp
- (L6450)	/bmp-server-all
- (L6498)	/bmp-servers

## XPaths Added

- (L709)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-percentage
- (L716)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-only
- (L726)	/{MAXIMUM-PREFIXES}/maximum-prefixes/restart-time
- (L732)	/{MAXIMUM-PREFIXES}/maximum-prefixes/discard-extra-paths
- (L2401)	/{EBGP-MULTIHOP}/ebgp-multihop/max-hop-count
- (L2407)	/{EBGP-MULTIHOP}/ebgp-multihop/mpls-deactivation
- (L4475)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/unequal-cost
- (L4481)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/selective
- (L4488)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/order-by-igp-metric
- (L4508)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/unequal-cost
- (L4514)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/selective
- (L4521)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/order-by-igp-metric
- (L4541)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/unequal-cost
- (L4548)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/selective
- (L4555)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/order-by-igp-metric
- (L5842)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/unequal-cost
- (L5848)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/selective
- (L5855)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/order-by-igp-metric
- (L5874)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/unequal-cost
- (L5880)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/selective
- (L5887)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/order-by-igp-metric
- (L5922)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/unequal-cost
- (L5929)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/selective
- (L5936)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/order-by-igp-metric

## XPaths Removed

- (L2719)	/{SUBSCRIBER-ROUTES}/subscriber-routes/multipath
- (L3054)	/{STATIC-ROUTES}/static-routes/multipath
- (L3911)	/{OSPF-ROUTE-TABLE}/ospf-routes/ospf-route[instance-name]/multipath
- (L2601)	/{LISP-ROUTES}/lisp-routes/multipath
- (L698)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-percentage
- (L705)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-only
- (L715)	/{MAXIMUM-PREFIXES}/maximum-prefixes/restart-time
- (L721)	/{MAXIMUM-PREFIXES}/maximum-prefixes/discard-extra-paths
- (L2955)	/{EIGRP-ROUTE-TABLE}/eigrp-routes/eigrp-route[instance-name]/multipath
- (L2181)	/{MOBILE-ROUTES}/mobile-routes/multipath
- (L2381)	/{EBGP-MULTIHOP}/ebgp-multihop/max-hop-count
- (L2387)	/{EBGP-MULTIHOP}/ebgp-multihop/mpls-deactivation
- (L1451)	/{APP-ROUTE-TABLE}/application-routes/application-route[instance-name]/multipath
- (L3610)	/{CONNECTED-ROUTES}/connected-routes/multipath
- (L3762)	/{RIP-ROUTES}/rip-routes/multipath
- (L4442)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/unequal-cost
- (L4448)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/selective
- (L4455)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/order-by-igp-metric
- (L4475)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/unequal-cost
- (L4481)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/selective
- (L4488)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/order-by-igp-metric
- (L4508)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/unequal-cost
- (L4515)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/selective
- (L4522)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/order-by-igp-metric
- (L5624)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/isis-routes/isis-route[instance-name]/multipath
- (L5808)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/unequal-cost
- (L5814)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/selective
- (L5821)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/order-by-igp-metric
- (L5840)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/unequal-cost
- (L5846)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/selective
- (L5853)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/order-by-igp-metric
- (L5888)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/unequal-cost
- (L5895)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/selective
- (L5902)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/order-by-igp-metric

## XPaths Modified

N/A

