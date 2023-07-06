## Cisco-IOS-XR-um-l2-ethernet-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added must statement dot1q, dot1ad, untagged, and default. Added leaf vlan-id as must constraint to configure dot1q/second-dot1q under dot1q/dot1ad containers. And when statement has been adjusted under containers carrier-delay, encapsulation, l2transport-encapsulation, l2protocol. Also added when constraint to reflect the existing constraints, which practically does not cause impact on customer operations. Added support for 800G interface.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L164)	/{IF-BODY}/l2transport-encapsulation/dot1q
- (L744)	/{IF-BODY}/l2transport-encapsulation/dot1ad
- (L1252)	/{IF-BODY}/l2transport-encapsulation/untagged
- (L1479)	/{IF-BODY}/l2transport-encapsulation/default

## XPaths Removed

N/A

## XPaths Modified

N/A

