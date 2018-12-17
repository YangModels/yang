## YANG Models and Platform Capabilities for Cisco NX-OS 7.0(3)I7(5a)

The YANG files in this directory detail the native and OpenConfig YANG models with deviations supported by NX-OS 7.0(3)I7(5a) release.

As a convenience, a copy of the "hello" message is also provided (netconf-capabilities.xml).

### YANG Syntax Issues With ```Cisco-NX-OS-device.yang```

The core native device model for NX-OS is [```Cisco-NX-OS-device.yang```](Cisco-NX-OS-device.yang). This model currently has a number of problems relating to non-compliant regular expresssion constraints (per RFC 6020) and incorrect default values. These issues will be fixed in a subsequent release.  Developers can examine the script [```check.sh```](../check.sh) for details of how the model is currently compiled to pass CI builds.


### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

From NX-OS 7.0.3 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs. These will be noted by running the ```check-models.sh``` script with the ```-b``` option.


### RPM Download

The RPMs supporting YANG models are available for download at the Cisco Artifactory http://devhub.cisco.com/artifactory/open-nxos-agents/7.0-3-I7-5a/.


### Prerequisites and Dependencies

#### VRRP Model

"Feature Vrrpv3" needs to enabled on the device.


Supported if-type (as per RFC7223): ianaift:ethernetCsmacd and ianaift:l2vlan

For the VRRP Model, user needs to install the following RPMs
mtx-openconfig-if-ip
mtx-openconfig-interfaces
mtx-openconfig-vlan


#### Routing Policy Model

For the Routing Policy Model , user needs to install the following RPMs
mtx-openconfig-routing-policy

#### Openconfig IF-IP Model

Supported if-type (as per RFC7223):

1. ianaift:ethernetCsmacd for Ethernet

2. ianaift:ieee8023adLag for port channel

3. ianaift:l2vlan for VLAN

For the IF-IP Model , user needs to install the following RPMs
mtx-openconfig-if-ip
mtx-openconfig-interfaces
mtx-openconfig-vlan

Following CLIs have to be manually executed on the device for the IF-IP Model to function properly

1. OC subinterface ip/ipv6 address configuration  cli "encapsulation dot1q <encap>", should be manually executed.

2. OC interface vlan ip/ipv6 interface configuration cli "feature interface-vlan,  vlan <xxx> " needs to be manually executed.

3.For port-channel interface the cli "channel-group xxx force" should be manually created on the interface.


#### Openconfig Local Routing Model

For the Local Routing Model, user needs to install the following RPMs

mtx-openconfig-local-routing


#### BGP Model

"feature bgp" needs to enabled on the device.

For the BGP Model , user needs to install the following RPMs
mtx-openconfig-bgp
mtx-openconfig-bgp-multiprotocol

Following CLIs have to be manually executed on the device for the different address-family to function properly for BGP Model

1. To enable address-family ipv4/6 labeled-unicast, cli configuration "install feature-set mpls" "feature-set mpls" and "feature mpls segment-routing" should be manually executed.

2. To enable address-family l2vpn-evpn, cli configuration "nv overlay evpn" should be manually executed. This configuration is mutually exclusive with the mpls configurations above.

### Caveats

Certain model implementations in NX-OS 7.0.3.I7 have caveats that will be addressed in upcoming releases. The details of the caveats and models are below.


#### VRRP Model

##### VRRPv3 issues with DELETE
The VRRP container is not deleted when the last IP address from the IP address list is deleted. As VRRP config is in the IP container, IP should send a delete to all its child configs when a delete of the IP happens. This is currently not supported with the current implementation of the ```openconfig-if-ip``` model.As a result of which when the last IP address from the IP list is getting removed from OC, VRRP config still remain on the box and are dangling configs which cannot be removed via the openconfig-if-ip model unless user configures an IP address on that interface and explicitly deletes the VRRP configuration.

##### VRRP Set/Get on a Specific IP
Via the ```openconfig-if-ip``` model user can configure **same** VR-ID under different IP addresses on the same interface. On the device side, these configurations are aggregated and put under single VR instance.
When a get or get-config via the ```openconfig-if-ip``` model is sent, the current implementation cannot return the exact configuration the user put in place.


