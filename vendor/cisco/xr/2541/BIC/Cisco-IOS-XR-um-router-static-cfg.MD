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

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L404)	/router/static/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L532)	/router/static/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L986)	/router/static/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L1114)	/router/static/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L1589)	/router/static/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L1717)	/router/static/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L2171)	/router/static/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L2299)	/router/static/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L2696)	/router/static/address-family/ipv4/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L2824)	/router/static/address-family/ipv4/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L3278)	/router/static/address-family/ipv4/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L3406)	/router/static/address-family/ipv4/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L3947)	/router/static/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L4085)	/router/static/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L4589)	/router/static/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L4727)	/router/static/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L5242)	/router/static/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L5380)	/router/static/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L5884)	/router/static/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L6022)	/router/static/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L6449)	/router/static/address-family/ipv6/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L6587)	/router/static/address-family/ipv6/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L7091)	/router/static/address-family/ipv6/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L7229)	/router/static/address-family/ipv6/multicast/topologies/topology[topology-name]/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L7871)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L7999)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L8453)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L8581)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L9037)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L9165)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L9614)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L9742)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv4/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L10381)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L10514)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L11018)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L11156)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/unicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address
- (L11652)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L11790)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/nexthop-addresses/nexthop-address[address]/address
- (L12289)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-interface-addresses/nexthop-interface-address[interface-name][address]/address
- (L12427)	/router/static/vrfs/vrf[vrf-name]/address-family/ipv6/multicast/prefixes/prefix[prefix-address][prefix-length]/vrfs/vrf[vrf-name]/nexthop-addresses/nexthop-address[address]/address

