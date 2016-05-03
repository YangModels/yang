## YANG Models for Cisco IOS-XR 5.3.2

The YANG files in this directory detail the YANG models supported by IOS-XR 5.3.2 releases. The schemas here may also be retrieved from devices running IOS-XR 5.3.2 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

### Compliance With "pyang --ietf"

The YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the "--ietf" flag. The errors and warnings exhibited by running pyang with the "--ietf" flag are currently deemed to be non-critical. A script has been provided, "check-models.sh", that runs pyang with IETF validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

Please note that as of writing, pyang is being updated to change the behavior of the "--ietf" flag when pyang is run against non-IETF modules. The changes will suppress IETF-specific warnings that do not apply to non-IETF modules.

### Revision Statements

From IOS-XR 5.3.2 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs.

### Backwards Compatibility Issues

It should be noted that some of the modules released in IOX-XR 5.3.2 do break the backwards compatibility guidelines defined in RFC 6020. This is because the "native" YANG modules for IOS-XR are generated from internal schema files that are an integral part of the implementation, and, as such, these can change when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Cisco cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the "check-models.sh" script, in conjunction with pyang 1.5, can be used to determine what technically incompatible changes have occurred.

The modules which have incompatible changes, along with the reported pyang incompatibility errors, in IOS-XR 5.3.2 when compared to IOS-XR 5.3.1 are:


#### Cisco-IOS-XR-drivers-media-eth-oper-sub1.yang

    Cisco-IOS-XR-drivers-media-eth-oper-sub1.yang:1: error: new revision 2015-01-07 is not newer than old revision 2015-01-07 (RFC 6020: 10, p2)
    Cisco-IOS-XR-drivers-media-eth-oper-sub1.yang:2076: error: the base type has illegally changed from uint32 to int32
    Cisco-IOS-XR-drivers-media-eth-oper-sub1.yang:2081: error: the base type has illegally changed from uint32 to int32

#### Cisco-IOS-XR-infra-syslog-cfg.yang

    Cisco-IOS-XR-infra-syslog-cfg.yang:1: error: the typedef 'Log-severity', defined at ../531/Cisco-IOS-XR-infra-syslog-cfg.yang:269 is illegally removed
    Cisco-IOS-XR-infra-syslog-cfg.yang:552: error: the container 'ipv6-severity-levels', defined at ../531/Cisco-IOS-XR-infra-syslog-cfg.yang:527 is illegally removed
    Cisco-IOS-XR-infra-syslog-cfg.yang:622: error: the container 'host-name-severities', defined at ../531/Cisco-IOS-XR-infra-syslog-cfg.yang:561 is illegally removed
    Cisco-IOS-XR-infra-syslog-cfg.yang:692: error: the container 'ipv4-severity-levels', defined at ../531/Cisco-IOS-XR-infra-syslog-cfg.yang:595 is illegally removed

#### Cisco-IOS-XR-ipv4-io-oper-sub2.yang

    Cisco-IOS-XR-ipv4-io-oper-sub2.yang:1: error: new revision 2015-01-07 is not newer than old revision 2015-01-07 (RFC 6020: 10, p2)
    Cisco-IOS-XR-ipv4-io-oper-sub2.yang:188: error: the leaf 'common-in-bound', defined at ../531/Cisco-IOS-XR-ipv4-io-oper-sub2.yang:196 is illegally removed
    Cisco-IOS-XR-ipv4-io-oper-sub2.yang:188: error: the leaf 'common-out-bound', defined at ../531/Cisco-IOS-XR-ipv4-io-oper-sub2.yang:201 is illegally removed
    Cisco-IOS-XR-ipv4-io-oper-sub2.yang:190: error: the leaf 'inbound' is illegally changed to a leaf-list
    Cisco-IOS-XR-ipv4-io-oper-sub2.yang:196: error: the leaf 'outbound' is illegally changed to a leaf-list
    Cisco-IOS-XR-ipv4-io-oper-sub2.yang:243: error: the leaf 'common-in-bound', defined at ../531/Cisco-IOS-XR-ipv4-io-oper-sub2.yang:243 (at ../531/Cisco-IOS-XR-ipv4-io-oper-sub2.yang:196) is illegally removed
    Cisco-IOS-XR-ipv4-io-oper-sub2.yang:243: error: the leaf 'common-out-bound', defined at ../531/Cisco-IOS-XR-ipv4-io-oper-sub2.yang:243 (at ../531/Cisco-IOS-XR-ipv4-io-oper-sub2.yang:201) is illegally removed

#### Cisco-IOS-XR-ipv4-ma-oper-sub1.yang

    Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:1: error: new revision 2015-01-07 is not newer than old revision 2015-01-07 (RFC 6020: 10, p2)
    Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:207: error: the leaf 'common-in-bound', defined at ../531/Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:215 is illegally removed
    Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:207: error: the leaf 'common-out-bound', defined at ../531/Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:220 is illegally removed
    Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:209: error: the leaf 'inbound' is illegally changed to a leaf-list
    Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:215: error: the leaf 'outbound' is illegally changed to a leaf-list
    Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:262: error: the leaf 'common-in-bound', defined at ../531/Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:262 (at ../531/Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:215) is illegally removed
    Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:262: error: the leaf 'common-out-bound', defined at ../531/Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:262 (at ../531/Cisco-IOS-XR-ipv4-ma-oper-sub1.yang:220) is illegally removed

#### Cisco-IOS-XR-ipv6-ma-oper-sub1.yang

    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:1: error: new revision 2015-01-07 is not newer than old revision 2015-01-07 (RFC 6020: 10, p2)
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:220: error: the leaf 'in-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:218 is illegally removed
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:220: error: the leaf 'out-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:223 is illegally removed
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:220: error: the leaf 'common-in-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:228 is illegally removed
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:220: error: the leaf 'common-out-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:233 is illegally removed
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259: error: the leaf 'in-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259 (at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:218) is illegally removed
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259: error: the leaf 'out-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259 (at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:223) is     illegally removed
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259: error: the leaf 'common-in-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259 (at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:228) is illegally removed
    Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259: error: the leaf 'common-out-bound', defined at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:259 (at ../531/Cisco-IOS-XR-ipv6-ma-oper-sub1.yang:233) is illegally removed

#### Cisco-IOS-XR-snmp-agent-cfg.yang

    Cisco-IOS-XR-snmp-agent-cfg.yang:978: error: the leaf 'access-list', defined at ../531/Cisco-IOS-XR-snmp-agent-cfg.yang:974 is illegally removed
    Cisco-IOS-XR-snmp-agent-cfg.yang:1036: error: the leaf 'access-list', defined at ../531/Cisco-IOS-XR-snmp-agent-cfg.yang:1015 is illegally removed
    Cisco-IOS-XR-snmp-agent-cfg.yang:1846: error: the leaf 'acl-name', defined at ../531/Cisco-IOS-XR-snmp-agent-cfg.yang:1790 is illegally removed
    Cisco-IOS-XR-snmp-agent-cfg.yang:1974: error: the leaf 'access-list', defined at ../531/Cisco-IOS-XR-snmp-agent-cfg.yang:1879 is illegally removed
