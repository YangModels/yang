## YANG Models and Platform Capabilities for Cisco NX-OS 7.0(3)I5(2)

The YANG files in this directory detail the native and OpenConfig YANG models with deviations supported by NX-OS 7.0(3)I5(2) release.

As a convenience, a copy of the "hello" message is also provided (netconf-capabilities.xml).

### YANG Syntax Issues With ```top.yang```

The core native device model for NX-OS is [```top.yang```](top.yang). This model currently has a number of problems relating to non-compliant regular expresssion constraints (per RFC 6020) and incorrect default values. These issues will be fixed in a subsequent release.  Developers can examine the script [```check.sh```](../check.sh) for details of how the model is currently compiled to pass CI builds.


### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

From NX-OS 7.0.3 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs. These will be noted by running the ```check-models.sh``` script with the ```-b``` option.


### RPM Download

The RPMs supporting YANG models are available for download at the Cisco Artifactory http://devhub.cisco.com/artifactory/open-nxos-agents/7.0-3-I5-2/.


### Prerequisites and Dependencies 

#### VRRP Model 

"Feature Vrrpv3" needs to enabled on the device . 


Supported if-type (as per RFC7223): ianaift:ethernetCsmacd and ianaift:l2vlan

For the VRRP Model , user needs to install the following RPMs 
mtx-openconfig-if-ip 
mtx-openconfig-interfaces 
mtx-openconfig-vlan

#### Openconfig IF-IP Model

Supported if-type (as per RFC7223): ianaift:ethernetCsmacd and ianaift:l2vlan

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


### Caveats

Certain model implementations in NX-OS 7.0.3 have caveats that will be addressed in upcoming releases. The details of the caveats and models are below.


#### VRRP Model 

##### Secondary Virtual IP address
Support for OC Model VRRP Configuration on the device allows users to manage multiple IP addresses, including secondary IP addresses. If multiple subnets are configured on an Ethernet interface, VRRP may be configured on each subnet. This support is **not** available with the current implementation of the ```openconfig-if-ip``` model.

Via the ```openconfig-if-ip``` model user can sends more than one IP address in a single payload for a specific VR-ID.As per the Current device model impleme
ntation,it will accept the First IP as the primary IP for the specified VR-ID and ignores the rest of the IP addresses in the given payload request.

##### VRRPv3 issues with DELETE
The VRRP container is not deleted when the last IP address from the IP address list is deleted. As VRRP configuration is in the IP container, IP should send a delete to all its child configs when a delete of the IP happens. This is currently not supported with the current implementation of the ```openconfig-if-ip``` model. As a result of which when the last IP address from the IP list is getting removed from OC, VRRP configuration still remain on the box and are dangling configuration which cannot be removed via the openconfig-if-ip model unless user configures an IP address on that interface and explicitly deletes the VRRP configuration. 



##### VRRP Set/Get on a Specific IP
Via the ```openconfig-if-ip``` model user can configure **same** VR-ID under different IP addresses on the same interface. On the device side, these configurations are aggregated and put under single VR instance.
When a get or get-config via the ```openconfig-if-ip``` model is sent, the current implementation cannot return the exact configuration the user put in place.


##### VRRP advertisement-interval Range
Via the ```openconfig-if-ip``` model user can configure advertisement-interval in the range of 1-4095 centi-seconds .On the device side implementation the advertisement-interval is in the range of 10-4095 centi-seconds . Hence the advertisement-interval with less than 10 is not accepted to the device model.


#### IF-IP Model

##### Multiple IP address Support for OC Model 
The ```openconfig-if-ip``` model support multiple IPVx addresses for an interface . But we are not supporting multiple IP addresses yet.

##### IF-IP issues with DELETE
1. DELETE works only for individual addresses configured on supported interface-types (ianaift:ethernetCsmacd and ianaift:l2vlan)

2. DELETE at container level, multiple DELETE in single RPC and multiple address (IPv6) DELETE will be supported in future releases


#### Local Routing Model


##### Non-Default Vrf is not supported 
The ```openconfig-local-routing``` model support multiple VRF. Currently , we are supporting only default-vrf. 


#####  set-tag not supported, set-tag is not supposed to be part of config-container 
set-tag for ```openconfig-local-routing``` is part of config-container which implies set-tag is specific for a prefix. set-tag is specific to combination of prefix and nexthop, So set-tag cannot supported for the current version of OC.

##### Recurse for local routing not supported.

###### Additional Info: 
1. Index should combination of Interface+IP+vrf, example: eth1/1+2.2.2.2+default
2. Index for DROP (NULL 0 Interface) should be +DROP+
