## Cisco-IOS-XE-mka.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted
N/A

## XPaths Deprecated
N/A

## XPaths Modified
N/A

## XPaths Added

### Description

YANG: mka needs to add dependency to key chain

### Reason

Previously dependencies for macsec key chain was not present, Which resulted in bad cli error in rpc reply.
There was no provision to add more than one macsec cipher suite under MKA policy.

- /native/interface/TenGigabitEthernet/ios-mka:mka/ios-mka:pre-shared-key/ios-mka:key-chain/ios-mka:name
- /native/mka/ios-mka:policy/ios-mka:macsec-cipher-suite
