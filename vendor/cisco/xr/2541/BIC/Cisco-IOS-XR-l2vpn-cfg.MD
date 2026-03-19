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

N/A

## XPaths Modified

- (L4486)	/l2vpn/database/xconnect-groups/xconnect-group[name]/p2p-xconnects/p2p-xconnect[name]/pseudowire-evpns/pseudowire-evpn[eviid][remote-acid][source-acid]/admission-control-bandwidth
- (L4672)	/l2vpn/database/xconnect-groups/xconnect-group[name]/p2p-xconnects/p2p-xconnect[name]/pseudowire-neighbor-pseudowire-ids/{PSEUDOWIRE-CONTENT}/bandwidth
- (L5028)	/l2vpn/database/xconnect-groups/xconnect-group[name]/p2p-xconnects/p2p-xconnect[name]/pseudowire-evpn-services/pseudowire-evpn-service[eviid][service-id]/admission-control-bandwidth

