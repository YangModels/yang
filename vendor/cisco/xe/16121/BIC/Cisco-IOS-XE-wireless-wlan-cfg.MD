## Cisco-IOS-XE-wireless-wlan-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

N/A


## XPaths Deprecated

N/A

## XPaths Modified

### Description
Added must constraints on AKM in WPA3 only WLAN

### Reason
To avoid wrong AKM configuration in WPA3 WLAN

- /wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/apf-vap-id-data/wlan-status
- /wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/wpa3-enabled
- /wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/wpa2-enabled
- /wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-psk
- /wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-psk-sha256
- /wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-ft-psk

## XPaths Added

N/A
