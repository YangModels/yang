## Cisco-IOS-XE-bridge-domain.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Reason
Portchannel member is not showing in netconf get-config of bridge-domain. Hence obsoleted the below nodes

- /native/bridge-domain/ios-bd:brd-id/ios-bd:member/ios-bd:_controller
- /native/bridge-domain/ios-bd:brd-id/ios-bd:member/ios-bd:member-interface/ios-bd:interface-id
- /native/bridge-domain/ios-bd:parameterized/ios-bd:vlan/ios-bd:member/ios-bd:_controller
- /native/bridge-domain/ios-bd:parameterized/ios-bd:vlan/ios-bd:member/ios-bd:member-interface/ios-bd:interface-id

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

### Reason
Yang model support for new configuration CLI of BD-VIF

- /native/bridge-domain/ios-bd:brd-id/ios-bd:member/ios-bd:BD-VIF
- /native/bridge-domain/ios-bd:brd-id/ios-bd:member/ios-bd:BD-VIF/ios-bd:name
- /native/bridge-domain/ios-bd:parameterized/ios-bd:vlan/ios-bd:member/ios-bd:BD-VIF
- /native/bridge-domain/ios-bd:parameterized/ios-bd:vlan/ios-bd:member/ios-bd:BD-VIF/ios-bd:name

