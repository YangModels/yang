## Cisco-IOS-XR-um-mpls-ldp-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Complex YFED internal support requirements dictated that we need unique list and leaf node names with the same parent for correct JSON data parsing via CSCvr15428. Moved out trap augments into um-traps-mpls-ldp model via via CSCvr62233.Redistribute option supported only for ipv4 address-family. So, adjusted when statement under redistribute container.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L1491)	/mpls/ldp/address-families/address-family[af-name]/redistribute

## XPaths Removed

N/A

## XPaths Modified

N/A

