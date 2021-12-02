## Cisco-IOS-XR-um-router-ospf-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Two nodes where even though they were correctly generated from CLI, the CLI hierarchy is incompatible for YANG. Added leaf use-interface-bandwidth, modified leaf bandwidth name to leaf reference and added mandatory for all the three leafs  under container apply-weight.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L6981)	/router/ospf/processes/process[process-name]/apply-weight/bandwidth
- (L6994)	/router/ospf/processes/process[process-name]/apply-weight/default-weight
- (L6966)	/router/ospf/processes/process[process-name]/apply-weight/use-interface-bandwidth

## XPaths Removed

N/A

## XPaths Modified

N/A

