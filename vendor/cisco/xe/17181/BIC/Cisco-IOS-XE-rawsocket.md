## Cisco-IOS-XE-rawsocket.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/line/async-line/raw-socket
- native/line/async-line/raw-socket/packet-length
- native/line/async-line/raw-socket/packet-length/fragment-off
- native/line/async-line/raw-socket/packet-length/packet-length-value
- native/line/async-line/raw-socket/packet-timer
- native/line/async-line/raw-socket/special-char
- native/line/async-line/raw-socket/tcp
- native/line/async-line/raw-socket/tcp/client
- native/line/async-line/raw-socket/tcp/client/destination-ip
- native/line/async-line/raw-socket/tcp/client/destination-port
- native/line/async-line/raw-socket/tcp/client/optional-local-ip
- native/line/async-line/raw-socket/tcp/client/optional-local-port
- native/line/async-line/raw-socket/tcp/dscp
- native/line/async-line/raw-socket/tcp/idle-timeout
- native/line/async-line/raw-socket/tcp/server
- native/line/async-line/raw-socket/tcp/server/local-ip
- native/line/async-line/raw-socket/tcp/server/local-port
- native/line/async-line/raw-socket/tcp/tcp-session
- native/line/async-line/raw-socket/udp
- native/line/async-line/raw-socket/udp/connection
- native/line/async-line/raw-socket/udp/connection/destination-ip
- native/line/async-line/raw-socket/udp/connection/destination-port
- native/line/async-line/raw-socket/udp/connection/local-port
- native/line/async-line/raw-socket/udp/connection/optional-local-ip

### Description

Status changed from deprecated to obsolete.

## XPaths Deprecated

### Description

## XPaths Modified

- config-rawsocket-grouping(grouping)/tcp/idle-timeout

### Description

Base type has been changed from uint8 to uint16.

### Description

The default 300 is changed from 5.

- native/line/async-line-range/raw-socket/tcp/idle-timeout
- native/line/async-line-single/raw-socket/tcp/idle-timeout

### Description

The grouping 'config-rawsocket-grouping-deprecated is removed.

- config-rawsocket-grouping-deprecated(grouping)

### Description

The if-feature 'ios-features:serial-pseudowire' is added in container raw-socket.

- native/interface/Loopback/raw-socket

## XPaths Added

### Description
