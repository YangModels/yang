## Cisco-IOS-XR-ncs4k-freqsync-cfg.yang

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

- (L361)	/frequency-synchronization/enable

## XPaths Modified

- (L137)	/interface-configurations/interface-configuration[active][interface-name]/frequency-synchronization/input-quality-level/quality-level-option
- (L165)	/interface-configurations/interface-configuration[active][interface-name]/frequency-synchronization/output-quality-level/quality-level-option
- (L261)	/clock-interface/clocks/clock[clock-name]/frequency-synchronization/input-quality-level/quality-level-option
- (L289)	/clock-interface/clocks/clock[clock-name]/frequency-synchronization/output-quality-level/quality-level-option

