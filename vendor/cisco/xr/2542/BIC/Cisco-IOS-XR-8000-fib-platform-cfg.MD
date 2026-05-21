## Cisco-IOS-XR-8000-fib-platform-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

parent of load-balance changed to new container-class platform.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L349)	/cef/platform/load-balance/instances/instance[npu-instance]/hash-location[location-string]/npu-spa-seed
- (L356)	/cef/platform/load-balance/instances/instance[npu-instance]/hash-location[location-string]/npu-ecmp-seed
- (L380)	/cef/platform/load-balance/extended-entropy-auto-global
- (L386)	/cef/platform/load-balance/extended-entropy-auto-instance
- (L392)	/cef/platform/load-balance/spa-seed
- (L399)	/cef/platform/load-balance/auto-instance
- (L405)	/cef/platform/load-balance/auto-global
- (L411)	/cef/platform/load-balance/user-extended-entropy
- (L419)	/cef/platform/load-balance/ecmp-seed

## XPaths Modified

- (L134)	/cef/platform/load-balance/hash/rotate
- (L351)	/cef/platform/load-balance/instances/instance[npu-instance]/hash-location[location-string]/npu-rotate

