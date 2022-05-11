## Cisco-IOS-XR-um-vrf-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

The list node 'selective-vrf-download-location' was found duplicated with the existing yang model Cisco-IOS-XR-config-mda-cfg thus the whole subtree is now augmented to Cisco-IOS-XR-config-mda-cfg. Moved out interface augments into um-if-vrf model.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L385)	/srlg/names/name[srlg-name]
- (L520)	/srlg/interfaces/interface[interface-name]/indexes/index[index-number]/priority
- (L651)	/srlg/groups/group[group-name]/indexes/index[index-number]/priority
- (L727)	/srlg/inherit-locations/inherit-location[location-name]/indexes/index[index-number]/priority

## XPaths Removed

- (L501)	/srlg/interfaces/interface[interface-name]/indexes/index[index-number]/priority
- (L632)	/srlg/groups/group[group-name]/indexes/index[index-number]/priority
- (L708)	/srlg/inherit-locations/inherit-location[location-name]/indexes/index[index-number]/priority

## XPaths Modified

N/A

