## Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- set-ap-country(grouping)/country-string
- set-ap-location(grouping)/location
- set-ap-name(grouping)/name

### Description

1. A new length expression '1..4'  added
2. A new pattern expression '[ -~]+'  added
3. A new length expression '1..256'  added
4. The pattern expression may be more constrained than before. Old pattern '[a-zA-Z0-9_\-]*' new pattern '[!-~]+'

### Reason

Adding a uniform validation for input in YANG (matching the matching TDL validation).

## XPaths Added

### Description
