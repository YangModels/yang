## Cisco-IOS-XR-um-router-pim-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed cisco-support task nodes which should not be exposed in yang model. Since it's not something that customers configure , so it will not impact their operations.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L678)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv4/mdt/c-multicast-routing/mdt-hello
- (L2074)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv6/mdt/c-multicast-routing/mdt-hello
- (L3152)	/router/pim/address-family/ipv4/global/maximum/packet-queue
- (L3644)	/router/pim/address-family/ipv4/mdt/c-multicast-routing/mdt-hello
- (L2963)	/router/pim/address-family/ipv4/nsf
- (L5029)	/router/pim/address-family/ipv6/global/maximum/packet-queue
- (L5401)	/router/pim/address-family/ipv6/mdt/c-multicast-routing/mdt-hello
- (L4840)	/router/pim/address-family/ipv6/nsf

## XPaths Modified

- (L1129)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv4/bsr/candidate-rps/candidate-rp[address]
- (L2472)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv6/bsr/candidate-rps/candidate-rp[address]
- (L4197)	/router/pim/address-family/ipv4/bsr/candidate-rps/candidate-rp[address]
- (L5703)	/router/pim/address-family/ipv6/bsr/candidate-rps/candidate-rp[address]

