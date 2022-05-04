## Cisco-IOS-XR-l2rib-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

A new cability to configure an infinite retry-count for mac mobility freeze criteria was added. The default value is set to be infinite, which is internally the value 1001, this could be misleading if populated in the yang response. So, making the default none to skip showing anything when 'dd-params-infinite-retry-count' is true.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L70)	/{DUPLICATE-DETECTION}/duplicate-detection/retry-count

## XPaths Modified

N/A

