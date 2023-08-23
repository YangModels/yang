## Cisco-IOS-XR-um-router-isis-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated lsp-password and summary-prefix trees with proper constaraint statements. Bandwidth node type moved from leaf to container and few backward in-compatible nodes were been removed. Also must constraints were been alingned in many nodes(Adding missing must constraints does not break backward-compatibility). Also, levels under lsp-password was moved out of lsp-password and renamed as lsp-password-levels to fix a model bug. Moved container levels from container max-metric, this will break backward compatiblity, Moved presence containers as leafs under snmp-server traps. Re-ordered nodes under lsp-gen-interval container. Added cisco-support task yang nodes, logically it will not create backward compatiblity as customer wont have cisco-support cli configured. Re-ordered per-link, per-prefix nodes under interface fast-reroute container which will create non-backward compatibility.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L2264)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/srv6/locators/locator[locator-name]/metric/levels/level[level-id]
- (L2308)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/srv6/locators/locator[locator-name]/tag/levels/level[level-id]

