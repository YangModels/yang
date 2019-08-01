## Cisco-IOS-XE-ospf.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)


## Description
- Moved the old model and xpaths to sub module Cisco-IOS-XE-ospf-obsolete.yang.Added new xpaths to Cisco-IOS-XE-ospf.yang
- Removed dependency of ospfv2 code from ospfv3 yang file and obsoleted/deprecated v2 dependencies

## XPaths Obsoleted


- /native/interface/\*/ip/ios-ospf:ospf
- /native/interface/\*/ip/ios-ospf:ospf/*
- /native/interface/\*/ip6/ios-ospf:ospf
- /native/interface/\*/ip6/ios-ospf:ospf/*
- /native/router/ios-ospf:ospf/ios-ospf:address-family
- /native/router/ios-ospf:ospf/ios-ospf:address-family/\*
- /native/router/ios-ospf:ospf/ios-ospf:event-log
- /native/router/ios-ospf:ospf/ios-ospf:event-log/\*
- /native/router/ios-ospf:ospf/ios-ospf:bfd
- /native/router/ios-ospf:ospf/ios-ospf:bfd/\*
- /native/router/ios-ospf:ospf/ios-ospf:interface-id
- /native/router/ios-ospf:ospf/ios-ospf:interface-id/\*
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:capability
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:default-cost
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:filter-list
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:filter-list/ios-ospf:in-out
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:filter-list/ios-ospf:prefix
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:ipv4-range/\*
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:ipv6-range/\*
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:nssa/\*
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:sham-link/\*
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:stub/\*
- /native/router/ios-ospf:ospf/ios-ospf:area/ios-ospf:virtual-link/\*
- /native/router/ios-ospf:ospf/ios-ospf:capability/\*
- /native/router/ios-ospf:ospf/ios-ospf:compatible/ios-ospf:rfc1587
- /native/router/ios-ospf:ospf/ios-ospf:compatible/ios-ospf:rfc5243
- /native/router/ios-ospf:ospf/ios-ospf:default-metric
- /native/router/ios-ospf:ospf/ios-ospf:discard-route/\*
- /native/router/ios-ospf:ospf/ios-ospf:distribute-list/\*
- /native/router/ios-ospf:ospf/ios-ospf:domain-id/\*
- /native/router/ios-ospf:ospf/ios-ospf:domain-tag
- /native/router/ios-ospf:ospf/ios-ospf:event-log/\*
- /native/router/ios-ospf:ospf/ios-ospf:fast-reroute/\*
- /native/router/ios-ospf:ospf/ios-ospf:graceful-restart/\*
- /native/router/ios-ospf:ospf/ios-ospf:ignore/\*
- /native/router/ios-ospf:ospf/ios-ospf:interface-id/\*
- /native/router/ios-ospf:ospf/ios-ospf:interface-id/ios-ospf:snmp-if-index
- /native/router/ios-ospf:ospf/ios-ospf:ispf
- /native/router/ios-ospf:ospf/ios-ospf:limit
- /native/router/ios-ospf:ospf/ios-ospf:limit/ios-ospf:retransmissions/\*
- /native/router/ios-ospf:ospf/ios-ospf:local-rib-criteria/\*
- /native/router/ios-ospf:ospf/ios-ospf:log-adjacency-changes/\*
- /native/router/ios-ospf:ospf/ios-ospf:max-lsa/\*
- /native/router/ios-ospf:ospf/ios-ospf:maximum-paths/\*
- /native/router/ios-ospf:ospf/ios-ospf:microloop/\*
- /native/router/ios-ospf:ospf/ios-ospf:mpls/\*
- /native/router/ios-ospf:ospf/ios-ospf:neighbor/\*
- /native/router/ios-ospf:ospf/ios-ospf:network/\*
- /native/router/ios-ospf:ospf/ios-ospf:nsf/\*
- /native/router/ios-ospf:ospf/ios-ospf:nsf/ios-ospf:cisco/\*
- /native/router/ios-ospf:ospf/ios-ospf:nsr/\*
- /native/router/ios-ospf:ospf/ios-ospf:prefix-priority/\*
- /native/router/ios-ospf:ospf/ios-ospf:priority
- /native/router/ios-ospf:ospf/ios-ospf:process-min-time/\*
- /native/router/ios-ospf:ospf/ios-ospf:queue-depth/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:application/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:as-number
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:redist-options/ios-ospf:metric
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:redist-options/ios-ospf:metric-type
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:redist-options/ios-ospf:nssa-only
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:redist-options/ios-ospf:subnets
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:isis
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:redist-options/ios-ospf:tag/*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:iso-igrp/8
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:lisp/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:maximum-prefix/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:mobile/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:ospf/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:rip/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:vrf/\*
- /native/router/ios-ospf:ospf/ios-ospf:shutdown
- /native/router/ios-ospf:ospf/ios-ospf:snmp/\*
- /native/router/ios-ospf:ospf/ios-ospf:summary-address/\*
- /native/router/ios-ospf:ospf/ios-ospf:timers/ios-ospf:lsa/\*
- /native/router/ios-ospf:ospf/ios-ospf:timers/ios-ospf:pacing/\*
- /native/router/ios-ospf:ospf/ios-ospf:timers/ios-ospf:throttle/ios-ospf:lsa/\*
- /native/router/ios-ospf:ospf/ios-ospf:traffic-share/\*
- /native/router/ios-ospf:ospf/ios-ospf:ttl-security
- /native/router/ios-ospf:ospf/ios-ospf:ttl-security/\*

## XPaths Deprecated


- /native/router/ios-ospf:ospf
- /native/router/ios-ospf:ospf/ios-ospf:id
- /native/router/ios-ospf:ospf/ios-ospf:vrf
- /native/router/ios-ospf:ospf/ios-ospf:area
- /native/router/ios-ospf:ospf/ios-ospf:area/\*
- /native/router/ios-ospf:ospf/ios-ospf:auto-cost/\*
- /native/router/ios-ospf:ospf/ios-ospf:compatible
- /native/router/ios-ospf:ospf/ios-ospf:default-information/\*
- /native/router/ios-ospf:ospf/ios-ospf:distance/\*
- /native/router/ios-ospf:ospf/ios-ospf:max-metric/\*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:redist-options
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/\*/ios-ospf:redist-options/ios-ospf:route-map
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:bgp
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:eigrp
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:connected
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:omp
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:nat-route
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:static
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:nat-route/ios-ospf:dia
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/ios-ospf:nat-route/ios-ospf:outside


## XPaths Modified

N/A

## XPaths Added

- /native/interface/\*/ip/ios-ospf:router-ospf
- /native/interface/\*/ip/ios-ospf:router-ospf/*
- /native/router/ios-ospf:router-ospf
- /native/router/ios-ospf:router-ospf/\*

