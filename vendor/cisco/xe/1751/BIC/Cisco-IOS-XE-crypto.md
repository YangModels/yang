## Cisco-IOS-XE-crypto.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- interface-grouping(grouping)/interface-choice/Loopback/Loopback
- crypto-ikev2-grouping(grouping)/authorization/policy/dhcp/timeout
- crypto-ipsec-grouping(grouping)/security-association/lifetime/days
- crypto-ipsec-grouping(grouping)/security-association/lifetime/seconds
- native/crypto/ikev2/profile/dynamic
- native/key/chain/key/cryptographic-algorithm-choice/default

### Description

1. A new must expression added
2. The range '[(0, 2147483647)]' is added
3. The range has been restricted (RFC 6020: 10, p5, bullet 3)
4. The must expression may be more constrained than before
5  The when expression may be different than before

### Reason

Current nodes were referencing the deprecated/obsolete nodes .Furthermore, NSO interoperability, which requires deselection of deprecated/obsolete nodes was breaking.So necessay "MUST" changes were made

## XPaths Added

### Description
