## Cisco-IOS-XR-um-telemetry-model-driven-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added appropriate must statements and modified the existing must statements to a simpler format. These will not break actual cusomer's operation.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

- (L162)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/grpc
- (L188)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/tcp
- (L194)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/protocol/udp
- (L214)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/encoding/gpb
- (L220)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/encoding/self-describing-gpb
- (L226)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv4/address[address][port-number]/encoding/json
- (L261)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/grpc
- (L287)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/tcp
- (L293)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/protocol/udp
- (L313)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/encoding/gpb
- (L319)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/encoding/self-describing-gpb
- (L325)	/telemetry/model-driven/destination-groups/destination-group[destination-group-id]/address-family/ipv6/address[address][port-number]/encoding/json

## XPaths Removed

N/A

## XPaths Modified

N/A

