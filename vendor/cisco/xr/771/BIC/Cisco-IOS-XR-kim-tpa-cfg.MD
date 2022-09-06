## Cisco-IOS-XR-kim-tpa-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updating the model for correct key order.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L94)	/{UPDATE-SOURCE}/update-source
- (L308)	/{DEFAULT-ROUTE}/default-route
- (L332)	/{EGRESS-UPDATE-SOURCE}/interface-names/interface-name[interface-name]/egress-interface-source
- (L327)	/{EGRESS-UPDATE-SOURCE}/interface-names/interface-name[interface-name]
- (L320)	/{EGRESS-UPDATE-SOURCE}/interface-names
- (L372)	/tpa/vrf-names/vrf-name[vrf-name]/east-west-names/east-west-name[east-west-name]
- (L365)	/tpa/vrf-names/vrf-name[vrf-name]/east-west-names
- (L399)	/tpa/vrf-names/vrf-name[vrf-name]/address-family/ipv6
- (L408)	/tpa/vrf-names/vrf-name[vrf-name]/address-family/ipv4
- (L393)	/tpa/vrf-names/vrf-name[vrf-name]/address-family
- (L419)	/tpa/vrf-names/vrf-name[vrf-name]/disable
- (L361)	/tpa/vrf-names/vrf-name[vrf-name]
- (L355)	/tpa/vrf-names
- (L446)	/tpa/logging/kim/rotation-max
- (L453)	/tpa/logging/kim/file-size-max-kb
- (L441)	/tpa/logging/kim
- (L435)	/tpa/logging
- (L466)	/tpa/statistics/disable
- (L474)	/tpa/statistics/max-intf-events
- (L480)	/tpa/statistics/max-lpts-events
- (L487)	/tpa/statistics/statistics-update-frequency
- (L460)	/tpa/statistics
- (L346)	/tpa

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L136)	/{PROTECTION}/allow-entries/allow-entry-local-address[protocol][local-port][local-address]
- (L156)	/{PROTECTION}/allow-entries/allow-entry-remote-address[protocol][local-port][remote-address]
- (L176)	/{PROTECTION}/allow-entries/allow-entry-local-address-remote-address[protocol][local-port][local-address][remote-address]
- (L201)	/{PROTECTION}/allow-entries/allow-entry-interface-name[protocol][local-port][interface-name]
- (L221)	/{PROTECTION}/allow-entries/allow-entry-local-address-interface-name[protocol][local-port][local-address][interface-name]
- (L246)	/{PROTECTION}/allow-entries/allow-entry-remote-address-interface-name[protocol][local-port][remote-address][interface-name]
- (L271)	/{PROTECTION}/allow-entries/allow-entry-local-address-remote-address-interface-name[protocol][local-port][local-address][remote-address][interface-name]

