## Cisco-IOS-XE-ppp


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/interface/*/ppp/multilink/endpoint
- native/interface/*/ppp/multilink/fragment
- native/interface/*/ppp/multilink/group
- native/interface/*/ppp/multilink/interleave
- native/interface/*/ppp/multilink/links

### Description
The  'endpoint' and  "fragment",  "group",  "interleave" and  "links" is removed.

### Reason
Interface <>, submode command "ppp chap password <>" is allowing special characters, as part of nvgen it is displaying with double-quotes. Hence amde these changes to fix this behaviour.

## XPaths Added

### Description
