## Cisco-IOS-XE-synce


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/network-clock/input-source-synce/controller
- native/network-clock/input-source-synce/controller/name
- native/network-clock/input-source-synce/controller/number
- native/network-clock/input-source-synce/controller/word

### Reason

Old model (network-clock input-source controller...) was incorrectly coded and so obsoleted it and modelled a new one.

## XPaths Deprecated

### Description

## XPaths Modified

- native/network-clock/input-source-synce
- native/network-clock/output-source/line/interface/interface-list/external
- native/network-clock/output-source/line/ptp/domain/external
- native/network-clock/output-source/system/external
- native/network-clock/participate
- native/network-clock/quality-level/ql-val-list
- native/network-clock/quality-level/ql-val-list/ptp/domain
- native/network-clock/quality-level/ql-val-list/ptp/domain-config
- native/tod-clock/input-source-synce

### Description

1. The case 'external' is removed.
2. The leaf 'domain' 
3. The leaf-list 'domain-config'
4. The container 'input-source-synce' is changed to a list

## XPaths Added

### Description
