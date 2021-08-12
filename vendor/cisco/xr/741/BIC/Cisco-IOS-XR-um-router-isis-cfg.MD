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

- (L859)	/router/isis/processes/process[process-id]/lsp-gen-interval
- (L989)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime
- (L9108)	/router/isis/processes/process[process-id]/flex-algos/flex-algo[algorithm-number]/metric-type/delay

## XPaths Removed

- (L800)	/router/isis/processes/process[process-id]/lsp-gen-interval/maximum-wait/maximum-wait-time
- (L810)	/router/isis/processes/process[process-id]/lsp-gen-interval/maximum-wait/levels
- (L844)	/router/isis/processes/process[process-id]/lsp-gen-interval/initial-wait/initial-wait-time
- (L854)	/router/isis/processes/process[process-id]/lsp-gen-interval/initial-wait/levels
- (L888)	/router/isis/processes/process[process-id]/lsp-gen-interval/secondary-wait/secondary-wait-time
- (L898)	/router/isis/processes/process[process-id]/lsp-gen-interval/secondary-wait/levels
- (L980)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/maximum-wait/maximum-wait-time
- (L990)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/maximum-wait/levels
- (L1024)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/initial-wait/initial-wait-time
- (L1034)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/initial-wait/levels
- (L1068)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/secondary-wait/secondary-wait-time
- (L1078)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/secondary-wait/levels
- (L3291)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf-interval/maximum-wait/levels
- (L3335)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf-interval/initial-wait/levels
- (L3379)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf-interval/secondary-wait/levels
- (L7354)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/per-link-computation
- (L7359)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/levels
- (L7441)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/per-prefix-computation
- (L7446)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/levels

## XPaths Modified

- (L863)	/router/isis/processes/process[process-id]/lsp-gen-interval/maximum-wait
- (L873)	/router/isis/processes/process[process-id]/lsp-gen-interval/initial-wait
- (L883)	/router/isis/processes/process[process-id]/lsp-gen-interval/secondary-wait
- (L993)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/maximum-wait
- (L1003)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/initial-wait
- (L1013)	/router/isis/processes/process[process-id]/min-lsp-arrivaltime/secondary-wait

