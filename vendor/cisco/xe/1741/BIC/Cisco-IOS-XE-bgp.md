## Cisco-IOS-XE-bgp.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-flowspec/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-flowspec/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-mdt/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-mdt/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-mvpn/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-mvpn/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-sr-policy/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-sr-policy/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-flowspec/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-flowspec/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-mvpn/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-mvpn/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/l2vpn/l2vpn-evpn/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/l2vpn/l2vpn-evpn/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/link-state/link-state/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/link-state/link-state/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/address-family/no-vrf/vpnv6/vpnv6-flowspec/peer-group/neighbor/inherit
- /native/router/bgp/address-family/no-vrf/vpnv6/vpnv6-flowspec/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/scope/global/address-family/no-vrf/l2vpn/l2vpn-evpn/peer-group/neighbor/inherit
- /native/router/bgp/scope/global/address-family/no-vrf/l2vpn/l2vpn-evpn/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/scope/global/address-family/no-vrf/link-state/link-state/peer-group/neighbor/inherit
- /native/router/bgp/scope/global/address-family/no-vrf/link-state/link-state/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/scope/vrf/address-family/no-vrf/l2vpn/l2vpn-evpn/peer-group/neighbor/inherit
- /native/router/bgp/scope/vrf/address-family/no-vrf/l2vpn/l2vpn-evpn/peer-group/neighbor/inherit/peer-policy
- /native/router/bgp/scope/vrf/address-family/no-vrf/link-state/link-state/peer-group/neighbor/inherit
- /native/router/bgp/scope/vrf/address-family/no-vrf/link-state/link-state/peer-group/neighbor/inherit/peer-policy

### Reason

Peer-policy cannot be inherited within a peer-group. It is an invalid config

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/template/peer-policy/advertise-map/name

### Description

Must expression changed

### Description

The mandatory 'true' is added.

- /native/router/bgp/template/peer-policy/inherit/peer-policy/template/range

### Reason

In Cli, when inheriting a template, seq number is mandatory. Seq number in config model corresponds to range field under inherit->peer-policy->template. This field should be made mandatoy as without it rpc edit returns an error.

### Description

The base type has changed from leafref to string

peer-group-inherit-grouping(grouping)/inherit/peer-policy

### Description

A When expression added

- /native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-flowspec/peer-group/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-unicast/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/address-family/no-vrf/vpnv4/vpnv4-unicast/peer-group/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/address-family/no-vrf/vpnv6/vpnv6-flowspec/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/address-family/no-vrf/vpnv6/vpnv6-flowspec/peer-group/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/address-family/no-vrf/vpnv6/vpnv6-unicast/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/address-family/no-vrf/vpnv6/vpnv6-unicast/peer-group/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/global/address-family/no-vrf/vpnv4/vpnv4-unicast/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/global/address-family/no-vrf/vpnv4/vpnv4-unicast/peer-group/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/global/address-family/no-vrf/vpnv6/vpnv6-unicast/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/global/address-family/no-vrf/vpnv6/vpnv6-unicast/peer-group/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/vrf/address-family/no-vrf/vpnv4/vpnv4-unicast/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/vrf/address-family/no-vrf/vpnv4/vpnv4-unicast/peer-group/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/vrf/address-family/no-vrf/vpnv6/vpnv6-unicast/neighbor/long-lived-graceful-restart/stale-time/send
- /native/router/bgp/scope/vrf/address-family/no-vrf/vpnv6/vpnv6-unicast/peer-group/neighbor/long-lived-graceful-restart/stale-time/send

### Description

A new must expression added.

- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-multicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv4/vrf/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/address-family/with-vrf/ipv6/vrf/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/global/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv4/ipv4-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv4/ipv4-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv6/ipv6-unicast/neighbor/advertise-map/name
- /native/router/bgp/scope/vrf/address-family/no-vrf/ipv6/ipv6-unicast/peer-group/neighbor/advertise-map/name
- /native/router/bgp/template/peer-policy/advertise-map/name

## XPaths Added

### Description