#### Routing Policy Model

##### Routing Policy config issue with match-tag-set
In the ```Openconfig-routing-policy``` model, the match-tag-set is defined as leaf node where as in the Device model it is currently defined as leaf-list. Hence the Replace operation is working as append operation.

##### Routing Policy config issue with match-prefix-set
In the ```Openconfig-routing-policy``` model, the match-prefix-set is defined as leaf node where as in the Device model it is currently defined as leaf-list. Hence the Replace operation is working as append operation.

#### IF-IP Model

##### Multiple IP address Support for OC Model
The ```openconfig-if-ip``` model support multiple IPVx addresses for an interface . But we are not supporting multiple IP addresses yet.

##### IF-IP issues with DELETE
1. DELETE works only for individual addresses configured on supported interface-types (ianaift:ethernetCsmacd and ianaift:l2vlan)

#### Local Routing Model


##### Non-Default Vrf is not supported
The ```openconfig-local-routing``` model support multiple VRF. Currently , we are supporting only default-vrf.


#####  set-tag not supported, set-tag is not supposed to be part of config-container
set-tag for ```openconfig-local-routing``` is part of config-container which implies set-tag is specific for a prefix. set-tag is specific to combination of prefix and nexthop, So set-tag cannot supported for the current version of OC.

##### Recurse for local routing not supported.

###### Additional Info:
1. Index should combination of Interface+IP+vrf, example: eth1/1+2.2.2.2+default
2. Index for DROP (NULL 0 Interface) should be +DROP+

#### BGP Model

##### Non-Default Vrf is not supported
The  ```openconfig-network-instance``` model supports multiple VRFs. BGP native YANG model also supports multiple VRFs. Currently, we are supporting only default-vrf.

##### Route-map is not supported
The  ```openconfig-bgp-policy``` model supports route maps. BGP native YANG model also supports route-map. Currently, we are not supporting route-map configuration from OC.

##### Address-family l2vpn-vpls is not supported
The  ```openconfig-bgp``` model supports afi-safi l2vpn-vpls. Currently, NXOS 9k series do not support address-family l2vpn-vpls.

##### Password property not supported
The ```openconfig-bgp``` model supports /bgp/neighbors/neighbor[neighbor-address]/config/auth-password and /bgp/peer-groups/peer-group[peer-group-name]/config/auth-password.
Currently, we are not supporting these properties.

##### NetConf "Replace" configuration not fully supported for certain containers.
NetConf agent supports "Replace" configuration. "Replace" config for some OpenConfig containers, such as /bgp/global, /bgp/neighbors and /bgp/peer-groups, are not fully supported.

##### 1-to-N properties special notes
There are several "1-to-N" mappings where a single OpenConfig property under a "higher level container" is mapped to multiple Cisco Device Model properties under "lower level containers".

For example:
/bgp/global/default-route-distance/config/external-route-distance --> /System/bgp-items/inst-items/dom-items/Dom-list[name]/af-items/DomAf-list[type]/adminDist-items/eDist
Here, OpenConfig property "external-route-distance" under "global" is mapped to Device Model property "eDist" under multiple "DomAf-list".

Behavior:
Upon configuring "external-route-distance" property, the operation will be propagated to **all** "eDist" properties under all "DomAf-list".
Upon reading "external-route-distance" property, the **first** "eDist" property value found among all "DomAf-list" will be returned.

