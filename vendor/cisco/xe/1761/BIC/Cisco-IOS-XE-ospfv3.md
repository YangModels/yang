## Cisco-IOS-XE-ospfv3.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/interface/\*/ipv6/ospf/encryption/\*
- native/interface/\*/ipv6/ospf/network/\*
- native/interface/\*/ospfv3/authentication/\*
- native/interface/\*/ospfv3/authentication-config/\*
- native/interface/\*/ospfv3/encryption/\*
- native/interface/\*/ospfv3/manet/peering/link-metrics
- native/interface/\*/ospfv3/network/\*
- native/interface/\*/ospfv3/process-id/ipv4/manet/peering/link-metrics
- native/interface/\*/ospfv3/process-id/ipv4/network/\*
- native/interface/\*/ospfv3/process-id/ipv6/manet/peering/link-metrics
- native/interface/\*/ospfv3/process-id/ipv6/network/\*
- native/interface/\*/ospfv3/process-id/manet/peering/link-metrics
- native/interface/\*/ospfv3/process-id/network/\*

### Reason

Obsolete the deprecated nodes introduced on or before 17.3

## XPaths Deprecated

### Description

## XPaths Modified

- native/router/ospfv3/address-family/ipv4/unicast/compatible/rfc1583
- native/router/ospfv3/address-family/ipv4/unicast/compatible/rfc1587
- native/router/ospfv3/address-family/ipv4/unicast/compatible/rfc5243
- native/router/ospfv3/address-family/ipv4/vrf/compatible/rfc1583
- native/router/ospfv3/address-family/ipv4/vrf/compatible/rfc1587
- native/router/ospfv3/address-family/ipv4/vrf/compatible/rfc5243
- native/router/ospfv3/address-family/ipv6/unicast/compatible/rfc1583
- native/router/ospfv3/address-family/ipv6/unicast/compatible/rfc1587
- native/router/ospfv3/address-family/ipv6/unicast/compatible/rfc5243
- native/router/ospfv3/address-family/ipv6/vrf/compatible/rfc1583
- native/router/ospfv3/address-family/ipv6/vrf/compatible/rfc1587
- native/router/ospfv3/address-family/ipv6/vrf/compatible/rfc5243
- ospfv3-common-address-family-grouping(grouping)/compatible/rfc1583
- ospfv3-common-address-family-grouping(grouping)/compatible/rfc1587
- ospfv3-common-address-family-grouping(grouping)/compatible/rfc5243
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv4/area
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv6/area
- native/interface/BD-VIF/ospfv3/process-id/ipv4/area
- native/interface/BD-VIF/ospfv3/process-id/ipv6/area
- native/interface/BDI/ospfv3/process-id/ipv4/area
- native/interface/BDI/ospfv3/process-id/ipv6/area
- native/interface/Dialer/ospfv3/process-id/ipv4/area
- native/interface/Dialer/ospfv3/process-id/ipv6/area
- native/interface/Ethernet/ospfv3/process-id/ipv4/area
- native/interface/Ethernet/ospfv3/process-id/ipv6/area
- native/interface/FastEthernet/ospfv3/process-id/ipv4/area
- native/interface/FastEthernet/ospfv3/process-id/ipv6/area
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv4/area
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv6/area
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv4/area
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv6/area
- native/interface/GigabitEthernet/ospfv3/process-id/ipv4/area
- native/interface/GigabitEthernet/ospfv3/process-id/ipv6/area
- native/interface/HundredGigE/ospfv3/process-id/ipv4/area
- native/interface/HundredGigE/ospfv3/process-id/ipv6/area
- native/interface/Loopback/ospfv3/process-id/ipv4/area
- native/interface/Loopback/ospfv3/process-id/ipv6/area
- native/interface/Port-channel/ospfv3/process-id/ipv4/area
- native/interface/Port-channel/ospfv3/process-id/ipv6/area
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv4/area
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv6/area
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv4/area
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv6/area
- native/interface/Tunnel/ospfv3/process-id/ipv4/area
- native/interface/Tunnel/ospfv3/process-id/ipv6/area
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv4/area
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv6/area
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv4/area
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv6/area
- native/interface/Vlan/ospfv3/process-id/ipv4/area
- native/interface/Vlan/ospfv3/process-id/ipv6/area

### Description

1. The default 'true', is illegally removed
2. The default 'false',is illegally removed
3. The max-elements '1' is illegally added

### Description

1. A new must expression cannot be added

