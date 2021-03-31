## Cisco-IOS-XE-dhcp.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/ip/dhcp/pool/hardware-addr-cient-id-choice(choice)/client-identifier(case)/client-identifier
- native/ip/dhcp/pool/hardware-addr-cient-id-choice(choice)/hardware-address(case)/hardware-address
- native/ip/dhcp/pool/host/number
- native/ip/dhcp/pool/host/mask
- native/ipv6/dhcp/guard/policy/match
- native/ip/dhcp/pool/host/mask
- interface-grouping(grouping)/interface-choice(choice)/Loopback(case)/Loopback
- native/ipv6/dhcp/pool/import/domain-name

### Description

- A new must expression added
- A new when expression added
- The leaf had an implicit default
- The range '[(0, 2147483647)]' is added
- The must expression may be more constrained than before

### Reason

The conditions were moved as the existing behaviour was not correct. Some of the configs were allowed even when role was not server. So updated the must conditions and moved them under necessary container.

## XPaths Added

### Description
