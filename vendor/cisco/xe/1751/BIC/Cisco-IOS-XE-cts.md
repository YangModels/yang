## Cisco-IOS-XE-cts.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/cts/role-based/sgt-map-vrf-list/sgt-map
- native/cts/sxp/default/key-chain
- native/cts/sxp/connection/peer/ipv4-no-vrf/max-time
- native/cts/sxp/connection/peer/ipv4-with-vrf/max-time

### Description

- A new must expression added
- The must expression may be more constrained than before

### Reason

1. Added must condition to make sure node-id details deleted first and then sxp-disabled from yang side.
2. Unfortunately above bug fix created issue that we cant send both the RPC together to create operation, Hence revoked these changes under another Bug and added just tailf notations

## XPaths Added

### Description
