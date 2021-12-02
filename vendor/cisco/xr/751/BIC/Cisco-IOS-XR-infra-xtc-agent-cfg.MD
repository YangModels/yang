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

- (L1895)	/sr/traffic-engineering/pcc/pce-peers/pce-peer[pce-address]/authentication-option
- (L1919)	/sr/traffic-engineering/pcc/pce-peers/pce-peer[pce-address]/password
- (L1926)	/sr/traffic-engineering/pcc/pce-peers/pce-peer[pce-address]/keychain
- (L1933)	/sr/traffic-engineering/pcc/pce-peers/pce-peer[pce-address]/precedence
- (L1947)	/sr/traffic-engineering/pcc/pce-peer-with-afs

## XPaths Modified

- (L1904)	/sr/traffic-engineering/policies/policy[policy-name]/candidate-paths/preferences/preference[path-index]/path-infos/path-info[type][hop-type][segment-list-name]

