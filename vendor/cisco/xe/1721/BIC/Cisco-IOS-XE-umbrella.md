## Cisco-IOS-XE-umbrella.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Modified

### Description

New "must" statement added

### Reason

YANG GET-config operation was failing for default value of UDP time config under umbrella parameter-map. This was corrected and for resolver addresses default address config is not allowed in CLI but was allowed via YANG. This behaviour was corrected and configuring of default addresses via YANG was blocked

- /native/parameter-map/type/ios-umbrella:umbrella/ios-umbrella:global/ios-umbrella:resolver/ios-umbrella:ipv4
- /native/parameter-map/type/ios-umbrella:umbrella/ios-umbrella:global/ios-umbrella:resolver/ios-umbrella:ipv6

## XPaths Added

N/A
