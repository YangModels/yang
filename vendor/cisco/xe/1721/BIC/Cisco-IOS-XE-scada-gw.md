## Cisco-IOS-XE-scada-gw.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description

Moved "scada" encapsulation to Cisco-IOS-XE-interfaces.yang

### Reason

vManage failed to recognize "scada" encapsulation when it was augmented from Cisco-IOS-XE-scada-gw.yang. Hence, moved it to common code in Cisco-IOS-XE-interfaces.yang

- /native/interface/Async/encapsulation/ios-scada-gw:scada

## XPaths Deprecated

N/A

## XPaths Modified

N/A

## XPaths Added

### Description

Moved "scada" encapsulation to Cisco-IOS-XE-interfaces.yang

### Reason

New Xpath added for the obsoleted node.

- /native/interface/Async/encapsulation/encap-choice/scada

