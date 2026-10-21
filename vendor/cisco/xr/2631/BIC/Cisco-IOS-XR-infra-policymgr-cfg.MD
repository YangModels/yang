## Cisco-IOS-XR-infra-policymgr-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added must constraint to prevent both event-mode-match-all and event-mode-match-first from being set simultaneously. ecn leaf node which is member of random-detect list is removed as it is duplicate node.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L2516)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/http-redirect

## XPaths Removed

N/A

## XPaths Modified

- (L1957)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/random-detect[threshold-min-value][threshold-min-units][threshold-max-value][threshold-max-units]/threshold-min-units
- (L1969)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/random-detect[threshold-min-value][threshold-min-units][threshold-max-value][threshold-max-units]/threshold-max-units

