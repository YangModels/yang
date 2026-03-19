## Cisco-IOS-XR-um-cont-optics-cfg.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Updated model as per 24I DT image CLI command. Updated add-drop-channel regex to match CLI command.Corrected range of egress-ampli-gain, ingress-ampli-gain and raman-tx-power/value as per CLI.

## XPaths Obsoleted

N/A

## XPaths Deprecated

- (L740)	/{CONT-BODY}/osri/off
- (L1072)	/{CONT-BODY}/ingress-ampli-osri/off
- (L1115)	/{CONT-BODY}/egress-ampli-osri/off
- (L1184)	/{CONT-BODY}/raman-osri/off

## XPaths Added

- (L1642)	/{CONT-BODY}/tone-pattern-expected
- (L1683)	/{CONT-BODY}/tone-pattern
- (L1694)	/{CONT-BODY}/ots-tone-pattern-expected

## XPaths Removed

- (L727)	/{CONT-BODY}/osri/on
- (L1064)	/{CONT-BODY}/ingress-ampli-osri/on
- (L1112)	/{CONT-BODY}/egress-ampli-osri/on
- (L1186)	/{CONT-BODY}/raman-osri/on

## XPaths Modified

N/A

