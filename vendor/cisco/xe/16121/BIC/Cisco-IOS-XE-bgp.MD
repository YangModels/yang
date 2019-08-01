## Cisco-IOS-XE-bgp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Marked distribute-list and access-list interface as obsolete

### Reason
Access-list and distribute list can be configured without interface

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:accesslist/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface/\*
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:accesslist/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface/\*
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:accesslist/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface/\*
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:accesslist/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface/\*
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:prefix-gateway-name/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:prefix-gateway-name/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:prefix-gateway-name/ios-bgp:interface/\*
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:prefix-gateway-name/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:prefix-gateway-name/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:prefix-gateway-name/ios-bgp:interface/\*
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:prefix-gateway-name/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:prefix-gateway-name/ios-bgp:interface/\*
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:with-interface/ios-bgp:prefix-gateway-name/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:prefix-gateway-name/ios-bgp:interface
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:prefix-gateway-name/ios-bgp:interface/\*

### Description
marking interface and redistribute commands as obsolete

### Reason
The redistribute nodes are not valid in the current location in the model and the interface nodes are not mappable to the new nodes

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface/ios-bgp:ATM-subinterface/ios-bgp:ATM
- /native/router/ios-bgp:bgp/ios-bgp:address-familyios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/ios-bgp:accesslist/ios-bgp:interface/ios-bgp:ATM-subinterface/ios-bgp:ATM
- /native/router/ios-bgp:bgp/ios-bgp:address-familyios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:import/ios-bgp:vpnv4/ios-bgp:unicast
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:redistribute/ios-bgp:bgp/ios-bgp:as-no
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:redistribute/ios-bgp:bgp/ios-bgp:metric
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:redistribute/ios-bgp:bgp/ios-bgp:route-map


## XPaths Deprecated

N/A

## XPaths Modified

### Description
Must constraints added.

### Reason
certain values cause a CLI side effect (values change from '1,0' to '0,0'); must will keep db in sync

- /native/router/ios-bgp:bgp/\*/\*/ios-bgp:timers
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/\*/ios-bgp:timers
- /native/router/ios-bgp:bgp/ios-bgp:timers

### Description
Added mandatory true to inject-map exist-map leaf and must statement to advertise best-path container

### Reason
Inject map configuration must be set with exist-map name and advertise best-path container has prerequisite configurations

- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:advertise/ios-bgp:diverse-path
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:advertise/ios-bgp:diverse-path
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:advertise/ios-bgp:diverse-path
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:bgp/ios-bgp:inject-map/ios-bgp:exist-map
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv6/ios-bgp:ipv6-unicast/ios-bgp:bgp/ios-bgp:inject-map/ios-bgp:exist-map


### Description
Added must statement to neighbor slow-peer container

### Reason
Must statement added to prevent enable and disable leafs from being configured together

- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:slow-peer/ios-bgp:detection
- /native/router/ios-bgp:bgp/ios-bgp:address-family/\*/\*/ios-bgp:vrf/\*/ios-bgp:bgp/ios-bgp:slow-peer/ios-bgp:detection
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:slow-peer/ios-bgp:detection


### Description
Add must restriction to neighbor advertise diverse-path

### Reason
neighbor advertise diverse-path must be configured with route-reflector-client

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:inject-map/ios-bgp:exist-map
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:inject-map/ios-bgp:exist-map
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv6/ios-bgp:ipv6-unicast/ios-bgp:bgp/ios-bgp:recursion
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/\*/ios-bgp:unicast/ios-bgp:bgp/ios-bgp:recursion/ios-bgp:host
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/ios-bgp:unicast/ios-bgp:bgp/ios-bgp:recursion
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:recursion
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:recursion/ios-bgp:host
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:recursion
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:recursion/ios-bgp:host

### Description
Update must statement on network configurations

