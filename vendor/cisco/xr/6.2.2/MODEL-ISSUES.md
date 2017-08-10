# Native Model Issues

A number of differences have crept in to a small number of YANG modules supported in IOS-XR 6.2.2. The differences, platforms impacted and where to find the alternate versions of models are detailed below. If you are working with an impacted platform, you should copy the YANG models from the relevant ```.incompatible``` subdirectory into your working directory and use that set of models instead.

If you retrieve models directly from a device, you will get the correct set of models.

The models in these directories are currently only relevant to the following images

* Cisco-IOS-XR-aaa-locald-cfg.yang:
    * asr9k-px
    * hfr-px
    * xrvr
* Cisco-IOS-XR-plat-chas-invmgr-oper.yang:
    * asr9k-px
    * hfr-px
    * xrvr
* Cisco-IOS-XR-infra-dumper-cfg.yang:
    * hfr-px
