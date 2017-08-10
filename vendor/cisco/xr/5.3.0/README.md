## YANG Models for Cisco IOS-XR 5.3.0

The YANG files in this directory detail the YANG models supported by IOS-XR 5.3.0 releases. The schemas here may also be retrieved from devices running IOS-XR 5.3.0 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

### Compliance With "pyang --ietf"

The YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the "--ietf" flag. The errors and warnings exhibited by running pyang with the "--ietf" flag are currently deemed to be non-critical. A script has been provided, "check-models.sh", that runs pyang with IETF validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.