- native/interface/AppGigabitEthernet/ospfv3/manet/peering/cost
- native/interface/AppGigabitEthernet/ospfv3/process-id/authentication
- native/interface/AppGigabitEthernet/ospfv3/process-id/demand-circuit
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv4/authentication
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv6/authentication
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/AppGigabitEthernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/AppGigabitEthernet/ospfv3/process-id/manet/peering/cost
- native/interface/BD-VIF/ospfv3/manet/peering/cost
- native/interface/BD-VIF/ospfv3/process-id/authentication
- native/interface/BD-VIF/ospfv3/process-id/demand-circuit
- native/interface/BD-VIF/ospfv3/process-id/ipv4/authentication
- native/interface/BD-VIF/ospfv3/process-id/ipv4/demand-circuit
- native/interface/BD-VIF/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/BD-VIF/ospfv3/process-id/ipv6/authentication
- native/interface/BD-VIF/ospfv3/process-id/ipv6/demand-circuit
- native/interface/BD-VIF/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/BD-VIF/ospfv3/process-id/manet/peering/cost
- native/interface/BDI/ospfv3/manet/peering/cost
- native/interface/BDI/ospfv3/process-id/authentication
- native/interface/BDI/ospfv3/process-id/demand-circuit
- native/interface/BDI/ospfv3/process-id/ipv4/authentication
- native/interface/BDI/ospfv3/process-id/ipv4/demand-circuit
- native/interface/BDI/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/BDI/ospfv3/process-id/ipv6/authentication
- native/interface/BDI/ospfv3/process-id/ipv6/demand-circuit
- native/interface/BDI/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/BDI/ospfv3/process-id/manet/peering/cost
- native/interface/Dialer/ospfv3/manet/peering/cost
- native/interface/Dialer/ospfv3/process-id/authentication
- native/interface/Dialer/ospfv3/process-id/demand-circuit
- native/interface/Dialer/ospfv3/process-id/ipv4/authentication
- native/interface/Dialer/ospfv3/process-id/ipv4/demand-circuit
- native/interface/Dialer/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/Dialer/ospfv3/process-id/ipv6/authentication
- native/interface/Dialer/ospfv3/process-id/ipv6/demand-circuit
- native/interface/Dialer/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/Dialer/ospfv3/process-id/manet/peering/cost
- native/interface/Ethernet/ospfv3/manet/peering/cost
- native/interface/Ethernet/ospfv3/process-id/authentication
- native/interface/Ethernet/ospfv3/process-id/demand-circuit
- native/interface/Ethernet/ospfv3/process-id/ipv4/authentication
- native/interface/Ethernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/Ethernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/Ethernet/ospfv3/process-id/ipv6/authentication
- native/interface/Ethernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/Ethernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/Ethernet/ospfv3/process-id/manet/peering/cost
- native/interface/FastEthernet/ospfv3/manet/peering/cost
- native/interface/FastEthernet/ospfv3/process-id/authentication
- native/interface/FastEthernet/ospfv3/process-id/demand-circuit
- native/interface/FastEthernet/ospfv3/process-id/ipv4/authentication
- native/interface/FastEthernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/FastEthernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/FastEthernet/ospfv3/process-id/ipv6/authentication
- native/interface/FastEthernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/FastEthernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/FastEthernet/ospfv3/process-id/manet/peering/cost
- native/interface/FiveGigabitEthernet/ospfv3/manet/peering/cost
- native/interface/FiveGigabitEthernet/ospfv3/process-id/authentication
- native/interface/FiveGigabitEthernet/ospfv3/process-id/demand-circuit
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv4/authentication
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv6/authentication
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/FiveGigabitEthernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/FiveGigabitEthernet/ospfv3/process-id/manet/peering/cost
- native/interface/FortyGigabitEthernet/ospfv3/manet/peering/cost
- native/interface/FortyGigabitEthernet/ospfv3/process-id/authentication
- native/interface/FortyGigabitEthernet/ospfv3/process-id/demand-circuit
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv4/authentication
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv6/authentication
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/FortyGigabitEthernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/FortyGigabitEthernet/ospfv3/process-id/manet/peering/cost
- native/interface/GigabitEthernet/ospfv3/manet/peering/cost
- native/interface/GigabitEthernet/ospfv3/process-id/authentication
- native/interface/GigabitEthernet/ospfv3/process-id/demand-circuit
- native/interface/GigabitEthernet/ospfv3/process-id/ipv4/authentication
- native/interface/GigabitEthernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/GigabitEthernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/GigabitEthernet/ospfv3/process-id/ipv6/authentication
- native/interface/GigabitEthernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/GigabitEthernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/GigabitEthernet/ospfv3/process-id/manet/peering/cost
- native/interface/HundredGigE/ospfv3/manet/peering/cost
- native/interface/HundredGigE/ospfv3/process-id/authentication
- native/interface/HundredGigE/ospfv3/process-id/demand-circuit
- native/interface/HundredGigE/ospfv3/process-id/ipv4/authentication
- native/interface/HundredGigE/ospfv3/process-id/ipv4/demand-circuit
- native/interface/HundredGigE/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/HundredGigE/ospfv3/process-id/ipv6/authentication
- native/interface/HundredGigE/ospfv3/process-id/ipv6/demand-circuit
- native/interface/HundredGigE/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/HundredGigE/ospfv3/process-id/manet/peering/cost
- native/interface/Loopback/ospfv3/manet/peering/cost
- native/interface/Loopback/ospfv3/process-id/authentication
- native/interface/Loopback/ospfv3/process-id/demand-circuit
- native/interface/Loopback/ospfv3/process-id/ipv4/authentication
- native/interface/Loopback/ospfv3/process-id/ipv4/demand-circuit
- native/interface/Loopback/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/Loopback/ospfv3/process-id/ipv6/authentication
- native/interface/Loopback/ospfv3/process-id/ipv6/demand-circuit
- native/interface/Loopback/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/Loopback/ospfv3/process-id/manet/peering/cost
- native/interface/Port-channel/ospfv3/manet/peering/cost
- native/interface/Port-channel/ospfv3/process-id/authentication
- native/interface/Port-channel/ospfv3/process-id/demand-circuit
- native/interface/Port-channel/ospfv3/process-id/ipv4/authentication
- native/interface/Port-channel/ospfv3/process-id/ipv4/demand-circuit
- native/interface/Port-channel/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/Port-channel/ospfv3/process-id/ipv6/authentication
- native/interface/Port-channel/ospfv3/process-id/ipv6/demand-circuit
- native/interface/Port-channel/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/Port-channel/ospfv3/process-id/manet/peering/cost
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/manet/peering/cost
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/authentication
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/demand-circuit
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv4/authentication
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv4/demand-circuit
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv6/authentication
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv6/demand-circuit
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/Port-channel-subinterface/Port-channel/ospfv3/process-id/manet/peering/cost
- native/interface/TenGigabitEthernet/ospfv3/manet/peering/cost
- native/interface/TenGigabitEthernet/ospfv3/process-id/authentication
- native/interface/TenGigabitEthernet/ospfv3/process-id/demand-circuit
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv4/authentication
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv6/authentication
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/TenGigabitEthernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/TenGigabitEthernet/ospfv3/process-id/manet/peering/cost
- native/interface/Tunnel/ospfv3/manet/peering/cost
- native/interface/Tunnel/ospfv3/process-id/authentication
- native/interface/Tunnel/ospfv3/process-id/demand-circuit
- native/interface/Tunnel/ospfv3/process-id/ipv4/authentication
- native/interface/Tunnel/ospfv3/process-id/ipv4/demand-circuit
- native/interface/Tunnel/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/Tunnel/ospfv3/process-id/ipv6/authentication
- native/interface/Tunnel/ospfv3/process-id/ipv6/demand-circuit
- native/interface/Tunnel/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/Tunnel/ospfv3/process-id/manet/peering/cost
- native/interface/TwentyFiveGigE/ospfv3/manet/peering/cost
- native/interface/TwentyFiveGigE/ospfv3/process-id/authentication
- native/interface/TwentyFiveGigE/ospfv3/process-id/demand-circuit
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv4/authentication
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv4/demand-circuit
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv6/authentication
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv6/demand-circuit
- native/interface/TwentyFiveGigE/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/TwentyFiveGigE/ospfv3/process-id/manet/peering/cost
- native/interface/TwoGigabitEthernet/ospfv3/manet/peering/cost
- native/interface/TwoGigabitEthernet/ospfv3/process-id/authentication
- native/interface/TwoGigabitEthernet/ospfv3/process-id/demand-circuit
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv4/authentication
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv4/demand-circuit
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv6/authentication
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv6/demand-circuit
- native/interface/TwoGigabitEthernet/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/TwoGigabitEthernet/ospfv3/process-id/manet/peering/cost
- native/interface/Vlan/ospfv3/manet/peering/cost
- native/interface/Vlan/ospfv3/process-id/authentication
- native/interface/Vlan/ospfv3/process-id/demand-circuit
- native/interface/Vlan/ospfv3/process-id/ipv4/authentication
- native/interface/Vlan/ospfv3/process-id/ipv4/demand-circuit
- native/interface/Vlan/ospfv3/process-id/ipv4/manet/peering/cost
- native/interface/Vlan/ospfv3/process-id/ipv6/authentication
- native/interface/Vlan/ospfv3/process-id/ipv6/demand-circuit
- native/interface/Vlan/ospfv3/process-id/ipv6/manet/peering/cost
- native/interface/Vlan/ospfv3/process-id/manet/peering/cost

## XPaths Added

### Description