### Reason
pyang build failing on BGP model due to usage of compare

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-multicast
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-flowspec
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-mvpn
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/ios-bgp:ipv4-unicast
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/ios-bgp:ipv4-multicast
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/ios-bgp:ipv4-flowspec
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/ios-bgp:ipv4-sr-policy
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/ios-bgp:ipv4-mvpn
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/ios-bgp:ipv4-mdt
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:nsap/ios-bgp:nsap
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:l2vpn/ios-bgp:l2vpn-evpn
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:l2vpn/ios-bgp:l2vpn-vpls
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:rtfilter/ios-bgp:rtfilter
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:link-state/ios-bgp:link-state

### Description
Update must statement for bgp dampening suppress-time and max-suppress-time. Moved must restriction into a different container. Changed string type to leafref

### Reason
current must statement missing = case, must statement in wrong location, peer-session/peer-policy configuration dependent on template configuration

- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:inherit/ios-bgp:peer-policy/\*
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:inherit/ios-bgp:peer-policy
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-policy
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-policy
- /native/router/ios-bgp:bgp/ios-bgp:address-family/\*/\*/ios-bgp:vrf/\*/*/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-policy
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-policy
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-policy
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:inherit/ios-bgp:peer-session
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-session
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-session
- /native/router/ios-bgp:bgp/ios-bgp:address-family/\*/\*/ios-bgp:vrf/\*/*/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-session
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-session
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:neighbor/ios-bgp:inherit/ios-bgp:peer-session

### Description
- Add must statement to neighbor announce
- Add must statement to neighbor disable-connected-check
- Add must statement to neighbor local-as
- Add must statement to ttl-security

### Reason
Some neighbor configurations have prerequisite configurations

- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:announce/ios-bgp:rpki/ios-bgp:state
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:announce/ios-bgp:rpki/ios-bgp:state
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:disable-connected-check
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:disable-connected-check
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:disable-connected-check
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/ios-bgp:neighbor/ios-bgp:disable-connected-check
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:local-as/
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:local-as/
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:local-as/
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:local-as
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:ttl-security/ios-bgp:hops
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:ttl-security/ios-bgp:hops
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:ttl-security/ios-bgp:hops
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:hops


### Description
Add when statement to bgp bestpath

### Reason
bgp bespath delay only allowed when bgp bestpath enabled is true

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:nexthop/ios-bgp:trigger/ios-bgp:delay

### Description
Mandatory true added to neighbor activate, Must statement added to neighbor - must have remote-as, peer-group, or template configured

### Reason
Neighbor must be activated. Neighbor must be configured with remote-as/peer-group/template

- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:id
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:activate
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:activate
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:id


### Description
Default added to maximum-prefix.When and must statement added to local-as no-prepend and replace-as


### Reason
Maximum-prefix config has default value. Local-as configurations has restrictions on sub-configs

- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:no-prepend
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:no-prepend
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:no-prepend
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/\*/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as


### Description
Must statement added to neighbor dmzlink-bw. Must statement added to neighbor slow-peer dectection

### Reason
dmzlink-bw cannot be configured on a multihop-neighbor.Threshold cannot be configured with disable

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:maximum-prefix
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:maximum-prefix
- /native/router/ios-bgp:bgp/ios-bgp:timers/ios-bgp:bgp
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:dmzlink-bw
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:slow-peer/ios-bgp:detection
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:slow-peer/ios-bgp:detection
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:slow-peer/ios-bgp:split-update-group/ios-bgp:dynamic
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:slow-peer/ios-bgp:split-update-group/ios-bgp:dynamic

### Description
1. Must statement added to neighbor cluster-id
2. Must statement added to neighbor-next-hop-unchanged
3. Default value added to neighbor ebgp-multihop
4. Must statement added to neighbor password
5. Default value added to neighbor advertisement-interval

### Reason
1. cluster-id can only be configured for ibgp peer
2. next-hop-unchanged must be configured with ebgp-multihop
3. Neighbor password must be configured with text
4. Advertisement interval has default value of 0 for ibgp peers


- /native/router/ios-bgp:bgp/ios-bgp:bgp/ios-bgp:cluster-id
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:cluster-id
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:cluster-id
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:cluster-id
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:cluster-id
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:next-hop/ios-bgp:unchanged
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:ebgp-multihop
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:ebgp-multihop
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:ebgp-multihop
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:ebgp/ios-bgp:multihop
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:password
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:password
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:password
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:password
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:neighbor/ios-bgp:advertisement-interval
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:advertisement-interval

