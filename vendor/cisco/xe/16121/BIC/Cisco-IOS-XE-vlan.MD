## Cisco-IOS-XE-vlan.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description
Deprecated old nodes and created new containers

### Reason
To make the model backward compatible

- /native/vlan/ios-vlan:filter/ios-vlan:vlan-list
- /native/vlan/ios-vlan:group/ios-vlan:vlan-list

## XPaths Modified

### Description
Changed type union to type uint16 and leaf to leaf-list

### Reason
Union of string and unit16 was giving issues when a range of vlan list (10-20) was sent through Netconf and later tried to delete single value so, changed type union to type uint16

- /native/vlan/ios-vlan:configuration/ios-vlan:vlan-id
- /native/vlan/ios-vlan:filter/ios-vlan:vlan-lists
- /native/vlan/ios-vlan:group/ios-vlan:vlan-lists

## XPaths Added

### Description
Added new CLI

### Reason
Vlan filter model was incorrect and some CLI's has issues

- /native/interface/Vlan/ios-vlan:service-routing/ios-vlan:mdns-sd/ios-vlan:service-policy
- /native/interface/Vlan/ios-vlan:service-routing/ios-vlan:mdns-sd/ios-vlan:service-policy/ios-vlan:dir
- /native/interface/Vlan/ios-vlan:service-routing/ios-vlan:mdns-sd/ios-vlan:service-policy/ios-vlan:name 

### Description
Deprecated old vlan-list and created new leaf-list "vlan-lists"

### Reason
list "tftp-server" was illegally removed causing backward incompatibiity

- /native/vlan/ios-vlan:filter/ios-vlan:vlan-lists
- /native/vlan/ios-vlan:group/ios-vlan:vlan-lists
