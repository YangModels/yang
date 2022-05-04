## Cisco-IOS-XR-infra-policymgr-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

ecn leaf node which is member of random-detect list is removed as it is duplicate node.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L860)	/{MATCH}/fr-de
- (L1101)	/{MATCH}/source-mac
- (L1109)	/{MATCH}/destination-mac
- (L1869)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/random-detect[threshold-min-value][threshold-min-units][threshold-max-value][threshold-max-units]/ecn

## XPaths Modified

- (L1164)	/{MATCH}/source-mac
- (L1169)	/{MATCH}/destination-mac
- (L1767)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/queue-limit[value][unit]
- (L2069)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/police/rate

