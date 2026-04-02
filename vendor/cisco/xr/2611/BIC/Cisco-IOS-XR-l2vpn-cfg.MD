## Cisco-IOS-XR-l2vpn-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed evpn-usid-allocation container, Removed evpn-srv6-locators container and evpn-srv6-locator-wide-function-allocation-table container, Removed evi-srv6-locators container and evi-srv6-locator-wide-function-allocation-table container, Moved wide-function allocation leaves to new containers, Added evpn-srv6-locator container and evpn-srv6-locator-name leaf, Added evi-srv6-locator container and evi-srv6-locator-name leaf.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L2174)	/{BRIDGE-DOMAIN-TABLE}/bridge-domains/bridge-domain[name]/bridge-domain-pbb
- (L6146)	/l2vpn/pbb
- (L1175)	/{Pbbvid-range}
- (L1668)	/{Pbbisid-range}

## XPaths Modified

- (L4218)	/l2vpn/database/xconnect-groups/xconnect-group[name]/p2p-xconnects/p2p-xconnect[name]/pseudowire-evpns/pseudowire-evpn[eviid][remote-acid][source-acid]/admission-control-bandwidth
- (L4404)	/l2vpn/database/xconnect-groups/xconnect-group[name]/p2p-xconnects/p2p-xconnect[name]/pseudowire-neighbor-pseudowire-ids/{PSEUDOWIRE-CONTENT}/bandwidth
- (L4760)	/l2vpn/database/xconnect-groups/xconnect-group[name]/p2p-xconnects/p2p-xconnect[name]/pseudowire-evpn-services/pseudowire-evpn-service[eviid][service-id]/admission-control-bandwidth
- (L5814)	/l2vpn/database/vlan-switches/vlan-switch[name]/name

