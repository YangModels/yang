## Cisco-IOS-XR-ipv4-bgp-cfg.yang

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

- (L703)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-percentage
- (L710)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-only
- (L720)	/{MAXIMUM-PREFIXES}/maximum-prefixes/restart-time
- (L726)	/{MAXIMUM-PREFIXES}/maximum-prefixes/discard-extra-paths
- (L2398)	/{EBGP-MULTIHOP}/ebgp-multihop/max-hop-count
- (L2404)	/{EBGP-MULTIHOP}/ebgp-multihop/mpls-deactivation
- (L4464)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/unequal-cost
- (L4470)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/selective
- (L4477)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ebgp/order-by-igp-metric
- (L4497)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/unequal-cost
- (L4503)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/selective
- (L4510)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/eibgp/order-by-igp-metric
- (L4530)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/unequal-cost
- (L4537)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/selective
- (L4544)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/vrfs/vrf[vrf-name]/vrf-global/vrf-global-afs/vrf-global-af[af-name]/ibgp/order-by-igp-metric
- (L5840)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/unequal-cost
- (L5846)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/selective
- (L5853)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ebgp/order-by-igp-metric
- (L5872)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/unequal-cost
- (L5878)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/selective
- (L5885)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/eibgp/order-by-igp-metric
- (L5920)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/unequal-cost
- (L5927)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/selective
- (L5934)	/bgp/instance[instance-name]/instance-as[as]/four-byte-as[as]/default-vrf/global/global-afs/global-af[af-name]/ibgp/order-by-igp-metric

## XPaths Removed

- (L698)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-percentage
- (L705)	/{MAXIMUM-PREFIXES}/maximum-prefixes/warning-only
- (L715)	/{MAXIMUM-PREFIXES}/maximum-prefixes/restart-time
- (L721)	/{MAXIMUM-PREFIXES}/maximum-prefixes/discard-extra-paths
- (L1451)	/{APP-ROUTE-TABLE}/application-routes/application-route[instance-name]/multipath
- (L2181)	/{MOBILE-ROUTES}/mobile-routes/multipath
- (L2381)	/{EBGP-MULTIHOP}/ebgp-multihop/max-hop-count
- (L2387)	/{EBGP-MULTIHOP}/ebgp-multihop/mpls-deactivation
- (L2601)	/{LISP-ROUTES}/lisp-routes/multipath
- (L2719)	/{SUBSCRIBER-ROUTES}/subscriber-routes/multipath
- (L2955)	/{EIGRP-ROUTE-TABLE}/eigrp-routes/eigrp-route[instance-name]/multipath
- (L3054)	/{STATIC-ROUTES}/static-routes/multipath
- (L3610)	/{CONNECTED-ROUTES}/connected-routes/multipath
- (L3762)	/{RIP-ROUTES}/rip-routes/multipath
- (L3911)	/{OSPF-ROUTE-TABLE}/ospf-routes/ospf-route[instance-name]/multipath
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

