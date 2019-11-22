## Cisco-IOS-XE-switch.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

obsoleting unused cli nodes

### Reason

"config-switch-virtual-grouping" grouping was initially part of "ned/cedge/Cisco-IOS-XE-switch.yang" model and it got deprecated. Related configs were deleted sometime back. Thus, same model is obsoleted in "ned/Cisco-IOS-XE-switch.yang" file to restore backward compatibility.

- /native/ios-sw:switch-virtual/ios-sw:domain
- /native/ios-sw:switch-virtual/ios-sw:dual-active
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:detection
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:detection/ios-sw:pagp
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:detection/ios-sw:pagp/ios-sw:trust
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:detection/ios-sw:pagp/ios-sw:trust/ios-sw:channel-group
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:recovery
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:recovery/ios-sw:ip
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:recovery/ios-sw:ip/ios-sw:address
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:recovery/ios-sw:ip/ios-sw:mask
- /native/ios-sw:switch-virtual/ios-sw:dual-active/ios-sw:recovery/ios-sw:switch
- /native/ios-sw:switch-virtual/ios-sw:mac-address
- /native/ios-sw:switch-virtual/ios-sw:mac-address/ios-sw:use-virtual
- /native/ios-sw:switch-virtual/ios-sw:switch
- /native/ios-sw:switch-virtual/ios-sw:switch/ios-sw:mode
- /native/ios-sw:switch-virtual/ios-sw:switch/ios-sw:priority
- /native/ios-sw:switch-virtual/ios-sw:switch/ios-sw:switch-number
- /native/ios-sw:switch-virtual/ios-sw:virtual

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

N/A



