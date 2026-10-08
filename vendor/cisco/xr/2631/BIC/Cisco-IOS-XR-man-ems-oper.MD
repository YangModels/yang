## Cisco-IOS-XR-man-ems-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Remove the CLI show grpc status.Show grpc CLI serves the purpose. Removed status container under gRPC after removing the show grpc status CLI.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L841)	{GRPC-SERVER-INFO-B}
- (L842)	{GRPC-SERVER-INFO-B}/address-family
- (L847)	{GRPC-SERVER-INFO-B}/port
- (L852)	{GRPC-SERVER-INFO-B}/listen-address-count
- (L857)	{GRPC-SERVER-INFO-B}/vrf
- (L862)	{GRPC-SERVER-INFO-B}/local-connection
- (L867)	{GRPC-SERVER-INFO-B}/tls
- (L872)	{GRPC-SERVER-INFO-B}/tls-mutual
- (L877)	{GRPC-SERVER-INFO-B}/trustpoint
- (L882)	{GRPC-SERVER-INFO-B}/common-name
- (L887)	{GRPC-SERVER-INFO-B}/metadata-auth
- (L892)	{GRPC-SERVER-INFO-B}/dscp
- (L897)	{GRPC-SERVER-INFO-B}/cipher-default
- (L902)	{GRPC-SERVER-INFO-B}/cipher-enable
- (L908)	{GRPC-SERVER-INFO-B}/cipher-disable
- (L914)	{GRPC-SERVER-INFO-B}/oper-cipher-enable
- (L920)	{GRPC-SERVER-INFO-B}/oper-cipher-disable
- (L926)	{GRPC-SERVER-INFO-B}/enable
- (L931)	{GRPC-SERVER-INFO-B}/server-disable-reason
- (L936)	{GRPC-SERVER-INFO-B}/ttl
- (L941)	{GRPC-SERVER-INFO-B}/server-name
- (L946)	{GRPC-SERVER-INFO-B}/keepalive-enforcement-min-time
- (L953)	{GRPC-SERVER-INFO-B}/keepalive-timeout
- (L959)	{GRPC-SERVER-INFO-B}/keepalive-time
- (L965)	{GRPC-SERVER-INFO-B}/max-concurrent-streams
- (L970)	{GRPC-SERVER-INFO-B}/min-tls-version
- (L975)	{GRPC-SERVER-INFO-B}/max-tls-version
- (L980)	{GRPC-SERVER-INFO-B}/latest-connection-id
- (L985)	{GRPC-SERVER-INFO-B}/service-count
- (L990)	{GRPC-SERVER-INFO-B}/server-id
- (L995)	{GRPC-SERVER-INFO-B}/certificate-id
- (L1000)	{GRPC-SERVER-INFO-B}/max-preauth-conns
- (L1006)	{GRPC-SERVER-INFO-B}/auth-deadline
- (L1012)	{GRPC-SERVER-INFO-B}/preauth-rejected-per-source
- (L1018)	{GRPC-SERVER-INFO-B}/preauth-dropped-auth-deadline
- (L1024)	{GRPC-SERVER-INFO-B}/laddr
- (L1030)	{GRPC-SERVER-INFO-B}/service
- (L570)	{GRPC-STATE}/address-family
- (L575)	{GRPC-STATE}/port
- (L580)	{GRPC-STATE}/gnmi-port
- (L585)	{GRPC-STATE}/p4rt-port
- (L590)	{GRPC-STATE}/gribi-port
- (L595)	{GRPC-STATE}/listen-address-count
- (L600)	{GRPC-STATE}/vrf
- (L605)	{GRPC-STATE}/tls
- (L610)	{GRPC-STATE}/tls-mutual
- (L615)	{GRPC-STATE}/trustpoint
- (L620)	{GRPC-STATE}/common-name
- (L625)	{GRPC-STATE}/cert-auth
- (L630)	{GRPC-STATE}/tlsv1-0
- (L660)	{GRPC-STATE}/dscp
- (L665)	{GRPC-STATE}/cipher-default
- (L670)	{GRPC-STATE}/cipher-enable
- (L676)	{GRPC-STATE}/cipher-disable
- (L682)	{GRPC-STATE}/oper-cipher-enable
- (L688)	{GRPC-STATE}/oper-cipher-disable
- (L694)	{GRPC-STATE}/server
- (L699)	{GRPC-STATE}/server-disable-reason
- (L704)	{GRPC-STATE}/ttl
- (L709)	{GRPC-STATE}/server-name
- (L714)	{GRPC-STATE}/keepalive-enforcement-min-time
- (L721)	{GRPC-STATE}/keepalive-timeout
- (L727)	{GRPC-STATE}/keepalive-time
- (L733)	{GRPC-STATE}/max-concurrent-streams
- (L738)	{GRPC-STATE}/min-tls-version
- (L743)	{GRPC-STATE}/max-tls-version
- (L748)	{GRPC-STATE}/latest-connection-id
- (L753)	{GRPC-STATE}/local-connection
- (L758)	{GRPC-STATE}/laddr
- (L115)	/grpc/certificate
- (L135)	/grpc/streams
- (L150)	/grpc/srte
- (L190)	/grpc/connections
- (L220)	/grpc/tunnel
- (L248)	/grpc/statistics
- (L11)	/

## XPaths Modified

N/A

