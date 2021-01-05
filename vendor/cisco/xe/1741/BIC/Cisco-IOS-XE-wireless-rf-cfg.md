## Cisco-IOS-XE-wireless-rf-cfg.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- /rf-cfg-data/rf-profile-default-entries/rf-profile-default-entry/client-reset-threshold
- /rf-cfg-data/rf-profile-default-entries/rf-profile-default-entry/client-select-threshold
- /rf-cfg-data/rf-profile-default-entries/rf-profile-default-entry/tx-power-max
- /rf-cfg-data/rf-profile-default-entries/rf-profile-default-entry/tx-power-min
- /rf-cfg-data/rf-profiles/rf-profile/client-reset-threshold
- /rf-cfg-data/rf-profiles/rf-profile/client-select-threshold
- /rf-cfg-data/rf-profiles/rf-profile/tx-power-max
- /rf-cfg-data/rf-profiles/rf-profile/tx-power-min

### Description

A new must expression added.

### Reason

Added validations in code ( green validation and validation in yang model) for the below configurations

1. Client select threshold must be greater than client reset threshold

2. Tx power max must be greater then Tx power min

## XPaths Added

### Description
