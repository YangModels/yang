## Cisco-IOS-XR-Ethernet-SPAN-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Files are now a valid SPAN destination, so the InvalidValue leaf needs to be updated to exclude them.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L432)	/span-monitor-session/sessions/session[session]/destination/destination-interface-name
- (L442)	/span-monitor-session/sessions/session[session]/destination/destination-ipv4-address
- (L452)	/span-monitor-session/sessions/session[session]/destination/destination-ipv6-address

