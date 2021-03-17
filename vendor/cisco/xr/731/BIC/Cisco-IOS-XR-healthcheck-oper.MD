## Cisco-IOS-XR-healthcheck-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Removed redundant leaves plane-up, plane-dn and plane-mcast-dn under health-check/metric-info/fabric-health/mdata/rack-mdata/ due to updates in the native model Cisco-IOS-XR-fabric-plane-health-oper revision 2019-04-05.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L513)	{HCMGR-FABRIC-HEALTH-METRIC-RACK-MDATA}/plane-up
- (L518)	{HCMGR-FABRIC-HEALTH-METRIC-RACK-MDATA}/plane-dn
- (L523)	{HCMGR-FABRIC-HEALTH-METRIC-RACK-MDATA}/plane-mcast-dn
- (L147)	{HCMGR-REPORT-METRIC-DATA}/health-msg

## XPaths Modified

- (L713)	{HCMGR-PLATFORM-METRIC-INFO}/card-redundancy-state

