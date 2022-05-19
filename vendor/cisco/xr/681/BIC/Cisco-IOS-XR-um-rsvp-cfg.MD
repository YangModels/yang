## Cisco-IOS-XR-um-rsvp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed Cisco-support task nodes as should not be exposed in yang model. Also it's not something that customers configure, so it will not impact their operations. Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L657)	/rsvp/interfaces/interface[interface-name]/signalling/rate-limit/rate

## XPaths Removed

- (L662)	/rsvp/interfaces/interface[interface-name]/signalling/rate-limit/interval
- (L838)	/rsvp/interfaces/interface[interface-name]/authentication/challenge
- (L913)	/rsvp/signalling/graceful-restart-recovery-time
- (L1073)	/rsvp/authentication/challenge
- (L1138)	/rsvp/neighbors/neighbor[neighbor-address]/authentication/challenge

## XPaths Modified

N/A

