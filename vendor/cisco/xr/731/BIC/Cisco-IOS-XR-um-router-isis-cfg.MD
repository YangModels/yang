## Cisco-IOS-XR-um-router-isis-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated lsp-password and summary-prefix trees with proper constaraint statements. Bandwidth node type moved from leaf to container and few backward in-compatible nodes were been removed. Also must constraints were been alingned in many nodes(Adding missing must constraints does not break backward-compatibility). Also, levels under lsp-password was moved out of lsp-password and renamed as lsp-password-levels to fix a model bug. Moved container levels from container max-metric, this will break backward compatiblity, Moved presence containers as leafs under snmp-server traps.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L183)	/snmp-server/traps/isis/all
- (L200)	/snmp-server/traps/isis/database-overload
- (L217)	/snmp-server/traps/isis/manual-address-drops
- (L234)	/snmp-server/traps/isis/corrupted-lsp-detected
- (L251)	/snmp-server/traps/isis/attempt-to-exceed-max-sequence
- (L268)	/snmp-server/traps/isis/id-len-mismatch
- (L285)	/snmp-server/traps/isis/max-area-addresses-mismatch
- (L302)	/snmp-server/traps/isis/own-lsp-purge
- (L319)	/snmp-server/traps/isis/sequence-number-skip
- (L336)	/snmp-server/traps/isis/authentication-type-failure
- (L353)	/snmp-server/traps/isis/authentication-failure
- (L370)	/snmp-server/traps/isis/version-skew
- (L387)	/snmp-server/traps/isis/area-mismatch
- (L404)	/snmp-server/traps/isis/rejected-adjacency
- (L421)	/snmp-server/traps/isis/lsp-too-large-to-propagate
- (L438)	/snmp-server/traps/isis/orig-lsp-buff-size-mismatch
- (L455)	/snmp-server/traps/isis/protocols-supported-mismatch
- (L472)	/snmp-server/traps/isis/adjacency-change
- (L489)	/snmp-server/traps/isis/lsp-error-detected
- (L166)	/snmp-server/traps/isis
- (L586)	/router/isis/processes/process[process-id]/lsp-password
- (L1206)	/router/isis/processes/process[process-id]/max-metric/on-startup/advertise-maximum-metric
- (L1223)	/router/isis/processes/process[process-id]/max-metric/on-startup/wait-for-bgp
- (L1805)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/prefixes/prefix[address-prefix]/index
- (L1822)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/prefixes/prefix[address-prefix]/absolute
- (L1870)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/flex-algo/prefix[address-prefix][flex-algo]/index
- (L1887)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/flex-algo/prefix[address-prefix][flex-algo]/absolute
- (L1925)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/strict-spf/prefix[address-prefix]/index
- (L1942)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/strict-spf/prefix[address-prefix]/absolute
- (L2198)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospf[process-id]/match/internal
- (L2204)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospf[process-id]/match/external
- (L2210)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospf[process-id]/match/nssa-external
- (L2295)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospfv3[process-id]/match/internal
- (L2301)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospfv3[process-id]/match/external
- (L2307)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospfv3[process-id]/match/nssa-external
- (L2877)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/eigrp[as-number]/match/internal
- (L2883)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/eigrp[as-number]/match/external
- (L3075)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/protected
- (L3081)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/segment-routing
- (L3102)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/apply-weight/ecmp-only
- (L3113)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/apply-weight/ucmp-only
- (L3220)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/narrow
- (L3226)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/wide
- (L3232)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/transition
- (L3255)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/levels/level[level-id]/narrow
- (L3261)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/levels/level[level-id]/wide
- (L3267)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/levels/level[level-id]/transition
- (L3450)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/prefix-priority[priority]/tag
- (L3461)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/prefix-priority[priority]/access-list-name
- (L3418)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/prefix-priority[priority]
- (L3512)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/levels/level[level-id][priority]/tag
- (L3523)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/levels/level[level-id][priority]/access-list-name
- (L3470)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/levels/level[level-id][priority]
- (L3637)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/attached-bit/send/always-set
- (L3643)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/attached-bit/send/never-set
- (L3680)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/critical
- (L3686)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/high
- (L3692)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/medium
- (L3716)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/levels/level[level-id]/critical
- (L3722)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/levels/level[level-id]/high
- (L3728)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/levels/level[level-id]/medium
- (L3779)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/critical
- (L3785)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/high
- (L3791)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/medium
- (L3815)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/levels/level[level-id]/critical
- (L3821)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/levels/level[level-id]/high
- (L3827)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/levels/level[level-id]/medium
- (L4649)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospf[process-id]/match/internal
- (L4655)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospf[process-id]/match/external
- (L4661)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospf[process-id]/match/nssa-external
- (L4746)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospfv3[process-id]/match/internal
- (L4752)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospfv3[process-id]/match/external
- (L4758)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospfv3[process-id]/match/nssa-external
- (L5328)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/eigrp[as-number]/match/internal
- (L5334)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/eigrp[as-number]/match/external
- (L5512)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/microloop/avoidance/protected
- (L5518)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/microloop/avoidance/segment-routing
- (L5539)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/apply-weight/ecmp-only
- (L5550)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/apply-weight/ucmp-only
- (L5656)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/narrow
- (L5662)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/wide
- (L5668)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/transition
- (L5691)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/levels/level[level-id]/narrow
- (L5697)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/levels/level[level-id]/wide
- (L5703)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/levels/level[level-id]/transition
- (L5886)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/prefix-priority[priority]/tag
- (L5897)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/prefix-priority[priority]/access-list-name
- (L5854)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/prefix-priority[priority]
- (L5948)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/levels/level[level-id][priority]/tag
- (L5959)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/levels/level[level-id][priority]/access-list-name
- (L5906)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/levels/level[level-id][priority]
- (L6073)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/attached-bit/send/always-set
- (L6079)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/attached-bit/send/never-set
- (L6222)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/disable
- (L6228)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/sometimes
- (L6251)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/levels/level[level-id]/disable
- (L6257)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/levels/level[level-id]/sometimes
- (L6403)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password/text
- (L6415)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password/hmac-md5
- (L6427)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password/keychain
- (L6468)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password-levels/level[level-id]/text
- (L6480)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password-levels/level[level-id]/hmac-md5
- (L6492)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password-levels/level[level-id]/keychain
- (L6831)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/override/metrics/maximum
- (L6837)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/override/metrics/high
- (L6843)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/override/metrics/disabled
- (L6918)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/passive
- (L6924)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/suppressed
- (L6930)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/shutdown
- (L7136)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/sid/index
- (L7153)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/sid/absolute
- (L7186)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/strict-spf/index
- (L7203)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/strict-spf/absolute
- (L7248)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/algorithms/algorithm[algorithm-number]/index
- (L7265)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/algorithms/algorithm[algorithm-number]/absolute
- (L8466)	/router/isis/processes/process[process-id]/affinity-maps/affinity-map[affinity-map-name]/bit-position

