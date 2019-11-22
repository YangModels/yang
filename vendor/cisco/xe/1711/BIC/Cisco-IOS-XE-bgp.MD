## Cisco-IOS-XE-bgp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

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

### Description
obsoleted nodes for "refresh timer" and additional-paths configuration

### Reason
previous models had incorrect ranges and had invalid nodes under address-family

- /native/router/ios-bgp:bgp/ios-bgp:bgp/ios-bgp:refresh/ios-bgp:max-eor-time/ios-bgp:refresh-disable
- /native/router/ios-bgp:bgp/ios-bgp:bgp/ios-bgp:refresh/ios-bgp:stalepath-time/ios-bgp:refresh-disable
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:bgp/ios-bgp:receive
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/\*/ios-bgp:vrf/\*/ios-bgp:bgp/ios-bgp:send
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:advertise/ios-bgp:additional-paths
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:advertise/ios-bgp:additional-paths
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:advertise/ios-bgp:diverse-path
- /native/router/ios-bgp:bgp/ios-bgp:template/ios-bgp:peer-policy/ios-bgp:advertise/ios-bgp:diverse-path
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:advertise/ios-bgp:additional-paths/ios-bgp:all
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:advertise/ios-bgp:additional-paths/ios-bgp:best
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:advertise/ios-bgp:best-external
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:advertise/ios-bgp:diverse-path/ios-bgp:backup
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv6/ios-bgp:vrf/ios-bgp:ipv6-flowspec/ios-bgp:redistribute-v6

### Description
Obsoleted child nodes whose parent node are obsoleted.

### Reason
Obsoleted child nodes to make it RFC compliant.

- /native/router/ios-bgp:bgp/ios-bgp:address-family/\*/\*/\*/\*/ios-bgp:aigp/ios-bgp:send/ios-bgp:send-options/ios-bgp:cost-community/ios-bgp:cost-community/ios-bgp:poi/ios-bgp:poi-options
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/\*/\*/\*/ios-bgp:aigp/ios-bgp:send/ios-bgp:send-options/ios-bgp:cost-community/ios-bgp:cost-community/ios-bgp:poi/ios-bgp:poi-options/ios-bgp:igp-cost
- /native/router/ios-bgp:bgp/ios-bgp:address-family/\*/\*/\*/\*/ios-bgp:aigp/ios-bgp:send/ios-bgp:send-options/ios-bgp:cost-community/ios-bgp:cost-community/ios-bgp:poi/ios-bgp:poi-options/ios-bgp:pre-bestpath
- /native/router/ios-bgp:bgp/ios-bgp:address-family/ios-bgp:no-vrf/ios-bgp:ipv4/ios-bgp:ipv4-unicast/ios-bgp:distribute-list/\*/ios-bgp:interface/ios-bgp:interface-choice

### Description


### Reason

- /native/router/ios-bgp:bgp
- /native/router/ios-bgp:bgp/ios-bgp:neighbor/ios-bgp:id
- /native/router/ios-bgp:bgp/ios-bgp:address-family/\*/\*/\*/ios-bgp:neighbor/ios-bgp:id

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

N/A
