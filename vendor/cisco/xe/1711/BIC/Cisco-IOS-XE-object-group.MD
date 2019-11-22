## Cisco-IOS-XE-object-group.yang

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
A must condition has been added to the IPv4 object-group name node, to ensure the object-group is not empty.

### Reason
IOS rejects configuration of empty object-groups, though it was allowed by yang. With this change, this restriction has been implemented in the model as well.

- /native/object-group/ios-og:network/ios-og:name

## XPaths Added
N/A
