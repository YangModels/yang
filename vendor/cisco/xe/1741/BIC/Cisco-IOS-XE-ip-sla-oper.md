## Cisco-IOS-XE-ip-sla-oper.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- /http-error-stats/tcp-error
- /http-error-stats/tcp-timeout
- /http-rtt-stats/message-size
- /http-rtt-stats/tcp-rtt
- /http-rtt-stats/time-to-first-byte
- /http-stats-info/http-errors/tcp-error
- /http-stats-info/http-errors/tcp-timeout
- /http-stats-info/http-stats/message-size
- /http-stats-info/http-stats/tcp-rtt
- /http-stats-info/http-stats/time-to-first-byte
- /ip-sla-stats/sla-oper-entry/stats/http-specific-stats/http-errors/tcp-error
- /ip-sla-stats/sla-oper-entry/stats/http-specific-stats/http-errors/tcp-timeout
- /ip-sla-stats/sla-oper-entry/stats/http-specific-stats/http-stats/message-size
- /ip-sla-stats/sla-oper-entry/stats/http-specific-stats/http-stats/tcp-rtt
- /ip-sla-stats/sla-oper-entry/stats/http-specific-stats/http-stats/time-to-first-byte
- /sla-oper-entry/stats/http-specific-stats/http-errors/tcp-error
- /sla-oper-entry/stats/http-specific-stats/http-errors/tcp-timeout
- /sla-oper-entry/stats/http-specific-stats/http-stats/message-size
- /sla-oper-entry/stats/http-specific-stats/http-stats/tcp-rtt
- /sla-oper-entry/stats/http-specific-stats/http-stats/time-to-first-byte
- /stats/http-specific-stats/http-errors/tcp-error
- /stats/http-specific-stats/http-errors/tcp-timeout
- /stats/http-specific-stats/http-stats/message-size
- /stats/http-specific-stats/http-stats/tcp-rtt
- /stats/http-specific-stats/http-stats/time-to-first-byte

### Description

A new when expression cannot be added

### Reason

‘when’ statements of the existing leafs are updated to support one more IPSLA statistics type - HTTPS and the newly added restriction will not impact the already supported statistics types.

### Description

This when expression may be different than before

- /ip-sla-stats/sla-oper-entry/stats
- /ip-sla-stats/sla-oper-entry/stats/http-specific-stats
- /ip-sla-stats/sla-oper-entry/stats/over-threshold
- /ip-sla-stats/sla-oper-entry/stats/rtt
- /sla-oper-entry/stats
- /sla-oper-entry/stats/http-specific-stats
- /sla-oper-entry/stats/over-threshold
- /sla-oper-entry/stats/rtt
- /stats/http-specific-stats
- /stats/over-threshold
- /stats/rtt

### XPaths Added

### Description
