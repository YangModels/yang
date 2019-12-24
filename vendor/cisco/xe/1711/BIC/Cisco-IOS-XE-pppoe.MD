## Cisco-IOS-XE-pppoe.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description

changed dial-pool-number from leaf to list

### Reason

IOS CLI supports multiple dial-pool-number. CONFD CLI only supports one. IOS's behavior is correct. So YANG nodes should be changed from leaf to list.

- /native/interface/ATM/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number
- /native/interface/ATM-subinterface/ATM/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number
- /native/interface/ATM-ACR/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number
- /native/interface/ATM-ACRsubinterface/ATM-ACR/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number
- /native/interface/BDI/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/CEM/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number
- /native/interface/CEM-ACR/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number
- /native/interface/Ethernet/ios-pppoe:pppoe-client/ios-pppoe:dial-pool-number
- /native/interface/FastEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/GigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/TwoGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/FiveGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/AppGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/TenGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/TwentyFiveGigE/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/FortyGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/HundredGigE/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/overlay/ios-otv:pppoe-client/ios-otv:dial-pool-number
- /native/interface/Port-channel/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/Port-channel-subinterface/Port-channel/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/Vlan/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/Virtual-Template/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/VirtualPortGroup/ios-eth:pppoe-client/ios-eth:dial-pool-number
- /native/interface/BD-VIF/ios-eth:pppoe-client/ios-eth:dial-pool-number


## XPaths Modified
N/A

## XPaths Added

### Description

changed dial-pool-number from leaf to list

### Reason

IOS CLI supports multiple dial-pool-number. CONFD CLI only supports one. IOS's behavior is correct. So YANG nodes should be changed from leaf to list.

- /native/interface/ATM/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number-list
- /native/interface/ATM-subinterface/ATM/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number-list
- /native/interface/ATM-ACR/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number-list
- /native/interface/ATM-ACRsubinterface/ATM-ACR/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number-list
- /native/interface/BDI/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/CEM/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number-list
- /native/interface/CEM-ACR/ios-atm:pvc/ios-atm:pppoe-client/ios-atm:dial-pool-number-list
- /native/interface/Ethernet/ios-pppoe:pppoe-client/ios-pppoe:dial-pool-number-list
- /native/interface/FastEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/GigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/TwoGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/FiveGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/AppGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/TenGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/TwentyFiveGigE/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/FortyGigabitEthernet/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/HundredGigE/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/overlay/ios-otv:pppoe-client/ios-otv:dial-pool-number-list
- /native/interface/Port-channel/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/Port-channel-subinterface/Port-channel/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/Vlan/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/Virtual-Template/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/VirtualPortGroup/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
- /native/interface/BD-VIF/ios-eth:pppoe-client/ios-eth:dial-pool-number-list
