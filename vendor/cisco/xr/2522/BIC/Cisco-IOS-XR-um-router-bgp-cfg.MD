## Cisco-IOS-XR-um-router-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated options for long-lived-graceful-restart.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L1767)	/{AS-COMMON}/address-families/address-family[af-name]/aggregate-addresses/aggregate-address[address][masklength]/set-tag

## XPaths Removed

- (L3692)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L3701)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L5910)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L5919)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L7965)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L7974)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L9979)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L9988)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L14250)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L14259)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L16229)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L16238)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept

## XPaths Modified

- (L3766)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L6071)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L8213)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L10314)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L14692)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L16739)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send

