## YANG Models and Platform Capabilities for Cisco IOS-XE 16.5.1

This directory contains the [MIBS](MIBS) subdirectory and YANG models supported by IOS-XE 16.5.1:

* Native models, unique to IOS-XE platforms
* Common Cisco models
* Platform deviations to models
* MIB-based models generated using the algorithms in [RFC 6643](https://tools.ietf.org/html/rfc6643)
* Copies of **draft** IETF models implemented by IOS-XE 16.5.1 (some with modifications)
* All IETF and tail-f models (without modification) that are supported by IOS-XE platforms 

The schemas here may also be retrieved from devices running IOS-XE 16.5.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of [RFC 6022](https://tools.ietf.org/html/rfc6022). Models listed in this repository are supported by following IOS-XE platforms:

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

### Major namespace and model changes in 16.5.1

### 16.5.1 Major model changes
  * 16.5.1 XE YANG model is changed from one single monolith model to 70+ individual feature modules. Top level feature has an anchor node in the main module (i.e. **module Cisco-IOS-XE-native**) and individual feature is argumenting the anchor node. As a result of this change, most of the features have **new module name, new namespace and prefix**.
 
 e.g.
  module Cisco-IOS-XE-aaa {
  namespace "http://cisco.com/ns/yang/Cisco-IOS-XE-aaa";
  prefix ios-aaa;

   **Please contact your CISCO technical assistance center representive to migrate pre-16.5.1 NETCONF RPC requests.**

  * access-list in **Cisco-IOS-XE-acl.yang** schema has changes that result in XPATH changes. 

    *  **tags under access-list that are changed**

     1. [**src-udp-eq**  | src-tcp-eq]  -> **src-eq**
     2. [src-udp-gt  | src-tcp-gt]  -> src-gt
     3. [src-udp-lt  | src-tcp-lt]  -> src-lt
     4. [src-udp-neq | src-tcp-neq] -> src-neq
     5. [src-udp-range1 | src-tcp-range1] -> src-range1
     6. [src-udp-range2 | src-tcp-range2] -> src-range2
     7. [dst-udp-eq  | dst-tcp-eq]  -> dst-eq
     8. [dst-udp-gt  | dst-tcp-gt]  -> dst-gt
     9. [dst-udp-lt  | dst-tcp-lt]  -> dst-lt
     10. [dst-udp-neq | dst-tcp-neq] -> dst-neq
     11. [dst-udp-range1 | dst-tcp-range1] -> dst-range1
     12. [dst-udp-range2 | dst-tcp-range2] -> dst-range2

     e.g.
      * original XPATH   
    /native/ip/access-list/extended/access-list-seq-rule/ace-rule/src-port-choice/src-eq-case/**src-udp-eq**)
      * new XPATH
    Cisco-IOS-XE-native/native/ip/access-list/ios-acl:extended/ios-acl:access-list-seq-rule/ios-acl:ace-rule/ios-acl:src-port-choice/ios-acl:src-eq-case/ios-acl:**src-eq**
  
  * There are 7 sub-modules that belong to the main Cisco-IOS-XE-native module

    1. submodule Cisco-IOS-XE-interfaces 
    2. submodule Cisco-IOS-XE-ip 
    3. submodule Cisco-IOS-XE-ipv6 
    4. submodule Cisco-IOS-XE-license 
    5. submodule Cisco-IOS-XE-line 
    6. submodule Cisco-IOS-XE-logging 
    7. submodule Cisco-IOS-XE-parser 

  * before and after the 16.5.1 netconf regquest
   * pre-16.5.1 NETCONF request
  ``` xml
       <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
               <edit-config>
                      <target>
                             <running/>
                      </target>
                      <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
                             <native xmlns="http://cisco.com/ns/yang/ned/ios">
                                        <call-home>
                                               <contact-email-addr xc:operation="create"> 
                                                      john.doe@cisco.com
                                               </contact-email-addr>
                                        </call-home>
                                        <hostname xc:operation="create">CISCO</hostname>
                             </native>
                      </config>
               </edit-config>
        </rpc>
   ``` 

   * post-16.5.1 NETCONF request

   ``` xml
       <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
               <edit-config>
                      <target>
                             <running/>
                      </target>
                      <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">             
                             <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" xmlns:ios-ch="http://cisco.com/ns/yang/Cisco-IOS-XE-call-home">                    
                                        <call-home>                            
                                               <ios-ch:contact-email-addr xc:operation="create">
                                                      john.doe@cisco.com 
                                               </ios-ch:contact-email-addr>                                                         
                                        </call-home>
                                     <hostname xc:operation="create">CISCO</hostname>
                             </native>
                      </config>
               </edit-config>
       </rpc>
   ```

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

