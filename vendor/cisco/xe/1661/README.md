## YANG Models and Platform Capabilities for Cisco IOS-XE 16.6.1

This directory contains the [MIBS](MIBS) subdirectory and YANG models supported by IOS-XE 16.6.1:

* Native models, unique to IOS-XE platforms
* Common Cisco models
* Platform deviations to models
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)
* Copies of **draft** IETF models implemented by IOS-XE 16.6.1 (some with modifications)
* All IETF and tail-f models (without modification) that are supported by IOS-XE platforms 

The schemas here may also be retrieved from devices running IOS-XE 16.6.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of [RFC 6022](https://tools.ietf.org/html/rfc6022). Models listed in this repository are supported by following IOS-XE platforms:

* Catalyst 3850 
* Catalyst 3650
* ASR1000
* CSR1000V/ISRv
* ISR4000
* Catalyst 9300
* Catalyst 9500

Model content may differ based on platform capability. As a convenience, copies of the platform "hello" messages are also provided:

* [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)
* [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
* [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
* [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)
* [cat9300-netconf-capability.xml](cat9300-netconf-capability.xml)
* [cat9500-netconf-capability.xml](cat9500-netconf-capability.xml)

### Major namespace and model changes in 16.6.1

### 16.6.1 Major Model Changes

 * 16.6.1 Model changes includes addition of Openconfig Models, new native models and existing native model updation.

   * List of Openconfig models added in 16.6.1:

         1. openconfig-interfaces
         2. openconfig-routing-policy
         3. openconfig-acl
         4. openconfig-vlan
         5. openconfig-network-instance
         6. openconfig-platform
 
   * List of Native models updated in 16.6.1

         1. Cisco-IOS-XE-native.yang
         2. Cisco-IOS-XE-types.yang
         3. Cisco-IOS-XE-interfaces.yang
	 4. Cisco-IOS-XE-aaa.yang
	 5. Cisco-IOS-XE-acl.yang 
	 6. Cisco-IOS-XE-bfd.yang	
	 7. Cisco-IOS-XE-bgp.yang
	 8. Cisco-IOS-XE-cef.yang
	 9. Cisco-IOS-XE-crypto.yang
	10. Cisco-IOS-XE-cts.yang
	11. Cisco-IOS-XE-dhcp.yang
	12. Cisco-IOS-XE-eem.yang
	13. Cisco-IOS-XE-eigrp.yang
	14. Cisco-IOS-XE-flow.yang
	15. Cisco-IOS-XE-ip.yang
	16. Cisco-IOS-XE-ipv6.yang
	17. Cisco-IOS-XE-isis.yang
	18. Cisco-IOS-XE-line.yang
	19. Cisco-IOS-XE-lisp.yang
	20. Cisco-IOS-XE-lldp.yang
        21. Cisco-IOS-XE-logging.yang
        22. Cisco-IOS-XE-mmode.yang
	23. Cisco-IOS-XE-multicast.yang
	24. Cisco-IOS-XE-nat.yang
	25. Cisco-IOS-XE-nd.yang
	26. Cisco-IOS-XE-ospf.yang
	27. Cisco-IOS-XE-ospfv3.yang
	28. Cisco-IOS-XE-policer.yang
        29. Cisco-IOS-XE-policy.yang
	30. Cisco-IOS-XE-rip.yang
	31. Cisco-IOS-XE-route-map.yang
	32. Cisco-IOS-XE-service-routing.yang
        33. Cisco-IOS-XE-snmp.yang
        34. Cisco-IOS-XE-switch.yang
	35. Cisco-IOS-XE-template.yang
	36. Cisco-IOS-XE-track.yang
	37. Cisco-IOS-XE-tunnel.yang
	38. Cisco-IOS-XE-vlan.yang

   * List of new native models added in 16.6.1:

	1. Cisco-IOS-XE-mmode.yang
	2. Cisco-IOS-XE-template.yang
	 
### Compliance With "pyang --lint"

The native and some common YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.


### Revision Statements

Revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced.


## Platform Differences

Each supported platform advertises NETCONF capabilities during NETCONF session establishment. 

#### Catalyst 3850, 3650

NETCONF capability statement: [cat3k-netconf-capability.xml](cat3k-netconf-capability.xml)

Exceptions to capability statement:

1. Common models not supported by cat3k platforms:

  - [nvo.yang](nvo.yang)
  - [nvo-devs.yang](nvo-devs.yang)

#### Catalyst 9300, 9500
NETCONF capability statement: [cat9300-netconf-capability.xml](cat9300-netconf-capability.xml)
NETCONF capability statement: [cat9500-netconf-capability.xml](cat9500-netconf-capability.xml)

#### ASR1000
NETCONF capability statement: [asr1k-netconf-capability.xml](asr1k-netconf-capability.xml)
#### CSR1000V
NETCONF capability statement: [csr1k-netconf-capability.xml](csr1k-netconf-capability.xml)
#### ISR4000
NETCONF capability statement: [isr4k-netconf-capability.xml](isr4k-netconf-capability.xml)

