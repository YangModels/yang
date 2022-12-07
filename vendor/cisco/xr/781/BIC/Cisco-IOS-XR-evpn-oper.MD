## Cisco-IOS-XR-evpn-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added Label Type and IP to internal-label and internal-id schema.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L681)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id/esi
- (L872)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label/esi

## XPaths Removed

- (L389)	{L2vpn-evpn-esi}
- (L394)	{L2vpn-evpn-esi}
- (L2271)	{L2VPN-EVPN-EAD}/ethernet-segment-identifier/entry
- (L359)	/{EVI-DETAIL}/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi1
- (L364)	/{EVI-DETAIL}/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi2
- (L369)	/{EVI-DETAIL}/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi3
- (L374)	/{EVI-DETAIL}/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi4
- (L379)	/{EVI-DETAIL}/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi5
- (L1973)	{L2VPN-EVPN-MAC}/local-ethernet-segment-identifier/entry
- (L1982)	{L2VPN-EVPN-MAC}/remote-ethernet-segment-identifier/entry
- (L3107)	{L2VPN-EVPN-IGMP}/ethernet-segment-identifier/entry
- (L538)	/{IGMP-TABLE}/igmps/igmp/esi1
- (L543)	/{IGMP-TABLE}/igmps/igmp/esi2
- (L548)	/{IGMP-TABLE}/igmps/igmp/esi3
- (L553)	/{IGMP-TABLE}/igmps/igmp/esi4
- (L558)	/{IGMP-TABLE}/igmps/igmp/esi5
- (L615)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]
- (L628)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi1
- (L633)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi2
- (L638)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi3
- (L643)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi4
- (L648)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi5
- (L653)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/ethernet-tag
- (L1636)	{L2VPN-EVPN-LABEL}/evpn-instance
- (L1357)	{L2VPN-EVPN-ES}/ethernet-segment-identifier/entry
- (L1411)	{L2VPN-EVPN-ES}/service-carving-evi-elected-result/entry
- (L1420)	{L2VPN-EVPN-ES}/service-carving-evi-not-elected-result/entry
- (L1429)	{L2VPN-EVPN-ES}/service-carving-vni-elected-result/entry
- (L1438)	{L2VPN-EVPN-ES}/service-carving-vni-not-elected-result/entry
- (L1447)	{L2VPN-EVPN-ES}/service-carving-srv6-elan-elected-result/entry
- (L1456)	{L2VPN-EVPN-ES}/service-carving-srv6-elan-not-elected-result/entry
- (L678)	/{ETHERNET-SEGMENT-TABLE}/ethernet-segments/ethernet-segment[interface-name][esi1][esi2][esi3][esi4][esi5]/esi1
- (L683)	/{ETHERNET-SEGMENT-TABLE}/ethernet-segments/ethernet-segment[interface-name][esi1][esi2][esi3][esi4][esi5]/esi2
- (L688)	/{ETHERNET-SEGMENT-TABLE}/ethernet-segments/ethernet-segment[interface-name][esi1][esi2][esi3][esi4][esi5]/esi3
- (L693)	/{ETHERNET-SEGMENT-TABLE}/ethernet-segments/ethernet-segment[interface-name][esi1][esi2][esi3][esi4][esi5]/esi4
- (L698)	/{ETHERNET-SEGMENT-TABLE}/ethernet-segments/ethernet-segment[interface-name][esi1][esi2][esi3][esi4][esi5]/esi5
- (L3147)	{L2VPN-EVPN-REMOTE-SHG}/ethernet-segment-identifier/entry
- (L743)	/{REMOTE-SHG-TABLE}/remote-shgs/remote-shg[evi][esi1][esi2][esi3][esi4][esi5]/esi1
- (L748)	/{REMOTE-SHG-TABLE}/remote-shgs/remote-shg[evi][esi1][esi2][esi3][esi4][esi5]/esi2
- (L753)	/{REMOTE-SHG-TABLE}/remote-shgs/remote-shg[evi][esi1][esi2][esi3][esi4][esi5]/esi3
- (L758)	/{REMOTE-SHG-TABLE}/remote-shgs/remote-shg[evi][esi1][esi2][esi3][esi4][esi5]/esi4
- (L763)	/{REMOTE-SHG-TABLE}/remote-shgs/remote-shg[evi][esi1][esi2][esi3][esi4][esi5]/esi5
- (L851)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]
- (L864)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi1
- (L869)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi2
- (L874)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi3
- (L879)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi4
- (L884)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/esi5
- (L889)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label[evi][encapsulation][esi1][esi2][esi3][esi4][esi5][ethernet-tag]/ethernet-tag
- (L1636)	{L2VPN-EVPN-LABEL}/evpn-instance

## XPaths Modified

- (L429)	/{EVI-DETAIL}/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery[evi][encapsulation][esi][ethernet-tag]
- (L2344)	{L2VPN-EVPN-EAD}/ethernet-segment-identifier
- (L1988)	{L2VPN-EVPN-MAC}/local-ethernet-segment-identifier
- (L1993)	{L2VPN-EVPN-MAC}/remote-ethernet-segment-identifier
- (L3154)	{L2VPN-EVPN-IGMP}/ethernet-segment-identifier
- (L675)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id/encapsulation
- (L680)	/{INTERNAL-ID-TABLE}/internal-ids/internal-id/esi
- (L708)	/{ETHERNET-SEGMENT-TABLE}/ethernet-segments/ethernet-segment[interface-name][esi]
- (L1103)	{L2VPN-EVPN-ES}/ethernet-segment-identifier
- (L755)	/{REMOTE-SHG-TABLE}/remote-shgs/remote-shg[evi][esi]
- (L3235)	{L2VPN-EVPN-REMOTE-SHG}/ethernet-segment-identifier
- (L866)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label/encapsulation
- (L871)	/{INTERNAL-LABEL-TABLE}/internal-labels/internal-label/esi

