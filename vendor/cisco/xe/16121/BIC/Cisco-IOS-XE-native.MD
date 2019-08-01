## Cisco-IOS-XE-native.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

No Xpaths obsoleted

## XPaths Deprecated 

### Description 
Earlier it was list and was changed to container, causing backward incompatibility. Hence deprecated the list and added a new leaf

- /native/hw-module/ios:switch/ios:usbflash1-password

### Description/Reason
tftp-server-list was illegally removed causing backward incompatibility.

- /native/tftp-server


## XPaths Modified

- call-home shall be a non-presence container in practice. Hence presence "true" removed from call-home container.

- /native/call-home

- /native/call-home/\* (all sub-trees and sub-leaves under call-home)


## XPaths Added

- /native/hw-module/ios:switch/ios:usbflash1-password1
- /native/tftp-server-config
