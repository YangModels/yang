# Cisco-IOS-XE-bfd.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Modeled map command to accept multiple entries. Hence we have removed the container and modeled it as a list. From the inputs from yang experts, "both" leafs should not be modeled as this might cause sync issue.
Also the multiplier leaf under template grouping does not have a default statement. But native CLI behavior suggests that it needs to have a default value.

### Reason
Map command is modeled as a list. Hence it can accept multiple instance of the entry.
Also "both" leafs has been removed from the tree. Mandatory and default statements are added to necessary leafs and nodes.

- /native/bfd/ios-bfd:map/ios-bfd:ipv4
- /native/bfd/ios-bfd:map/ios-bfd:ipv6

## XPaths Deprecated

- /native/bfd-template/ios-bfd:multi-hop/ios-bfd:interval (all nodes under interval)
- /native/bfd-template/ios-bfd:single-hop/ios-bfd:interval (all nodes under interval)
- /native/interface/*/bfd/ios-bfd:interval

## XPaths Added
Below are the XPaths added for the above depreacted and obsoleted nodes. 

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
- /native/interface/*/bfd/ios-bfd:interval-interface

## XPaths Modified

### Description
Min-tx leaf under interval container is mandatory. Hence not able to get the template config

### Reason
Added presence true statement, in interval container to fix this bug.

- /native/bfd-template/ios-bfd:single-hop/ios-bfd:interval-singlehop
- /native/bfd-template/ios-bfd:multi-hop/ios-bfd:interval-multihop
- /native/bfd-template/ios-bfd:multi-hop/ios-bfd:interval-multihop