List of OpenConfig "1-to-N" properties:
/bgp/global/default-route-distance/config/external-route-distance
/bgp/global/default-route-distance/state/external-route-distance
/bgp/global/default-route-distance/config/internal-route-distance
/bgp/global/default-route-distance/state/internal-route-distance
/bgp/global/use-multiple-paths/ebgp/config/maximum-paths
/bgp/global/use-multiple-paths/ebgp/state/maximum-paths
/bgp/global/use-multiple-paths/ibgp/config/maximum-paths
/bgp/global/use-multiple-paths/ibgp/state/maximum-paths
/bgp/neighbors/neighbor[neighbor-address]/config/send-community
/bgp/neighbors/neighbor[neighbor-address]/state/send-community
/bgp/neighbors/neighbor[neighbor-address]/timers/config/minimum-advertisement-interval
/bgp/neighbors/neighbor[neighbor-address]/timers/state/minimum-advertisement-interval
/bgp/neighbors/neighbor[neighbor-address]/transport/state/local-address
/bgp/neighbors/neighbor[neighbor-address]/transport/state/local-port
/bgp/neighbors/neighbor[neighbor-address]/transport/state/remote-address
/bgp/neighbors/neighbor[neighbor-address]/transport/state/remote-port
/bgp/neighbors/neighbor[neighbor-address]/route-reflector/config/route-reflector-client
/bgp/neighbors/neighbor[neighbor-address]/route-reflector/state/route-reflector-client
/bgp/neighbors/neighbor[neighbor-address]/as-path-options/config/allow-own-as
/bgp/neighbors/neighbor[neighbor-address]/as-path-options/state/allow-own-as
/bgp/peer-groups/peer-group[peer-group-name]/config/send-community
/bgp/peer-groups/peer-group[peer-group-name]/state/send-community
/bgp/peer-groups/peer-group[peer-group-name]/timers/config/minimum-advertisement-interval
/bgp/peer-groups/peer-group[peer-group-name]/timers/state/minimum-advertisement-interval

##### N-to-1 properties special notes
There are several "N-to-1" mappings where multiple OpenConfig properties under "lower level containers" are mapped to a single Cisco Device Model property under a "higher level container".

For example:
/bgp/global/afi-safis/afi-safi[afi-safi-name]/route-selection-options/config/always-compare-med --> /System/bgp-items/inst-items/dom-items/Dom-list[name]/pathctrl-items/alwaysCompMed
Here, OpenConfig property "always-compare-med" under multiple "afi-safi" are mapped to Device Model property "alwaysCompMed" under "Dom-list[default]".

Behavior:
For "route-reflector-cluster-id" property under "peer-groups" and "neighbors", both Read and Write operations are supported.
For "Remove" and "Delete" write operations, "route-reflector-cluster-id" property will only be deleted on Cisco Device Model when the last "peer-group" and the last "neighbor" are deleted.

For all other "N-to-1" properties, we support only Read operation. Write operation can be performed at the "global" level.

List of OpenConfig "N-to-1" properties:
/bgp/global/afi-safis/afi-safi[afi-safi-name]/graceful-restart/state/enabled
/bgp/global/afi-safis/afi-safi[afi-safi-name]/route-selection-options/state/always-compare-med
/bgp/global/afi-safis/afi-safi[afi-safi-name]/route-selection-options/state/ignore-as-path-length
/bgp/global/afi-safis/afi-safi[afi-safi-name]/route-selection-options/state/external-compare-router-id
/bgp/neighbors/neighbor[neighbor-address]/route-reflector/config/route-reflector-cluster-id
/bgp/neighbors/neighbor[neighbor-address]/route-reflector/state/route-reflector-cluster-id
/bgp/neighbors/neighbor[neighbor-address]/afi-safis/afi-safi[afi-safi-name]/graceful-restart/state/enabled
/bgp/neighbors/neighbor[neighbor-address]/graceful-restart/state/enabled
/bgp/neighbors/neighbor[neighbor-address]/graceful-restart/state/restart-time
/bgp/neighbors/neighbor[neighbor-address]/graceful-restart/state/stale-routes-time
/bgp/neighbors/neighbor[neighbor-address]/graceful-restart/state/helper-only
/bgp/peer-groups/peer-group[peer-group-name]/route-reflector/config/route-reflector-cluster-id
/bgp/peer-groups/peer-group[peer-group-name]/route-reflector/state/route-reflector-cluster-id
/bgp/peer-groups/peer-group[peer-group-name]/afi-safis/afi-safi[afi-safi-name]/graceful-restart/state/enabled
/bgp/peer-groups/peer-group[peer-group-name]/graceful-restart/state/enabled
/bgp/peer-groups/peer-group[peer-group-name]/graceful-restart/state/restart-time
/bgp/peer-groups/peer-group[peer-group-name]/graceful-restart/state/stale-routes-time
/bgp/peer-groups/peer-group[peer-group-name]/graceful-restart/state/helper-only
