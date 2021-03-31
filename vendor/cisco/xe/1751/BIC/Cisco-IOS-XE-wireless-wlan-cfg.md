## Cisco-IOS-XE-wireless-- wlan-cfg.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- st-wlan-policies(grouping)/wlan-switching-policy/central-assoc-enable
- wlan-cfg-data/wlan-policies/wlan-policy/wlan-switching-policy/central-assoc-enable
- wlan-switching-policy(grouping)/central-assoc-enable

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- st-wlan-local-profiling-policy(grouping)/subscriber-policy-name
- st-wlan-policies(grouping)/wlan-local-profiling/subscriber-policy-name
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/apf-vap-id-data/wlan-status
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-dot1x-sha256
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-ft-dot1x
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-ft-psk
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-psk
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-psk-sha256
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/ft-mode
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/webauth-on-mac-auth-failure
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/webauth-on-mac-auth-failure
- wlan-cfg-data/wlan-policies/wlan-policy/wlan-local-profiling/subscriber-policy-name
- wlan-data-config-file(grouping)/wlan-status
- wlan-profile(grouping)/apf-vap-id-data/wlan-status
- wlan-profile(grouping)/auth-key-mgmt-dot1x-sha256
- wlan-profile(grouping)/auth-key-mgmt-ft-dot1x
- wlan-profile(grouping)/auth-key-mgmt-ft-psk
- wlan-profile(grouping)/auth-key-mgmt-psk
- wlan-profile(grouping)/auth-key-mgmt-psk-sha256
- wlan-profile(grouping)/ft-mode
- wlan-profile(grouping)/webauth-on-mac-auth-failure
- wlan-profile(grouping)/webauth-on-mac-auth-failure
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/mpsk-enable
- wlan-profile(grouping)/mpsk-enable
- st-wlan-policies(grouping)/policy-profile-name
- wlan-profile(grouping)/profile-name

### Description

1. a new pattern expression '[!-~]([ -~]*[!-~])?' cannot be added
2. a new must expression cannot be added
3. this must expression may be more constrained than before

### Reason

Reverting green checks introduced with because they are causing WLAN config change issues during upgrade

## XPaths Added

### Description
