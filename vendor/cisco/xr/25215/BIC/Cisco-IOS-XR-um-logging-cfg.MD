## Cisco-IOS-XR-um-logging-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Changed sch-type for the node ipv6-address under container host-ipv6-addresses.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L1620)	/logging/files/file[file-name]/path/path-name
- (L1631)	/logging/files/file[file-name]/path/maxfilesize
- (L1642)	/logging/files/file[file-name]/path/severity
- (L1538)	/logging/files/file[file-name]
- (L2122)	/logging/vrfs/vrf[vrf-name]/vrf-name
- (L2116)	/logging/vrfs/vrf[vrf-name]

## XPaths Removed

- (L171)	/logging/monitor
- (L69)	/logging/console
- (L614)	/logging/ipv6/dscp
- (L734)	/logging/ipv6/precedence
- (L435)	/logging/ipv4/dscp
- (L555)	/logging/ipv4/precedence
- (L898)	/logging/buffered/buffered-entries
- (L912)	/logging/buffered/logging-buffer-size
- (L922)	/logging/buffered/level
- (L2159)	/logging/source-interfaces/source-interface[source-interface-name]/source-interface-name
- (L2164)	/logging/source-interfaces/source-interface[source-interface-name]/vrfs
- (L2205)	/logging/format/rfc5424
- (L2211)	/logging/format/bsd
- (L1339)	/logging/history
- (L793)	/logging/facility/level
- (L1065)	/logging/files/file[file-name]/path
- (L1075)	/logging/files/file[file-name]/maxfilesize
- (L1086)	/logging/files/file[file-name]/severity
- (L1133)	/logging/files/file[file-name]/local-accounting
- (L1482)	/logging/tls-servers/tls-server[tls-server-name]/severity
- (L310)	/logging/archive/device/disk0
- (L316)	/logging/archive/device/disk1
- (L322)	/logging/archive/device/harddisk
- (L332)	/logging/archive/frequency/daily
- (L338)	/logging/archive/frequency/weekly
- (L397)	/logging/archive/severity
- (L1517)	/logging/vrfs/vrf[vrf-name]/vrf-name
- (L1523)	/logging/vrfs/vrf[vrf-name]/vrf-name
- (L1533)	/logging/vrfs/vrf[vrf-name]/host-names
- (L1736)	/logging/vrfs/vrf[vrf-name]/host-ipv4-addresses
- (L1933)	/logging/vrfs/vrf[vrf-name]/host-ipv6-addresses
- (L221)	/logging/console-logging
- (L240)	/logging/monitor-discriminator
- (L1389)	/logging/history-size

## XPaths Modified

- (L402)	/logging/monitor
- (L572)	/logging/console
- (L1299)	/logging/source-interfaces/source-interface[interface-name][vrf-name]
- (L1319)	/logging/format
- (L1338)	/logging/suppress/duplicates
- (L1344)	/logging/history
- (L1411)	/logging/localfilesize
- (L1419)	/logging/facility
- (L1523)	/logging/container/fetch-timestamp
- (L1528)	/logging/container/all
- (L1616)	/logging/files/file[file-name]/path
- (L2009)	/logging/archive/frequency
- (L2121)	/logging/vrfs/vrf[vrf-name]/vrf-name

