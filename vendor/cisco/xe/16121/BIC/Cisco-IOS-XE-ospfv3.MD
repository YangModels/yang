## Cisco-IOS-XE-ospfv3.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsoleting the few leafs which are not having corresponding IOS CLI.

### Reason
Earlier, ospf and ospfv3 had common groupings which led to lot of extra content for ospfv3. So separated the groupings and removed the ospfv2 dependency by obsoleting not required nodes.

- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:traffic-share
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:traffic-share/\*
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:ttl-security
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:ttl-security/\*
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:traffic-share
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:traffic-share/*
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:ttl-security
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:ttl-security/*
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:application/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:bgp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:connected/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:isis/ios-ospfv3:isis-area/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:isis/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:iso-igrp/ios-ospfv3:iso-igrp-container/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:lisp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:mobile/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:odr/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:omp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospf/ios-ospfv3:match/ios-ospfv3:internal/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospf/ios-ospfv3:match/ios-ospfv3:external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospf/ios-ospfv3:match/*-external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospf/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospfv3/ios-ospfv3:match/ios-ospfv3:internal/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospfv3/ios-ospfv3:match/ios-ospfv3:external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospfv3/ios-ospfv3:match/*-external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:ospfv3/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:rip/ios-ospfv3:id
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:rip/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:static/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:application/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:bgp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:connected/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:eigrp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:isis/ios-ospfv3:isis-area/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:isis/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:iso-igrp/ios-ospfv3:iso-igrp-container/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:lisp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:mobile/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:odr/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:omp/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospf/ios-ospfv3:match/ios-ospfv3:internal/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospf/ios-ospfv3:match/ios-ospfv3:external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospf/ios-ospfv3:match/*-external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospf/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospfv3/ios-ospfv3:match/ios-ospfv3:internal/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospfv3/ios-ospfv3:match/ios-ospfv3:external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospfv3/ios-ospfv3:match/*-external/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:ospfv3/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:rip/ios-ospfv3:id
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:rip/ios-ospfv3:redist-options/ios-ospfv3:subnets
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/*/*/ios-ospfv3:static/ios-ospfv3:redist-options/ios-ospfv3:subnets


## XPaths Deprecated

### Description
Deprecated unsupported nodes

### Reason
Few commands under ospfv3 address family ipv4 not working

- /native/interface/GigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:authentication
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:default-information-originate/ios-ospfv3:no-ext-capability
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:no-ext-capability
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:area/\*/ios-ospfv3:default-information-originate/ios-ospfv3:no-ext-capability
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:area/\*/ios-ospfv3:no-ext-capability
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:default-information-originate/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:lisp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:nat-route/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:rip/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:global/ios-ospfv3:eigrp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:global/ios-ospfv3:lisp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:global/ios-ospfv3:nat-route/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:global/ios-ospfv3:rip/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:non-global-vrf/ios-ospfv3:eigrp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:non-global-vrf/ios-ospfv3:lisp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:non-global-vrf/ios-ospfv3:nat-route/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/ios-ospfv3:non-global-vrf/ios-ospfv3:rip/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:default-information-originate/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:application/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:lisp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:nat-route/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:default-information-originate/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:area/*/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:application/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:lisp/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:nat-route/ios-ospfv3:redist-options/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:area/\*/ios-ospfv3:default-information-originate/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:area/\*/ios-ospfv3:nssa-only
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp/*
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:vrf/*/ios-ospfv3:isis/ios-ospfv3:isis-area


## XPaths Modified

### Description
Added deviations for type changes and removing max-elements constraints

### Reason
To make the model backward compatible, deviations were added

- /native/router/ospfv3/address-family/\*/*/compatible/rfc1583
- /native/router/ospfv3/address-family/\*/*/compatible/rfc1587
- /native/router/ospfv3/address-family/\*/*/compatible/rfc5243

### Description
New Range value added

## Reason
Range value set earlier were incorrect.

- /native/interface/\*/ios-ospfv3:ospfv3/ios-ospfv3:encryption/ios-ospfv3:ipsec/ios-ospfv3:spi
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:max-lsa/ios-ospfv3:ignore-count
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/ios-ospfv3:max-lsa/ios-ospfv3:ignore-count
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:max-lsa/ios-ospfv3:ignore-time
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/ios-ospfv3:max-lsa/ios-ospfv3:ignore-time
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:max-lsa/ios-ospfv3:reset-time
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:max-lsa/ios-ospfv3:reset-time
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3:lsa/ios-ospfv3:all/ios-ospfv3:min-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3:lsa/ios-ospfv3:all/ios-ospfv3:min-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3:lsa/ios-ospfv3:all/ios-ospfv3:max-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3:lsa/ios-ospfv3:all/ios-ospfv3:max-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3:spf/ios-ospfv3:delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3-spf/ios-ospfv3:delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3:spf/ios-ospfv3:min-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3-spf/ios-ospfv3:min-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3:spf/ios-ospfv3:max-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:timers/ios-ospfv3:throttle/ios-ospfv3-spf/ios-ospfv3:max-delay
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:manetios-ospfv3:peering/ios-ospfv3:selective/ios-ospfv3:redundancy
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3-address-family/\*/*/ios-ospfv3:manetios-ospfv3:peering/ios-ospfv3:selective/ios-ospfv3:redundancy
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:graceful-restart/ios-ospfv3:restart-interval
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3-address-family/\*/*/ios-ospfv3:graceful-restart/ios-ospfv3:restart-interval


## XPaths Added

### Description/Reason
Deprecated and added new containers as there are issue with old containers


- /native/interface/GigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:authentication-config
- /native/interface/GigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:authentication-config/\*
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp-config
- /native/router/ios-ospfv3:ospfv3/ios-ospfv3:address-family/\*/*/ios-ospfv3:redistribute/ios-ospfv3:eigrp-config/\*
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:authentication-config
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:authentication-config/\*
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:encryption-config
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:encryption-config/\*
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:manet/ios-ospfv3:peering/ios-ospfv3:link-metrics-config
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:manet/ios-ospfv3:peering/ios-ospfv3:link-metrics-config/\*
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:network-type
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:network-type/\*
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:process-id/\*/ios-ospfv3:manet/ios-ospfv3:peering/ios-ospfv3:link-metrics-config
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:process-id/\*/ios-ospfv3:manet/ios-ospfv3:peering/ios-ospfv3:link-metrics-config/\*
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:process-id/\*/ios-ospfv3:network-type
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:process-id/\*/ios-ospfv3:network-type/\*
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:process-id/ios-ospfv3:network-type
- /native/interface/AppGigabitEthernet/ios-ospfv3:ospfv3/ios-ospfv3:process-id/ios-ospfv3:network-type/\*
- /native/interface/AppGigabitEthernet/ipv6/ios-ospfv3:ospf
- /native/interface/AppGigabitEthernet/ipv6/ios-ospfv3:ospf/\*
- /native/interface/\*/ios-ospfv3:ospfv3

