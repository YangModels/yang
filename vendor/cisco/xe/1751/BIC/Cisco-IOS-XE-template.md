## Cisco-IOS-XE-template.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/template/type/pseudowire/control-word

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- native/template/type/pseudowire/preferred-path/interface
- native/template/type/pseudowire/preferred-path/peer-container
- native/template/type/pseudowire/preferred-path/segment-routing/traffic-eng/attribute-set
- native/template/type/pseudowire/preferred-path/segment-routing/traffic-eng/policy
- native/template/type/pseudowire/signaling
- native/template/type/pseudowire/preferred-path
- native/template/type/pseudowire/status
- interface-grouping(grouping)/interface-choice/Loopback/Loopback
- native/template/type/pseudowire/signaling

### Description

1. A new must expression added
2. A new when expression added
3. The range '[(0, 2147483647)]' is added
4. This when expression may be different than before

### Reason

Loopback range in yang interface-grouping was 0-4294967295. However, from device side loopback interface can only support range from 0 to 2147483647. Hence loopback range in yang was modified to be inline with device range.

## XPaths Added

### Description
