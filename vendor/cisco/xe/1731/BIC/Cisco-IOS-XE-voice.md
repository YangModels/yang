## Cisco-IOS-XE-voice


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

- native/voice/service/fax/fallback
- native/voice/service/fax/codec
- native/voice/service/fax/hs-redundancy
- native/voice/service/fax/ls-redundancy
- native/voice/service/fax/version

### Description

Obsoleted the nodes that was not working in the model.

## XPaths Deprecated

### Description

## XPaths Modified

- native/voice/register/pool
- native/dspfarm/profile/noise-reduction
- native/dspfarm/profile/plc
- native/dspfarm/profile/acoustic-shock-protection
- native/dspfarm/profile/call-progress-analysis
- native/dspfarm/profile/cng-fax-detect
- native/dspfarm/profile/codec/g711alaw
- native/dspfarm/profile/codec/g722-64
- native/dspfarm/profile/codec/g729abr8
- native/dspfarm/profile/codec/g729ar8
- native/dspfarm/profile/codec/g729br8
- native/dspfarm/profile/codec/g729r8
- native/dspfarm/profile/codec/ilbc
- native/dspfarm/profile/codec/pass-through
- native/dspfarm/profile/conference-join
- native/dspfarm/profile/conference-leave
- native/dspfarm/profile/dtmf
- native/dspfarm/profile/maximum/conference-participants
- native/dspfarm/profile/maximum/session
- native/sccp
- native/sccp-config/sccp/local
- native/trunk/group/translation-profile
- native/voice/register/global/max-pool

### Description

1. The container 'session' is removed.
2. New "when" constarint added.
3. The default 'false' is removed.
4. The container 'local' is changed to leaf.
5. The container 'translation-profile' is removed.
6. The default '2000' is removed.

## XPaths Added

### Description
