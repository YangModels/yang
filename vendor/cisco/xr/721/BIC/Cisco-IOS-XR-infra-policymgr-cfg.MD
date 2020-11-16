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

- (L709)	/{MATCH}/ethernet-services-acl
- (L756)	/{MATCH}/mpls-disposition-ipv4-access-list
- (L764)	/{MATCH}/mpls-disposition-ipv6-access-list
- (L860)	/{MATCH}/fr-de
- (L1869)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/random-detect[threshold-min-value][threshold-min-units][threshold-max-value][threshold-max-units]/ecn

## XPaths Modified

- (L724)	/{MATCH}/ethernet-services-acl
- (L770)	/{MATCH}/mpls-disposition-ipv4-access-list
- (L777)	/{MATCH}/mpls-disposition-ipv6-access-list
- (L872)	/{MATCH}/fr-de
- (L1714)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/queue-limit[value][unit]
- (L2004)	/{POLICY-MAP-RULE}/policy-map-rule[class-name][class-type]/police/rate

