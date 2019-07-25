## Cisco-IOS-XE-ntp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
source option was removed/obsoleted from the model in "ntp server vrf 1 10.1.1.2 source GigabitEthernet5 key 1 prefer version 4" CLI

### Reason
source option is not valid in IOS. It was wrongly placed in model.

- /native/ntp/ios-ntp:peer/ios-ntp:vrf/ios-ntp:ipv6/ios-ntp:source
- /native/ntp/ios-ntp:peer/ios-ntp:vrf/ios-ntp:server-list/ios-ntp:source
- /native/ntp/ios-ntp:server/ios-ntp:vrf/ios-ntp:ip/ios-ntp:source
- /native/ntp/ios-ntp:server/ios-ntp:vrf/ios-ntp:server-list/ios-ntp:source
- /native/ntp/ios-ntp:source/ios-ntp:TwentyFiveGigabitEthernet

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

- /native/ntp/ios-ntp:authentication-key/ios-ntp:encryption-type
- /native/ntp/ios-ntp:source/ios-ntp:BD-VIF
- /native/ntp/ios-ntp:source/ios-ntp:TwentyFiveGigabitEthernet
- /native/ntp/ios-ntp:trusted-key/ios-ntp:hyphen




