# Native Model Issues

A number of differences have crept in to a small number of YANG modules supported in IOS-XR 6.0.1. The differences, platforms impacted and where to find the alternate versions of models are detailed below. If you are working with an impacted platform, you should copy the YANG models from the relevant ```.incompatible``` subdirectory into your working directory and use that set of models instead.

If you retrieve models directly from a device, you will get the correct set of models.

Finally, it should be noted that there some Cisco YANG extensions that are referred to in modules. These may be safely ignored, but developers should note that when downloading schemas from devices some file sizes may differ from the files in the YangModels/yang git repository. Most of the common models were sources from the ncs5500


## Cisco-IOS-XR-aaa-locald-cfg

A sample difference is shown below:

```
--- asr9k-px/Cisco-IOS-XR-aaa-locald-cfg.tree	Thu Sep 22 07:21:13 2016
+++ asr9k-x64/Cisco-IOS-XR-aaa-locald-cfg.tree	Thu Sep 22 07:23:57 2016
@@ -5,12 +5,13 @@
    +--rw default-taskgroup?   string
 augment /a1:aaa:
    +--rw usernames
-      +--rw username* [name]
+      +--rw username* [ordering-index name]
          +--rw usergroup-under-usernames
          |  +--rw usergroup-under-username* [name]
          |     +--rw name    xr:Cisco-ios-xr-string
          +--rw secret?                      xr:Md5-password
          +--rw password?                    xr:Proprietary-password
+         +--rw ordering-index               int32
          +--rw name                         string
 augment /a1:aaa:
    +--rw taskgroups
```

Platforms that have a username list indexed solely by name are:

* asr9k-px
* hfr
* xrvr

The version of the model for these platforms is stored in the directory [Cisco-IOS-XR-aaa-locald-cfg.incompatible](Cisco-IOS-XR-aaa-locald-cfg.incompatible)


## Cisco-IOS-XR-crypto-macsec-mka-cfg

A sample difference is shown below:

```
--- asr9k-px/Cisco-IOS-XR-crypto-macsec-mka-cfg.tree	Thu Sep 22 07:21:17 2016
+++ hfr/Cisco-IOS-XR-crypto-macsec-mka-cfg.tree	Thu Sep 22 07:26:44 2016
@@ -4,7 +4,6 @@
          +--rw security-policy?       Macsec-mka-security-policy
          +--rw key-server-priority?   Macsec-mka-key-server-priority
          +--rw conf-offset?           Macsec-mka-conf-offset
-         +--rw policy-exception?      Macsec-mka-policy-exception
          +--rw window-size?           Macsec-mka-window-size
          +--rw cipher-suite?          Macsec-mka-cipher-suite
          +--rw vlan-tags-in-clear?    Macsec-mka-vlan-tags-in-clear
```

The platforms that have the extra ```policy-exception``` leaf are:

* asr9k-px

The version of the model for these platforms is stored in the directory [Cisco-IOS-XR-crypto-macsec-mka-cfg.incompatible](Cisco-IOS-XR-crypto-macsec-mka-cfg.incompatible)


## Cisco-IOS-XR-infra-dumper-cfg

This model, only used on the asr9k-px, hfr and xrvr platforms has the following issue:

```
--- asr9k-px/Cisco-IOS-XR-infra-dumper-cfg.tree	Thu Sep 22 07:21:25 2016
+++ xrvr/Cisco-IOS-XR-infra-dumper-cfg.tree	Thu Sep 22 07:43:20 2016
@@ -1,18 +1,18 @@
 module: Cisco-IOS-XR-infra-dumper-cfg
    +--rw exception
-      +--rw choice1
+      +--rw choice1!
       |  +--rw compress?       boolean
       |  +--rw lower-limit?    uint32
       |  +--rw higher-limit?   uint32
       |  +--rw file-path?      string
       |  +--rw filename?       string
-      +--rw choice3
+      +--rw choice3!
       |  +--rw compress?       boolean
       |  +--rw lower-limit?    uint32
       |  +--rw higher-limit?   uint32
       |  +--rw file-path?      string
       |  +--rw filename?       string
-      +--rw choice2
+      +--rw choice2!
       |  +--rw compress?       boolean
       |  +--rw lower-limit?    uint32
       |  +--rw higher-limit?   uint32
```

The following platform makes the choices containers presence containers:

* xrvr

The version of the model for this platforms is stored in the directory [Cisco-IOS-XR-infra-dumper-cfg.incompatible](Cisco-IOS-XR-infra-dumper-cfg.incompatible)

## Cisco-IOS-XR-ip-bfd-oper

This model has cross-platform incompatibilities that manifest as type changes from ```uint32``` to ```uint64```. This has resulted from certain the automated translation of types that became 64-bit on 64-bit platforms.

For example, in this **partial** diff:

