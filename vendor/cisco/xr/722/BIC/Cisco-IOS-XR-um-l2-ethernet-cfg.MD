## Cisco-IOS-XR-um-l2-ethernet-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added leaf vlan-id as must constraint to configure dot1q/second-dot1q under dot1q/dot1ad containers. And when statement has been adjusted under containers carrier-delay, encapsulation, l2transport-encapsulation, l2protocol.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L107)	/{IF-BODY}/encapsulation/dot1q/second-dot1q
- (L132)	/{IF-BODY}/encapsulation/dot1ad/dot1q

## XPaths Removed

N/A

## XPaths Modified

- (L65)	/{IF-BODY}/carrier-delay
- (L82)	/{IF-BODY}/encapsulation
- (L139)	/{IF-BODY}/l2transport-encapsulation
- (L1935)	/{L2TRANS-BODY}/l2protocol

