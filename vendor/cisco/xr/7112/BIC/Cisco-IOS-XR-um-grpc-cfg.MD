## Cisco-IOS-XR-um-grpc-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Added must statements under tls-cipher and address-family containers for mutually exclusive cases (these are missing constraints in the existing nodes thus practically does not break backward-compatibility).

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L188)	/grpc/address-family/ipv4
- (L194)	/grpc/address-family/ipv6
- (L200)	/grpc/address-family/dual
- (L567)	/grpc/tunnel/destinations/destination[destination-name][port-id]/address-family/ipv4
- (L573)	/grpc/tunnel/destinations/destination[destination-name][port-id]/address-family/ipv6
- (L518)	/grpc/tunnel/destinations/destination[destination-name][port-id]/destination-name
- (L528)	/grpc/tunnel/destinations/destination[destination-name][port-id]/port-id
- (L447)	/grpc/tls-cipher/default
- (L648)	/grpc/p4rt/locations/location[location-name][npu-id]/location-name
- (L207)	/grpc/service-layer
- (L489)	/grpc/tls-v1-disable

## XPaths Modified

- (L85)	/grpc/certificate-authentication
- (L90)	/grpc/tls-mutual
- (L289)	/grpc/local-connection
- (L326)	/grpc/segment-routing/traffic-eng/policy-service
- (L479)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]
- (L527)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]/address-family
- (L552)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]/source/ipv6/virtual/address
- (L565)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]/source/ipv4/virtual/address
- (L616)	/grpc/no-tls
- (L678)	/grpc/p4rt/locations/location[npu-location][npu-id]

