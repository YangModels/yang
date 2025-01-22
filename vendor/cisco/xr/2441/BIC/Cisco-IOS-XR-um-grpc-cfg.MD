## Cisco-IOS-XR-um-grpc-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updating model for um2 changes.

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
- (L489)	/grpc/tls-v1-disable

## XPaths Modified

- (L93)	/grpc/certificate-authentication
- (L98)	/grpc/tls-mutual
- (L321)	/grpc/local-connection
- (L368)	/grpc/segment-routing/traffic-eng/policy-service
- (L521)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]
- (L569)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]/address-family
- (L594)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]/source/ipv6/virtual/address
- (L607)	/grpc/tunnel/destinations/destination[grpc-tunnel-destination][port-number]/source/ipv4/virtual/address
- (L658)	/grpc/no-tls
- (L669)	/grpc/gribi/port
- (L684)	/grpc/p4rt/port
- (L720)	/grpc/p4rt/locations/location[npu-location][npu-id]
- (L780)	/grpc/gnmi/port

