## Cisco-IOS-XE-ethernet.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

### Description

A new When expression added

- native/interface/AppGigabitEthernet/channel-group/mode
- native/interface/BD-VIF/channel-group/mode
- native/interface/BDI/channel-group/mode
- native/interface/FastEthernet/channel-group/mode
- native/interface/FiveGigabitEthernet/channel-group/mode
- native/interface/FortyGigabitEthernet/channel-group/mode
- native/interface/GigabitEthernet/channel-group/mode
- native/interface/HundredGigE/channel-group/mode
- native/interface/Port-channel/channel-group/mode
- native/interface/Port-channel-subinterface/Port-channel/channel-group/mode
- native/interface/TenGigabitEthernet/channel-group/mode
- native/interface/TwentyFiveGigE/channel-group/mode
- native/interface/TwoGigabitEthernet/channel-group/mode
- native/interface/Virtual-Template/channel-group/mode
- native/interface/VirtualPortGroup/channel-group/mode
- native/interface/Vlan/channel-group/mode
- native/interface/ucse/channel-group/mode

### Description

The range '[(0, 65535)]' is added
The range '[(1, 16)]' is added

- config-interface-ethernet-member-link-lacp-grouping(grouping)/lacp/port-priority
- config-interface-port-channel-lacp-grouping(grouping)/lacp/max-bundle
- config-interface-port-channel-lacp-grouping(grouping)/lacp/min-bundle

### Reason

'no channel-group 1" results in unexpected failure with "channel-group mode active"

## XPaths Added

### Description
