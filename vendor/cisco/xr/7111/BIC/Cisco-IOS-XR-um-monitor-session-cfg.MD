## Cisco-IOS-XR-um-monitor-session-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Remove sflow destination, replace MPLS-IPv4 and MPLS-IPv6 ACLs with a single MPLS ACL.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L238)	/{IF-BODY}/monitor-sessions/monitor-session[session-name]/acl-mpls-ipv4
- (L273)	/{IF-BODY}/monitor-sessions/monitor-session[session-name]/acl-mpls-ipv6
- (L1582)	/monitor-sessions/monitor-session[session-name]/destination/sflow
- (L1832)	/monitor-sessions/monitor-session[session-name]/rx/sflow
- (L2035)	/monitor-sessions/monitor-session[session-name]/tx/sflow

## XPaths Modified

N/A

