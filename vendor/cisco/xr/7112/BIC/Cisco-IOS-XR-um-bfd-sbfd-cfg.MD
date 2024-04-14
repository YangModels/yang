## Cisco-IOS-XR-um-bfd-sbfd-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L130)	/bfd/echo/ipv4/bundle-per-member/minimum-interval/preferred-minimum-interval
- (L120)	/bfd/echo/ipv4/source
- (L160)	/bfd/multipath/include
- (L299)	/bfd/bundle/coexistence/bob-blb/inherit
- (L305)	/bfd/bundle/coexistence/bob-blb/logical
- (L339)	/bfd/interfaces/interface[interface-name]/echo/ipv4/source
- (L421)	/sbfd/local-discriminator/local-discriminators
- (L440)	/sbfd/local-discriminator/ip-addresses
- (L496)	/sbfd/remote-target/ipv4s/ipv4[address]/remote-discriminators/remote-discriminator[remote-discriminator-value]/remote-discriminator-value
- (L484)	/sbfd/remote-target/ipv4s/ipv4[address]/address
- (L529)	/sbfd/remote-target/ipv6s/ipv6[address]/remote-discriminators/remote-discriminator[remote-discriminator-value]/remote-discriminator-value
- (L517)	/sbfd/remote-target/ipv6s/ipv6[address]/address

## XPaths Modified

- (L58)	/bfd/echo/ipv4/bundle-per-member/minimum-interval
- (L69)	/bfd/echo/ipv4/source
- (L86)	/bfd/echo/startup/validate/force
- (L123)	/bfd/echo/disable
- (L135)	/bfd/trap/singlehop/pre-mapped
- (L214)	/bfd/dampening/bundle-member/l3-only-mode
- (L220)	/bfd/dampening/disable
- (L228)	/bfd/dampening/extensions/down-monitoring
- (L281)	/bfd/bundle/coexistence/bob-blb
- (L305)	/bfd/ipv6/checksum/disable
- (L330)	/bfd/interfaces/interface[interface-name]/echo/ipv4/source
- (L340)	/bfd/interfaces/interface[interface-name]/echo/disable
- (L364)	/bfd/interfaces/interface[interface-name]/ipv6/checksum/disable
- (L371)	/bfd/interfaces/interface[interface-name]/disable
- (L453)	/sbfd/local-discriminator/dynamic
- (L504)	/sbfd/remote-target/ipv4s/ipv4[ipv4-address]
- (L484)	/sbfd/remote-target/{REMOTE-DISCRIMINATORS}/remote-discriminators/remote-discriminator[remote-discriminator-number]
- (L519)	/sbfd/remote-target/ipv6s/ipv6[ipv6-address]
- (L484)	/sbfd/remote-target/{REMOTE-DISCRIMINATORS}/remote-discriminators/remote-discriminator[remote-discriminator-number]

