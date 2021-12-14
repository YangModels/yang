## Cisco-IOS-XR-um-router-static-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added must statements under list node prefix and vrf (these are missing constraints in the existing nodes thus practically does not break backward-compatibility).

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L708)	/router/static/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L83)	/router/static/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]
- (L1843)	/router/static/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L1218)	/router/static/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]
- (L2900)	/router/static/address-family/ipv4/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L2346)	/router/static/address-family/ipv4/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]
- (L4022)	/router/static/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L3397)	/router/static/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]
- (L5157)	/router/static/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L4532)	/router/static/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]
- (L6214)	/router/static/address-family/ipv6/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L5660)	/router/static/address-family/ipv6/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]
- (L7357)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L6732)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]
- (L8473)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L7848)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]
- (L9593)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L8968)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]
- (L10709)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]
- (L10084)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]

## XPaths Removed

N/A

## XPaths Modified

N/A

