## Cisco-IOS-XE-device-tracking.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsolete unsupported  group 'config-ip-device-grouping

### Reason
'ip device tracking' models in Cisco-IOS-XE-device-tracking was mistakenly set.Polaris does not support these IPDT CLIs. Also when tested it by Yang Suite, error messages returned

- /native/device-tracking/ios-dt:policy
- /native/vlan/ios-vlan:configuration/ios-vlan:device-tracking
- /native/interface/FastEthernet/switchport/ios-sw:device-tracking
- /native/interface/GigabitEthernet/switchport/ios-sw:device-tracking
- /native/interface/TwoGigabitEthernet/switchport/ios-sw:device-tracking
- /native/interface/FiveGigabitEthernet/switchport/ios-sw:device-tracking
- /native/interface/AppGigabitEthernet/switchport/ios-sw:device-tracking
- /native/interface/TenGigabitEthernet/switchport/ios-sw:device-tracking
- /native/interface/Port-channel/switchport/ios-sw:device-tracking

## XPaths Deprecated

N/A

### XPaths Modified

Added must statement

/native/interface/Port-channel/ios-sw:device-tracking/ios-sw:attach-policy

## XPaths Added

### Description
Add new SISF config yang models and supports for vlan and interface po-channel

### Reason
Add new SISF yang model for port-channel and vlan targets. In 'device-tracking' model, add 'presence true' to represent default device-tracking policy

/native/device-tracking/ios-dt:policy/ios-dt:destination-glean
/native/device-tracking/ios-dt:policy/ios-dt:destination-glean/ios-dt:log-only
/native/device-tracking/ios-dt:policy/ios-dt:prefix-glean
/native/device-tracking/ios-dt:policy/ios-dt:trusted-port
/native/interface/Port-channel/ios-sw:device-tracking
/native/interface/Port-channel/switchport/ios-sw:device-tracking
/native/interface/Port-channel/switchport/ios-sw:device-tracking/ios-sw:attach-policy
/native/vlan/ios-vlan:configuration/ios-vlan:device-tracking
/native/vlan/ios-vlan:configuration/ios-vlan:device-tracking/ios-vlan:attach-policy
/native/vlan/ios-vlan:device-tracking
/native/vlan/ios-vlan:device-tracking/ios-vlan:attach-policy
