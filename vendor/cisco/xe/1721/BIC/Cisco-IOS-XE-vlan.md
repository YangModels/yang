## Cisco-IOS-XE-vlan.yang


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

The old key ‘name’ of access-map list has been changed to new key 'name value’ (to include value)

### Reason

The model for VACL is not usable since the same model is getting overwritten and then push to the switch. The model is keyed only with the "name" of the VACL. So, both default VACLs and VACLs with same name and different sequence numbers are not working. Only the last entry in the list was programmed.

- /native/vlan/ios-vlan:access-map/ios-vlan:name

## XPaths Added

N/A
