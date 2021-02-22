## Cisco-IOS-XR-um-router-isis-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated lsp-password and summary-prefix trees with proper constaraint statements. Bandwidth node type moved from leaf to container and few backward in-compatible nodes were been removed. Also must constraints were been alingned in many nodes(Adding missing must constraints does not break backward-compatibility). Also, levels under lsp-password was moved out of lsp-password and renamed as lsp-password-levels to fix a model bug.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L321)	/router/isis/processes/process[process-id]/lsp-password
- (L984)	/router/isis/processes/process[process-id]/max-metric/on-startup/advertise-maximum-metric
- (L1001)	/router/isis/processes/process[process-id]/max-metric/on-startup/wait-for-bgp
- (L1044)	/router/isis/processes/process[process-id]/max-metric/on-startup/levels/level[level-id]/advertise-maximum-metric
- (L1061)	/router/isis/processes/process[process-id]/max-metric/on-startup/levels/level[level-id]/wait-for-bgp
- (L1593)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/prefixes/prefix[address-prefix]/index
- (L1610)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/prefixes/prefix[address-prefix]/absolute
- (L1658)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/flex-algo/prefix[address-prefix][flex-algo]/index
- (L1675)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/flex-algo/prefix[address-prefix][flex-algo]/absolute
- (L1713)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/strict-spf/prefix[address-prefix]/index
- (L1730)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/segment-routing/mpls/connected-prefix-sid-map/strict-spf/prefix[address-prefix]/absolute
- (L1976)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospf[process-id]/match/internal
- (L1982)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospf[process-id]/match/external
- (L1988)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospf[process-id]/match/nssa-external
- (L2073)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospfv3[process-id]/match/internal
- (L2079)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospfv3[process-id]/match/external
- (L2085)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/ospfv3[process-id]/match/nssa-external
- (L2655)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/eigrp[as-number]/match/internal
- (L2661)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/redistribute/eigrp[as-number]/match/external
- (L2853)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/protected
- (L2859)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/segment-routing
- (L2880)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/apply-weight/ecmp-only
- (L2891)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/apply-weight/ucmp-only
- (L2998)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/narrow
- (L3004)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/wide
- (L3010)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/transition
- (L3033)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/levels/level[level-id]/narrow
- (L3039)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/levels/level[level-id]/wide
- (L3045)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/metric-style/levels/level[level-id]/transition
- (L3310)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/prefix-priority[priority]/tag
- (L3321)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/prefix-priority[priority]/access-list-name
- (L3278)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/prefix-priority[priority]
- (L3372)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/levels/level[level-id][priority]/tag
- (L3383)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/levels/level[level-id][priority]/access-list-name
- (L3330)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/spf/prefix-priority/levels/level[level-id][priority]
- (L3497)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/attached-bit/send/always-set
- (L3503)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/attached-bit/send/never-set
- (L3540)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/critical
- (L3546)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/high
- (L3552)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/medium
- (L3576)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/levels/level[level-id]/critical
- (L3582)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/levels/level[level-id]/high
- (L3588)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-link/priority-limit/levels/level[level-id]/medium
- (L3639)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/critical
- (L3645)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/high
- (L3651)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/medium
- (L3675)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/levels/level[level-id]/critical
- (L3681)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/levels/level[level-id]/high
- (L3687)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/fast-reroute/per-prefix/priority-limit/levels/level[level-id]/medium
- (L4460)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospf[process-id]/match/internal
- (L4466)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospf[process-id]/match/external
- (L4472)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospf[process-id]/match/nssa-external
- (L4557)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospfv3[process-id]/match/internal
- (L4563)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospfv3[process-id]/match/external
- (L4569)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/ospfv3[process-id]/match/nssa-external
- (L5139)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/eigrp[as-number]/match/internal
- (L5145)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/redistribute/eigrp[as-number]/match/external
- (L5323)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/microloop/avoidance/protected
- (L5329)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/microloop/avoidance/segment-routing
- (L5350)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/apply-weight/ecmp-only
- (L5361)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/apply-weight/ucmp-only
- (L5467)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/narrow
- (L5473)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/wide
- (L5479)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/transition
- (L5502)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/levels/level[level-id]/narrow
- (L5508)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/levels/level[level-id]/wide
- (L5514)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/metric-style/levels/level[level-id]/transition
- (L5779)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/prefix-priority[priority]/tag
- (L5790)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/prefix-priority[priority]/access-list-name
- (L5747)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/prefix-priority[priority]
- (L5841)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/levels/level[level-id][priority]/tag
- (L5852)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/levels/level[level-id][priority]/access-list-name
- (L5799)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/spf/prefix-priority/levels/level[level-id][priority]
- (L5966)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/attached-bit/send/always-set
- (L5972)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/attached-bit/send/never-set
- (L6115)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/disable
- (L6121)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/sometimes
- (L6144)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/levels/level[level-id]/disable
- (L6150)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-padding/levels/level[level-id]/sometimes
- (L6296)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password/text
- (L6308)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password/hmac-md5
- (L6320)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password/keychain
- (L6361)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password-levels/level[level-id]/text
- (L6373)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password-levels/level[level-id]/hmac-md5
- (L6385)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/hello-password-levels/level[level-id]/keychain
- (L6724)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/override/metrics/maximum
- (L6730)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/override/metrics/high
- (L6736)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/override/metrics/disabled
- (L6811)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/passive
- (L6817)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/suppressed
- (L6823)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/shutdown
- (L7025)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/sid/index
- (L7042)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/sid/absolute
- (L7075)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/strict-spf/index
- (L7092)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/strict-spf/absolute
- (L7137)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/algorithms/algorithm[algorithm-number]/index
- (L7154)	/router/isis/processes/process[process-id]/interfaces/interface[interface-name]/address-families/address-family[af-name][saf-name]/prefix-sid/algorithms/algorithm[algorithm-number]/absolute
- (L8350)	/router/isis/processes/process[process-id]/affinity-maps/affinity-map[affinity-map-name]/bit-position

## XPaths Removed

- (L368)	/router/isis/processes/process[process-id]/lsp-password/levels
- (L451)	/router/isis/processes/process[process-id]/lsp-password/accept
- (L2825)	/router/isis/processes/process[process-id]/address-families/address-family[af-name][saf-name]/microloop/avoidance/rib-update-delay
- (L5258)	/router/isis/processes/process[process-id]/address-families/address-family-topology[af-name][saf-name][topology-name]/microloop/avoidance/rib-update-delay

## XPaths Modified

N/A

