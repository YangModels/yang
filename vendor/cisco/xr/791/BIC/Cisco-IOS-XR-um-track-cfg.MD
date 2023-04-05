## Cisco-IOS-XR-um-track-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

changed /action/track-(down(or)up)/auto-recover to container to align with CLI.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L214)	/tracks/track[track-name]/type/boolean/expression/string

## XPaths Removed

- (L1954)	/tracks/track[track-name]/action/track-down/error-disable/interfaces/interface[interface-name]/auto-recover
- (L1993)	/tracks/track[track-name]/action/track-up/error-disable/interfaces/interface[interface-name]/auto-recover

## XPaths Modified

- (L1959)	/tracks/track[track-name]/action/track-down/error-disable/interfaces/interface[interface-name]/auto-recover
- (L1986)	/tracks/track[track-name]/action/track-up/error-disable/interfaces/interface[interface-name]/auto-recover

