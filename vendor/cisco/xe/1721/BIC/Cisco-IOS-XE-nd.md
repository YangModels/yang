## Cisco-IOS-XE-nd.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Reason

Adding switchconf constraint checks so that raguard policy cannot be attached to an interface when it is not in switch mode. Enforcing the condition for setting the switch-conf to True before policy can be attached to an interface. This is one time action, once switchconf is set to True, interface stays in switch mode and can be disabled by running command with switch-conf set to False. To ensure user explicitly set the switchport-conf to True, which attaching a raguard policy on an interface

- /ios:native/ios:ipv6/ios:nd/ios-nd:raguard/ios-nd:attach-policy//ios:native/ios:ipv6/ios:nd/ios-nd:raguard/ios-nd:policy

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

### Description

New xpaths added for the obsoleted nodes.

- /native/interface/AppGigabitEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/FastEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/FiveGigabitEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/FortyGigabitEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/GigabitEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/HundredGigE/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/Loopback/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/Port-channel/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/TenGigabitEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/TwentyFiveEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/TwoGigabitEthernet/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/Vlan/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/Tunnel/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
- /native/interface/vasileft/ipv6/nd/ios-nd:raguard/ios-nd:attach-policy
