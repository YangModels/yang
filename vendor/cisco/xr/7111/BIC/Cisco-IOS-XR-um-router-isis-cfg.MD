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

- (L3381)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/protected
- (L3387)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/segment-routing
- (L9578)	/router/isis/processes/process[process-id]/algorithm/zero/address-family/ipv4/unicast/maximum-paths
- (L9597)	/router/isis/processes/process[process-id]/algorithm/zero/address-family/ipv6/unicast/maximum-paths
- (L9828)	/router/isis/processes/process[process-id]/flex-algos/flex-algo[algorithm-number]/address-family/ipv4/unicast/maximum-paths
- (L9847)	/router/isis/processes/process[process-id]/flex-algos/flex-algo[algorithm-number]/address-family/ipv6/unicast/maximum-paths

## XPaths Modified

- (L9596)	/router/isis/processes/process[process-id]/algorithm/zero/address-family/ipv4/unicast/maximum-paths
- (L9624)	/router/isis/processes/process[process-id]/algorithm/zero/address-family/ipv6/unicast/maximum-paths
- (L9884)	/router/isis/processes/process[process-id]/flex-algos/flex-algo[algorithm-number]/address-family/ipv4/unicast/maximum-paths
- (L9912)	/router/isis/processes/process[process-id]/flex-algos/flex-algo[algorithm-number]/address-family/ipv6/unicast/maximum-paths

