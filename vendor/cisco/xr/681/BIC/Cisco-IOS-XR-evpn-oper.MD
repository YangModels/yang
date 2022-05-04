## Cisco-IOS-XR-evpn-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated EVPN Preferred Nexthop Mode to include ECMP disable as an option.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L650)	/{TEP-TABLE}/teps/tep[tep-id]
- (L830)	{L2VPN-EVPN-ES-NH-BUFFER}/df-dont-prempt
- (L1212)	{L2VPN-EVPN-LABEL}/ecmp-disable
- (L2261)	{L2VPN-EVPN-SUMMARY}/cost-out
- (L2364)	{EVPN-IGMP-CHILD-INFO}/client-type
- (L138)	/{Rdas-range}

## XPaths Modified

- (L405)	/{EVI-DETAIL}/evi-detail/evi-children/route-targets/route-target/as
- (L1526)	{L2VPN-EVPN-LABEL}/preferred-nh-mode
- (L2503)	{L2VPN-EVPN-EVI-DETAIL}/preferred-nh-mode
- (L2748)	{EVPN-IGMP-CHILD-INFO}/fwd-info
- (L2757)	{EVPN-IGMP-CHILD-INFO}/subif-info

