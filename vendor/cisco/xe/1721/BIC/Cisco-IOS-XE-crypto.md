## Cisco-IOS-XE-crypto.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

Obsoleted the nodes that cannot be use to configure the model.

### Reason

Old Models that can't be used to configure to achieve crypto map session between peers since subtree models are not as per Native Model

- /native/crypto/ios-crypto:crypto-map/native/crypto/ios-crypto:crypto-map/*/native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:peer-container
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:peer-container/ios-crypto:default
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:peer-container/ios-crypto:peer
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:aaa/ios-crypto:attribute/ios-crypto:aaa-attribute-list
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:set/ios-crypto:interface/ios-crypto:interface-name-list/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:ikev2/ios-crypto:client/ios-crypto:flexvpn/ios-crypto:client/ios-crypto:inside/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:ikev2/ios-crypto:client/ios-crypto:flexvpn/ios-crypto:source/ios-crypto:interface-name/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:ikev2/ios-crypto:profile/ios-crypto:config-exchange/ios-crypto:request
- /native/crypto/ios-crypto:ikev2/ios-crypto:profile/ios-crypto:match/ios-crypto:address/ios-crypto:local/ios-crypto:interface-options/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:default/ios-crypto:set/ios-crypto:group
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:group
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer/ios-crypto:address
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer/ios-crypto:default
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer/ios-crypto:dynamic
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:access-restrict-option/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:local-address/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:match/ios-crypto:identity/ios-crypto:host/ios-crypto:domain-match
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:match/ios-crypto:identity/ios-crypto:host/ios-crypto:domain-match/ios-crypto:domain
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:match/ios-crypto:identity/ios-crypto:host/ios-crypto:domain-match/ios-crypto:vrf
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:match/ios-crypto:identity/ios-crypto:host/ios-crypto:domain-name
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:match/ios-crypto:identity/ios-crypto:host/ios-crypto:domain-name/ios-crypto:name
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:match/ios-crypto:identity/ios-crypto:host/ios-crypto:domain-name/ios-crypto:vrf
- /native/crypto/ios-crypto:key/ios-crypto:export
- /native/crypto/ios-crypto:key/ios-crypto:generate
- /native/crypto/ios-crypto:key/ios-crypto:import
- /native/crypto/ios-crypto:key/ios-crypto:move
- /native/crypto/ios-crypto:key/ios-crypto:zeroize
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:local-address/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:keyring/ios-crypto:local-address/ios-crypto:TwentyFiveGigabitEthernet/native/crypto/ios-crypto:map-client/native/crypto/ios-crypto:map-client/*/native/crypto/ios-crypto:map-ipv6-gdoi/native/crypto/ios-crypto:map-ipv6-gdoi/*/native/crypto/ios-crypto:map/ios-crypto:ipv6/ios-crypto:map-local/ios-crypto:map/ios-crypto:local-address/ios-crypto:TwentyFiveGigabitEthernet
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:autorization
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:client
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:list
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:autorization/ios-crypto:name
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:configuration-respond/ios-crypto:client
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:configuration-respond/ios-crypto:name
- /native/crypto/ios-crypto:map/ios-crypto:map-local/ios-crypto:map/ios-crypto:local-address/ios-crypto:TwentyFiveGigabitEthernet
- /native/interface/Tunnel/ios-tun:tunnel/ios-tun:protection/ios-crypto:ipsec/ios-crypto:local-address/ios-crypto:TwentyFiveGigabitEthernet
- /native/interface/Virtual-Template/ios-tun:tunnel/ios-tun:protection/ios-crypto:ipsec/ios-crypto:local-address/ios-crypto:TwentyFiveGigabitEthernet/native/key/ios-crypto:chain/ios-crypto:key/native/key/ios-crypto:chain/ios-crypto:key/*


## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

N/A
