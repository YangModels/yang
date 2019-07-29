## Cisco-IOS-XE-nbar.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Obsoleting unsupported nodes

### Reason
Yang model was not updated when CLI was removed/changed

- /native/ip/ios-nbar:nbar/ios-nbar:attribute-map/ios-nbar:attribute/ios-nbar:p2p-technology
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:direction
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:direction/ios-nbar:destination
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:direction/ios-nbar:source
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number0
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number1
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number2
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number3
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number4
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number5
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number6
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:port-numbers/ios-nbar:port-number7
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:range
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:range/ios-nbar:end-range
- /native/ip/ios-nbar:nbar/ios-nbar:custom/ios-nbar:ip/\*/ios-nbar:port/ios-nbar:range/ios-nbar:start-range

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

### Description
Added "ip nbar resources" and transport containers

### Reason
Yang model was not updated when CLI was removed/changed.

- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport
- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport/ios-nbar:application-updates
- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport/ios-nbar:application-updates/ios-nbar:ftp
- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport/ios-nbar:application-updates/ios-nbar:ftp/ios-nbar:url-prefix
- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport/ios-nbar:application-updates/ios-nbar:http
- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport/ios-nbar:application-updates/ios-nbar:http/ios-nbar:url-prefix
- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport/ios-nbar:application-updates/ios-nbar:https
- /native/avc/ios-nbar:sd-service/ios-nbar:controller/ios-nbar:transport/ios-nbar:application-updates/ios-nbar:https/ios-nbar:url-prefix
- /native/ip/ios-nbar:nbar/ios-nbar:resources
- /native/ip/ios-nbar:nbar/ios-nbar:resources/ios-nbar:flow
- /native/ip/ios-nbar:nbar/ios-nbar:resources/ios-nbar:flow/ios-nbar:max-session
- /native/ip/ios-nbar:nbar/ios-nbar:resources/ios-nbar:protocol
- /native/ip/ios-nbar:nbar/ios-nbar:resources/ios-nbar:protocol/ios-nbar:link-age
- /native/ip/ios-nbar:nbar/ios-nbar:resources/ios-nbar:protocol/ios-nbar:protocol-name





