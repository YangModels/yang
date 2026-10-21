## Cisco-IOS-XR-um-router-vrrp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Renamed lonklocal to linklocal under vrrp address and vrrp-subordinates.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L170)	/router/vrrp/interfaces/interface[interface-name]/address-family/ipv4/vrrps/vrrp[vrrp-id][version]/timer/advertisement-time-in-seconds
- (L313)	/router/vrrp/interfaces/interface[interface-name]/address-family/ipv4/vrrps/vrrp[vrrp-id][version]/text-authentication

## XPaths Removed

N/A

## XPaths Modified

- (L466)	/router/vrrp/interfaces/interface[interface-name]/address-family/ipv6/vrrps/vrrp[vrrp-id]/timer/advertisement-time-in-seconds

