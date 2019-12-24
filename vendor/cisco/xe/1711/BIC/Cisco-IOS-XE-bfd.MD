## Cisco-IOS-XE-bfd.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

Min-tx leaf under interval container is mandatory. Hence not able to get the template config.

### Reason

Added presence true statement, in interval container to fix this bug. Also obsoleted leafs as part of hardening activity

- /native/bfd/ios-bfd:map/ios-bfd:ipv4
- /native/bfd/ios-bfd:map/ios-bfd:ipv6

## XPaths Deprecated

### Description

Min-tx leaf under interval container is mandatory. Hence not able to get the template config

### Reason

Added presence true statement, in interval container to fix this bug. Also obsoleted leafs as part of hardening activity

- /native/bfd-template/ios-bfd:single-hop/ios-bfd:interval
- /native/bfd-template/ios-bfd:multi-hop/ios-bfd:interval
- /native/interface/GigabitEthernet/bfd/ios-bfd:interval

## XPaths Modified

N/A

## XPaths Added

### Description

New nodes added for the obsoleted and deprecated nodes.

- /native/bfd/ios-bfd:map/ios-bfd:ipv4-list-with-both-vrf
- /native/bfd/ios-bfd:map/ios-bfd:ipv4-list-without-vrf
- /native/bfd/ios-bfd:map/ios-bfd:ipv4-list-with-src-vrf
- /native/bfd/ios-bfd:map/ios-bfd:ipv4-list-with-dst-vrf
- /native/bfd/ios-bfd:map/ios-bfd:ipv6-list-with-both-vrf
- /native/bfd/ios-bfd:map/ios-bfd:ipv6-list-without-vrf
- /native/bfd/ios-bfd:map/ios-bfd:ipv6-list-with-src-vrf
- /native/bfd/ios-bfd:map/ios-bfd:ipv6-list-with-dst-vrf
- /native/bfd-template/ios-bfd:single-hop/ios-bfd:interval-singlehop
- /native/bfd-template/ios-bfd:multi-hop/ios-bfd:interval-multihop
- /native/bfd-template/ios-bfd:multi-hop/ios-bfd:interval-multihop
- /native/interface/GigabitEthernet/bfd/ios-bfd:interval-interface
