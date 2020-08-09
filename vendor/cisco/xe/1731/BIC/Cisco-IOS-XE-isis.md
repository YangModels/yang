## Cisco-IOS-XE-isis


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/interface/Loopback/isis/adjacency-filter/\*
- native/interface/Loopback/isis/authentication-lan/\*
- native/interface/Loopback/isis/bfd/\*
- native/interface/Loopback/isis/csnp-interval/\*
- native/interface/Loopback/isis/fast-reroute
- native/interface/Loopback/isis/fast-reroute/\*
- native/interface/Loopback/isis/hello
- native/interface/Loopback/isis/hello/*
- native/interface/Loopback/isis/ipv6/bfd
- native/interface/Loopback/isis/ipv6/bfd/*
- native/interface/Loopback/isis/lsp-interval
- native/interface/Loopback/isis/mesh-group
- native/interface/Loopback/isis/password-lan
- native/interface/Loopback/isis/password-lan/\*
- native/interface/Loopback/isis/priority
- native/interface/Loopback/isis/priority/\*
- native/interface/Loopback/isis/retransmit-interval
- native/interface/Loopback/isis/retransmit-interval/\*

### Reason

Certain commands on Loopback interfaces are not supported and were hidden/obsolete.

## XPaths Deprecated

### Description

## XPaths Modified

- native/interface/\*/isis/fast-reroute/exclude/fast-reroute-exclude-list/interface
- native/router/isis/address-family/ipv6/distribute-list/prefix-list/interface
- native/router/isis/address-family/ipv6/router-id
- native/router/isis/distribute-list/distribute-list/interface
- native/router/isis/mpls/traffic-eng/router-id
- native/router/isis/passive-interface/interface
- native/router/isis/passive-interface/interface
- native/router/isis/passive-interface/interface
- native/router/isis/router-id
- native/router/isis-container/isis/address-family/ipv6/distribute-list/prefix-list/interface
- native/router/isis-container/isis/address-family/ipv6/router-id
- native/router/isis-container/isis/distribute-list/distribute-list/interface
- native/router/isis-container/isis/mpls/traffic-eng/router-id
- native/router/isis-container/isis/passive-interface/interface
- native/router/isis-container/isis/passive-interface/interface
- native/router/isis-container/isis/passive-interface/interface
- native/router/isis-container/isis/router-id

### Description

New must constraint added.

### Reason

Changes made to adhere to the pyang YANG validation.

## XPaths Added

### Description

