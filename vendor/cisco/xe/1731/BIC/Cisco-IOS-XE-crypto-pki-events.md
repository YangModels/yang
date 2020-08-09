## Cisco-IOS-XE-crypto-pki-events.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

## XPaths Deprecated

### Description

## XPaths Modified

- crypto-pki-events

### Description

The container 'crypto-pki-events' is removed.

### Reason

TDL2Yang "events" models hold notifications. Due to an oversight when generating the models, in previous releases they also contained empty containers matching the name of the model. These containers are guaranteed to be empty and do not provide any data externally.

## XPaths Added

### Description
