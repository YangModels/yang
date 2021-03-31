## Cisco-IOS-XE-boot-integrity-oper


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/key/chain/tcp
- boot-integrity(grouping)
- boot-integrity-oper-data/boot-integrity
- package-signature(grouping)
- pcr-register(grouping)

### Description

1. A new Must statement added
2. The grouping 'boot-integrity is removed
3. The container 'boot-integrity' is removed
4. The grouping 'package-signature' is removed
5. The grouping 'pcr-register' is removed

### Reason

There was a design flaw in the models such that it assumed that each row in package-signature table was unique, using the name of the package as a key value. The support for the hot or cold SMU rendered this assumption to be incorrect. When applying a SMU it is possible to add multiple entries associated with the same package name. Therefore, the package-signature table was redesigned to use an index as the key value and the name was relegated to simple payload. Because the YANG is generated from tdl, this necessitated change in the other two tables: boot-integrity, par-register.

## XPaths Added

### Description
