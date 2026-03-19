## Cisco-IOS-XR-pmengine-oper.yang

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Added](#xpaths-added)
- [XPaths Removed](#xpaths-removed)
- [XPaths Modified](#xpaths-modified)

### Description

Changed data type of some leaf nodes from uint32 to uint64.

## XPaths Obsoleted

N/A

## XPaths Deprecated

N/A

## XPaths Added

N/A

## XPaths Removed

- (L220)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-minute15/macsec-minute15secyifs
- (L235)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-minute15/macsec-minute15secyrxes
- (L250)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-minute15/macsec-minute15secytxes
- (L284)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-second30/macsec-second30secyifs
- (L299)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-second30/macsec-second30secyrxes
- (L329)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-second30/macsec-second30secytxes
- (L427)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-hour24/macsec-hour24secyifs
- (L442)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-hour24/macsec-hour24secyrxes
- (L457)	/performance-management/macsec/macsec-ports/macsec-port[name]/macsec-current/macsec-hour24/macsec-hour24secytxes
- (L559)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-minute15/fc-minute15fecs
- (L576)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-minute15/minute15fcs
- (L593)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-minute15/fc-minute15prbses
- (L610)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-minute15/fc-minute15pcses
- (L632)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-second30/fc-second30fecs
- (L649)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-second30/second30fcs
- (L666)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-second30/fc-second30prbses
- (L683)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-second30/fc-second30pcses
- (L778)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-hour24/fc-hour24prbses
- (L795)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-hour24/fc-hour24fcs
- (L812)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-hour24/fc-hour24pcses
- (L829)	/performance-management/fibre-channel/fc-ports/fc-port[name]/fc-current/fc-hour24/fc-hour24fecs
- (L1023)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-minute15/odu-minute15gfps
- (L1038)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-minute15/odu-minute15prbses
- (L1053)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-minute15/odu-minute15otnsecs
- (L1068)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-minute15/odu-minute15otns
- (L1151)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-second30/odu-second30prbses
- (L1166)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-second30/odu-second30otns
- (L1181)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-second30/odu-second30otnsecs
- (L1196)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-second30/odu-second30gfps
- (L1215)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-hour24/odu-hour24prbses
- (L1230)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-hour24/odu-hour24otnsecs
- (L1245)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-hour24/odu-hour24gfps
- (L1260)	/performance-management/odu/odu-ports/odu-port[name]/odu-current/odu-hour24/odu-hour24otns
- (L1354)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-minute15/otu-minute15fecs
- (L1369)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-minute15/otu-minute15otns
- (L1384)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-minute15/otu-minute15prbses
- (L1403)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-second30/otu-second30fecs
- (L1418)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-second30/otu-second30otns
- (L1433)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-second30/otu-second30prbses
- (L1501)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-hour24/otu-hour24fecs
- (L1516)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-hour24/otu-hour24prbses
- (L1531)	/performance-management/otu/otu-ports/otu-port[name]/otu-current/otu-hour24/otu-hour24otns
- (L1572)	/performance-management/stm/stm-ports/stm-port[name]/stm-current/stm-hour24/stm-hour24prbses
- (L1589)	/performance-management/stm/stm-ports/stm-port[name]/stm-current/stm-hour24/stm-hour24stms
- (L1630)	/performance-management/stm/stm-ports/stm-port[name]/stm-current/stm-minute15/stm-minute15prbses
- (L1647)	/performance-management/stm/stm-ports/stm-port[name]/stm-current/stm-minute15/stm-minute15stms
- (L1666)	/performance-management/stm/stm-ports/stm-port[name]/stm-current/stm-second30/stm-second30prbses
- (L1750)	/performance-management/sonet/sonet-ports/sonet-port[name]/sonet-current/sonet-minute15/sonet-minute15ocns
- (L1769)	/performance-management/sonet/sonet-ports/sonet-port[name]/sonet-current/sonet-hour24/sonet-hour24ocns
- (L1875)	/performance-management/optics/optics-ports/optics-port[name]/optics-current/optics-hour24/optics-hour24fecs
- (L1909)	/performance-management/optics/optics-ports/optics-port[name]/optics-current/optics-minute15/optics-minute15fecs
- (L1928)	/performance-management/optics/optics-ports/optics-port[name]/optics-current/optics-second30/optics-second30fecs
- (L2084)	/performance-management/cem/cem-ports/cem-port[name]/cem-current/cem-minute15/minute15cems
- (L2106)	/performance-management/cem/cem-ports/cem-port[name]/cem-current/cem-second30/second30cems
- (L2128)	/performance-management/cem/cem-ports/cem-port[name]/cem-current/cem-hour24/cem-hour24cems
- (L2219)	/performance-management/dwdm/dwdm-ports/dwdm-port[name]/dwdm-current/dwdm-minute15/dwdm-minute15fecs
- (L2249)	/performance-management/dwdm/dwdm-ports/dwdm-port[name]/dwdm-current/dwdm-minute15/dwdm-minute15otns
- (L2283)	/performance-management/dwdm/dwdm-ports/dwdm-port[name]/dwdm-current/dwdm-hour24/dwdm-hour24fecs
- (L2298)	/performance-management/dwdm/dwdm-ports/dwdm-port[name]/dwdm-current/dwdm-hour24/dwdm-hour24otns
- (L2339)	/performance-management/oc/oc-ports/oc-port[name]/oc-current/oc-hour24/oc-hour24prbses
- (L2356)	/performance-management/oc/oc-ports/oc-port[name]/oc-current/oc-hour24/oc-hour24ocns
- (L2375)	/performance-management/oc/oc-ports/oc-port[name]/oc-current/oc-minute15/oc-minute15prbses
- (L2392)	/performance-management/oc/oc-ports/oc-port[name]/oc-current/oc-minute15/oc-minute15ocns
- (L2411)	/performance-management/oc/oc-ports/oc-port[name]/oc-current/oc-second30/oc-second30prbses
- (L2502)	/performance-management/e1/e1-ports/e1-port[name]/e1-current/e1-minute15/e1-minute15e1s
- (L2521)	/performance-management/e1/e1-ports/e1-port[name]/e1-current/e1-hour24/e1-hour24e1s
- (L2645)	/performance-management/ethernet/ethernet-ports/ethernet-port[name]/ethernet-current/ethernet-second30/second30pcses
- (L2661)	/performance-management/ethernet/ethernet-ports/ethernet-port[name]/ethernet-current/ethernet-second30/ethernet-second30prbses
- (L2713)	/performance-management/ethernet/ethernet-ports/ethernet-port[name]/ethernet-current/ethernet-hour24/ethernet-hour24prbses
- (L2730)	/performance-management/ethernet/ethernet-ports/ethernet-port[name]/ethernet-current/ethernet-hour24/hour24pcses
- (L2745)	/performance-management/ethernet/ethernet-ports/ethernet-port[name]/ethernet-current/ethernet-hour24/ethernet-hour24fecs
- (L2780)	/performance-management/ethernet/ethernet-ports/ethernet-port[name]/ethernet-current/minute15/minute15pcses
- (L2812)	/performance-management/ethernet/ethernet-ports/ethernet-port[name]/ethernet-current/minute15/ethernet-minute15prbses
- (L2934)	/performance-management-history/global/periodic/sonet-history/sonet-port-histories/sonet-port-history[name]/sonet-minute15-history/sonet-minute15ocn-histories
- (L3031)	/performance-management-history/global/periodic/sonet-history/sonet-port-histories/sonet-port-history[name]/sonet-hour24-history/sonet-hour24ocn-histories
- (L3173)	/performance-management-history/global/periodic/cem-history/cem-port-histories/cem-port-history[name]/cem-second30-history/second30cem-histories
- (L3213)	/performance-management-history/global/periodic/cem-history/cem-port-histories/cem-port-history[name]/cem-hour24-history/cem-hour24cem-histories
- (L3253)	/performance-management-history/global/periodic/cem-history/cem-port-histories/cem-port-history[name]/cem-minute15-history/minute15cem-histories
- (L3310)	/performance-management-history/global/periodic/e1-history/e1-port-histories/e1-port-history[name]/e1-hour24-history/e1-hour24e1-histories
- (L3343)	/performance-management-history/global/periodic/e1-history/e1-port-histories/e1-port-history[name]/e1-minute15-history/e1-minute15e1-histories
- (L3395)	/performance-management-history/global/periodic/ethernet-history/ethernet-port-histories/ethernet-port-history[name]/ethernet-second30-history/ethernet-second30prbs-histories
- (L3430)	/performance-management-history/global/periodic/ethernet-history/ethernet-port-histories/ethernet-port-history[name]/ethernet-second30-history/second30pcs-histories
- (L3528)	/performance-management-history/global/periodic/ethernet-history/ethernet-port-histories/ethernet-port-history[name]/ethernet-hour24-history/hour24pcs-histories
- (L3559)	/performance-management-history/global/periodic/ethernet-history/ethernet-port-histories/ethernet-port-history[name]/ethernet-hour24-history/ethernet-hour24fec-histories
- (L3590)	/performance-management-history/global/periodic/ethernet-history/ethernet-port-histories/ethernet-port-history[name]/ethernet-hour24-history/ethernet-hour24prbs-histories
- (L3660)	/performance-management-history/global/periodic/ethernet-history/ethernet-port-histories/ethernet-port-history[name]/ethernet-minute15-history/minute15pcs-histories
- (L3756)	/performance-management-history/global/periodic/ethernet-history/ethernet-port-histories/ethernet-port-history[name]/ethernet-minute15-history/ethernet-minute15prbs-histories
- (L3813)	/performance-management-history/global/periodic/dwdm-history/dwdm-port-histories/dwdm-port-history[name]/dwdm-minute15-history/dwdm-minute15otn-histories
- (L3844)	/performance-management-history/global/periodic/dwdm-history/dwdm-port-histories/dwdm-port-history[name]/dwdm-minute15-history/dwdm-minute15fec-histories
- (L3911)	/performance-management-history/global/periodic/dwdm-history/dwdm-port-histories/dwdm-port-history[name]/dwdm-hour24-history/dwdm-hour24otn-histories
- (L3942)	/performance-management-history/global/periodic/dwdm-history/dwdm-port-histories/dwdm-port-history[name]/dwdm-hour24-history/dwdm-hour24fec-histories
- (L4027)	/performance-management-history/global/periodic/stm-history/stm-port-histories/stm-port-history[name]/stm-hour24-history/stm-hour24stm-histories
- (L4058)	/performance-management-history/global/periodic/stm-history/stm-port-histories/stm-port-history[name]/stm-hour24-history/stm-hour24prbs-histories
- (L4097)	/performance-management-history/global/periodic/stm-history/stm-port-histories/stm-port-history[name]/stm-minute15-history/stm-minute15stm-histories
- (L4128)	/performance-management-history/global/periodic/stm-history/stm-port-histories/stm-port-history[name]/stm-minute15-history/stm-minute15prbs-histories
- (L4168)	/performance-management-history/global/periodic/stm-history/stm-port-histories/stm-port-history[name]/stm-second30-history/stm-second30prbs-histories
- (L4225)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-minute15-history/macsec-minute15secyrx-histories
- (L4289)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-minute15-history/macsec-minute15secytx-histories
- (L4321)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-minute15-history/macsec-minute15secyif-histories
- (L4388)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-hour24-history/macsec-hour24secytx-histories
- (L4419)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-hour24-history/macsec-hour24secyif-histories
- (L4450)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-hour24-history/macsec-hour24secyrx-histories
- (L4485)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-second30-history/macsec-second30secyrx-histories
- (L4547)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-second30-history/macsec-second30secytx-histories
- (L4578)	/performance-management-history/global/periodic/macsec-history/macsec-port-histories/macsec-port-history[name]/macsec-second30-history/macsec-second30secyif-histories
- (L4631)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-hour24-history/odu-hour24gfp-histories
- (L4662)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-hour24-history/odu-hour24prbs-histories
- (L4693)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-hour24-history/odu-hour24otn-histories
- (L4728)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-second30-history/odu-second30otn-histories
- (L4759)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-second30-history/odu-second30prbs-histories
- (L4790)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-second30-history/odu-second30gfp-histories
- (L4825)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-minute15-history/odu-minute15prbs-histories
- (L4856)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-minute15-history/odu-minute15gfp-histories
- (L4887)	/performance-management-history/global/periodic/odu-history/odu-port-histories/odu-port-history[name]/odu-minute15-history/odu-minute15otn-histories
- (L4940)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-second30-history/otu-second30fec-histories
- (L4971)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-second30-history/otu-second30prbs-histories
- (L5002)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-second30-history/otu-second30otn-histories
- (L5037)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-minute15-history/otu-minute15fec-histories
- (L5068)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-minute15-history/otu-minute15prbs-histories
- (L5099)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-minute15-history/otu-minute15otn-histories
- (L5134)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-hour24-history/otu-hour24prbs-histories
- (L5165)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-hour24-history/otu-hour24otn-histories
- (L5196)	/performance-management-history/global/periodic/otu-history/otu-port-histories/otu-port-history[name]/otu-hour24-history/otu-hour24fec-histories
- (L5338)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-minute15-history/fc-minute15fec-histories
- (L5373)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-minute15-history/fc-minute15prbs-histories
- (L5408)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-minute15-history/minute15fc-histories
- (L5443)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-minute15-history/fc-minute15pcs-histories
- (L5483)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-second30-history/fc-second30fec-histories
- (L5518)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-second30-history/fc-second30prbs-histories
- (L5553)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-second30-history/fc-second30pcs-histories
- (L5588)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-second30-history/second30fc-histories
- (L5628)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-hour24-history/fc-hour24pcs-histories
- (L5663)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-hour24-history/fc-hour24fec-histories
- (L5698)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-hour24-history/fc-hour24fc-histories
- (L5733)	/performance-management-history/global/periodic/fc-history/fc-port-histories/fc-port-history[name]/fc-hour24-history/fc-hour24prbs-histories
- (L5821)	/performance-management-history/global/periodic/optics-history/optics-port-histories/optics-port-history[name]/optics-hour24-history/optics-hour24fec-histories
- (L5887)	/performance-management-history/global/periodic/optics-history/optics-port-histories/optics-port-history[name]/optics-second30-history/optics-second30fec-histories
- (L5953)	/performance-management-history/global/periodic/optics-history/optics-port-histories/optics-port-history[name]/optics-minute15-history/optics-minute15fec-histories
- (L6007)	/performance-management-history/global/periodic/oc-history/oc-port-histories/oc-port-history[name]/oc-second30-history/oc-second30prbs-histories
- (L6046)	/performance-management-history/global/periodic/oc-history/oc-port-histories/oc-port-history[name]/oc-hour24-history/oc-hour24prbs-histories
- (L6081)	/performance-management-history/global/periodic/oc-history/oc-port-histories/oc-port-history[name]/oc-hour24-history/oc-hour24ocn-histories
- (L6116)	/performance-management-history/global/periodic/oc-history/oc-port-histories/oc-port-history[name]/oc-minute15-history/oc-minute15ocn-histories
- (L6147)	/performance-management-history/global/periodic/oc-history/oc-port-histories/oc-port-history[name]/oc-minute15-history/oc-minute15prbs-histories

## XPaths Modified

N/A

