## Cisco-IOS-XE-l2vpn


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/interface/pseudowire/pseudowire-sequencing/sequencing-option/resync-case(case)/resync
- native/l2vpn/pseudowire/tlv/template/tlv
- native/l2vpn/pseudowire/tlv/template/tlv/tlv-description
- native/l2vpn/pseudowire/tlv/template/tlv/tlv-description/description
- native/l2vpn/pseudowire/tlv/template/tlv/tlv-type
- native/l2vpn/pseudowire/tlv/template/tlv/tlv-type/type
- native/l2vpn/xconnect/context/xc-Mode-config-xconnect/redundancy/delay
- native/l2vpn/xconnect/context/xc-Mode-config-xconnect/remote/circuit/id
- native/l2vpn/xconnect/context/xc-Mode-config-xconnect/remote/link/failure

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/interface/pseudowire/bandwidth
- native/interface/pseudowire/label
- native/interface/pseudowire/neighbor
- native/interface/pseudowire/preferred-path/interface
- native/interface/pseudowire/preferred-path/peer-container
- native/interface/pseudowire/signaling/protocol/protocol-options/l2tpv3-case(case)/l2tpv3/l2tp-class-name
- native/l2vpn/vfi/context/autodiscovery/bgp/signaling/bgp
- native/l2vpn/vfi/context/autodiscovery/bgp/signaling/ldp
- native/l2vpn-config/l2vpn/pseudowire/pseudowire-routing/routing/switching-point/vcid
- interface-grouping(grouping)/interface-choice/Loopback(case)/Loopback
- native/interface/pseudowire/ip
- native/interface/pseudowire/mtu
- native/interface/pseudowire/preferred-path

### Description

1. New must expression added
2. New when expression added
3. The range '[(0, 2147483647)]' is illegally added
4. The when expression may be different than before

### Reason

"container send" was by mistakenly removed and changed to "leaf send". Since this is not yet released to customer, hence the changes are reverted.

## XPaths Added

### Description
