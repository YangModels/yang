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

- /native/interface/AppGigabitEthernet/channel-group/number
- /native/interface/BD-VIF/channel-group/number
- /native/interface/BDI/channel-group/number
- /native/interface/FastEthernet/channel-group/number
- /native/interface/FiveGigabitEthernet/channel-group/number
- /native/interface/FortyGigabitEthernet/channel-group/number
- /native/interface/GigabitEthernet/channel-group/number
- /native/interface/HundredGigE/channel-group/number
- /native/interface/Port-channel/channel-group/number
- /native/interface/Port-channel-subinterface/Port-channel/channel-group/number
- /native/interface/TenGigabitEthernet/channel-group/number
- /native/interface/TwentyFiveGigE/channel-group/number
- /native/interface/TwoGigabitEthernet/channel-group/number
- /native/interface/Virtual-Template/channel-group/number
- /native/interface/VirtualPortGroup/channel-group/number
- /native/interface/Vlan/channel-group/number
- /native/interface/ucse/channel-group/number

### Description

A new must expression dded

### Reason

channel-group was not getting deleted from cdb even though we remove port-channel CLI, but was getting deleted in device.Hence added the must condition to resolve the issue.

### Description

The default '10000' and '2500' is removed

### Reason

The default value showing up is wrong as we don’t have such default val in IOS-XE.

- /native/ethernet/cfm/alarm/reset
- /native/interface/AppGigabitEthernet/service/instance/cfm/mep/alarm/reset
- /native/interface/AppGigabitEthernet/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/BDI/service/instance/cfm/mep/alarm/reset
- /native/interface/BDI/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/FastEthernet/service/instance/cfm/mep/alarm/reset
- /native/interface/FastEthernet/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/FiveGigabitEthernet/service/instance/cfm/mep/alarm/reset
- /native/interface/FiveGigabitEthernet/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/FortyGigabitEthernet/service/instance/cfm/mep/alarm/reset
- /native/interface/FortyGigabitEthernet/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/GigabitEthernet/service/instance/cfm/mep/alarm/reset
- /native/interface/GigabitEthernet/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/HundredGigE/service/instance/cfm/mep/alarm/reset
- /native/interface/HundredGigE/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/Port-channel/service/instance/cfm/mep/alarm/reset
- /native/interface/Port-channel/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/Port-channel-subinterface/Port-channel/service/instance/cfm/mep/alarm/reset
- /native/interface/Port-channel-subinterface/Port-channel/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/TenGigabitEthernet/service/instance/cfm/mep/alarm/reset
- /native/interface/TenGigabitEthernet/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/TwentyFiveGigE/service/instance/cfm/mep/alarm/reset
- /native/interface/TwentyFiveGigE/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/TwoGigabitEthernet/service/instance/cfm/mep/alarm/reset
- /native/interface/TwoGigabitEthernet/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/Virtual-Template/service/instance/cfm/mep/alarm/reset
- /native/interface/Virtual-Template/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/VirtualPortGroup/service/instance/cfm/mep/alarm/reset
- /native/interface/VirtualPortGroup/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/Vlan/service/instance/cfm/mep/alarm/reset
- /native/interface/Vlan/service/instance/cfm/mep-list/domain/alarm/reset
- /native/interface/ucse/service/instance/cfm/mep/alarm/reset
- /native/interface/ucse/service/instance/cfm/mep-list/domain/alarm/reset

### Description

The if-feature 'ios-features:eth-evc' is illegally added

- /native/interface/AppGigabitEthernet/service/instance/ethernet-evc-name
- /native/interface/BDI/service/instance/ethernet-evc-name
- /native/interface/FastEthernet/service/instance/ethernet-evc-name
- /native/interface/FiveGigabitEthernet/service/instance/ethernet-evc-name
- /native/interface/FortyGigabitEthernet/service/instance/ethernet-evc-name
- /native/interface/GigabitEthernet/service/instance/ethernet-evc-name
- /native/interface/HundredGigE/service/instance/ethernet-evc-name
- /native/interface/Port-channel/service/instance/ethernet-evc-name
- /native/interface/Port-channel-subinterface/Port-channel/service/instance/ethernet-evc-name
- /native/interface/TenGigabitEthernet/service/instance/ethernet-evc-name
- /native/interface/TwentyFiveGigE/service/instance/ethernet-evc-name
- /native/interface/TwoGigabitEthernet/service/instance/ethernet-evc-name
- /native/interface/Virtual-Template/service/instance/ethernet-evc-name
- /native/interface/VirtualPortGroup/service/instance/ethernet-evc-name
- /native/interface/Vlan/service/instance/ethernet-evc-name
- /native/interface/ucse/service/instance/ethernet-evc-name

## XPaths Added

### Description
