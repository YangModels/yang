## Cisco-IOS-XE-switch.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- /native/interface/\*/switchport/port-security-cfg
- /native/interface/\*/switchport/port-security-cfg/\*

### Reason

Had to obsolete the port-security-cfg leaf and port-security-conf added by CSCvq35048 because we cannot have tailf:cli-drop-node-name in a container under the switchport container. The tailf annotation causes "no switchport" to fail as an incomplete CLI in confd_cli, since there is another switchport leaf under the switchport-conf container with tailf:cli-drop-node-name.

## XPaths Deprecated

### Description

## XPaths Modified

- /native/interface/AppGigabitEthernet/macsec
- /native/interface/AppGigabitEthernet/macsec-option
- /native/interface/FastEthernet/macsec
- /native/interface/FastEthernet/macsec-option
- /native/interface/FiveGigabitEthernet/macsec
- /native/interface/FiveGigabitEthernet/macsec-option
- /native/interface/FortyGigabitEthernet/macsec
- /native/interface/FortyGigabitEthernet/macsec-option
- /native/interface/GigabitEthernet/macsec
- /native/interface/GigabitEthernet/macsec-option
- /native/interface/HundredGigE/macsec
- /native/interface/HundredGigE/macsec-option
- /native/interface/Port-channel/macsec
- /native/interface/Port-channel/macsec-option
- /native/interface/Port-channel-subinterface/Port-channel/macsec
- /native/interface/Port-channel-subinterface/Port-channel/macsec-option
- /native/interface/TenGigabitEthernet/macsec
- /native/interface/TenGigabitEthernet/macsec-option
- /native/interface/TwentyFiveGigE/macsec
- /native/interface/TwentyFiveGigE/macsec-option
- /native/interface/TwentyFiveGigabitEthernet/macsec
- /native/interface/TwentyFiveGigabitEthernet/macsec-option
- /native/interface/TwoGigabitEthernet/macsec
- /native/interface/TwoGigabitEthernet/macsec-option

### Description

The if-feature 'ios-features:macsec-common' is illegally added

### Description

The case 'all' is removed.

- /config-interface-switchport-grouping/trunk/allowed/vlan/vlan-choice/all

### Description

The container 'port-security' is removed.

config-interface-switchport-grouping/port-security

### Description

The container 'port-security-conf' is illegally changed to a leaf

- /config-interface-switchport-grouping/port-security-conf

### Description

The container 'Vlan-config' is removed.

config-interface-switchport-grouping/trunk/native/vlan-config

### Description

The default 'true' is removed.

- /native/interface/AppGigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/Ethernet-Internal(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/FastEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/FiveGigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/FortyGigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/GigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/HundredGigE(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/Port-channel(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/Port-channel-subinterface/Port-channel(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/TenGigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/TwentyFiveGigE(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/TwentyFiveGigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/TwoGigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/Wlan-GigabitEthernet(list)/switchport/trunk/native/vlan-config/tag
- /native/interface/ucse(list)/switchport/trunk/native/vlan-config/tag

### Description

The if-feature 'ios-features:macsec-common' is illegally added

config-interface-switch-grouping/macsec
config-interface-switch-grouping/macsec-option
- /native/interface/AppGigabitEthernet(list)/macsec
- /native/interface/AppGigabitEthernet(list)/macsec-option
- /native/interface/FastEthernet(list)/macsec
- /native/interface/FastEthernet(list)/macsec-option
- /native/interface/FiveGigabitEthernet(list)/macsec
- /native/interface/FiveGigabitEthernet(list)/macsec-option
- /native/interface/FortyGigabitEthernet(list)/macsec
- /native/interface/FortyGigabitEthernet(list)/macsec-option
- /native/interface/GigabitEthernet(list)/macsec
- /native/interface/GigabitEthernet(list)/macsec-option
- /native/interface/HundredGigE(list)/macsec
- /native/interface/HundredGigE(list)/macsec-option
- /native/interface/Port-channel(list)/macsec
- /native/interface/Port-channel(list)/macsec-option
- /native/interface/Port-channel-subinterface/Port-channel(list)/macsec
- /native/interface/Port-channel-subinterface/Port-channel(list)/macsec-option
- /native/interface/TenGigabitEthernet(list)/macsec
- /native/interface/TenGigabitEthernet(list)/macsec-option
- /native/interface/TwentyFiveGigE(list)/macsec
- /native/interface/TwentyFiveGigE(list)/macsec-option
- /native/interface/TwentyFiveGigabitEthernet(list)/macsec
- /native/interface/TwentyFiveGigabitEthernet(list)/macsec-option
- /native/interface/TwoGigabitEthernet(list)/macsec
- /native/interface/TwoGigabitEthernet(list)/macsec-option

### Description

The leaf 'add' is removed.

- /config-interface-switchport-grouping/private-vlan/mapping/add

### Description

The leaf 'name' is removed.

- /config-interface-switchport-grouping/access/vlan/name

### Description

The leaf 'port-security-cfg' is removed.

- /config-interface-switchport-grouping/port-security-cfg

### Description

The leaf 'remove' is removed.

- /config-interface-switchport-grouping/private-vlan/mapping/remove

### Description

The leaf 'vlan' is illegally changed to a container

- /config-interface-switchport-grouping/trunk/native/vlan

## XPaths Added

### Description
