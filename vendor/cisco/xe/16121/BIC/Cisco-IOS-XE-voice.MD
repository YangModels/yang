## Cisco-IOS-XE-voice.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
obsolete voice-card <slot>

### Reason
To fix backward incompatible issue in the model.

- /native/ios-voice:voice-card/ios-voice:slot

## XPaths Deprecated


## XPaths Modified

### Description
Enumeration has been reordered

### Reason
To implement new SIP line phase 2 Yang Model CLI's

- /native/ios-voice:dsapp/ios-voice:dsappline/ios-voice:line/ios-voice:feature/ios-voice:access-code

### Description
Change type of list voice-card from type uint8 to type ios-types:slot-bay-type which accepts input slot#/subslot#

### Reason
the original code was incorrect since the correct syntax for voice-card is voice-card slot#/subslot# not voice-card slot# for ISR4K

- /native/ios-voice:voice-card/ios-voice:id

### Description
Revert enum code changes for voip_ext

### Reason
To fix backward incompatibility

- /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:extension/ios-voice:voip_ext

## XPaths Added

### Reason 
New Xpaths added as part of the new SIP line phase 2 CLI's

- /native/ios-voice:dsapp/ios-voice:dsappline
- /native/ios-voice:dsapp/ios-voice:dsappline/
