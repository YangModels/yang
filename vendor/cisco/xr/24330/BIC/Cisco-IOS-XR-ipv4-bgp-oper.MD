## Cisco-IOS-XR-ipv4-bgp-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed LLGR as a reset reason as it no longer resets sessions.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L998)	{Bgp-reset-reason-index}
- (L18827)	{VERSION-RATE-AFI}/nbr-total-ver-bump-count
- (L18832)	{VERSION-RATE-AFI}/nbr-ver-rate-stat
- (L18948)	{BGP-NBR-BRIEF-BAG}/nbr-total-ver-bump-count
- (L18953)	{BGP-NBR-BRIEF-BAG}/nbr-ver-rate-stat
- (L18948)	{BGP-NBR-BRIEF-BAG}/nbr-total-ver-bump-count
- (L18953)	{BGP-NBR-BRIEF-BAG}/nbr-ver-rate-stat
- (L18657)	{BGP-DRYRUN-POLICY-STATS-AFI}/num-networks
- (L18662)	{BGP-DRYRUN-POLICY-STATS-AFI}/num-paths-afi
- (L18575)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/num-prefix-modified
- (L18580)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/num-prefix-accepted
- (L18585)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/num-prefix-denied
- (L18590)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/curr-policy-pfx-acc-mod
- (L18596)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/curr-policy-denied
- (L18602)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/curr-policy-accepted
- (L18615)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/num-path-memory
- (L18622)	{BGP-DRYRUN-POLICY-STATS-NBR-BAG}/num-paths-nbr
- (L15879)	{BGP-PROCESS-INFO-AF-VRF}/num-path-denied
- (L15884)	{BGP-PROCESS-INFO-AF-VRF}/path-accepted-sum
- (L15889)	{BGP-PROCESS-INFO-AF-VRF}/path-modified-sum
- (L15894)	{BGP-PROCESS-INFO-AF-VRF}/path-modified-sum-hwm
- (L15906)	{BGP-PROCESS-INFO-AF-VRF}/path-modified-sum-hwm-time
- (L15614)	{BGP-PERF-PROCESS-AF-GBL}/total-ver-bump-count
- (L15619)	{BGP-PERF-PROCESS-AF-GBL}/ver-rate-stat
- (L13218)	{BGP-NH-PERF-CTRS}/total-reachable-count
- (L13224)	{BGP-NH-PERF-CTRS}/total-unreachable-count
- (L13230)	{BGP-NH-PERF-CTRS}/total-metric-increase-count
- (L13236)	{BGP-NH-PERF-CTRS}/total-metric-decrease-count
- (L13218)	{BGP-NH-PERF-CTRS}/total-reachable-count
- (L13224)	{BGP-NH-PERF-CTRS}/total-unreachable-count
- (L13230)	{BGP-NH-PERF-CTRS}/total-metric-increase-count
- (L13236)	{BGP-NH-PERF-CTRS}/total-metric-decrease-count
- (L13080)	{BGP-NEXTHOP-GW-INFO}/total-unreachable-count
- (L13085)	{BGP-NEXTHOP-GW-INFO}/total-reachable-count
- (L13090)	{BGP-NEXTHOP-GW-INFO}/total-metric-increase-count
- (L13096)	{BGP-NEXTHOP-GW-INFO}/total-metric-decrease-count
- (L8974)	{BGP-NBR-THROTL-STATS-BAG}/throttle-duration-msec
- (L8974)	{BGP-NBR-THROTL-STATS-BAG}/throttle-duration-msec
- (L8974)	{BGP-NBR-THROTL-STATS-BAG}/throttle-duration-msec
- (L8974)	{BGP-NBR-THROTL-STATS-BAG}/throttle-duration-msec
- (L9491)	{BGP-NBR-AF}/prefixes-accepted-hwmts
- (L9509)	{BGP-NBR-AF}/prefixes-accepted-modified-hwmts
- (L9994)	{BGP-NBR-AF}/prefixes-denied-non-cumulative-hwmts
- (L10107)	{BGP-NBR-AF}/nbr-total-ver-bump-count
- (L10112)	{BGP-NBR-AF}/ver-rate-stat
- (L11402)	{BGP-NBR-BAG}/hold-time-low-thresh-percent
- (L11409)	{BGP-NBR-BAG}/hold-time-high-thresh-percent
- (L11428)	{BGP-NBR-BAG}/num-hold-time-low-thresh-exceed
- (L11434)	{BGP-NBR-BAG}/num-hold-time-high-thresh-exceed
- (L11452)	{BGP-NBR-BAG}/num-hold-time-low-thresh-exceed-reset
- (L11458)	{BGP-NBR-BAG}/num-hold-time-high-thresh-exceed-reset
- (L11497)	{BGP-NBR-BAG}/nbr-total-ver-bump-count
- (L11502)	{BGP-NBR-BAG}/nbr-ver-rate-stat
- (L11509)	{BGP-NBR-BAG}/read-throttle-recent-event
- (L11515)	{BGP-NBR-BAG}/read-throttle-recent-events-reset
- (L11521)	{BGP-NBR-BAG}/write-throttle-recent-event
- (L11527)	{BGP-NBR-BAG}/write-throttle-recent-events-reset
- (L11402)	{BGP-NBR-BAG}/hold-time-low-thresh-percent
- (L11409)	{BGP-NBR-BAG}/hold-time-high-thresh-percent
- (L11428)	{BGP-NBR-BAG}/num-hold-time-low-thresh-exceed
- (L11434)	{BGP-NBR-BAG}/num-hold-time-high-thresh-exceed
- (L11452)	{BGP-NBR-BAG}/num-hold-time-low-thresh-exceed-reset
- (L11458)	{BGP-NBR-BAG}/num-hold-time-high-thresh-exceed-reset
- (L11497)	{BGP-NBR-BAG}/nbr-total-ver-bump-count
- (L11502)	{BGP-NBR-BAG}/nbr-ver-rate-stat
- (L11509)	{BGP-NBR-BAG}/read-throttle-recent-event
- (L11515)	{BGP-NBR-BAG}/read-throttle-recent-events-reset
- (L11521)	{BGP-NBR-BAG}/write-throttle-recent-event
- (L11527)	{BGP-NBR-BAG}/write-throttle-recent-events-reset
- (L6012)	{BGP-PERF-PROCESS-GBL}/scoped-sync-batch-cnt
- (L6072)	{BGP-PERF-PROCESS-GBL}/receieve-stat
- (L5242)	{BGP-PERF-PROCESS-VRF}/nbr-num-curr-read-throttled
- (L5248)	{BGP-PERF-PROCESS-VRF}/max-nbrs-read-throttled
- (L5254)	{BGP-PERF-PROCESS-VRF}/max-nbrs-read-throttled-time
- (L5260)	{BGP-PERF-PROCESS-VRF}/nbr-num-curr-write-throttled
- (L5266)	{BGP-PERF-PROCESS-VRF}/max-nbrs-write-throttled
- (L5272)	{BGP-PERF-PROCESS-VRF}/max-nbrs-write-throttled-time

## XPaths Modified

- (L1032)	{Bgp-reset-reason-index}
- (L1033)	{Bgp-reset-reason-index}
- (L1037)	{Bgp-reset-reason-index}
- (L1038)	{Bgp-reset-reason-index}
- (L1042)	{Bgp-reset-reason-index}
- (L1043)	{Bgp-reset-reason-index}
- (L1047)	{Bgp-reset-reason-index}
- (L1048)	{Bgp-reset-reason-index}
- (L1052)	{Bgp-reset-reason-index}
- (L1053)	{Bgp-reset-reason-index}
- (L1957)	{Bgp-bfd-enable-mode}
- (L1958)	{Bgp-bfd-enable-mode}
- (L740)	/{MEMORY-INFO}/memory-info/memory-info-entries/memory-info-entry[index]/index
- (L20250)	{BGP-AF-DEP}/af-long-lived-graceful-restart-capable

