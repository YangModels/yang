## Cisco-IOS-XE-crypto.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native(container)/crypto(container)/pki(container)/server(list)/default(container)/shutdown(leaf)
- native(container)/crypto(container)/pki(container)/server(list)/shutdown(leaf)

### Reason


## XPaths Deprecated

### Description

## XPaths Modified

- crypto-pki-server-grouping(grouping)/lifetime(container)/days(leaf)

### Description

The range has been illegally restricted

### Reason

- native(container)/crypto(container)/ikev2(container)/profile(list)/dpd(container)/interval(leaf)
- native(container)/crypto(container)/ikev2(container)/profile(list)/dpd(container)/retry(leaf)
- native(container)/crypto(container)/vpn(container)/anyconnect(container)/profile-container(container)/filename(leaf)
- native(container)/crypto(container)/vpn(container)/anyconnect(container)/profile-container(container)/profile(leaf)
- native(container)/key(container)/chain(list)/key(list)/key-string(container)/key(leaf)

### Description

A new must expression added

### Reason

Some of CLI's necessary for RA feature is not hardened, and these CLI's are necessary for complete testing of the feature.


## XPaths Added

### Description
