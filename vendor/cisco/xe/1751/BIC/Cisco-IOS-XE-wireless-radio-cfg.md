## Cisco-IOS-XE-wireless-radio-cfg.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- radio-cfg-data/ap-specific-configs/ap-specific-config/ap-specific-slot-configs/ap-specific-slot-config/radio-params-24ghz/transmit-power-level
- radio-cfg-data/ap-specific-configs/ap-specific-config/ap-specific-slot-configs/ap-specific-slot-config/radio-params-5ghz/transmit-power-level
- st-ap-specific-config(grouping)/ap-specific-slot-configs/ap-specific-slot-config/radio-params-24ghz/transmit-power-level
- st-ap-specific-config(grouping)/ap-specific-slot-configs/ap-specific-slot-config/radio-params-5ghz/transmit-power-level
- st-ap-specific-slot-config(grouping)/radio-params-24ghz/transmit-power-level
- st-ap-specific-slot-config(grouping)/radio-params-5ghz/transmit-power-level
- st-radio-params-24ghz(grouping)/transmit-power-level
- st-radio-params-5ghz(grouping)/transmit-power-level

### Reason

The datatype of leaf "transmit-power" in openconfig was a "uint" earlier. Now the openconfig model is updated and the datatype of leaf "transmit-power" is changed to "int".
To fix this we needs tdl and cli changes

## XPaths Deprecated

### Description

## XPaths Modified

### Description

## XPaths Added

### Description
