## Cisco-IOS-XE-ip.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsoleted nodes for backward compatibility

- /native/vrf/definition/address-family/\*/mdt/default/mpls/mldp

### Description
Obsoleting ununsed CLI nodes

### Reason
In 16.11 Native Yang Model, we do have model for following 2 IOS CLI(s),ip domain-list and ip domain-lookup.But these CLI(s) actually does not exists and was deprecated. So we just have Models with no underlying CLI(s) for them. Hence marking both these CLI as obsolete.

- /native/ip/domain-list
- /native/ip/domain-list/domain-name
- /native/ip/domain-list/vrf
- /native/ip/domain-list/vrf/domain-name
- /native/ip/domain-list/vrf/vrf-name
- /native/ip/domain-lookup
- /native/ip/domain-lookup-conf
- /native/ip/domain-lookup-conf/domain-lookup
- /native/ip/domain-lookup/nsap
- /native/ip/domain-lookup/source-interface
- /native/ip/domain-lookup/source-interface/TwentyFiveGigabitEthernet

## XPaths Deprecated

### Description
Deprecated old nodes for backward compatibility

- /native/vrf/definition/address-family/\*/mdt/auto-discovery/pim
- /native/vrf/definition/address-family/\*/mdt/overlay/use-bgp


## XPaths Modified

### Description
Added when statement in route-target option under vrf 

### Reason
IP Yang model route-target vrf option is changed to match IOSD CLI behavior as deleting rd, deletes the route-target command automatically.

- /native/vrf/definition/address-family/ipv6/route-target

## XPaths Added

### Description
New paths added for extensive model restructuring to support mVPN

- /native/vrf/definition/address-family/\*/mdt/default/mpls/mldp-config
- /native/vrf/definition/address-family/\*/mdt/auto-discovery/mldp
- /native/vrf/definition/address-family/\*/mdt/auto-discovery/pim-options
- /native/vrf/definition/address-family/\*/mdt/auto-discovery/ingress-replication
- /native/vrf/definition/address-family/\*/mdt/auto-discovery/receiver-site
- /native/vrf/definition/address-family/\*/mdt/data/ingress-replication
- /native/vrf/definition/address-family/\*/mdt/data/mpls
- /native/vrf/definition/address-family/ipv4/mdt/data/multicast/list
- /native/vrf/definition/address-family/ipv4/mdt/default/ingress-replication
- /native/vrf/definition/address-family/ipv4/mdt/default/mpls/mldp-config
- /native/vrf/definition/address-family/ipv4/mdt/direct
- /native/vrf/definition/address-family/ipv4/mdt/mdt-preference
- /native/vrf/definition/address-family/ipv4/mdt/overlay/bgp
- /native/vrf/definition/address-family/ipv4/mdt/overlay/use-bgp-config
- /native/vrf/definition/address-family/ipv4/mdt/partitioned
- /native/vrf/definition/address-family/ipv4/mdt/strict-rpf
- /native/vrf/definition/address-family/ipv6/mdt/auto-discovery
- /native/vrf/definition/address-family/ipv6/mdt/data
- /native/vrf/definition/address-family/ipv6/mdt/default
- /native/vrf/definition/address-family/ipv6/mdt/direct
- /native/vrf/definition/address-family/ipv6/mdt/log-reuse
- /native/vrf/definition/address-family/ipv6/mdt/mdt-preference
- /native/vrf/definition/address-family/ipv6/mdt/overlay
- /native/vrf/definition/address-family/ipv6/mdt/partitioned
- /native/vrf/definition/address-family/ipv6/mdt/preference
- /native/vrf/definition/address-family/ipv6/mdt/strict-rpf
