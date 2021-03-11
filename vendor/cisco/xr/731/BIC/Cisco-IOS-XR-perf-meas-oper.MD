## Cisco-IOS-XR-perf-meas-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Renamed leaf nodes current-packet-t-xin-window to current-packet-tx-in-window, lspid to lsp-id, numberof-packets-received to number-of-packets-received, received-packet-error-urotlv-not-present to received-packet-error-uro-tlv-not-present to make them consistent with naming rule.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L577)	{PM-LIVENESS-PROFILE-BAG}/multiplier
- (L614)	{PM-DELAY-TRANSPORT-PROFILE-BAG}/liveness-detection-config
- (L873)	{PM-LOSS-WINDOW-BAG}/current-packet-t-xin-window
- (L878)	{PM-LOSS-WINDOW-BAG}/current-packet-r-xin-window
- (L1357)	{PM-RSVPTE-LSP-HISTORY-BAG}/lspid
- (L1387)	{PM-RSVPTE-LSP-DELAY-METRICS-BAG}/lspid
- (L1463)	{PM-RSVPTE-LSP-DELAY-BAG}/lspid
- (L1524)	{PM-RSVPTE-LSP-DELAY-COUNTERS-BAG}/lspid
- (L2617)	{PM-SCB-PROBE-RESULTS-BAG}/numberof-packets-received
- (L157)	{PM-COUNTER-RESP-BAG}/received-packet-error-urotlv-not-present

## XPaths Modified

N/A

