## Cisco-IOS-XE-crypto.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Updated backward compatibility support for some of the IPSec, IKE CLIs which had backward incompatibility issue

### Reason
As per Yang Police guidelines, added backward compatibility support by obsoleting and deprecating the below nodes.

- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:peer-container
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:peer-container/ios-crypto:default
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:peer-container/ios-crypto:peer
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer/ios-crypto:address
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer/ios-crypto:default
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/ios-crypto:peer/ios-crypto:dynamic


## XPaths Deprecated

### Description/Reason
To make model backward compatible depreacted some of the IPSec and IKE CLI's.

- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip-in
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip-in/ios-crypto:ip/ios-crypto:access-group
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip-in/ios-crypto:ip/ios-crypto:in
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip-out/ios-crypto:ip
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip-out/ios-crypto:ip/ios-crypto:access-group
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip-out/ios-crypto:ip/ios-crypto:out
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:email
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:email/ios-crypto:domain
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:email/ios-crypto:name
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:fqdn
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:fqdn/ios-crypto:domain
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:fqdn/ios-crypto:name
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:key-id
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:address
- /native/crypto/ios-crypto:ikev2/ios-crypto:profile/ios-crypto:match/ios-crypto:address/ios-crypto:local/ios-crypto:interface
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:set/ios-crypto:interface/ios-crypto:interface-list/ios-crypto:interface-name
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:accept/ios-crypto:any
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:accept/ios-crypto:any/ios-crypto:tag
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:accept/ios-crypto:any/ios-crypto:distance
- /native/crypto/ios-crypto:ikev2/ios-crypto:client/ios-crypto:flexvpn/ios-crypto:peer/ios-crypto:peer-id-list/ios-crypto:peer-id-container/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:set/ios-crypto:interface/ios-crypto:interface-list/ios-crypto:interface-name
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:addr/ios-crypto:address
- /native/crypto/ios-crypto:ikev2/ios-crypto:cluster/\*
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:addr
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:addr/ios-crypto:way
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:name/ios-crypto:address
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:name/ios-crypto:address/ios-crypto:ip
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:name/ios-crypto:key-string
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:name/ios-crypto:key-string/ios-crypto:hex-data
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:name/ios-crypto:key-string/ios-crypto:quit
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:name/ios-crypto:serial-number
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:initiate/ios-crypto:mode/ios-crypto:aggressive
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:access-restrict
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:dhcp/ios-crypto:server
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:wins/ios-crypto:secondary
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:browser-proxy
- /native/interface/Tunnel/ios-tun:tunnel/ios-tun:protection/ios-crypto:ipsec/ios-crypto:profile
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:browser-proxy
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:access-restrict
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:dhcp/ios-crypto:server
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:initiate/ios-crypto:mode/ios-crypto:aggressive


### Description
container inside is under connect. Added grouping under crypto ikev2 keyring peer preshared

### Reason
Under crypto ikev2 client flexvpn, container inside is under connect but it should be under client and grouping should be properly added under crypto ikev2 keyring peer preshared. Hence deprecated the old node and the new xpaths specified below.

- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:pre-shared-key/ios-crypto:local
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:pre-shared-key/ios-crypto:remote


### Description/Reason
Crypto map command has been modified to support as per IOS. Removed "group" cli. 

- /native/crypto/ios-crypto:crypto-map
- /native/crypto/ios-crypto:crypto-map/\*
- /native/crypto/ios-crypto:map-ipv6-gdoi
- /native/crypto/ios-crypto:map-ipv6-gdoi/\*
- /native/crypto/ios-crypto:map-client
- /native/crypto/ios-crypto:map-client/\*
- /native/crypto/ios-crypto:map/ios-crypto:map-client/ios-crypto:authorization

## XPaths Modified

### Description
Must condition added and Updated comparison statement against keyring under ISAKMP profile.

### Reason
Need to revise comparision statement as it was reported as backward incompatible.

- - /native/crypto/isakmp/profile/keyring/ios-crypto:name

## XPaths Added

### Description
Crypto map has been modified to include multiple crypto maps and options.

- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip
- /native/crypto/ios-crypto:dynamic-map/ios-crypto:set/ios-crypto:ip/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:email-option
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:email-option/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:fqdn-option
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:fqdn-option/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:key-id-number
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:pre-shared-key/ios-crypto:local-option
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:pre-shared-key/ios-crypto:local-option/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:pre-shared-key/ios-crypto:remote-option
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:pre-shared-key/ios-crypto:remote-option/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:keyring/ios-crypto:peer/ios-crypto:identity/ios-crypto:address-type
- /native/crypto/ios-crypto:ikev2/ios-crypto:profile/ios-crypto:match/ios-crypto:address/ios-crypto:local/ios-crypto:interface-options/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:set/ios-crypto:interface/ios-crypto:interface-name-list/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:accept/ios-crypto:any-option
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:accept/ios-crypto:any-option/ios-crypto:tag
- /native/crypto/ios-crypto:ikev2/ios-crypto:authorization/ios-crypto:policy/ios-crypto:route/ios-crypto:accept/ios-crypto:any-option/ios-crypto:distance
- /native/crypto/ios-crypto:ikev2/ios-crypto:client/ios-crypto:flexvpn/ios-crypto:peer/ios-crypto:peer-id-list/ios-crypto:peer-id-container-option
- /native/crypto/ios-crypto:ikev2/ios-crypto:client/ios-crypto:flexvpn/ios-crypto:peer/ios-crypto:peer-id-list/ios-crypto:peer-id-container-option/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:client/ios-crypto:flexvpn/ios-crypto:source/ios-crypto:interface-name/\*
- /native/crypto/ios-crypto:ikev2/ios-crypto:cluster-options
- /native/crypto/ios-crypto:ikev2/ios-crypto:cluster-options/\*
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:address
- /native/crypto/ios-crypto:keyring/ios-crypto:default/ios-crypto:rsa-pubkey/ios-crypto:address/\*
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:initiate/ios-crypto:mode
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:initiate/ios-crypto:mode/ios-crypto:mode-name
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template-option
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template-option/ios-crypto:virtual-template-number
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template-option/ios-crypto:per-user
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:access-restrict-option/\*
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:dhcp/ios-crypto:server-option
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:dhcp/ios-crypto:server-option/ios-crypto:dhcp-server
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:wins/ios-crypto:secondary-address
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:browser-proxy-option
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:browser-proxy-option/\*
- /native/interface/Tunnel/ios-tun:tunnel/ios-tun:protection/ios-crypto:ipsec/ios-crypto:profile-option
- /native/interface/Tunnel/ios-tun:tunnel/ios-tun:protection/ios-crypto:ipsec/ios-crypto:profile-option/\*
- /native/crypto/ios-crypto:map
- /native/crypto/ios-crypto:map/\*

### Description
Rearranged some of the CLI models grouping

### Reason
In order to match native IOS CLI model and behavior, made rearrangement in groups	

- /native/crypto/ios-crypto:ipsec/ios-crypto:df-bit
- /native/crypto/ios-crypto:ipsec/ios-crypto:exclude/\*
- /native/crypto/ios-crypto:ipsec/ios-crypto:fragmentation
- /native/crypto/ios-crypto:ipsec/ios-crypto:ipv4-deny
- /native/crypto/ios-crypto:ipsec/ios-crypto:nat-transparency
- /native/crypto/ios-crypto:ipsec/ios-crypto:optional
- /native/crypto/ios-crypto:ipsec/ios-crypto:optional/ios-crypto:retry
- /native/crypto/ios-crypto:ipsec/ios-crypto:transform-set/\*
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:name
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:default/\*
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:description
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:dialer
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:dialer/ios-crypto:pre-classify
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:redundancy
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:redundancy/ios-crypto:name
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:redundancy/ios-crypto:stateful
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:responder-only
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:reverse-route/\*
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:reverse-route/ios-crypto:static
- /native/crypto/ios-crypto:ipsec/ios-crypto:security-association/ios-crypto:dummy
- /native/crypto/ios-crypto:ipsec/ios-crypto:profile/ios-crypto:set/\*
- /native/crypto/ios-crypto:ipsec/ios-crypto:security-association/\*
- /native/crypto/ios-crypto:ipsec/ios-crypto:session-key/\*

### Description
Moved aggressive mode option as enumeration type from leaf type data under crypto isakmp initiate CLI

### Reason
crypto isakmp initiate mode CLI model changed to match native IOS CLI options and behavior

native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:client/ios-crypto:authentication/ios-crypto:password
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:client/ios-crypto:authentication/ios-crypto:username
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:client/ios-crypto:pki/ios-crypto:authorization/ios-crypto:password
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:client/ios-crypto:pki/ios-crypto:authorization/ios-crypto:password/ios-crypto:encryption
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:client/ios-crypto:pki/ios-crypto:authorization/ios-crypto:password/ios-crypto:user-password
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:isakmp/ios-crypto:authorization/ios-crypto:password
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:isakmp/ios-crypto:authorization/ios-crypto:password/ios-crypto:encryption
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:isakmp/ios-crypto:authorization/ios-crypto:password/ios-crypto:user-password
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:rekey
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:initiate/ios-crypto:mode/ios-crypto:mode-name
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template-option
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template-option/ios-crypto:per-user
- /native/crypto/ios-crypto:isakmp/ios-crypto:profile/ios-crypto:virtual-template-option/ios-crypto:virtual-template-number
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:access-restrict-option
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:access-restrict-option/\*
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:dhcp/ios-crypto:server-option
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:dhcp/ios-crypto:server-option/ios-crypto:dhcp-server
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:group/ios-crypto:route-metric
- /native/crypto/ios-crypto:isakmp/ios-crypto:client/ios-crypto:configuration/ios-crypto:browser-proxy-option/\*
- /native/crypto/ios-crypto:isakmp/ios-crypto:diagnose
- /native/crypto/ios-crypto:isakmp/ios-crypto:diagnose/ios-crypto:error
- /native/crypto/ios-crypto:isakmp/ios-crypto:performance

