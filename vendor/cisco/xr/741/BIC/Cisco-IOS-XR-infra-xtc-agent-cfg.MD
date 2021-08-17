## Cisco-IOS-XR-infra-xtc-agent-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

This change is mandatory as part of requirement to refactor XTCAgentPolicySteeringApplicationType according to applicable scope (Global and per-policy).

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L414)	/{Xtc-adj-sid-protection}
- (L1715)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]/hop-type
- (L336)	/{Xtc-path-hop}

## XPaths Modified

- (L1748)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][segment-list-name]

