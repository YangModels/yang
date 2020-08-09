## Cisco-IOS-XE-ipv6.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Reason

IPv6 prefix lists are erased with the upgrade. Hence changed the status to deprecated

- /native/ipv6/prefix-list/prefixes/permit
- /native/ipv6/prefix-list/prefixes/permit/\*
- /native/ipv6/prefix-list/prefixes/deny
- /native/ipv6/prefix-list/prefixes/deny/\*

## XPaths Modified

### Description

Range 1-255  and default 1 is added

- /native/ipv6/route/ipv6-route-list/ipv6-fwd-list/distance

## XPaths Added

N/A
