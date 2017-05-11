## Broadband Forum YANG Modules

### 2017-05-05: [WT-385_draft1]: ITU-T PON YANG Modules
*Tags: [v2.0.0-WT-383-draft1](https://github.com/BroadbandForum/yang/tree/v2.0.0-WT-383-draft1), [v3.0.0-WT-385-draft1](https://github.com/BroadbandForum/yang/tree/v3.0.0-WT-385-draft1)*

Full [WT-385_draft1] release (including documentation) plus partial [WT-383_draft1] (Common YANG Modules for Access Networks) release (only what's needed by WT-385).

WT-385 YANG modules in the [draft/interface](draft/interface) directory:

* [bbf-fiber.yang](draft/interface/bbf-fiber.yang): This is the main module.

* [bbf-fiber-if-type.yang](draft/interface/bbf-fiber-if-type.yang): This module defines xPON interface types, including channelgroup, channelpartition, channelpair and channeltermination.

* [bbf-fiber-types.yang](draft/interface/bbf-fiber-types.yang): This module defines identities and data types used by the xPON YANG Modules.

* [bbf-link-table-body.yang](draft/interface/bbf-link-table-body.yang): This module defines a generic link table where each entry links two IETF interfaces. The link relations are used horizontally between the counterpart interfaces on the OLT and the ONU in Combined-NE mode.

[WT-383_draft1]: https://www.broadband-forum.org/software#WT-383_draft1
[WT-385_draft1]: https://www.broadband-forum.org/software#WT-385_draft1

### 2017-03-13: [TR-355c1](https://www.broadband-forum.org/technical/download/TR-355_Corrigendum-1.pdf) YANG Modules for FTTdp Management
*Tag: [v1.0.1-TR-355c1](https://github.com/BroadbandForum/yang/tree/v1.0.1-TR-355c1)*

Various corrections to existing modules and sub-modules. Some of these corrections are not fully backwards compatible.

### 2016-07-18: [TR-355](https://www.broadband-forum.org/technical/download/TR-355.pdf) YANG Modules for FTTdp Management
*Tag: [v1.0.0-TR-355](https://github.com/BroadbandForum/yang/tree/v1.0.0-TR-355)*

TR-355 YANG modules in the [standard/interface](standard/interface) directory:

* [bbf-fastdsl](standard/interface/bbf-fastdsl.yang): This module contains a collection of YANG definitions for an interface which may support one or more DSL or G.fast technologies.

* [bbf-fast](standard/interface/bbf-fast.yang): This module contains a collection of YANG definitions for managing G.fast lines.

* [bbf-vdsl](standard/interface/bbf-vdsl.yang): This module contains a collection of YANG definitions for managing VDSL and DSL lines.

* [bbf-ghs](standard/interface/bbf-ghs.yang): This module contains a collection of YANG definitions for managing G.handshake (ITU-T G.994.1).

* [bbf-melt](standard/interface/bbf-melt.yang): This module contains a collection of YANG definitions for managing Metallic Line Test (MELT) (ITU-T G.996.2).

* [bbf-selt](standard/interface/bbf-selt.yang): This module contains a collection of YANG definitions for managing Single Ended Line Test (SELT) (ITU-T G.996.2).

TR-355 YANG modules in the [standard/common](standard/common) directory:

* [bbf-yang-types](standard/common/bbf-yang-types.yang): This module contains a collection of YANG definitions for common types used throughout Broadband Forum defined modules.
