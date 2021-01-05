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

- (L93)	/{THRESH-BAG}/thresh-bag
- (L123)	/{ATTRIBUTES}/attributes/inv-asset-bag
- (L129)	/{ATTRIBUTES}/attributes/inv-eeprom-info
- (L135)	/{ATTRIBUTES}/attributes/inv-basic-bag
- (L141)	/{ATTRIBUTES}/attributes/env-sensor-info
- (L147)	/{ATTRIBUTES}/attributes/pwg-info
- (L157)	/{ATTRIBUTES}/attributes/threshold/major-hi
- (L163)	/{ATTRIBUTES}/attributes/threshold/critical-hi
- (L169)	/{ATTRIBUTES}/attributes/threshold/minor-lo
- (L175)	/{ATTRIBUTES}/attributes/threshold/major-lo
- (L181)	/{ATTRIBUTES}/attributes/threshold/minor-hi
- (L187)	/{ATTRIBUTES}/attributes/threshold/critical-lo
- (L153)	/{ATTRIBUTES}/attributes/threshold
- (L194)	/{ATTRIBUTES}/attributes/fru-info
- (L200)	/{ATTRIBUTES}/attributes/env-sensor-info-xml
- (L118)	/{ATTRIBUTES}/attributes
- (L312)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]/tsi10s/tsi10[name]/tsi11s/tsi11[name]
- (L307)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]/tsi10s/tsi10[name]/tsi11s
- (L303)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]/tsi10s/tsi10[name]
- (L298)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]/tsi10s
- (L294)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]
- (L289)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s
- (L285)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]
- (L280)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s
- (L276)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]
- (L271)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s
- (L267)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]
- (L262)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s
- (L258)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]
- (L253)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s
- (L249)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]
- (L244)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s
- (L240)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]
- (L235)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s
- (L231)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]
- (L226)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s
- (L222)	/{SLOT}/slot[name]/tsi1s/tsi1[name]
- (L217)	/{SLOT}/slot[name]/tsi1s
- (L213)	/{SLOT}/slot[name]
- (L426)	/inventory/racks/rack[name]/powershelf
- (L432)	/inventory/racks/rack[name]/entity
- (L438)	/inventory/racks/rack[name]/fantray
- (L422)	/inventory/racks/rack[name]
- (L417)	/inventory/racks

## XPaths Added

N/A

## XPaths Removed

- (L520)	{INVMGR-EEPROM-OPAQUE-DATA}/has-eeprom
- (L462)	/inventory/entities/entity[name]/attributes/node-id

## XPaths Modified

- (L85)	{ENVMON-THRESHOLD-INFO}/threshold-value
- (L668)	{INVMGR-EEPROM-OPAQUE-DATA}/opaque-data
- (L667)	{INVMGR-EEPROM-OPAQUE-DATA}/opaque-data
- (L555)	/inventory/entities/entity[name]/attributes/node-id

