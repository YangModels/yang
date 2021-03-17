## Cisco-IOS-XR-invmgr-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

leaf threshold-value changed from uint32 to int32 in order to display negative values.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L178)	/{ATTRIBUTES}/attributes/threshold/major-lo
- (L166)	/{ATTRIBUTES}/attributes/threshold/critical-hi
- (L184)	/{ATTRIBUTES}/attributes/threshold/minor-hi
- (L160)	/{ATTRIBUTES}/attributes/threshold/major-hi
- (L190)	/{ATTRIBUTES}/attributes/threshold/critical-lo
- (L172)	/{ATTRIBUTES}/attributes/threshold/minor-lo
- (L556)	/inventory/entities/entity[name]/attributes/node-id

## XPaths Modified

- (L529)	{INVMGR-EEPROM-OPAQUE-DATA}/opaque-data
- (L528)	{INVMGR-EEPROM-OPAQUE-DATA}/opaque-data
- (L522)	/inventory/entities/entity[name]/attributes/node-id

