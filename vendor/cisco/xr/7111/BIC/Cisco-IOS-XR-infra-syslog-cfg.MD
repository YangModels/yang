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

- (L1000)	/syslog/host-server/vrfs/vrf[vrf-name]/ipv6s/ipv6[address]/ipv6-severity-levels
- (L1030)	/syslog/host-server/vrfs/vrf[vrf-name]/hosts/host[host-name]/host-name-severities
- (L1094)	/syslog/host-server/vrfs/vrf[vrf-name]/ipv4s/ipv4[address]/ipv4-severity-levels
- (L1302)	/syslog/ipv4/dscp
- (L1352)	/syslog/ipv4/precedence
- (L1428)	/syslog/ipv6/dscp
- (L1478)	/syslog/ipv6/precedence
- (L392)	/{Logging-dscp}
- (L474)	/{Logging-precedence}

## XPaths Modified

N/A

