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

- (L3675)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L3684)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L5893)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L5902)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L7948)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L7957)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L9962)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L9971)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L14226)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L14235)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L16205)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L16214)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/accept
- (L18542)	/bmp/servers/all/route-monitoring/policy

## XPaths Modified

- (L3766)	/{AS-COMMON}/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L6071)	/{AS-COMMON}/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L8213)	/{AS-COMMON}/af-groups/af-group[af-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L10314)	/{AS-COMMON}/neighbor-groups/neighbor-group[neighbor-group-name]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L14692)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor[neighbor-address]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send
- (L16739)	/{AS-COMMON}/vrfs/vrf[vrf-name]/neighbors/neighbor-range[neighbor-address][prefix-length]/address-families/address-family[af-name]/long-lived-graceful-restart/stale-time/send

