## Cisco-IOS-XE-acl.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/dst/destination-choice/address-case/destination-address
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/dst/destination-choice/address-case/destination-wildcard-bits
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/dst/destination-choice/any-case/destination-any
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/dst/destination-choice/host-case/destination-host
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/dst/destination-choice/prefix-case/destination-prefix
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/object-group-str
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/dst/destination-choice/address-case/destination-address
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/dst/destination-choice/address-case/destination-wildcard-bits
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/dst/destination-choice/any-case/destination-any
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/dst/destination-choice/host-case/destination-host
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/dst/destination-choice/prefix-case/destination-prefix
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/source-choice/address-case/source-address
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/source-choice/address-case/source-wildcard-bits
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/source-choice/any-case/any
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/source-choice/host-case/source-host
- /native/ip/access-list/role-based/access-list-seq-rule/ace-rule/src/source-choice/prefix-case/source-prefix
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/dst/destination-choice/address-case/destination-address
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/dst/destination-choice/address-case/destination-wildcard-bits
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/dst/destination-choice/any-case/destination-any
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/dst/destination-choice/host-case/destination-host
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/dst/destination-choice/prefix-case/destination-prefix
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/object-group-str
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/dst/destination-choice/address-case/destination-address
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/dst/destination-choice/address-case/destination-wildcard-bits
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/dst/destination-choice/any-case/destination-any
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/dst/destination-choice/host-case/destination-host
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/dst/destination-choice/prefix-case/destination-prefix
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/source-choice/address-case/source-address
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/source-choice/address-case/source-wildcard-bits
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/source-choice/any-case/any
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/source-choice/host-case/source-host
- /native/ip/access-list/role-based/default/access-list-seq-rule/ace-rule/src/source-choice/prefix-case/source-prefix

### Description

Status of the nodes changed to obsolete.

### Reason

The role-based ACL CLI does not support source/destination address options. But because of incorrect modelling, these options were added in the model. They never worked from the beginning. So they are now obsoleted, as part of hardening.

## XPaths Deprecated

### Description

## XPaths Modified

### Description

## XPaths Added

### Description
