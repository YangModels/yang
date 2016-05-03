## YANG Models for Cisco IOS-XR 5.3.2

The YANG files in this directory detail the YANG models supported by IOS-XR 5.3.3 releases. The schemas here may also be retrieved from devices running IOS-XR 5.3.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

### Compliance With "pyang --ietf"

The YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the "--ietf" flag. The errors and warnings exhibited by running pyang with the "--ietf" flag are currently deemed to be non-critical. A script has been provided, "check-models.sh", that runs pyang with IETF validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

Please note that as of writing, pyang is being updated to change the behavior of the "--ietf" flag when pyang is run against non-IETF modules. The changes will suppress IETF-specific warnings that do not apply to non-IETF modules.

### Revision Statements

From IOS-XR 5.3.2 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs.

### Backwards Compatibility Issues

It should be noted that some of the modules released in IOX-XR 5.3.3 do break the backwards compatibility guidelines defined in RFC 6020. This is because the "native" YANG modules for IOS-XR are generated from internal schema files that are an integral part of the implementation, and, as such, these can change when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Cisco cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the "check-models.sh" script, in conjunction with pyang 1.5, can be used to determine what technically incompatible changes have occurred.

The modules which have incompatible changes, along with the reported pyang incompatibility errors, in IOS-XR 5.3.3 when compared to IOS-XR 5.3.2 are:


### Cisco-IOS-XR-infra-syslog-cfg.yang

    Cisco-IOS-XR-infra-syslog-cfg.yang:530: error: the default '2097152' is illegally changed from '307200'

### Cisco-IOS-XR-infra-syslog-oper-sub1.yang

    Cisco-IOS-XR-infra-syslog-oper-sub1.yang:1: error: new revision 2015-01-07 is not newer than old revision 2015-01-07 (RFC 6020: 10, p2)

### Cisco-IOS-XR-ipv4-bgp-oper-sub1.yang

    Cisco-IOS-XR-ipv4-bgp-oper-sub1.yang:1: error: new revision 2015-08-27 is not newer than old revision 2015-08-27 (RFC 6020: 10, p2)

### Cisco-IOS-XR-policy-repository-cfg.yang

    Cisco-IOS-XR-policy-repository-cfg.yang:1: error: new revision 2015-08-27 is not newer than old revision 2015-08-27 (RFC 6020: 10, p2)
    Cisco-IOS-XR-policy-repository-cfg.yang:540: error: the default '15000' is illegally changed from '5000'
