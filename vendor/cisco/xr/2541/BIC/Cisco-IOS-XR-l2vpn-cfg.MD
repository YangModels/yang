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

- (L6215)	/l2vpn/mtu-mismatch-ignore-auto-discovery

## XPaths Added

N/A

## XPaths Removed

- (L2305)	/{BRIDGE-DOMAIN-TABLE}/bridge-domains/bridge-domain[name]/bridge-domain-pbb/pbb-core/pbb-core-evis
- (L5721)	/l2vpn/pwoam-refresh
- (L6326)	/evpn/evpn-tables/evpn-instances/evpn-instance[vpn-id][encapsulation][side]/evi-ecmp-disable
- (L6558)	/evpn/evpn-tables/evpn-interfaces/evpn-interface[interface-name]/ethernet-segment/backbone-source-mac

## XPaths Modified

N/A

