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

- (L792)	/telemetry/model-driven/gnmi/bundling/size
- (L793)	/telemetry/model-driven/gnmi/bundling/size
- (L383)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/address-family/ipv4
- (L389)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/address-family/ipv6
- (L399)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/protocol/grpc
- (L427)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/protocol/tcp
- (L433)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/protocol/udp
- (L453)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/encoding/gpb
- (L459)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/encoding/self-describing-gpb
- (L465)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/encoding/json
- (L360)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/destination-name
- (L370)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destinations/destination[destination-name][port-number]/port-number
- (L131)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destination-group-id
- (L151)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family
- (L483)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/subscription-id
- (L609)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/sensor-groups
- (L674)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/destinations
- (L110)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-id]/sensor-paths/sensor-path[sensor-path-id]/sensor-path-id
- (L93)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-id]/sensor-group-id

## XPaths Modified

- (L114)	/telemetry/model-driven/strict-timer
- (L146)	/telemetry/model-driven/include/select-leaves-on-events
- (L154)	/telemetry/model-driven/include/empty/values
- (L167)	/telemetry/model-driven/gnmi/heartbeat/always
- (L193)	/telemetry/model-driven/destination-groups/destination-group[destination-group-string]
- (L335)	/telemetry/model-driven/destination-groups/destination-group[destination-group-string]/destinations/destination[destination-string][port]
- (L358)	/telemetry/model-driven/destination-groups/destination-group[destination-group-string]/destinations/destination[destination-string][port]/address-family
- (L433)	/telemetry/model-driven/destination-groups/destination-group[destination-group-string]/destinations/destination[destination-string][port]/encoding
- (L462)	/telemetry/model-driven/subscriptions/subscription[subscription-string]
- (L711)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-string]
- (L728)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-string]/sensor-paths/sensor-path[sensor-path-string]

