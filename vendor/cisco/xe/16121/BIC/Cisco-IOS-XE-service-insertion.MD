## Cisco-IOS-XE-service-insertion.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description
Depreacted the leaf-list appnav-controller

### Reason
To add support for AppNav changes done in SDWAN

- /native/service-insertion/ios-service-insertion:appnav-controller-group/ios-service-insertion:appnav-controller

## XPaths Modified

### Description
Added leafref to the appnav and service node group

### Reason
Due to order dependency in IOSd, config fails when vManage pushes entire appqoe config.

- /native/service-insertion/ios-service-insertion:service-context/ios-service-insertion:appqoe/ios-service-insertion:appnav-controller-group
- /native/service-insertion/ios-service-insertion:service-context/ios-service-insertion:appqoe/ios-service-insertion:service-node-group
- /native/service-insertion/ios-service-insertion:service-context/ios-service-insertion:waas/ios-service-insertion:appnav-controller-group
- /native/service-insertion/ios-service-insertion:service-context/ios-service-insertion:waas/ios-service-insertion:service-node-group


## XPaths Added

### Reason
To add support for AppNav changes done in SDWAN

- /native/service-insertion/ios-service-insertion:appnav-controller-group/ios-service-insertion:appnav-controllers
- /native/service-insertion/ios-service-insertion:appnav-controller-group/ios-service-insertion:appnav-controllers/ios-service-insertion:address
- /native/service-insertion/ios-service-insertion:appnav-controller-group/ios-service-insertion:appnav-controllers/ios-service-insertion:vrf
- /native/service-insertion/ios-service-insertion:appnav-controller-group/ios-service-insertion:appqoe
- /native/service-insertion/ios-service-insertion:service-node-group/ios-service-insertion:appqoe



