## Cisco-IOS-XR-clns-isis-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Change in Yang tool corrected strings repair-s-rv6* to repair-srv6*, end-xsid* to end-x-sid*, and is-s-rv6 to is-srv6. Changed avg-dela-rawy to avg-delay-raw to fix misspelling. Changed SRv6 function-type to sid-behavior, uint32_t to mgmt_srv6_sid_fmt, and num-sid to num-sids for consistency and to comply with current IETF ISIS SRv6 draft.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L10422)	{ISIS-TRAFFIC-GLOBAL-TYPE}/hello-count
- (L10427)	{ISIS-TRAFFIC-GLOBAL-TYPE}/csnp-count
- (L10432)	{ISIS-TRAFFIC-GLOBAL-TYPE}/psnp-count
- (L10437)	{ISIS-TRAFFIC-GLOBAL-TYPE}/lsp-count
- (L10442)	{ISIS-TRAFFIC-GLOBAL-TYPE}/hello-recv-time
- (L10447)	{ISIS-TRAFFIC-GLOBAL-TYPE}/csnp-recv-time
- (L10452)	{ISIS-TRAFFIC-GLOBAL-TYPE}/psnp-recv-time
- (L10457)	{ISIS-TRAFFIC-GLOBAL-TYPE}/lsp-recv-time
- (L10462)	{ISIS-TRAFFIC-GLOBAL-TYPE}/hello-transmit-time
- (L10467)	{ISIS-TRAFFIC-GLOBAL-TYPE}/csnp-transmit-time
- (L10472)	{ISIS-TRAFFIC-GLOBAL-TYPE}/psnp-transmit-time
- (L10477)	{ISIS-TRAFFIC-GLOBAL-TYPE}/lsp-transmit-time
- (L10482)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-hello-recv-rate
- (L10488)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-csnp-recv-rate
- (L10494)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-psnp-recv-rate
- (L10500)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-lsp-recv-rate
- (L10506)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-hello-send-rate
- (L10512)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-csnp-send-rate
- (L10518)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-psnp-send-rate
- (L10524)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-lsp-send-rate
- (L10530)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-hello-recv-rate
- (L10536)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-csnp-recv-rate
- (L10542)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-psnp-recv-rate
- (L10548)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-lsp-recv-rate
- (L10554)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-hello-send-rate
- (L10560)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-csnp-send-rate
- (L10566)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-psnp-send-rate
- (L10572)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-lsp-send-rate
- (L10593)	{ISIS-TRAFFIC-GLOBAL-TYPE}/maximum-iih-queue-length
- (L10598)	{ISIS-TRAFFIC-GLOBAL-TYPE}/maximum-pdu-queue-length
- (L10603)	{ISIS-TRAFFIC-GLOBAL-TYPE}/pdu-queue-length
- (L9300)	{ISIS-SH-IPV4-PATH}/is-sr-exclude-tunnel-interface
- (L9002)	{ISIS-SH-IPV4-UCMP-PATH}/is-sr-exclude-tunnel-interface
- (L9300)	{ISIS-SH-IPV4-PATH}/is-sr-exclude-tunnel-interface
- (L9300)	{ISIS-SH-IPV4-PATH}/is-sr-exclude-tunnel-interface
- (L9300)	{ISIS-SH-IPV4-PATH}/is-sr-exclude-tunnel-interface
- (L8569)	{ISIS-SH-IPV6-PATH}/is-sr-exclude-tunnel-interface
- (L8346)	{ISIS-SH-IPV6-UCMP-PATH}/is-sr-exclude-tunnel-interface
- (L8569)	{ISIS-SH-IPV6-PATH}/is-sr-exclude-tunnel-interface
- (L8569)	{ISIS-SH-IPV6-PATH}/is-sr-exclude-tunnel-interface
- (L8569)	{ISIS-SH-IPV6-PATH}/is-sr-exclude-tunnel-interface
- (L9300)	{ISIS-SH-IPV4-PATH}/is-sr-exclude-tunnel-interface
- (L9300)	{ISIS-SH-IPV4-PATH}/is-sr-exclude-tunnel-interface
- (L8569)	{ISIS-SH-IPV6-PATH}/is-sr-exclude-tunnel-interface
- (L8569)	{ISIS-SH-IPV6-PATH}/is-sr-exclude-tunnel-interface
- (L7111)	{ISIS-SH-TE-TUNNEL}/te-segment-routing-exclude
- (L10422)	{ISIS-TRAFFIC-GLOBAL-TYPE}/hello-count
- (L10427)	{ISIS-TRAFFIC-GLOBAL-TYPE}/csnp-count
- (L10432)	{ISIS-TRAFFIC-GLOBAL-TYPE}/psnp-count
- (L10437)	{ISIS-TRAFFIC-GLOBAL-TYPE}/lsp-count
- (L10442)	{ISIS-TRAFFIC-GLOBAL-TYPE}/hello-recv-time
- (L10447)	{ISIS-TRAFFIC-GLOBAL-TYPE}/csnp-recv-time
- (L10452)	{ISIS-TRAFFIC-GLOBAL-TYPE}/psnp-recv-time
- (L10457)	{ISIS-TRAFFIC-GLOBAL-TYPE}/lsp-recv-time
- (L10462)	{ISIS-TRAFFIC-GLOBAL-TYPE}/hello-transmit-time
- (L10467)	{ISIS-TRAFFIC-GLOBAL-TYPE}/csnp-transmit-time
- (L10472)	{ISIS-TRAFFIC-GLOBAL-TYPE}/psnp-transmit-time
- (L10477)	{ISIS-TRAFFIC-GLOBAL-TYPE}/lsp-transmit-time
- (L10482)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-hello-recv-rate
- (L10488)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-csnp-recv-rate
- (L10494)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-psnp-recv-rate
- (L10500)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-lsp-recv-rate
- (L10506)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-hello-send-rate
- (L10512)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-csnp-send-rate
- (L10518)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-psnp-send-rate
- (L10524)	{ISIS-TRAFFIC-GLOBAL-TYPE}/avg-lsp-send-rate
- (L10530)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-hello-recv-rate
- (L10536)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-csnp-recv-rate
- (L10542)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-psnp-recv-rate
- (L10548)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-lsp-recv-rate
- (L10554)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-hello-send-rate
- (L10560)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-csnp-send-rate
- (L10566)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-psnp-send-rate
- (L10572)	{ISIS-TRAFFIC-GLOBAL-TYPE}/peak-lsp-send-rate
- (L10593)	{ISIS-TRAFFIC-GLOBAL-TYPE}/maximum-iih-queue-length
- (L10598)	{ISIS-TRAFFIC-GLOBAL-TYPE}/maximum-pdu-queue-length
- (L10603)	{ISIS-TRAFFIC-GLOBAL-TYPE}/pdu-queue-length

## XPaths Modified

N/A

