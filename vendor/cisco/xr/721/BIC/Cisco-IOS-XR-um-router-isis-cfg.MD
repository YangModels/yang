## Cisco-IOS-XR-um-router-isis-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated lsp-password and summary-prefix trees with proper constaraint statements.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L306)	/router/isis/processes/process[process-id]/lsp-password/text
- (L318)	/router/isis/processes/process[process-id]/lsp-password/hmac-md5
- (L330)	/router/isis/processes/process[process-id]/lsp-password/keychain
- (L387)	/router/isis/processes/process[process-id]/lsp-password/levels/level[level-id]/text
- (L399)	/router/isis/processes/process[process-id]/lsp-password/levels/level[level-id]/hmac-md5
- (L411)	/router/isis/processes/process[process-id]/lsp-password/levels/level[level-id]/keychain
- (L8076)	/router/isis/processes/process[process-id]/adjacency/stagger/initial-number-of-neighbors
- (L8087)	/router/isis/processes/process[process-id]/adjacency/stagger/maximum-simultaneous-neighbors

## XPaths Removed

- (L1709)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/srv6/capability-subsubtlv
- (L7933)	/router/isis/processes/process[process-id]/flex-algos/flex-algo[algorithm-number]/affinity/exclude-any

## XPaths Modified

N/A

