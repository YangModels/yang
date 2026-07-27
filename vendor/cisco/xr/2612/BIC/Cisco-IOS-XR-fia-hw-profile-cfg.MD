## Cisco-IOS-XR-fia-hw-profile-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Old SRV6 leaf no more supported and replaced by new SRv6 and Mode leaves.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L2197)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf1
- (L2204)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf2
- (L2211)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf3
- (L2218)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf4
- (L2225)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf5
- (L2232)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf6
- (L2239)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf7
- (L2246)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-default/ipv6-acl-default-table/udf8
- (L2337)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf1
- (L2344)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf2
- (L2351)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf3
- (L2358)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf4
- (L2365)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf5
- (L2372)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf6
- (L2379)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf7
- (L2386)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-default/ipv4-acl-default-table/udf8
- (L2477)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf1
- (L2484)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf2
- (L2491)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf3
- (L2498)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf4
- (L2505)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf5
- (L2512)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf6
- (L2519)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf7
- (L2526)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv6-acl-tables/ipv6-acl-table[location-string]/udf8
- (L2622)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf1
- (L2629)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf2
- (L2636)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf3
- (L2643)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf4
- (L2650)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf5
- (L2657)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf6
- (L2664)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf7
- (L2671)	/hw-module-profile-config-tcam/profile-tcam/profile-tcam-key/key-format/key-format-acl-table/ipv4-acl-tables/ipv4-acl-table[location-string]/udf8

## XPaths Removed

N/A

## XPaths Modified

N/A

