## Cisco-IOS-XR-infra-syslog-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Remove LOG_SYS9 -> LOG_SYS14 logging facility enum values. These are non-standard (i.e. XR-specific not in RFC5425) and also had no functional effect in any previous XR release.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L375)	/{Facility}
- (L380)	/{Facility}
- (L385)	/{Facility}
- (L390)	/{Facility}
- (L395)	/{Facility}
- (L400)	/{Facility}
- (L688)	/syslog-service/timestamps/log/log-datetime/log-datetime-value/msec
- (L735)	/syslog-service/timestamps/debug/debug-datetime/datetime-value/msec

## XPaths Modified

N/A

