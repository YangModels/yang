## Cisco-IOS-XR-um-logging-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Length for TLS configuration name and peer name reduced to 253. Changed sch-type for the node ipv6-address under container host-ipv6-addresses.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L2167)	/logging/vrfs/vrf[vrf-name]/ipv4-hostnames/ipv4-hostname[ipv4-address]/ipv4-address
- (L2162)	/logging/vrfs/vrf[vrf-name]/ipv4-hostnames/ipv4-hostname[ipv4-address]
- (L2157)	/logging/vrfs/vrf[vrf-name]/ipv4-hostnames
- (L2185)	/logging/vrfs/vrf[vrf-name]/ipv6-hostnames/ipv6-hostname[ipv6-address]/ipv6-address
- (L2180)	/logging/vrfs/vrf[vrf-name]/ipv6-hostnames/ipv6-hostname[ipv6-address]
- (L2175)	/logging/vrfs/vrf[vrf-name]/ipv6-hostnames
- (L2209)	/logging/vrfs/vrf[vrf-name]/hostnames/hostname[host]/host
- (L2198)	/logging/vrfs/vrf[vrf-name]/hostnames/hostname[host]
- (L2193)	/logging/vrfs/vrf[vrf-name]/hostnames

## XPaths Added

N/A

## XPaths Removed

- (L2027)	/logging/archive/device

## XPaths Modified

- (L1340)	/logging/source-interfaces/source-interface[interface-name][vrf-name]/vrf-name
- (L2152)	/logging/vrfs/vrf[vrf-name]/vrf-name

