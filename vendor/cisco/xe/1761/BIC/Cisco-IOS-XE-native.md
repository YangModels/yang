## Cisco-IOS-XE-native.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/monitor/event-trace/atom/error/disable
- native/monitor/event-trace/atom/error/enable
- native/monitor/event-trace/atom/event/disable
- native/monitor/event-trace/atom/event/enable
- native/monitor/event-trace/atom/major/disable
- native/monitor/event-trace/atom/major/enable

### Reason

Removed support for the deprecated enable/disable keywords from the 'monitor event-trace' commands.

## XPaths Deprecated

### Description

## XPaths Modified

- native/fhrp/bfd
- native/fhrp/ssonative/vrf/definition/address-family/ipv4/mdt/default/mpls/mldp-config/mp2mp-root-address
- native/vrf/definition/address-family/ipv4/mdt/default/mpls/mldp-config/p2mp
- native/vrf/definition/address-family/ipv6/mdt/default/mpls/mldp-config/mp2mp-root-address
- native/vrf/definition/address-family/ipv6/mdt/default/mpls/mldp-config/p2mp

### Description

1. The default 'false' is illegally changed from 'true'
2. This must expression may be more constrained than before

### Reason

Get-config not reflected properly with template configs post replace/delete

## XPaths Added

### Description
