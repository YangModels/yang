## Cisco-IOS-XR-um-monitor-session-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added merge-group, priority, mpls-acls under monitor-session interface config and sflow destination, erspan-session-id under monitor-session config.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L140)	/{IF-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv4
- (L150)	/{IF-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv6
- (L953)	/{L2TRANS-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv4
- (L963)	/{L2TRANS-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv6

## XPaths Modified

- (L166)	/{IF-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv4
- (L201)	/{IF-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv6
- (L1122)	/{L2TRANS-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv4
- (L1157)	/{L2TRANS-BODY}/monitor-sessions/monitor-session[session-name]/acl-ipv6

