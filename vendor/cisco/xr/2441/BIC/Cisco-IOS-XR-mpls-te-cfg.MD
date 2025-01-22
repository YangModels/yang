## Cisco-IOS-XR-mpls-te-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removal of leaf 'oor-recovery-duration' and add back as grouping 'OOR-RECOVERY-DURATION', the grouping is used by multiple parents.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L3318)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/protected-by-preference-level

## XPaths Removed

- (L3213)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/path-property
- (L3224)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/output-label
- (L3230)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/destination
- (L3236)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/lockdown
- (L3242)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/verbatim
- (L3248)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/pce
- (L3254)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/pce-address
- (L3260)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/igp-type
- (L3273)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/igp-area
- (L3279)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/igp-area-ip-address-id
- (L3300)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/segment-routing
- (L3306)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/sticky
- (L3292)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/protected-by-preference-level

## XPaths Modified

- (L3316)	/interface-configurations/interface-configuration[active][interface-name]/tunnel-te-attributes/path-option-protects/path-option-protect[protection]/path-options/path-option[preference-level]/protected-by-preference-level

