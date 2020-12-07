## Cisco-IOS-XE-ospf.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- /native/router/router-ospf/ospf/process-id/timers/throttle/lsa/max-delay
- /native/router/router-ospf/ospf/process-id/timers/throttle/lsa/min-delay
- /native/router/router-ospf/ospf/process-id/timers/throttle/spf/max-delay
- /native/router/router-ospf/ospf/process-id/timers/throttle/spf/min-delay
- /native/router/router-ospf/ospf/process-id-vrf/timers/throttle/lsa/max-delay
- /native/router/router-ospf/ospf/process-id-vrf/timers/throttle/lsa/min-delay
- /native/router/router-ospf/ospf/process-id-vrf/timers/throttle/spf/max-delay
- /native/router/router-ospf/ospf/process-id-vrf/timers/throttle/spf/min-delay

### Description

A new must expression added

### Reason

In IOS CLI Timers throttle spf/lsa command have a restriction that - initial delay <= min delay <= max delay

## XPaths Added

### Description
