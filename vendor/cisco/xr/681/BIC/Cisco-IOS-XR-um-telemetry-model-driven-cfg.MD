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

- (L171)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/grpc
- (L197)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/tcp
- (L203)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/udp
- (L223)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/encoding/gpb
- (L229)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/encoding/self-describing-gpb
- (L235)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/encoding/json
- (L270)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/grpc
- (L296)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/tcp
- (L302)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/udp
- (L322)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/encoding/gpb
- (L328)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/encoding/self-describing-gpb
- (L334)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/encoding/json
- (L603)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/sensor-groups/sensor-group[sensor-group-id]

## XPaths Removed

N/A

## XPaths Modified

- (L85)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-id]/sensor-group-id
- (L102)	/telemetry/model-driven/sensor-groups/sensor-group[sensor-group-id]/sensor-paths/sensor-path[sensor-path-id]/sensor-path-id
- (L123)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/destination-group-id
- (L182)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/grpc/tls-hostname
- (L281)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/grpc/tls-hostname
- (L475)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/subscription-id
- (L609)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/sensor-groups/sensor-group[sensor-group-id]/sensor-group-id
- (L662)	/telemetry/model-driven/subscriptions/subscription[subscription-id]/destinations/destination[destination-id]/destination-id

