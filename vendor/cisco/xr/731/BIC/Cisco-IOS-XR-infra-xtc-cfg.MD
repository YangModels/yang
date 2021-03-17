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

- (L1032)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/policies/policy[policy-name]/profile-id

## XPaths Removed

- (L841)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]/constraints

## XPaths Modified

- (L1031)	/pce/segment-routing/traffic-engineering/peers/peer[peer-addr]/policies/policy[policy-name]/profile-id
- (L1279)	/pce/segment-routing/traffic-engineering/p2mp/p2mp-timers/p2mp-timers-cleanup
- (L1440)	/pce/timers/initial-verify-startup

