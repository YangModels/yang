## Cisco-IOS-XR-um-router-ospfv3-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Moved out translate node from under nssa into its own node due to sysdb incompat ibilities. Removed container include-stub from stub-router/router-lsa/r-bit|v6-bit. Added leaf route-policy under default-information container.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L4139)	/router/ospfv3/processes/process[process-name]/vrfs/vrf[vrf-name]/domain-id/value
- (L4178)	/router/ospfv3/processes/process[process-name]/vrfs/vrf[vrf-name]/domain-id/secondaries/secondary[type][value]/value
- (L8390)	/router/ospfv3/processes/process[process-name]/trace/sizes/size[trace-buffer-name]/trace-buffer-name

## XPaths Removed

N/A

## XPaths Modified

N/A

