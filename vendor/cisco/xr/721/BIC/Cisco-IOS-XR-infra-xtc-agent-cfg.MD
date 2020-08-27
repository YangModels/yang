## Cisco-IOS-XR-infra-xtc-agent-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

This change is mandatory as part of the development of the feature XTC lateral API for sibling PCEs.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L444)	/{PERFORMANCE-MEASUREMENT}/performance-measurement/delay-measurement
- (L647)	/{BFD}/bfd/reverse-path/enable
- (L670)	/{BFD}/bfd/bfd-logging/enable
- (L776)	/sr/traffic-engineering/on-demand-colors/on-demand-color[color]/on-demand-color-dyn-mpls/on-demand-color-dyn-mpls-anycast/enable
- (L790)	/sr/traffic-engineering/on-demand-colors/on-demand-color[color]/on-demand-color-dyn-mpls/on-demand-color-dyn-mpls-metric/enable
- (L800)	/sr/traffic-engineering/on-demand-colors/on-demand-color[color]/on-demand-color-dyn-mpls/on-demand-color-dyn-mpls-pce/enable
- (L839)	/sr/traffic-engineering/on-demand-colors/on-demand-color[color]/on-demand-color-dyn-mpls/enable
- (L845)	/sr/traffic-engineering/on-demand-colors/on-demand-color[color]/on-demand-color-dyn-mpls
- (L862)	/sr/traffic-engineering/on-demand-colors/on-demand-color[color]
- (L867)	/sr/traffic-engineering/on-demand-colors/on-demand-color[color]
- (L926)	/sr/traffic-engineering/segments/segment[path-name]
- (L1013)	/sr/traffic-engineering/bfd-global/bfd-timers/enable
- (L1027)	/sr/traffic-engineering/bfd-global/enable
- (L1189)	/sr/traffic-engineering/policies/policy[policy-name]/auto-route/forward-class
- (L1202)	/sr/traffic-engineering/policies/policy[policy-name]/auto-route
- (L1259)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/constraints
- (L1285)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]/metric
- (L1291)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]/anycast
- (L1296)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]/pcep
- (L1322)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]
- (L1332)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]
- (L1335)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths
- (L1362)	/sr/traffic-engineering/policies/policy[policy-name]
- (L1366)	/sr/traffic-engineering/policies/policy[policy-name]
- (L1404)	/sr/traffic-engineering/srte-interfaces/srte-interface[srte-interface-name]
- (L1431)	/sr/traffic-engineering/pcc/pce-peers/pce-peer[pce-address]/enable
- (L1494)	/sr/traffic-engineering/pcc/enable
- (L1598)	/sr/traffic-engineering/candidate-path-types/candidate-path-type[candidate-path-type]/candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep
- (L1612)	/sr/traffic-engineering
- (L1614)	/sr/traffic-engineering
- (L449)	/{STEERING}
- (L513)	/{CUMULATIVE-METRIC-BOUNDS}
- (L589)	/{ENABLE}

## XPaths Modified

- (L987)	/sr/traffic-engineering/segments/segment[path-name]/segments/segment[segment-index]/address

