## Cisco-IOS-XE-multicast.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsoleted few nodes that were functionally broken.

- /native/ip/ios-mc:msdp/ios-mc:keepalive
- /native/ip/ios-mc:msdp/ios-mc:keepalive/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:keepalive
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:keepalive/\*
- /native/ip/ios-mc:msdp/ios-mc:default-peer
- /native/ip/ios-mc:msdp/ios-mc:default-peer/\*
- /native/ip/ios-mc:msdp/ios-mc:description
- /native/ip/ios-mc:msdp/ios-mc:description/\*
- /native/ip/ios-mc:msdp/ios-mc:mesh-group
- /native/ip/ios-mc:msdp/ios-mc:mesh-group/\*
- /native/ip/ios-mc:msdp/ios-mc:password/ios-mc:peer
- /native/ip/ios-mc:msdp/ios-mc:password/ios-mc:peer/\*
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in/ios-mc:addr
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in/ios-mc:list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in/ios-mc:route-map
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in/ios-mc:rp-list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in/ios-mc:rp-route-map
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out/\*
- /native/ip/ios-mc:msdp/ios-mc:sa-limit
- /native/ip/ios-mc:msdp/ios-mc:shutdown
- /native/ip/ios-mc:msdp/ios-mc:shutdown/\*
- /native/ip/ios-mc:msdp/ios-mc:ttl-threshold
- /native/ip/ios-mc:msdp/ios-mc:ttl-threshold/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:border/ios-mc:sa-address/ios-mc:TwentyFiveGigabitEthernet
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:default-peer
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:default-peer/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:description
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:description/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:filter-sa-request
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:filter-sa-request/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:keepalive
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:keepalive/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:mesh-group
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:mesh-group/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:password/ios-mc:peer
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:password/ios-mc:peer/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:peer/ios-mc:connect-source/ios-mc:TwentyFiveGigabitEthernet
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:sa-filter/ios-mc:in
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:sa-filter/ios-mc:in/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:sa-filter/ios-mc:out
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:sa-filter/ios-mc:out/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:sa-limit
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:sa-limit/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:shutdown
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:shutdown/\*
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:ttl-threshold
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:ttl-threshold/\*

## XPaths Deprecated

### Description
Deprecated nodes to make the model backward compatible 

- /native/ip/multicast/ios-mc:route-limit 
- /native/ip/pim/ios-mc:autorp 
- /native/ip/pim/ios-mc:autorp/ios-mc:listener 
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:interface_list
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:interface_list/ios-mc:if-name
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:interface_list/ios-mc:scope
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:interface_list/ios-mc:scope/\*
- /native/interface/Tunnel/ip/pim/ios-mc:pim-mode
- /native/interface/Tunnel/ipv6
- /native/interface/Tunnel/ipv6/ios-mc:no-pim
- /native/interface/\*/ipv6/ios-mc:no-pim/ios-mc:pim
- /native/interface/\*/ipv6/ios-mc:pim
- /native/interface/\*/ipv6/ios-mc:pim/ios-mc:bfd
- /native/interface/\*/ipv6/ios-mc:pim/ios-mc:bsr
- /native/interface/\*/ipv6/ios-mc:pim/ios-mc:bsr/ios-mc:border
- /native/interface/\*/ipv6/ios-mc:pim/ios-mc:dr-priority
- /native/interface/LISP/ipv6/ios-mc:pim/ios-mc:lisp/ios-mc:transport
- /native/interface/LISP/ipv6/ios-mc:pim/ios-mc:lisp/ios-mc:transport/\*
- /native/interface/LISP/ipv6/ios-mc:pim/ios-mc:lisp/ios-mc:transport-container/ios-mc:unicast
- /native/interface/LISP/ipv6/ios-mc:pim/ios-mc:lisp/ios-mc:transport-container/ios-mc:unicast/ios-mc:ipv4
- /native/ipv6/ios-mc:multicast-routing
- /native/ipv6/ios-mc:multicast-routing/ios-mc:vrf
- /native/ip/ios-mc:msdp/ios-mc:redistribute
- /native/ip/ios-mc:msdp/ios-mc:redistribute/ios-mc:list
- /native/ip/ios-mc:msdp/ios-mc:redistribute/ios-mc:asn
- /native/ip/ios-mc:msdp/ios-mc:redistribute/ios-mc:route-map

## XPaths Modified

### Description
Modified value range

- /native/ip/ios-mc:msdp/ios-mc:peer/ios-mc:remote-as
- /native/ip/ios-mc:msdp/ios-mc:vrf/ios-mc:peer/ios-mc:remote-as
- /native/ip/pim/ios-mc:ssm/ios-mc:range

### Description
Modified type and default

- /native/ipv6/multicast/ios-mc:rpf/ios-mc:use-bgp

## XPaths Added

### Description
New nodes created for the depreacted and obsoleted xpaths

