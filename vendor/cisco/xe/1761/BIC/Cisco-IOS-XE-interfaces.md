## Cisco-IOS-XE-interfaces


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- config-interface-grouping(grouping)/interface/\*/ip/address-choice/address/address/address-choice/fixed-case/primary/address
- config-interface-grouping(grouping)/interface/\*/ip/rip/authentication/mode

### Description

A new must statement added

### Reason

Configuring IP Address in sub-interface was giving trouble from Yang side.

- config-interface-grouping(grouping)/interface/\*/ipv6/destination-guard
- config-interface-grouping(grouping)/interface/\*/ipv6/source-guard

### Description

The presence 'destination-guard' and 'source-guard' is removed.

### Reason

Get-config not reflected properly with template configs post replace/delete

## XPaths Added

### Description
