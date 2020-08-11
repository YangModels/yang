## Cisco-IOS-XE-controller.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/controller/SHDSL/dsl-group/efm-grp

- native/controller/SHDSL/dsl-group/efm-grp/\*

### Reason

CLI is no longer supported in controller mode, status is changed to obsoleted

## XPaths Deprecated

- native/controller/SHDSL/dsl-group/shdsl/four-wire/mode/enhanced/vendor-id-npsg

### Reason

In shdsl 4-wire, we were supposed to have a presence true container as it should act as a leaf as well.Hence deprecated the old nodes and added new one.

## XPaths Modified

- native/controller/SHDSL/dsl-group/efm-bond
- native/controller/SHDSL/dsl-group/handshake
- native/controller/SHDSL/dsl-group/m-pair
- native/controller/SHDSL/dsl-group/shdsl/annex
- native/controller/SHDSL/dsl-group/m-pair
- native/controller/SHDSL/dsl-group/shdsl/annex
- native/controller/SHDSL/dsl-group/handshake
- native/controller/SHDSL/dsl-group/shdsl/rate/enhanced

### Description

New When statement added

### Reason

In the SHDSL model, few of the leaf/containers were required only for a certain dsl-group or a termination.Henace added/modified few of them

- native/controller/SHDSL/dsl-group/shdsl/rate/enhanced
- native/controller/controller-tx-ex-list/line-termination
- native/controller/controller-tx-ex-list/trunk-group
- native/controller/controller-tx-ex-list/line-termination

### Description

Changed line-termination default value from 75-ohm to 120-ohm

### Reason

In the SHDSL model, few of the leaf/containers were required only for a certain dsl-group or a termination.Henace added/modified few of them

## XPaths Added

### Description
