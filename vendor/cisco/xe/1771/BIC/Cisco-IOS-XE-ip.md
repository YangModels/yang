## Cisco-IOS-XE-ip.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

### Description

The ordered-by 'user' is added

- config-ip-grouping(grouping)/ip/name-server/no-vrf
- config-ip-grouping(grouping)/ip/name-server/vrf/server-ip-list

### Reason

To avoid sync issues and capture the ordered-by-user backward incompatible change.

### Description

The base type has changed from uint8 to enumeration

- config-ip-grouping(grouping)/ip/ssh/version
- config-ip-grouping(grouping)/ip/ssh/version

### Reason

To avoid error seen when attach global template with SSH version set to 1_

### Description

The must expression is more constrained.

- config-mvpn-mdt-grouping(grouping)/mdt/default/mpls/mldp-config/mp2mp-root-address
- config-mvpn-mdt-grouping(grouping)/mdt/default/mpls/mldp-config/p2mp
- config-vrf-definition-grouping(grouping)/vrf/definition/address-family/ipv4/mdt/default/mpls/mldp-config/mp2mp-root-address
- config-vrf-definition-grouping(grouping)/vrf/definition/address-family/ipv4/mdt/default/mpls/mldp-config/p2mp
- config-vrf-definition-grouping(grouping)/vrf/definition/address-family/ipv6/mdt/default/mpls/mldp-config/mp2mp-root-address
- config-vrf-definition-grouping(grouping)/vrf/definition/address-family/ipv6/mdt/default/mpls/mldp-config/p2mp

### Reason

To check for the non-existence of the path

## XPaths Added

### Description
