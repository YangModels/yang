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

- (L6803)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/prefix-attributes

## XPaths Removed

- (L3367)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/periodic/interval/interval-time
- (L3377)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/periodic/interval/levels
- (L3408)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/periodic/disable
- (L5769)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf-interval/maximum-wait/levels
- (L5813)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf-interval/initial-wait/levels
- (L5857)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf-interval/secondary-wait/levels
- (L5898)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/periodic/interval/interval-time
- (L5908)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/periodic/interval/levels
- (L5939)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/periodic/disable
- (L6935)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/affinity/flex-algos/flex-algo

## XPaths Modified

- (L3376)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/periodic/interval
- (L5846)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/periodic/interval

