## Cisco-IOS-XR-npu-hw-profile-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Changed the options to the enum for which the asic compatibility can be enabled.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L177)	/macsec-hw-module/fips-post-location-tables/fips-post-location-table[location-string]/fips-post-location[location-id]
- (L180)	/macsec-hw-module/fips-post-location-tables/fips-post-location-table[location-string]/fips-post-location[location-id]/location-id
- (L185)	/macsec-hw-module/fips-post-location-tables/fips-post-location-table[location-string]/fips-post-location[location-id]/enable-val
- (L207)	/macsec-hw-module/macsec-mode-location-tables/macsec-mode-location-table[location-string]/macsec-mode-location[location-id]
- (L210)	/macsec-hw-module/macsec-mode-location-tables/macsec-mode-location-table[location-string]/macsec-mode-location[location-id]/location-id
- (L215)	/macsec-hw-module/macsec-mode-location-tables/macsec-mode-location-table[location-string]/macsec-mode-location[location-id]/enable-val

## XPaths Modified

- (L205)	/macsec-hw-module/fips-post-location-tables/fips-post-location-table[location-string]/fips-post-location
- (L224)	/macsec-hw-module/macsec-mode-location-tables/macsec-mode-location-table[location-string]/macsec-mode-location
- (L414)	/npu-hw-module-profile-config/profile/l2fib/bd-flush-conv
- (L548)	/npu-hw-module-profile-config/profile/npu-compatibility

