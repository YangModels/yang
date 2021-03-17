## Cisco-IOS-XR-um-telemetry-model-driven-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Enable string length restrictions for tls-hostname that is missed in the model, but present in the code implementation.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

N/A

## XPaths Modified

- (L83)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-id]/sensor-group-id
- (L100)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-id]/sensor-paths/sensor-path[sensor-path-id]/sensor-path-id
- (L121)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destination-group-id
- (L180)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/grpc/tls-hostname
- (L279)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/grpc/tls-hostname
- (L400)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/protocol/grpc/tls-hostname
- (L472)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/subscription-id
- (L605)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/sensor-groups/sensor-group[sensor-group-id]/sensor-group-id
- (L658)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/destinations/destination[destination-id]/destination-id

