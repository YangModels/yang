## Cisco-IOS-XE-ospfv3


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/interface/Port-channel-subinterface/ospfv3
- native/interface/Port-channel-subinterface/ospfv3/\*

### Reason

OSPFv3 interface commands were added at the wrong location in Port-channel subinterface. Hence Obsoleted.

## XPaths Deprecated

### Description

## XPaths Modified

- native/router/ospfv3/address-family/ipv4/unicast/area-config/nssa
- native/router/ospfv3/address-family/ipv4/unicast/area-config/stub
- native/router/ospfv3/address-family/ipv4/vrf/area-config/nssa
- native/router/ospfv3/address-family/ipv4/vrf/area-config/stub
- native/router/ospfv3/address-family/ipv6/unicast/area-config/nssa
- native/router/ospfv3/address-family/ipv6/unicast/area-config/stub
- native/router/ospfv3/address-family/ipv6/vrf/area-config/nssa
- native/router/ospfv3/address-family/ipv6/vrf/area-config/stub

### Reason

Added must statement to reflect the restriction in IOS CLI. An area can't be changed from NSSA to stub directly or STUB to NSSA.

## XPaths Added

### Description
