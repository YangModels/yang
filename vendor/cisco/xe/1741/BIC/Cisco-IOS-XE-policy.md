## Cisco-IOS-XE-policy.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- /native/parameter-map/type/webauth/name
- /native/parameter-map/type/webauth/type
- /native/parameter-map/type/webauth-global/webauth/global/consent/email
- /native/parameter-map/type/webauth-global/webauth/global/type
- /native/policy/policy-map/class/action-list/action-param/set-case/set/ipv4/ipv4-choice/set-vrf/vrf/vrf-name
- /native/policy/policy-map/class/action-list/action-param/set-case/set/ipv6/ipv6-choice/set-vrf/vrf/vrf-name

### Description

A new must expression added.

### Reason

The new CLI "verify-availability" is conflict with the old CLI. So add a "must not" on the old CLI.

### Description

The base type has illegally changed from uint16 to uint32

- /config-policy-map-grouping/policy-map/class/action-list/action-param/bandwidth-case/bandwidth/remaining/ratio

### Description

The range has been illegally restricted (RFC 6020: 10, p5, bullet 3)

- /config-parameter-map-type-webauth-global-grouping/webauth-global/webauth/global/sleeping-client/timeout

## XPaths Added

### Description
