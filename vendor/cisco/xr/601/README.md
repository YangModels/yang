## YANG Models for Cisco IOS-XR 6.0.1

The YANG files in this directory detail the YANG models supported by IOS-XR 6.0.1 releases. The schemas here may also be retrieved from devices running IOS-XR 6.0.1 by using the NETCONF "get-schema" RPC as detailed in Section 3.1 of RFC 6022.

### Deviation Modules for openconfig-bgp and openconfig-routing-policy

IOS-XR 6.0.1 provides support for several openconfig models, but also publishes a number of deviations against those models. The deviation modules provided are:

* [cisco-xr-bgp-deviations.yang](cisco-xr-bgp-deviations.yang)
* [cisco-xr-bgp-policy-deviations.yang](cisco-xr-bgp-policy-deviations.yang)
* [cisco-xr-routing-policy-deviations.yang](cisco-xr-routing-policy-deviations.yang)

The matching openconfig modules are found in the git repository [YangModels/yang](https://github.com/YangModels/yang.git), commit id f6b4e2d59d4eedf31ae8b2fa3119468e4c38259c. To compile the deviatioon modules you will either need to download the openconfig modules from an IOS-XR 6.0.1 router or you will need to checout those specific versions of the openconfig models. To work in offline mode you may use commands similar to:

```
$ git clone https://github.com/YangModels/yang.git
Cloning into 'yang'...
remote: Counting objects: 2596, done.
remote: Total 2596 (delta 0), reused 0 (delta 0), pack-reused 2596
Receiving objects: 100% (2596/2596), 5.78 MiB | 336.00 KiB/s, done.
Resolving deltas: 100% (1309/1309), done.
Checking connectivity... done.
$ cd yang
$ git checkout f6b4e2d59d4eedf31ae8b2fa3119468e4c38259c
Note: checking out 'f6b4e2d59d4eedf31ae8b2fa3119468e4c38259c'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at f6b4e2d... Typos corrected.
$
```

### Compliance With "pyang --lint"

The native YANG models are not fully compliant with all IETF guidelines as exemplified by running the pyang tool with the ```--lint``` flag. The errors and warnings exhibited by running pyang with the ```--lint``` flag are currently deemed to be non-critical as they do not impact the semantic of the models or prevent the models being used as part of toolchains. A script has been provided, "check-models.sh", that runs pyang with ```--lint``` validation enabled, but ignoring certain errors. This allows the developer to determine what issues may be present.

### Revision Statements

From IOS-XR 5.3.2 and onwards, the revision statements embedded in the YANG files **should** accurately reflect whether or not a new revision has been introduced. However, there are some bugs.

### Backwards Compatibility Issues

It should be noted that some of the modules released in IOX-XR 6.0.1 break the backwards compatibility guidelines defined in RFC 6020 when compared to the same modules released in IOS-XR 6.0.1. This is because the "native" YANG modules for IOS-XR are generated from internal schema files that are an integral part of the implementation, and, as such, these can change in ways that break backwards compatibility per RFC 6020 guidelines when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Cisco cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the [```check-models.sh```](check-models.sh) script, in conjunction with pyang 1.6, can be used to determine what technically incompatible changes have occurred. Please run ```check.sh``` from this directory with pyang 1.5 or greater on your path thus:

```
$ ./check.sh -b 600
```

The script will check basic compilation using pyang (some open modules will be reported missing unless you include them on your pyang moduke path) and then run backwards compatibility checks against the model in the ```../600``` directory.

