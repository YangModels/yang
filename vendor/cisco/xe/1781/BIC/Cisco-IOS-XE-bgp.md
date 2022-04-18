## Cisco-IOS-XE-bgp.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/router/bgp/address-family/\*/\*/\*/neighbor/advertisement-interval-ebgp
- native/router/bgp/address-family/\*/\*/\*/peer-group/neighbor/advertisement-interval-ebgp
- native/router/bgp/address-family/no-vrf/ipv4/\*/peer-group/neighbor/additional-paths/receive
- native/router/bgp/address-family/no-vrf/ipv4/\*/peer-group/neighbor/additional-paths/send
- native/router/bgp/address-family/no-vrf/ipv4/\*/peer-group/neighbor/additional-paths/send/receive
- native/router/bgp/address-family/no-vrf/ipv4/\*/peer-group/neighbor/additional-paths/disable
- native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/neighbor/long-lived-graceful-restart/stale-time
- native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/peer-group/neighbor/long-lived-graceful-restart/stale-time
- native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/neighbor/long-lived-graceful-restart/stale-time/\*
- native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/peer-group/neighbor/long-lived-graceful-restart/stale-time/\*
- native/router/bgp/address-family/\*/\*/\*/\*/neighbor/update-source/interface-choice/\*

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-flowspec/neighbor/peer-group/peer-group-name
- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/neighbor/peer-group/peer-group-name
- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/neighbor/peer-group/peer-group-name
- native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-flowspec/neighbor/peer-group/peer-group-name
- native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-multicast/neighbor/peer-group/peer-group-name
- native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/neighbor/peer-group/peer-group-name
- native/router/bgp/neighbor/peer-group/peer-group-name

### Description

A new must expression added.

- native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/maximum-secondary-paths
- native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/maximum-secondary-paths
- native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/maximum-secondary-paths
- native/router/bgp/scope/vrf/address-family/no-vrf/ipv4/ipv4-unicast/maximum-secondary-paths

### Description

The must expression is more constrained than before.

## XPaths Added

### Description
