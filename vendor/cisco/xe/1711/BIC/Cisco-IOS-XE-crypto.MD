## Cisco-IOS-XE-crypto.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Moved some of the crypto map related yang models as obsolete

### Reason
Old Models that can't be used to configure to achieve crypto map session between peers since subtree models are not as per Native Model

- /native/crypto/ios-crypto:map
- /native/crypto/ios-crypto:map-ipv6-gdoi
- /native/crypto/ios-crypto:map-client

### Description
Moved some of the crypto map client related yang models as obsolete

### Reason
Since old Models are not as per Native CLI and it is not working moved to new yang model

- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:name
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:client
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:autorization
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:list
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer/ios-crypto:address

## XPaths Deprecated

### Description
Deprecated the stand-by group node

### Reason
Since old Models are not as per Native CLI and it is not working moved to new yang model

- /native/crypto/ios-crypto:ikev2/ios-crypto:cluster/ios-crypto:standby-group
- /native/crypto/ios-crypto:ikev2/ios-crypto:cluster/ios-crypto:standby-group/ios-crypto:name

## XPaths Modified
N/A

## XPaths Added

- /native/crypto/ios-crypto:ikev2/ios-crypto:cluster-options/ios-crypto:standby-group
- /native/crypto/ios-crypto:ikev2/ios-crypto:cluster-options/ios-crypto:standby-group/ios-crypto:name