## XPaths Removed

- (L368)	/router/isis/processes/process[process-id]/lsp-password/levels
- (L451)	/router/isis/processes/process[process-id]/lsp-password/accept
- (L1004)	/router/isis/processes/process[process-id]/max-metric/on-startup/levels
- (L2825)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/rib-update-delay
- (L3145)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/periodic
- (L5258)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/microloop/avoidance/rib-update-delay
- (L5577)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/periodic
- (L6816)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/metric/fallback/bandwidth
- (L6826)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/metric/fallback/threshold
- (L7799)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric/fallback/bandwidth
- (L7809)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric/fallback/threshold
- (L509)	/router/isis/processes/process[process-id]/lsp-check-interval
- (L1460)	/router/isis/processes/process[process-id]/triggers

## XPaths Modified

- (L170)	/snmp-server/traps/isis/all
- (L187)	/snmp-server/traps/isis/database-overload
- (L204)	/snmp-server/traps/isis/manual-address-drops
- (L221)	/snmp-server/traps/isis/corrupted-lsp-detected
- (L238)	/snmp-server/traps/isis/attempt-to-exceed-max-sequence
- (L255)	/snmp-server/traps/isis/id-len-mismatch
- (L272)	/snmp-server/traps/isis/max-area-addresses-mismatch
- (L289)	/snmp-server/traps/isis/own-lsp-purge
- (L306)	/snmp-server/traps/isis/sequence-number-skip
- (L323)	/snmp-server/traps/isis/authentication-type-failure
- (L340)	/snmp-server/traps/isis/authentication-failure
- (L357)	/snmp-server/traps/isis/version-skew
- (L374)	/snmp-server/traps/isis/area-mismatch
- (L391)	/snmp-server/traps/isis/rejected-adjacency
- (L408)	/snmp-server/traps/isis/lsp-too-large-to-propagate
- (L425)	/snmp-server/traps/isis/orig-lsp-buff-size-mismatch
- (L442)	/snmp-server/traps/isis/protocols-supported-mismatch
- (L459)	/snmp-server/traps/isis/adjacency-change
- (L476)	/snmp-server/traps/isis/lsp-error-detected
- (L7030)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/metric/fallback/bandwidth
- (L8023)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric/fallback/bandwidth

