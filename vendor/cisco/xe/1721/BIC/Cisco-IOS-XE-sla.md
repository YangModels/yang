## Cisco-IOS-XE-sla.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Reason

In IPSLA, the probe creation and the modification modes are different. So to support the modification of the submode commands for each probe, a new container (modification-configuration) was defined under the list (- /native/ip/ios-sla:sla/ios-sla:entry) which will have all the sub-mode commands applicable for all the probes and all the nodes under each probe specific container are linked to the nodes under the modification-configuration container

- /native/ios-sla:auto/ios-sla:ip/ios-sla:sla/ios-sla:mpls-lsp-monitor/ios-sla:entry/ios-sla:modification-configuration
- /native/ios-sla:auto/ios-sla:ip/ios-sla:sla/ios-sla:mpls-lsp-monitor/ios-sla:entry/ios-sla:modification-configuration/\*
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:modification-configuration//native/ip/ios-sla:sla/ios-sla:entry/ios-sla:modification-configuration/\*
- /native/ip/ios-sla:sla/ios-sla:ethernet-monitor/ios-sla:entry/ios-sla:ethernet-monitor-modification-configuration
- /native/ip/ios-sla:sla/ios-sla:ethernet-monitor/ios-sla:entry/ios-sla:ethernet-monitor-modification-configuration/\*

## XPaths Deprecated

N/A

## XPaths Modified

### Description

Default value is changed from 255 to 30.

- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:mpls/ios-sla:lsp/ios-sla:trace/ios-sla:ipv4/ios-sla:ttl

## XPaths Added

N/A
