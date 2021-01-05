## Cisco-IOS-XR-um-router-ospfv3-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Moved out translate node from under nssa into its own node due to sysdb incompat ibilities. Removed container include-stub from stub-router/router-lsa/r-bit|v6-bit.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L231)	/router/ospfv3/processes/process[process-name]/areas/area[area-id]/nssa/translate
- (L3579)	/router/ospfv3/processes/process[process-name]/stub-router/router-lsa/r-bit/include-stub
- (L3645)	/router/ospfv3/processes/process[process-name]/stub-router/router-lsa/v6-bit/include-stub
- (L4146)	/router/ospfv3/processes/process[process-name]/vrfs/vrf[vrf-name]/areas/area[area-id]/nssa/translate
- (L7712)	/router/ospfv3/processes/process[process-name]/vrfs/vrf[vrf-name]/stub-router/router-lsa/r-bit/include-stub

## XPaths Modified

N/A

