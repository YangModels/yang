## Cisco-IOS-XE-mka.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Modified

### Description
Changed the node type from container to leaf list

### Reason
There was no provision to add more than one macsec cipher suite under MKA policy.

- /native/mka/ios-mka:policy/ios-mka:macsec-cipher-suite

### Description
YANG: mka needs to add dependency to key chain

### Reason
Previously dependencies for macsec key chain was not present, Which resulted in bad cli error in rpc reply

- /native/interface/*/ios-mka:mka/ios-mka:pre-shared-key/ios-mka:key-chain/ios-mka:name


## XPaths Added

- /native/mka/ios-mka:policy/ios-mka:delay-protection
- /native/mka/ios-mka:policy/ios-mka:include-icv-indicator
- /native/mka/ios-mka:policy/ios-mka:sak-rekey
- /native/mka/ios-mka:policy/ios-mka:sak-rekey/ios-mka:interval
- /native/mka/ios-mka:policy/ios-mka:sak-rekey/ios-mka:interval/ios-mka:time
- /native/mka/ios-mka:policy/ios-mka:sak-rekey/ios-mka:on-live-peer-loss
- /native/mka/ios-mka:policy/ios-mka:use-updated-eth-header
- /native/mka/ios-mka:suppress
- /native/mka/ios-mka:suppress/ios-mka:syslogs
- /native/mka/ios-mka:suppress/ios-mka:syslogs/ios-mka:sak-rekey

## XPaths Removed

### Description
YANG: mka needs to add dependency to key chain

### Reason
There was no provision to add more than one macsec cipher suite under MKA policy.

- /native/mka/ios-mka:policy/ios-mka:macsec-cipher-suite/ios-mka:gcm-aes-128
- /native/mka/ios-mka:policy/ios-mka:macsec-cipher-suite/ios-mka:gcm-aes-256

