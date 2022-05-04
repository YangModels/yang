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

- (L329)	/{SPAN-MONITOR-SESSION-TABLE}/span-monitor-sessions
- (L359)	/{ETHERNET-SPAN-INTERFACE-CFG-SPAN-MONITOR-SESSION-TABLE}/span-monitor-sessions

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L781)	/span-monitor-session/sessions/session[session]/destination/destination-interface-name
- (L791)	/span-monitor-session/sessions/session[session]/destination/destination-ipv4-address
- (L801)	/span-monitor-session/sessions/session[session]/destination/destination-ipv6-address

