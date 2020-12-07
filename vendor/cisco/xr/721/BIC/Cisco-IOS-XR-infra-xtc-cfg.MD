## Cisco-IOS-XR-infra-xtc-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Renamed and moved te-latency leaf to cspf container.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L438)	/pce/pcc-addresses/pcc-address[address]/lsp-names/lsp-name[name]/rsvp-te
- (L456)	/pce/pcc-addresses/pcc-address[address]/lsp-names/lsp-name[name]
- (L464)	/pce/pcc-addresses/pcc-address[address]
- (L716)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]/enable
- (L741)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/enable
- (L755)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/policies/policy[policy-name]/candidate-paths/enable
- (L762)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/policies/policy[policy-name]/enable
- (L777)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/enable
- (L887)	/pce/segment-routing/traffic-engineering/p2mp/p2mp-policies/p2mp-policy[policy-name]/p2mp-candidate-paths/p2mp-preferences/p2mp-preference[path-index]/p2mp-path-infos/p2mp-path-info[type][hop-type][segment-list-name]
- (L897)	/pce/segment-routing/traffic-engineering/p2mp/p2mp-policies/p2mp-policy[policy-name]/p2mp-candidate-paths/p2mp-preferences/p2mp-preference[path-index]
- (L913)	/pce/segment-routing/traffic-engineering/p2mp/p2mp-policies/p2mp-policy[policy-name]
- (L941)	/pce/segment-routing/traffic-engineering/p2mp/p2mp-endpoint-sets/p2mp-endpoint-set[endpoint-set-name]/p2mp-endpoint-set-addresses/p2mp-endpoint-set-address[af-type][endpoint-address]
- (L951)	/pce/segment-routing/traffic-engineering/p2mp/p2mp-endpoint-sets/p2mp-endpoint-set[endpoint-set-name]
- (L1033)	/pce/segment-routing/traffic-engineering/segments/segment[path-name]
- (L1036)	/pce/segment-routing/traffic-engineering/enable
- (L1042)	/pce/segment-routing/te-latency
- (L1133)	/pce/netconf
- (L1203)	/pce/disjoint-path/groups/group[group-id][dp-type][sub-id]
- (L1206)	/pce/disjoint-path
- (L548)	/pce/rest
- (L1232)	/pce
- (L265)	/{Pcerest-authentication}
- (L309)	/{ENABLE}

## XPaths Modified

- (L1143)	/pce/segment-routing/traffic-engineering/segments/segment[path-name]/segments/segment[segment-index]/address