```
--- asr9k-px/Cisco-IOS-XR-ip-bfd-oper.tree	Thu Sep 22 07:19:43 2016
+++ asr9k-x64/Cisco-IOS-XR-ip-bfd-oper.tree	Thu Sep 22 07:22:28 2016
@@ -179,18 +179,18 @@
       |     |  +--ro internal-label?                           uint32
       |     +--ro mp-download-state
       |     |  +--ro change-time
-      |     |  |  +--ro seconds?       uint32
+      |     |  |  +--ro seconds?       uint64
       |     |  |  +--ro nanoseconds?   uint32
       |     |  +--ro mp-download-state?   Bfd-mp-download-state
       |     +--ro lsp-ping-info
       |     |  +--ro lsp-ping-tx-last-time
-      |     |  |  +--ro seconds?       uint32
+      |     |  |  +--ro seconds?       uint64
       |     |  |  +--ro nanoseconds?   uint32
       |     |  +--ro lsp-ping-tx-last-error-time
-      |     |  |  +--ro seconds?       uint32
+      |     |  |  +--ro seconds?       uint64
       |     |  |  +--ro nanoseconds?   uint32
       |     |  +--ro lsp-ping-rx-last-time
-      |     |  |  +--ro seconds?       uint32
+      |     |  |  +--ro seconds?       uint64
       |     |  |  +--ro nanoseconds?   uint32
       |     |  +--ro lsp-ping-tx-count?             uint32
       |     |  +--ro lsp-ping-tx-error-count?       uint32

```

The following platforms use the ```uint32``` type for all seconds fields:
 
* asr9k-px
* hfr
* xrvr

The versions of the models for these platforms is stored in the directory [Cisco-IOS-XR-ip-bfd-oper.incompatible](Cisco-IOS-XR-ip-bfd-oper.incompatible)


## Cisco-IOS-XR-qos-ma-bng-cfg

This model has cross-platform incompatibilities that manifest as shown in this diff:

```
--- asr9k-px/Cisco-IOS-XR-qos-ma-bng-cfg.tree	Thu Sep 22 07:21:51 2016
+++ asr9k-x64/Cisco-IOS-XR-qos-ma-bng-cfg.tree	Thu Sep 22 07:24:36 2016
@@ -1,67 +0,0 @@
-module: Cisco-IOS-XR-qos-ma-bng-cfg
-augment /a1:dynamic-template/a1:subscriber-services/a1:subscriber-service:
-   +--rw qos
-      +--rw service-policy
-      |  +--rw input!
-      |  |  +--rw policy-name      string
-      |  |  +--rw spi-name?        string
-      |  |  +--rw merge?           boolean
-      |  |  +--rw merge-id?        uint32
-      |  |  +--rw account-stats?   boolean
-      |  +--rw output!
-      |     +--rw policy-name      string
-      |     +--rw spi-name?        string
-      |     +--rw merge?           boolean
-      |     +--rw merge-id?        uint32
-      |     +--rw account-stats?   boolean
-      +--rw account
-      |  +--rw aal?             Qosl2-data-link
-      |  +--rw encapsulation?   Qosl2-encap
-      |  +--rw atm-cell-tax?    empty
-      |  +--rw user-defined?    int32
-      +--rw output
-         +--rw minimum-bandwidth?   uint32
-augment /a1:dynamic-template/a1:ip-subscribers/a1:ip-subscriber:
-   +--rw qos
-      +--rw service-policy
-      |  +--rw input!
-      |  |  +--rw policy-name      string
-      |  |  +--rw spi-name?        string
-      |  |  +--rw merge?           boolean
-      |  |  +--rw merge-id?        uint32
-      |  |  +--rw account-stats?   boolean
-      |  +--rw output!
-      |     +--rw policy-name      string
-      |     +--rw spi-name?        string
-      |     +--rw merge?           boolean
-      |     +--rw merge-id?        uint32
-      |     +--rw account-stats?   boolean
-      +--rw account
-      |  +--rw aal?             Qosl2-data-link
-      |  +--rw encapsulation?   Qosl2-encap
-      |  +--rw atm-cell-tax?    empty
-      |  +--rw user-defined?    int32
-      +--rw output
-         +--rw minimum-bandwidth?   uint32
-augment /a1:dynamic-template/a1:ppps/a1:ppp:
-   +--rw qos
-      +--rw service-policy
-      |  +--rw input!
-      |  |  +--rw policy-name      string
-      |  |  +--rw spi-name?        string
-      |  |  +--rw merge?           boolean
-      |  |  +--rw merge-id?        uint32
-      |  |  +--rw account-stats?   boolean
-      |  +--rw output!
-      |     +--rw policy-name      string
-      |     +--rw spi-name?        string
-      |     +--rw merge?           boolean
-      |     +--rw merge-id?        uint32
-      |     +--rw account-stats?   boolean
-      +--rw account
-      |  +--rw aal?             Qosl2-data-link
-      |  +--rw encapsulation?   Qosl2-encap
-      |  +--rw atm-cell-tax?    empty
-      |  +--rw user-defined?    int32
-      +--rw output
-         +--rw minimum-bandwidth?   uint32
```

The following platforms have this extra content:

* asr9k-px
* hfr
* xrvr

The version of the model for these platforms is stored in the directory [Cisco-IOS-XR-qos-ma-bng-cfg](Cisco-IOS-XR-qos-ma-bng-cfg)

The following platforms have the YANG file, but it contains no leaves:

* asr9k-x64
* ncs1k
* ncs5k
* ncs5500
* ncs6k
* xrv9k
