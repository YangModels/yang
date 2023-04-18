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

- (L926)	/span-monitor-session/sessions/session[session]/forward-drops
- (L941)	/span-monitor-session/sessions/session[session]/tm-drops

## XPaths Modified

- (L685)	/span-monitor-session/sessions/session[session]/forward-drops
- (L716)	/span-monitor-session/sessions/session[session]/tm-drops