- /native/ip/multicast/ios-mc:rpf/ios-mc:select/ios-mc:vrf-list
- /native/ip/multicast/ios-mc:rpf/ios-mc:select/ios-mc:vrf-list/ios-mc:group-list
- /native/ip/multicast/ios-mc:rpf/ios-mc:select/ios-mc:vrf-list/ios-mc:name
- /native/ip/pim/ios-mc:spt-threshold-list
- /native/ip/pim/ios-mc:spt-threshold-list/ios-mc:group-list
- /native/ip/pim/ios-mc:spt-threshold-list/ios-mc:how
- /native/ip/ios-mc:msdp/ios-mc:default-peer-list
- /native/ip/ios-mc:msdp/ios-mc:default-peer-list/ios-mc:name-addr
- /native/ip/ios-mc:msdp/ios-mc:default-peer-list/ios-mc:prefix-list
- /native/ip/ios-mc:msdp/ios-mc:description-list
- /native/ip/ios-mc:msdp/ios-mc:description-list/ios-mc:name-addr
- /native/ip/ios-mc:msdp/ios-mc:description-list/ios-mc:description
- /native/ip/ios-mc:msdp/ios-mc:filter-sa-request-list
- /native/ip/ios-mc:msdp/ios-mc:filter-sa-request-list/ios-mc:name-addr
- /native/ip/ios-mc:msdp/ios-mc:filter-sa-request-list/ios-mc:list
- /native/ip/ios-mc:msdp/ios-mc:keepalive-list
- /native/ip/ios-mc:msdp/ios-mc:keepalive-list/ios-mc:name-addr
- /native/ip/ios-mc:msdp/ios-mc:keepalive-list/ios-mc:keepalive
- /native/ip/ios-mc:msdp/ios-mc:keepalive-list/ios-mc:max-wait
- /native/ip/ios-mc:msdp/ios-mc:mesh-group-list
- /native/ip/ios-mc:msdp/ios-mc:mesh-group-list/ios-mc:name
- /native/ip/ios-mc:msdp/ios-mc:mesh-group-list/ios-mc:addr
- /native/ip/ios-mc:msdp/ios-mc:password/ios-mc:peer-list
- /native/ip/ios-mc:msdp/ios-mc:password/ios-mc:peer-list/ios-mc:addr
- /native/ip/ios-mc:msdp/ios-mc:password/ios-mc:peer-list/ios-mc:encryption
- /native/ip/ios-mc:msdp/ios-mc:password/ios-mc:peer-list/ios-mc:password
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in-list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in-list/ios-mc:addr
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in-list/ios-mc:list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in-list/ios-mc:route-map
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in-list/ios-mc:rp-list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:in-list/ios-mc:rp-route-map
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out-list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out-list/ios-mc:addr
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out-list/ios-mc:list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out-list/ios-mc:route-map
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out-list/ios-mc:rp-list
- /native/ip/ios-mc:msdp/ios-mc:sa-filter/ios-mc:out-list/ios-mc:rp-route-map
- /native/ip/ios-mc:msdp/ios-mc:sa-limit-list
- /native/ip/ios-mc:msdp/ios-mc:sa-limit-list/ios-mc:name-addr
- /native/ip/ios-mc:msdp/ios-mc:sa-limit-list/ios-mc:limit
- /native/ip/ios-mc:msdp/ios-mc:shutdown-list
- /native/ip/ios-mc:msdp/ios-mc:shutdown-list/ios-mc:name-addr
- /native/ip/ios-mc:msdp/ios-mc:ttl-threshold-list
- /native/ip/ios-mc:msdp/ios-mc:ttl-threshold-list/ios-mc:name-addr
- /native/ip/multicast/ios-mc:route-limit-container/ios-mc:routelimit
- /native/ip/ios-mc:msdp/ios-mc:ttl-threshold-list/ios-mc:threshold
- /native/ip/pim/ios-mc:autorp-container/ios-mc:autorp
- /native/ip/pim/ios-mc:autorp-container/ios-mc:listener
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:send-rp-announce-list
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:send-rp-announce-list/ios-mc:if-name
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:send-rp-announce-list/ios-mc:scope
- /native/ip/pim/ios-mc:send-rp-announce/ios-mc:send-rp-announce-list/ios-mc:group-list
- /native/interface/Tunnel/ip/pim/ios-mc:passive
- /native/interface/Tunnel/ip/pim/ios-mc:dense-mode
- /native/interface/Tunnel/ip/pim/ios-mc:sparse-mode
- /native/interface/Tunnel/ip/pim/ios-mc:sparse-dense-mode
- /native/interface/Tunnel/ipv6/ios-mc:pim-conf/ios-mc:pim
- /native/interface/Tunnel/ipv6/ios-mc:pim-container/ios-mc:bfd
- /native/interface/Tunnel/ipv6/ios-mc:pim-container/ios-mc:bsr/ios-mc:border
- /native/interface/Tunnel/ipv6/ios-mc:pim-container/ios-mc:dr-priority
- /native/interface/LISP/ipv6/ios-mc:pim/ios-mc:lisp/ios-mc:transport-container/ios-mc:unicast
- /native/interface/LISP/ipv6/ios-mc:pim/ios-mc:lisp/ios-mc:transport-container/ios-mc:unicast/ios-mc:ipv4
- /native/ipv6/ios-mc:multicast-routing-container/ios-mc:vrf/ios-mc:name
- /native/ip/ios-mc:msdp/ios-mc:redistribute-container
- /native/ip/ios-mc:msdp/ios-mc:redistribute-container/ios-mc:list
- /native/ip/ios-mc:msdp/ios-mc:redistribute-container/ios-mc:asn
- /native/ip/ios-mc:msdp/ios-mc:redistribute-container/ios-mc:route-map
