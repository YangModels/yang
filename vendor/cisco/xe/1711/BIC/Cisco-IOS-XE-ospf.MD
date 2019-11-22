## Cisco-IOS-XE-ospf.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Reason

Obsoleted all the the paths in Cisco-IOS-XE-ospf-obsoleted.yang file. Later moved SD-WAN used commands to deperecated.

- /native/interface/*/ip/ios-ospf:ospf
- /native/interface/*/ip/ios-ospf:ospf/*

### Description

The leaf is not a valid option in IOS CLI.

### Reason

Leaf got wrongly added, no mapping is availble so obsoleted the leaf

- /native/router/ios-ospf:router-ospf/ios-ospf:ospf/ios-ospf:process-id/ios-ospf:fast-reroute/ios-ospf:per-prefix/ios-ospf:tie-break/ios-ospf:lowest-metric/ios-ospf:required

### Description

The old leaf was not working properly, mapping was not possible due to dependencies.

### Reason

Mapping is not feasible, moved the leaf from deprecate to obsolete

- /native/router/ios-ospf:router-ospf/ios-ospf:ospf/ios-ospf:process-id/ios-ospf:domain-id/ios-ospf:ip-format-secondary/ios-ospf:secondary
- /native/router/ios-ospf:router-ospf/ios-ospf:ospf/ios-ospf:process-id-vrf/ios-ospf:domain-id/ios-ospf:ip-format-secondary/ios-ospf:secondary

### Description

OSPF model is rewritten newly in 16.12 by obsoleting/deprecating old model, but at few places it missed out marking child node status ad obsolete/deprecated.

### Reason

Marking child nodes obsoleted, it was using a common group where it is being used by other models, had to bring the content and obsolete them

- /native/router/ios-ospf:ospf/ios-ospf:passive-interface
- /native/router/ios-ospf:ospf/ios-ospf:passive-interface/ios-ospf:default
- /native/router/ios-ospf:ospf/ios-ospf:passive-interface/ios-ospf:interface
- /native/router/ios-ospf:ospf/ios-ospf:disable
- /native/router/ios-ospf:ospf/ios-ospf:disable/ios-ospf:passive-interface
- /native/router/ios-ospf:ospf/ios-ospf:disable/ios-ospf:passive-interface/ios-ospf:interface

## XPaths Deprecated

### Description

Moved the leafs to deprecated from obsolete which are used by SD-WAN.

- /native/router/ios-ospf:ospf
- /native/router/ios-ospf:ospf/ios-ospf:id
- /native/router/ios-ospf:ospf/ios-ospf:vrf
- /native/router/ios-ospf:ospf/ios-ospf:area/*
- /native/router/ios-ospf:ospf/ios-ospf:auto-cost/*
- /native/router/ios-ospf:ospf/ios-ospf:max-metric/*
- /native/router/ios-ospf:ospf/ios-ospf:timers/*
- /native/router/ios-ospf:ospf/ios-ospf:router-id
- /native/router/ios-ospf:ospf/ios-ospf:compatible
- /native/router/ios-ospf:ospf/ios-ospf:default-information/*
- /native/router/ios-ospf:ospf/ios-ospf:distance/*
- /native/router/ios-ospf:ospf/ios-ospf:redistribute/*
- /native/router/ios-ospf:ospf/ios-ospf:table-map/*

## XPaths Modified

N/A

## XPaths Added

N/A

