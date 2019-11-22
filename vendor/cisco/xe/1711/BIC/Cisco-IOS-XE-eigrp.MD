## Cisco-IOS-XE-eigrp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Mark all the sub nodes 'obsoleted' or 'deprecated' whose parent has been done the same.

### Reason
Obsoleted child nodes to make it RFC compliant.

- /native/ipv6/router/eigrp
- /native/ipv6/router/eigrp/id
- /native/ipv6/router/eigrp/ios-eigrp:distribute-list
- /native/ipv6/router/eigrp/ios-eigrp:distribute-list/ios-eigrp:prefix-list
- /native/ipv6/router/eigrp/ios-eigrp:distribute-list/ios-eigrp:prefix-list/ios-eigrp:name
- /native/ipv6/router/eigrp/ios-eigrp:distribute-list/ios-eigrp:prefix-list/ios-eigrp:in
- /native/ipv6/router/eigrp/ios-eigrp:distribute-list/ios-eigrp:prefix-list/ios-eigrp:out
- /native/interface/*/ip/hello-interval
- /native/interface/*/ip/hello-interval/eigrp
- /native/interface/*/ip/hello-interval/seconds
- /native/interface/*/ip/authentication
- /native/interface/*/ip/authentication/key-chain
- /native/interface/*/ip/authentication/key-chain/eigrp
- /native/interface/*/ip/authentication/key-chain/name
- /native/interface/*/ip/authentication/mode
- /native/interface/*/ip/authentication/mode/eigrp
- /native/interface/*/ip/authentication/mode/md5
- /native/interface/*/ip/hold-time
- /native/interface/*/ip/hold-time/eigrp
- /native/interface/*/ip/hold-time/seconds
- /native/interface/*/ip/summary-address/eigrp
- /native/interface/*/ip/summary-address/eigrp/id
- /native/interface/*/ip/summary-address/eigrp/ip
- /native/interface/*/ip/summary-address/eigrp/mask
- /native/interface/*/ip/summary-address/eigrp/metric
- /native/router/ios-eigrp:eigrp/ios-eigrp:address-family/ios-eigrp:af-ip-list/ios-eigrp:bfd/ios-eigrp:interface/*
- /native/router/ios-eigrp:eigrp/ios-eigrp:address-family/ios-eigrp:af-ip-vrf-list/ios-eigrp:bfd/ios-eigrp:interface/
- /native/router/ios-eigrp:eigrp/ios-eigrp:address-family/ios-eigrp:af-ip-list/ios-eigrp:neighbor/ios-eigrp:ipv4/ios-eigrp:interface/*
- /native/router/ios-eigrp:eigrp/ios-eigrp:address-family/ios-eigrp:af-ip-vrf-list/ios-eigrp:neighbor/ios-eigrp:ipv4/ios-eigrp:interface/*

### Description
Obsolete the old EIGRP YANG Model. The csv files show the xpaths touched with commit.

### Reason
There was a split in the top most node in the model.


- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:classic-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4-vrf/ios-eigrp:redistribute/ios-eigrp:nhrp
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:classic-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4-vrf/ios-eigrp:redistribute/ios-eigrp:nhrp/*
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:classic-mode/ios-eigrp:redistribute/ios-eigrp:nhrp
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:classic-mode/ios-eigrp:redistribute/ios-eigrp:nhrp/*
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:classic-mode/ios-eigrp:redistribute/ios-eigrp:nhrp/ios-eigrp:route-map
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4/ios-eigrp:af-interface/ios-eigrp:add-path
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4/ios-eigrp:eigrp/ios-eigrp:default-route-tag
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4/ios-eigrp:topology/ios-eigrp:topo-base/ios-eigrp:redistribute/ios-eigrp:maximum-prefix
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4/ios-eigrp:topology/ios-eigrp:topo-base/ios-eigrp:redistribute/ios-eigrp:maximum-prefix/*
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4-vrf/ios-eigrp:af-interface/ios-eigrp:add-path
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4-vrf/ios-eigrp:eigrp/ios-eigrp:default-route-tag
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4-vrf/ios-eigrp:topology/ios-eigrp:topo-base/ios-eigrp:redistribute/ios-eigrp:maximum-prefix
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv4/ios-eigrp:af-ipv4-vrf/ios-eigrp:topology/ios-eigrp:topo-base/ios-eigrp:redistribute/ios-eigrp:maximum-prefix/*
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv6/ios-eigrp:af-ipv6/ios-eigrp:af-interface/ios-eigrp:add-path
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv6/ios-eigrp:af-ipv6/ios-eigrp:eigrp/ios-eigrp:default-route-tag
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv6/ios-eigrp:af-ipv6-vrf/ios-eigrp:af-interface/ios-eigrp:add-path
- /native/router/ios-eigrp:router-eigrp/ios-eigrp:eigrp/ios-eigrp:named-mode/ios-eigrp:address-family/ios-eigrp:ipv6/ios-eigrp:af-ipv6-vrf/ios-eigrp:eigrp/ios-eigrp:default-route-tag

## XPaths Deprecated
N/A

## XPaths Modified
N/A

## XPaths Added
N/A

