## Cisco-IOS-XR-um-router-pim-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed cisco-support task nodes which should not be exposed in yang model. Since it's not something that customers configure , so it will not impact their operations. Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1416)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-inc-masks
- (L1441)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-source-address
- (L1455)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-inc-mask-source-address
- (L1485)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-source-address-inc-mask
- (L1515)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-inc-mask-source-inc-mask
- (L2636)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-inc-masks
- (L2661)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-source-address
- (L2675)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-inc-mask-source-address
- (L2705)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-address-source-address-inc-mask
- (L2735)	/router/pim/vrfs/vrf[vrf-name]/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[policy-name]/static-group/group-address[group-address]/group-inc-mask-source-inc-mask
- (L4552)	/router/pim/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-inc-masks
- (L4577)	/router/pim/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-source-address
- (L4591)	/router/pim/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-inc-mask-source-address
- (L4621)	/router/pim/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-source-address-inc-mask
- (L4651)	/router/pim/address-family/ipv4/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-inc-mask-source-inc-mask
- (L5973)	/router/pim/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-inc-masks
- (L5998)	/router/pim/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-source-address
- (L6012)	/router/pim/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-inc-mask-source-address
- (L6042)	/router/pim/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-address-source-address-inc-mask
- (L6072)	/router/pim/address-family/ipv6/sr-p2mp-policies/sr-p2mp-policy[sr-p2mp-policy-id]/static-group/group-address[group-address]/group-inc-mask-source-inc-mask

## XPaths Modified

N/A

