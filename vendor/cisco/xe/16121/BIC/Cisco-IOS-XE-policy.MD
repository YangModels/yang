## Cisco-IOS-XE-policy.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Modified

### Description
Add parameter default account-on-resolution under policy-map type performance-monitor

### Reason
Account-on-resolution can be configured

- /native/policy/ios-policy:policy-map/ios-policy:parameter/ios-policy:default/ios-policy:account-on-resolution
- /native/policy/ios-policy:policy-map/ios-policy:parameter/ios-policy:default/ios-policy:flow-stickness

### Description
Must constraints are added

### Reason
In QoS Policy map, Few combination of action configurations are not allowed in IOS CLI.

- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:conform-drop/ios-policy:conform-action/ios-policy:drop
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-dscp/ios-policy:exceed-action/ios-policy:dscp
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-clp-transmit/ios-policy:exceed-action/ios-policy:set-clp-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-cos-transmit/ios-policy:exceed-action/ios-policy:set-cos-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-discard-class-transmit/ios-policy:exceed-action/ios-policy:set-discard-class-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-dscp-transmit-table/ios-policy:exceed-action/ios-policy:set-dscp-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-frde-transmit/ios-policy:exceed-action/ios-policy:set-frde-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-mpls-exp-imposition-transmit/ios-policy:exceed-action/ios-policy:set-mpls-exp-imposition-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-mpls-exp-topmost-transmit/ios-policy:exceed-action/ios-policy:set-mpls-exp-topmost-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-prec-transmit/ios-policy:exceed-action/ios-policy:set-prec-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-set-qos-transmit/ios-policy:exceed-action/ios-policy:set-qos-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-transmit/ios-policy:exceed-action/ios-policy:transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:exceed-drop/ios-policy:exceed-action/ios-policy:drop
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:violate-set-clp-transmit/ios-policy:violate-action/ios-policy:set-clp-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:violate-set-cos-transmit/ios-policy:violate-action/ios-policy:set-cos-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:violate-set-dscp-transmit/ios-policy:violate-action/ios-policy:set-dscp-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:violate-set-prec-transmit/ios-policy:violate-action/ios-policy:set-prec-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:violate-transmit/ios-policy:violate-action/ios-policy:transmit

### Description
Added Must constraints to restrict the invalid combination of configurations in model.

### Reason
QoS policy-map commands has many configurations which are not supported if they are configured at the same time under them. Added must statements to handle these restrictions in the model level

- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:conform-set-clp-transmit/ios-policy:conform-action/ios-policy:set-clp-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:conform-set-cos-transmit/ios-policy:conform-action/ios-policy:set-cos-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:conform-set-dscp-transmit/ios-policy:conform-action/ios-policy:set-dscp-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:conform-set-prec-transmit/ios-policy:conform-action/ios-policy:set-prec-transmit
- /native/policy/ios-policy:policy-map/ios-policy:class/ios-policy:action-list/ios-policy:police-rate-unit/ios-policy:police/ios-policy:rate/ios-policy:actions/ios-policy:conform-transmit/ios-policy:conform-action/ios-policy:transmit

### Description
Must statements added

### Reason
Enforce correct policy type checks in the model

- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:input 
- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:output
- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:type/ios-policy:access-control/ios-policy:input
- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:type/ios-policy:access-control/ios-policy:output
- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:type/ios-policy:packet-service/ios-policy:input
- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:type/ios-policy:packet-service/ios-policy:output
- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:type/ios-policy:performance-monitor/ios-policy:input
- /native/interface/FortyGigabitEthernet/ios-policy:service-policy/ios-policy:type/ios-policy:performance-monitor/ios-policy:output

### Description
Add parameter default account-on-resolution under policy-map type performance-monitor

### Reason
account-on-resolution can be configured

- /native/policy/ios-policy:policy-map/ios-policy:parameter/ios-policy:default/ios-policy:account-on-resolution
- /native/policy/ios-policy:policy-map/ios-policy:parameter/ios-policy:default/ios-policy:flow-stickness

## XPaths Added

N/A
