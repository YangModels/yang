## Cisco-IOS-XE-dhcp.yang

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
Hardening - Added missing when constraints

### Reason
Added ‘when’ constraints to leaves 'hours' and 'minutes' within container 'lease-value' since yang model was accepting values for minutes/hours even when hours/days value was not provided respectively.

- /native/ip/dhcp/ios-dhcp:pool/ios-dhcp:lease/ios-dhcp:lease-value/ios-dhcp:minutes
- /native/ip/dhcp/ios-dhcp:pool/ios-dhcp:lease/ios-dhcp:lease-value/ios-dhcp:hours

## XPaths Added
N/A

