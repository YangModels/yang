## Cisco-IOS-XE-sla.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Need to mark nodes obsolete or deprecated to make it RFC compliant.

### Reason
Some of the nodes are not marked either as obsolete or deprecated while its parent node is, which makes it non RFC compliant.
Hence marked the status as obsolete or deprecated based on the status of the parent node.

- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:buckets-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:distributions-of-statistics-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:enhanced
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:enhanced/ios-sla:buckets
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:enhanced/ios-sla:interval
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:filter
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:hours-of-statistics-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:lives-kept
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ftp/ios-sla:get/ios-sla:history/ios-sla:statistics-distribution-interval

### Description
Choice and case nodes are not marked as deprecated or obsoleted while it's parent is marked as deprecated or obsolete.

### Reason
Some of the nodes are not marked either as obsolete or deprecated while its parent node is, which makes it non RFC compliant. Hence marked the status as obsolete or deprecated based on the status of the parent node.

- /native/ios-sla:auto/ios-sla:ip/ios-sla:sla/ios-sla:mpls-lsp-monitor/ios-sla:entry/ios-sla:type/ios-sla:type/ios-sla:jitter-case/ios-sla:jitter/ios-sla:vrf
- /native/ios-sla:auto/ios-sla:ip/ios-sla:sla/ios-sla:mpls-lsp-monitor/ios-sla:entry/ios-sla:type/ios-sla:type/ios-sla:jitter-case/ios-sla:jitter/ios-sla:vrf/ios-sla:ipsla-vrf-all-case/ios-sla:ipsla-vrf-all
- /native/ios-sla:auto/ios-sla:ip/ios-sla:sla/ios-sla:mpls-lsp-monitor/ios-sla:entry/ios-sla:type/ios-sla:type/ios-sla:jitter-case/ios-sla:jitter/ios-sla:vrf/ios-sla:vrf_container-case

## XPaths Deprecated

### Description
Need to mark nodes obsolete or deprecated to make it RFC compliant.

### Reason
Some of the nodes are not marked either as obsolete or deprecated while its parent node is, which makes it non RFC compliant. Hence marked the status as obsolete or deprecated based on the status of the parent node.

- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:burst
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:cos
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:domain
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:evc
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:name
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:source
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:source/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:source/ios-sla:mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:vlan
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:burst
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:cos
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:domain
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:evc
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:name
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:source
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:source/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:source/ios-sla:mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:vlan
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:udp-jitter/ios-sla:clock-tolerance/ios-sla:ntp
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:udp-jitter/ios-sla:clock-tolerance/ios-sla:ntp/ios-sla:oneway
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:udp-jitter/ios-sla:clock-tolerance/ios-sla:ntp/ios-sla:oneway/ios-sla:absolute
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:udp-jitter/ios-sla:clock-tolerance/ios-sla:ntp/ios-sla:oneway/ios-sla:percent

### Description
Choice and case nodes are not marked as deprecated or obsoleted while it's parent is marked as deprecated or obsolete.

### Reason
Some of the nodes are not marked either as obsolete or deprecated while its parent node is, which makes it non RFC compliant.Hence marked the status as obsolete or deprecated based on the status of the parent node.

- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:udp-jitter-case/ios-sla:udp-jitter/ios-sla:clock-tolerance/ios-sla:ntp/ios-sla:oneway/ios-sla:clock-tolerance-param
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:udp-jitter-case/ios-sla:udp-jitter/ios-sla:clock-tolerance/ios-sla:ntp/ios-sla:oneway/ios-sla:clock-tolerance-param/ios-sla:absolute-type
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:udp-jitter-case/ios-sla:udp-jitter/ios-sla:clock-tolerance/ios-sla:ntp/ios-sla:oneway/ios-sla:clock-tolerance-param/ios-sla:percent-type
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:evc-or-vlan
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:evc-or-vlan/ios-sla:evc
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:evc-or-vlan/ios-sla:vlan
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:mac-or-mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:mac-or-mpid/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:mac-or-mpid/ios-sla:mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:source/ios-sla:mac-or-mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:source/ios-sla:mac-or-mpid/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:delay/ios-sla:source/ios-sla:mac-or-mpid/ios-sla:mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:evc-or-vlan
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:evc-or-vlan/ios-sla:evc
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:evc-or-vlan/ios-sla:vlan
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:mac-or-mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:mac-or-mpid/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:mac-or-mpid/ios-sla:mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:source/ios-sla:mac-or-mpid
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:source/ios-sla:mac-or-mpid/ios-sla:mac-address
- /native/ip/ios-sla:sla/ios-sla:entry/ios-sla:sla-param/ios-sla:ethernet-case/ios-sla:ethernet/ios-sla:y1731/ios-sla:loss/ios-sla:source/ios-sla:mac-or-mpid/ios-sla:mpid

## XPaths Modified
N/A

## XPaths Added
N/A
