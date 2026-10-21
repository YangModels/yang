## Cisco-IOS-XR-um-router-bgp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Fixed Bandwidth-group AS range. Reduced the number of BMP servers supported from 8 to 4.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1632)	/{INSTANCE-AS}/{NEIGHBOR}/dmz-link-bandwidth/inheritance-disable
- (L3398)	/{INSTANCE-AS}/{ADDRESS-FAMILY}/import/re-originate
- (L4513)	/{INSTANCE-AS}/{SNGRP}/dmz-link-bandwidth/inheritance-disable
- (L5839)	/{INSTANCE-AS}/{NBRGRP}/dmz-link-bandwidth/inheritance-disable
- (L11801)	/{INSTANCE-AS}/vrfs/vrf[vrf-name]/{NEIGHBOR-VRF}/dmz-link-bandwidth/inheritance-disable
- (L15498)	/bmp/servers/server[server-number]/host/host-name
- (L15509)	/bmp/servers/server[server-number]/host/port

## XPaths Modified

- (L1194)	/{INSTANCE-AS}/{NEIGHBOR}/bmp-activate/servers/server[server-number]/server-number
- (L3572)	/{INSTANCE-AS}/{ADDRESS-FAMILY}/import/re-originate
- (L4285)	/{INSTANCE-AS}/{SNGRP}/bmp-activate/servers/server[server-number]/server-number
- (L5627)	/{INSTANCE-AS}/{NBRGRP}/bmp-activate/servers/server[server-number]/server-number
- (L11718)	/{INSTANCE-AS}/vrfs/vrf[vrf-name]/{NEIGHBOR-VRF}/bmp-activate/servers/server[server-number]/server-number
- (L15957)	/bmp/servers/server[server-number]/server-number