### Description
When statement added to neighbor maximum-prefix threshold

### Reason
Default value for threshold causes out of sync error, when statement prevents the default from existing without max-prefix-no

- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:global/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold
- /native/router/ios-bgp:bgp/ios-bgp:scope/ios-bgp:vrf/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:threshold

### Description
- Peer-group capability obsoleted under certain address-families
- Must statement added to bgp advertise best-external

### Reason
Configuration does not exist in the BGP CLI/config and revents best-external and additional-path from being configured together

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:advertise-best-external
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:bgp/ios-bgp:advertise-best-external
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv6/ios-bgp:vrf/ios-bgp:ipv6-unicast/ios-bgp:bgp/ios-bgp:advertise-best-external

### Description
1. Must statement added to path-attribute discard range
2. Must statement added to AF maximum-paths
3. Must statement added to AF maximum-prefix restart
4. Must statement added to bgp consistency-checker

### Reason
1. range requires all 3 values to be configured
2. only 1 type of maximum-path can be configured at a time
3. maximum-path restart cannot be configured with warning-only
4. consistency-checker sub-configs have restricitions

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:bgp:/ios-bgp:dampening-choice/ios-bgp:dampen/ios-bgp:dampen/ios-bgp:suppress-time
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4/ios-bgp:vrf/ios-bgp:ipv4-unicast/ios-bgp:bgp/ios-bgp:dampening/ios-bgp:dampen/ios-bgp:suppress-time
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:id
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:id
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:no-prepend
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:path-attribute/ios-bgp:discard/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:path-attribute/ios-bgp:discard/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:path-attribute/ios-bgp:discard/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:path-attribute/ios-bgp:discard/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:path-attribute/ios-bgp:treat-as-withdraw/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:path-attribute/ios-bgp:treat-as-withdraw/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:path-attribute/ios-bgp:treat-as-withdraw/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:path-attribute/ios-bgp:treat-as-withdraw/ios-bgp:range
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:maximum-paths
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:maximum-path
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:restart
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:neighbor/ios-bgp:maximum-prefix/ios-bgp:restart
- /native/router/ios-bgp:bgp/ios-bgp:bgp/ios-bgp:consistency-checker


### Description
When statement added to neighbor route-reflector-client

### Reason
route-reflector-client cannot be configured with advertise best-externa

- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:route-reflector-client

### Description
1. When statement added to peer-group route-reflector-client
2. Must statement updated for neighbor local-as dual-as
3. Range updated for ebgp-multihop
4. Must statement added for ip community-list, ip extcommunity-list and ip as-path access-list

### Reason
1. route-reflector-client cannot be configured with advertise best-external
2. neighbor local-as must statment missing case
3. ebgp-multihop 1 does not get nvgenned
4. must statement added to deal with list within a list deletion

- /native/ip/as-path/ios-bgp:access-list/ios-bgp:name
- /native/ip/ios-bgp:community-list/ios-bgp:expanded/ios-bgp:name
- /native/ip/ios-bgp:community-list/ios-bgp:standard/ios-bgp:name
- /native/ip/ios-bgp:extcommunity-list/ios-bgp:number-standard/\*/\*/ios-bgp:name
- /native/ip/ios-bgp:extcommunity-list/ios-bgp:expanded/ios-bgp:name
- /native/ip/ios-bgp:extcommunity-list/ios-bgp:standard/ios-bgp:name
- /native/ip/ios-bgp:extcommunity-list/ios-bgp:standard/\*/\*/ios-bgp:name
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:route-reflector-client
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:route-reflector-client
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:neighbor/ios-bgp:route-reflector-client
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:link-state/ios-bgp:link-state/ios-bgp:neighbor/ios-bgp:route-reflector-client
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:dmzlink-bw
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:dmzlink-bw
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/ios-bgp:bgp/ios-bgp:dmzlink-bw
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-session/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:peer-group/ios-bgp:neighbor/ios-bgp:local-as/ios-bgp:dual-as

## XPaths Added
