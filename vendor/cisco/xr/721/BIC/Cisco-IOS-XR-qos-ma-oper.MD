## Cisco-IOS-XR-qos-ma-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

The previous yang path was wrong and hence the VOQ-STATS was moved inside another container service-policy-name with per-policy path, so that stats will be fetched per-policy.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1561)	/qos/nodes/node[node-name]/policy-map/shared-policy-instances/shared-policy-instance[spi-name]
- (L1562)	/qos/nodes/node[node-name]/policy-map/shared-policy-instances/shared-policy-instance[spi-name]
- (L1563)	/qos/nodes/node[node-name]/policy-map/shared-policy-instances/shared-policy-instance[spi-name]
- (L1611)	/qos/qos-global/vo-q/vo-q-statistics/vo-qinterfaces/vo-qinterface[interface-name]/output-vo-q
- (L1623)	/qos/qos-global/vo-q/vo-q-statistics/vo-qinterfaces/vo-qinterface[interface-name]/vo-q-member-interfaces/vo-q-member-interface[interface-name]/vo-qoutput

## XPaths Modified

N/A

