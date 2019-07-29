## Cisco-IOS-XE-nhrp.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Handled backward compatibility changes for NHRP , by making old container "nhrp" status as obsolete

### Reason
Already implemented NHRP cli's are not working as functional and only ipv4 support is there in 16.11. so we are supporting IPV4 +IPV6 nhrp configs in 16.12.1

- /native/interface/Tunnel/ip/ios-nhrp:nhrp
- /native/interface/Tunnel/ip/ios-nhrp:nhrp/\*

"NOTE":
None of the child nodes under "- /native/interface/Tunnel/ip/ios-nhrp:nhrp" are obsoleted. This issue is being addresses currently and will be released in the next releases.

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

### Description
container "nhrp" moved to down in the file

### Revision
we are supporting IPV4 and IPV6 nhrp cli's. intial revision contains only ipv4. now made changes according to IOS Native CLI for IPV4 & IPV6. nhrp position remains same in yang tree

- /native/interface/Tunnel/ios-nhrp:if-state-tunnel/ios-nhrp:if-state/ios-nhrp:nhrp
- /native/interface/Tunnel/ios-nhrp:nhrp-tunn
- /native/interface/Tunnel/ios-nhrp:nhrp-tunn/\*
- /native/interface/Tunnel/ip/ios-nhrp:nhrp-v4
- /native/interface/Tunnel/ip/ios-nhrp:nhrp-v4/\*
- /native/interface/Tunnel/ipv6/ios-nhrp:nhrp
- /native/interface/Tunnel/ipv6/ios-nhrp:nhrp/\*
- /native/interface/Virtual-Template/ipv6/ios-nhrp:nhrp
- /native/interface/Virtual-Template/ipv6/ios-nhrp:nhrp/\*
- /native/interface/Virtual-Template/ios-nhrp:if-state-tunnel/ios-nhrp:if-state/ios-nhrp:nhrp
- /native/interface/Virtual-Template/ip/ios-nhrp:nhrp-v4
- /native/interface/Virtual-Template/ip/ios-nhrp:nhrp-v4/\*
- /native/interface/Virtual-Template/ios-nhrp:nhrp-tunn
- /native/interface/Virtual-Template/ios-nhrp:nhrp-tunn/\*
- /native/ios-nhrp:nhrp
- /native/ios-nhrp:nhrp/\*



