## Cisco-IOS-XR-qos-ma-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

The units of total-drop-rate which should be kbits/sec, has been marked as bytes. Similar issues were seen with a few other Yang variables. The values and descriptions of such variables are modified accordingly.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L336)	/{CAC-STATS-ST}/admitpackets
- (L380)	/{IPHC-STATS-ST}/non-tcp-bytes-sent-rate
- (L851)	/{GEN-STATS-ST}/transmit-packets
- (L863)	/{GEN-STATS-ST}/total-drop-packets
- (L875)	/{GEN-STATS-ST}/total-drop-rate
- (L1561)	/qos/nodes/node[node-name]/policy-map/shared-policy-instances/shared-policy-instance[spi-name]
- (L1562)	/qos/nodes/node[node-name]/policy-map/shared-policy-instances/shared-policy-instance[spi-name]
- (L1563)	/qos/nodes/node[node-name]/policy-map/shared-policy-instances/shared-policy-instance[spi-name]
- (L1611)	/qos/qos-global/vo-q/vo-q-statistics/vo-qinterfaces/vo-qinterface[interface-name]/output-vo-q
- (L1623)	/qos/qos-global/vo-q/vo-q-statistics/vo-qinterfaces/vo-qinterface[interface-name]/vo-q-member-interfaces/vo-q-member-interface[interface-name]/vo-qoutput

## XPaths Modified

N/A

