## Cisco-IOS-XE-object-group


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- /native/object-group/service/tcp-conf/tcp/tcp-src-dst-port-list-dst-op/source
- /native/object-group/service/tcp-conf/tcp/tcp-src-dst-port-list-op/source
- /native/object-group/service/tcp-udp/tcp-udp-src-dst-port-list-dst-op/source
- /native/object-group/service/tcp-udp/tcp-udp-src-dst-port-list-op/source

### Description

The key 'tcp-src-port dst-operator tcp-dst-port' is changed from 'tcp-src-port tcp-dst-port dst-operator'
The key 'src-operator tcp-src-port dst-operator tcp-dst-port' is changed from 'tcp-src-port src-operator dst-operator tcp-dst-port'
The key 'tcp-udp-src-port dst-operator tcp-udp-dst-port' is illegally changed from 'tcp-udp-src-port tcp-udp-dst-port dst-operator'
The key 'src-operator tcp-udp-src-port dst-operator tcp-udp-dst-port' is illegally changed from 'tcp-udp-src-port src-operator dst-operator tcp-udp-dst-port'

### Reason

Objectgroup model hardening for clis with source, destination ports

## XPaths Added

### Description
