## Cisco-IOS-XE-l2vpn.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

1. Available encapsulation types changed to just "mpls" and "l2tpv3".
2. Added "exclude" and "include" enum.
3. Changed "protocol" to "signaling protocol", removed "l2tpv2".
4. Only enable "resync" for L2TPv3, added resync threshold.

### Reason

1. "l2tpv2" and "udp" are not supported.
2. "exclude" and "include" were missing.
3. Previous syntax was incorrect and resync is not supported for MPLS

- /native/interface/pseudowire/ios-l2vpn:encapsulation
- /native/interface/pseudowire/ios-l2vpn:control-word
- /native/interface/pseudowire/ios-l2vpn:protocol-mpls/ios-l2vpn:protocol
- /native/interface/pseudowire/ios-l2vpn:protocol-l2tpv3/ios-l2vpn:protocol
- /native/interface/pseudowire/ios-l2vpn:protocol-l2tpv2/ios-l2vpn:protocol
- /native/interface/pseudowire/ios-l2vpn:sequencing

### Description

1. Changed "deprecated" to "obsolete".
2. Added template, group, and priority
3. Group name made a group object for re-use for different member types.
4. Changed service-instance from a leaf to a container.
5. Removed separate VLAN interface node.

### Reason

1. Template, group, and priority were missing.
2. Group name pertains to other member types, not just interfaces.
3. Service instance requires instance ID, can have redundancy group and priority.
4. Incorporated in interface node.

- /native/l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:group
- /native/l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:routing
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:ipv4/ios-l2vpn:mem-vcid
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:interface/ios-l2vpn:group
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:interface/ios-l2vpn:service-instance
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:Vlan

### Description

1. Changed "deprecated" to "obsolete".
2. Added template, group, and priority
3. Group name made a group object for re-use for different member types.
4. Changed service-instance from a leaf to a container.
5. Removed separate VLAN interface node.

### Reason

Template, group, and priority were missing.
Group name pertains to other member types, not just interfaces.
Service instance requires instance ID, can have redundancy group and priority.
Incorporated in interface node.

- /native/l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:group
- /native/l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:routing
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:ipv4/ios-l2vpn:mem-vcid
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:interface/ios-l2vpn:group
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:interface/ios-l2vpn:service-instance
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:Vlan


### Description

Obsoleted some leafs to make it RFC compliant

### Reason

Parent node was obsoleted previously but this child leaf node was not.

- /native/interface/pseudowire/pseudowire/protocol-mpls/protocol
- /native/interface/pseudowire/pseudowire/protocol-l2tpv2/protocol
- /native/interface/pseudowire/pseudowire/protocol-l2tpv3/protocol
- /native/l2vpn/pseudowire/group/status

### Description

Removed 'arp flooding-suppression disable', replaced with 'flooding suppression address-resolution disable'

### Reason

The original CLI was never implemented and was disabled by platform capability.  Now that the feature has been implemented, the CLI is different from originally planned.

- /native/l2vpn/evpn/arp/flooding-suppression/disable

## XPaths Deprecated

### Description

Moved commands under global l2vpn sub-mode.

### Reason

Previous syntax was incorrect.

- /native/l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:group
- /native/l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:routing

## XPaths Modified
N/A

## XPaths Added

### Description

1. Available encapsulation types changed to just "mpls" and "l2tpv3".
2. Added "exclude" and "include" enum.
3. Changed "protocol" to "signaling protocol", removed "l2tpv2".
4. Only enable "resync" for L2TPv3, added resync threshold.

### Reason

1. "l2tpv2" and "udp" are not supported.
2. "exclude" and "include" were missing.
3. Previous syntax was incorrect and resync is not supported for MPLS

- /native/interface/pseudowire/ios-l2vpn:encapsulation-config
- /native/interface/pseudowire/ios-l2vpn:control-word-config
- /native/interface/pseudowire/ios-l2vpn:signaling/ios-l2vpn:protocol/ios-l2vpn:ldp
- /native/interface/pseudowire/ios-l2vpn:signaling/ios-l2vpn:protocol/ios-l2vpn:l2tpv3/ios-l2vpn:l2tp-class-name
- /native/interface/pseudowire/ios-l2vpn:pseudowire-sequencing

### Description

1. Added template, group, and priority
2. Group name made a group object for re-use for different member types.
3. Changed service-instance from a leaf to a container.
4. Removed separate VLAN interface node.

- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:ipv4/ios-l2vpn:config-ipv4/ios-l2vpn:mem-vcid
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:interface/ios-l2vpn:config-interface/ios-l2vpn:config-interface-service-instance/ios-l2vpn:service-instance-config/ios-l2vpn:group-name
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:interface/ios-l2vpn:config-interface/ios-l2vpn:config-interface-service-instance
- /native/l2vpn/ios-l2vpn:xconnect/ios-l2vpn:context/ios-l2vpn:xc-Mode-config-xconnect/ios-l2vpn:member/ios-l2vpn:interface/ios-l2vpn:interface

### Description

Removed 'arp flooding-suppression disable', replaced with 'flooding suppression address-resolution disable'

### Reason

The original CLI was never implemented and was disabled by platform capability.  Now that the feature has been implemented, the CLI is different from originally planned.

- /native/l2vpn/evpn/flooding-suppression/address-resolution/disable

### Description

Moved commands under global l2vpn sub-mode.

### Reason

Previous syntax was incorrect.

- /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:group
- /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:pseudowire/ios-l2vpn:pseudowire-routing
