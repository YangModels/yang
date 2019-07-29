## Cisco-IOS-XE-crypto-rpc.yang

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
Added new crypto exec CLI. removed mandatory attribute from server node

### Reason
There are some CLI's which are non-nvgen, and multiple invocation to the same CLI works on IOS model but not via yang.Hence a call was made to make them exec-CLIs and hence these changes were done.

- /crypto/pki/authenticate
- /crypto/pki/authenticate/\*
- /crypto/pki/enroll
- /crypto/pki/enroll/\*
- /crypto/pki/import
- /crypto/pki/import/\*
- /crypto/pki/export
- /crypto/pki/export/\*
- /crypto/pki/server
- /crypto/pki/server/\*
- /crypto/pki/certificate/validate
- /crypto/pki/certificate/validate/\*
