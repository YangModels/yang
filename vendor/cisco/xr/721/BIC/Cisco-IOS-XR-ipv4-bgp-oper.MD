## Cisco-IOS-XR-ipv4-bgp-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

More flag bits were added for epe peerset feature which required extending 1 byte flag to 2 bytes. Some prefix-sid related leaf and container names in BGP did not follow the naming convention. Moreover, as SRv6 draft moved from v4 to v6 new leaves were added and old ones were removed.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L1215)	/{AF-TABLE}/afs/af[af-name]/epes
- (L2752)	{BGP-EDM-LOCATOR-ENTRY}/stale
- (L5132)	{BGP-PROCESS-INFO-GBL}/prefix-sids-rv6vpnsid-count
- (L5137)	{BGP-PROCESS-INFO-GBL}/prefix-sids-rv6vpnsid-memory
- (L6465)	{BGP-GLOBAL-PROCESS-INFO-GBL}/gshut-all-nbrs-ts
- (L6470)	{BGP-GLOBAL-PROCESS-INFO-GBL}/gshu-all-nbrs-age
- (L9497)	{BGP-EPE-SET-BAG}/epe-key-length-xr
- (L9947)	{BGP-NET-BAG}/has-s-rv6sid-allocated
- (L9952)	{BGP-NET-BAG}/srv6sid-address
- (L9957)	{BGP-NET-BAG}/srv6sid-address-len
- (L12149)	{BGP-RPC-SET-BAG}/srv6sid-address
- (L12154)	{BGP-RPC-SET-BAG}/srv6sid-address-len
- (L13843)	{BGP-COMMON-ATTR-ENTRY}/prefix-sids-rv6vpnsid
- (L13848)	{BGP-COMMON-ATTR-ENTRY}/prefix-sid-unk-tl-vs
- (L13942)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sid-label-indexpresent
- (L13947)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sid-orig-srg-bpresent
- (L13952)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sids-rv6vpnsi-dpresent
- (L13957)	{BGP-COMMON-ATTR-ENTRY}/is-prefix-sid-unk-tl-vspresent
- (L16732)	{BGP-AF-INDEP}/suppress4-byte-as

## XPaths Modified

- (L7623)	{BGP-EPE-SET-BAG}/epe-flags
- (L16050)	{BGP-CONFIG-RELATIVES-BAG}/address-family-identifier
- (L16688)	{BGP-CONFIG-ENTID}/bgp-config-entid/address-family-identifier
- (L17797)	{BGP-CONFIG-ENTITY-BAG}/address-family-identifier

