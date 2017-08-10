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
