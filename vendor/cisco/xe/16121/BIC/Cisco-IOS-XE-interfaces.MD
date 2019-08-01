## Cisco-IOS-XE-interfaces.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

### Description/Reason
Deprecated the port-control container for backward compatibility.

- /native/interface/\*/access-session/port-control
- /native/interface/nve/member/vni/default/ingress-replication
- /native/interface/nve/member/vni/ingress-replication
- /native/interface/nve/member/vni/no/ingress-replication

## XPaths Modified

N/A

## XPaths Added

### Description/Reason
Added new node and depreacted the old container for backward compatibility

- /native/interface/\*/access-session/port-control-config
- /native/interface/nve/member/vni/ingress-replication-config
- /native/interface/nve/member/vni/ingress-replication-config/cp-signal
- /native/interface/nve/member/vni/ingress-replication-config/peer-addr
- /native/interface/\*/ip/router/isis/tag
