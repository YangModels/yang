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

- (L1354)	/syslog/files/file[file-name]/file-specification/path
- (L1425)	/syslog/files/file[file-name]/file-name

## XPaths Removed

N/A

## XPaths Modified

N/A

