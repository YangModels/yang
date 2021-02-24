## Cisco-IOS-XR-um-policymap-classmap-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Deprecated YANG-XML unsupported class-map features/containers. Ipv4/Ipv6/Ethernet match-access-group have been moved as leaf-list.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1693)	/{match-flow-key}/flow-key/flow-cache/max-count
- (L3056)	/{pbr-actions}/copy
- (L3157)	/{pbr-actions}/punt
- (L4015)	/{performance-traffic-actions}/react[operation-id]/trigger/value/upper-number
- (L4055)	/{performance-traffic-actions}/react[operation-id]/action/clone
- (L3912)	/{performance-traffic-actions}/react[operation-id]/rtp-loss-fraction
- (L3917)	/{performance-traffic-actions}/react[operation-id]/rtp-jitter
- (L3922)	/{performance-traffic-actions}/react[operation-id]/rtp-max-jitter
- (L3927)	/{performance-traffic-actions}/react[operation-id]/rtp-out-of-order
- (L3932)	/{performance-traffic-actions}/react[operation-id]/rtp-loss-pkts
- (L3937)	/{performance-traffic-actions}/react[operation-id]/rtp-transport-availability
- (L3942)	/{performance-traffic-actions}/react[operation-id]/rtp-error-seconds
- (L3947)	/{performance-traffic-actions}/react[operation-id]/mdi-mlr
- (L3952)	/{performance-traffic-actions}/react[operation-id]/mdi-mdc
- (L3957)	/{performance-traffic-actions}/react[operation-id]/mdi-jitter
- (L3962)	/{performance-traffic-actions}/react[operation-id]/mpeg-loss-pkts
- (L3967)	/{performance-traffic-actions}/react[operation-id]/mdi-transport-availability
- (L3972)	/{performance-traffic-actions}/react[operation-id]/mdi-error-seconds
- (L3516)	/{performance-traffic-actions}/flow
- (L3534)	/{performance-traffic-actions}/monitor
- (L4531)	/{qos-actions}/police/bucket
- (L5486)	/policy-map/type/accounting[policy-map-name]/class[name][type]
- (L255)	/
- (L465)	/
- (L470)	/
- (L475)	/
- (L510)	/
- (L525)	/
- (L575)	/
- (L580)	/
- (L585)	/
- (L590)	/
- (L595)	/
- (L600)	/
- (L605)	/
- (L610)	/
- (L615)	/
- (L620)	/
- (L625)	/
- (L630)	/
- (L645)	/
- (L680)	/
- (L725)	/
- (L730)	/
- (L2817)	/{accounting-actions}

## XPaths Modified

- (L1242)	/{match-access-group}/access-group/ipv4
- (L1248)	/{match-access-group}/access-group/ipv6
- (L1254)	/{match-access-group}/access-group/ethernet-services
- (L3827)	/{qos-actions}/police/rate

