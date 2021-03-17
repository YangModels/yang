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

- (L719)	/{TEP-TABLE}/teps/tep[tep-id]
- (L914)	{L2VPN-EVPN-ES}/msti-flush-count
- (L1434)	{L2VPN-EVPN-LABEL}/ecmp-disable
- (L2538)	{L2VPN-EVPN-SUMMARY}/cost-out
- (L2548)	{L2VPN-EVPN-SUMMARY}/holding-bundles-down
- (L143)	/{Rdas-range}

## XPaths Modified

- (L405)	/{EVI-DETAIL}/evi-detail/evi-children/route-targets/route-target/as
- (L1526)	{L2VPN-EVPN-LABEL}/preferred-nh-mode
- (L2498)	{L2VPN-EVPN-EVI-DETAIL}/preferred-nh-mode

