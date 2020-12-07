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

- (L89)	/{THRESH-BAG}/thresh-bag
- (L119)	/{ATTRIBUTES}/attributes/inv-basic-bag
- (L125)	/{ATTRIBUTES}/attributes/env-sensor-info
- (L131)	/{ATTRIBUTES}/attributes/pwg-info
- (L137)	/{ATTRIBUTES}/attributes/env-sensor-info-xml
- (L143)	/{ATTRIBUTES}/attributes/inv-asset-bag
- (L153)	/{ATTRIBUTES}/attributes/threshold/major-lo
- (L159)	/{ATTRIBUTES}/attributes/threshold/critical-hi
- (L165)	/{ATTRIBUTES}/attributes/threshold/minor-hi
- (L171)	/{ATTRIBUTES}/attributes/threshold/major-hi
- (L177)	/{ATTRIBUTES}/attributes/threshold/critical-lo
- (L183)	/{ATTRIBUTES}/attributes/threshold/minor-lo
- (L149)	/{ATTRIBUTES}/attributes/threshold
- (L190)	/{ATTRIBUTES}/attributes/fru-info
- (L196)	/{ATTRIBUTES}/attributes/inv-eeprom-info
- (L114)	/{ATTRIBUTES}/attributes
- (L303)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]/tsi10s/tsi10[name]/tsi11s
- (L299)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]/tsi10s/tsi10[name]
- (L294)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]/tsi10s
- (L290)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s/tsi9[name]
- (L285)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]/tsi9s
- (L281)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s/tsi8[name]
- (L276)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]/tsi8s
- (L272)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s/tsi7[name]
- (L267)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]/tsi7s
- (L263)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s/tsi6[name]
- (L258)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]/tsi6s
- (L254)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s/tsi5[name]
- (L249)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]/tsi5s
- (L245)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s/tsi4[name]
- (L240)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]/tsi4s
- (L236)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s/tsi3[name]
- (L231)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]/tsi3s
- (L227)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s/tsi2[name]
- (L222)	/{SLOT}/slot[name]/tsi1s/tsi1[name]/tsi2s
- (L218)	/{SLOT}/slot[name]/tsi1s/tsi1[name]
- (L213)	/{SLOT}/slot[name]/tsi1s
- (L209)	/{SLOT}/slot[name]
- (L534)	/inventory/racks/rack[name]/entity
- (L540)	/inventory/racks/rack[name]/powershelf
- (L546)	/inventory/racks/rack[name]/fantray
- (L530)	/inventory/racks/rack[name]
- (L525)	/inventory/racks

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L183)	{ENVMON-THRESHOLD-INFO}/threshold-value

