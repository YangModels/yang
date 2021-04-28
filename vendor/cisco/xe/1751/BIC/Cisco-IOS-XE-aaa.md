## Cisco-IOS-XE-aaa.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- interface-grouping/interface-choice/Loopback/Loopback
- native/radius/server/address/acct-port
- native/radius/server/address/auth-port

### Description

1. The range '[(0, 2147483647)]' is illegally added
2. The default '1813' is illegally changed from '1646'
3. The default '1812' is illegally changed from '1645'

### Reason

Loopback range in yang interface-grouping was 0-4294967295. However, from device side loopback interface can only support range from 0 to 2147483647. Hence loopback range in yang was modified to be inline with device range

## XPaths Added

### Description
