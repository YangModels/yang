## Cisco-IOS-XR-freqsync-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removal of the Enable item was required to for submode-enter and dependent syntax migration due to the non-unique name.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L389)	/frequency-synchronization/enable

## XPaths Modified

- (L151)	/{NODE-CFG}/clock-interface/clocks/clock[clock-type][port]/frequency-synchronization/output-quality-level/quality-level-option
- (L179)	/{NODE-CFG}/clock-interface/clocks/clock[clock-type][port]/frequency-synchronization/input-quality-level/quality-level-option
- (L266)	/interface-configurations/interface-configuration[active][interface-name]/frequency-synchronization/input-quality-level/quality-level-option
- (L294)	/interface-configurations/interface-configuration[active][interface-name]/frequency-synchronization/output-quality-level/quality-level-option

