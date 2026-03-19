## Cisco-IOS-XR-ipv4-bgp-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated bgp_updgrp_wdr_types with new enum value for EVPN IMET PMSI Tunnel ID not v4.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L463)	/{BMP}/bmp/server-summaries/server-summary[server-id]
- (L456)	/{BMP}/bmp/server-summaries
- (L502)	/{BMP}/bmp/server-neighbors/server-neighbor[server-id]/monitored-neighbors/monitored-neighbor
- (L495)	/{BMP}/bmp/server-neighbors/server-neighbor[server-id]/monitored-neighbors
- (L488)	/{BMP}/bmp/server-neighbors/server-neighbor[server-id]
- (L480)	/{BMP}/bmp/server-neighbors
- (L450)	/{BMP}/bmp

## XPaths Added

N/A

## XPaths Removed

- (L998)	{Bgp-reset-reason-index}
- (L1285)	{Bgp-bmp-mode}
- (L1290)	{Bgp-bmp-mode}
- (L1295)	{Bgp-bmp-mode}
- (L1300)	{Bgp-bmp-mode}
- (L1305)	{Bgp-bmp-mode}
- (L6691)	{BGP-BMP-SRVR-AFI}/bmp-init-eor-end-version
- (L6696)	{BGP-BMP-SRVR-AFI}/bmp-init-eor-pending-cnt
- (L6792)	{BGP-BMP-SRVR-BAG}/bmp-status-report-count
- (L6843)	{BGP-BMP-SRVR-BAG}/bmp-update-mode
- (L6900)	{BGP-BMP-SRVR-BAG}/path-update-count
- (L6905)	{BGP-BMP-SRVR-BAG}/path-withdraw-count
- (L6910)	{BGP-BMP-SRVR-BAG}/path-update-drop
- (L6915)	{BGP-BMP-SRVR-BAG}/path-withdraw-drop
- (L6943)	{BGP-BMP-SRVR-BAG}/bmpr-mon-upd-messages
- (L6948)	{BGP-BMP-SRVR-BAG}/bmpr-mon-wdraw-messages
- (L6965)	{BGP-BMP-SRVR-BAG}/bmp-per-peer-msg-route-mon-count
- (L6976)	{BGP-BMP-SRVR-BAG}/bmpr-mon-eo-rmessages
- (L7007)	{BGP-BMP-SRVR-BAG}/bmp-in-post-pol-advertisement-interval-sec
- (L7014)	{BGP-BMP-SRVR-BAG}/bmp-in-post-pol-advertisement-interval-msec
- (L7021)	{BGP-BMP-SRVR-BAG}/bmp-in-post-pol-scan-time
- (L7027)	{BGP-BMP-SRVR-BAG}/bmp-local-rib-advertisement-interval-sec
- (L7033)	{BGP-BMP-SRVR-BAG}/bmp-local-rib-advertisement-interval-msec
- (L7040)	{BGP-BMP-SRVR-BAG}/bmp-local-rib-scan-time
- (L6557)	{BGP-BMP-NBR-BAG}/vrf-name-xr
- (L6562)	{BGP-BMP-NBR-BAG}/bmp-neighbor-msg-pending
- (L6568)	{BGP-BMP-NBR-BAG}/bmp-neighbor-msg-dropped
- (L6586)	{BGP-BMP-NBR-BAG}/bmp-neighbor-route-monitor-sent
- (L6591)	{BGP-BMP-NBR-BAG}/bmp-neighbor-route-monitor-eor-sent
- (L6596)	{BGP-BMP-NBR-BAG}/bmp-neighbor-path-update-sent
- (L6601)	{BGP-BMP-NBR-BAG}/bmp-neighbor-path-withdraw-sent
- (L6606)	{BGP-BMP-NBR-BAG}/bmp-neighbor-path-update-drop
- (L6611)	{BGP-BMP-NBR-BAG}/bmp-neighbor-path-withdraw-drop
- (L6616)	{BGP-BMP-NBR-BAG}/bmp-neighbor-upd-msg-sent
- (L6621)	{BGP-BMP-NBR-BAG}/bmp-neighbor-wdraw-msg-sent
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
- (L12477)	{BGP-BMP-PATH-BAG}/bmp-path-adv-bit-map
- (L12482)	{BGP-BMP-PATH-BAG}/bmp-path-snd-bit-map
- (L12192)	{BGP-BMP-CONVERGENCE-MODE}/inbound-pre-policy-information
- (L12201)	{BGP-BMP-CONVERGENCE-MODE}/inbound-post-policy-information
- (L12210)	{BGP-BMP-CONVERGENCE-MODE}/local-rib-information
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

- (L1044)	{Bgp-reset-reason-index}
- (L1045)	{Bgp-reset-reason-index}
- (L1049)	{Bgp-reset-reason-index}
- (L1050)	{Bgp-reset-reason-index}
- (L1054)	{Bgp-reset-reason-index}
- (L1055)	{Bgp-reset-reason-index}
- (L1059)	{Bgp-reset-reason-index}
- (L1060)	{Bgp-reset-reason-index}
- (L1064)	{Bgp-reset-reason-index}
- (L1065)	{Bgp-reset-reason-index}
- (L2006)	{Bgp-bfd-enable-mode}
- (L2007)	{Bgp-bfd-enable-mode}
- (L1746)	/{AF-TABLE}/afs/af[af-name]/bmp-modes/bmp-mode[mode]/mode
- (L798)	/{MEMORY-INFO}/memory-info/memory-info-entries/memory-info-entry[index]/index
- (L20730)	{BGP-AF-DEP}/af-long-lived-graceful-restart-capable

