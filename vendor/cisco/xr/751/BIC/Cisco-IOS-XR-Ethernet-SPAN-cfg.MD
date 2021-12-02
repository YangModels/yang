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

- (L660)	/span-monitor-session/sessions/session[session]/destination-rx/vrf-name
- (L794)	/span-monitor-session/sessions/session[session]/destination-tx/vrf-name
- (L918)	/span-monitor-session/sessions/session[session]/destination/vrf-name

