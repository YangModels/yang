## Cisco-IOS-XE-ip.yang


- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

## XPaths Obsoleted

### Description
Separated export/import stitching (added new) and export/import without stitching in netconf. Export/import with stitching has asn-ip as key and stitching as mandatory true. Export/import has asn-ip as key and obsoleted stitching.

### Reason
Unable to get normal RTs when stitching RTs are present with the same RT value using netconf/yang.

- /native/vrf/definition/address-family/ipv4/route-target/export/stitching
- /native/vrf/definition/address-family/ipv4/route-target/import/stitching
- /native/vrf/definition/address-family/ipv6/route-target/export/stitching
- /native/vrf/definition/address-family/ipv6/route-target/import/stitching


### Description
route-target import/export is not seen in yang get-config under af-ipv4 under vrf

### Reason
Fixed the model so that configure from ioscli/confd and netconf is reflected correctly 

- /native/vrf/definition/address-family/ipv4/route-target/export/
- /native/vrf/definition/address-family/ipv4/route-target/export/asn-ip
- /native/vrf/definition/address-family/ipv4/route-target/import/
- /native/vrf/definition/address-family/ipv4/route-target/import/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/export/
- /native/vrf/definition/address-family/ipv6/route-target/export/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/import/
- /native/vrf/definition/address-family/ipv6/route-target/import/asn-ip

## XPaths Deprecated
N/A

## XPaths Modified
N/A

## XPaths Added

### Description
Separated export/import stitching (added new) and export/import without stitching in netconf. Export/import with stitching has asn-ip as key and stitching as mandatory true. Export/import has asn-ip as key and obsoleted stitching.

### Reason
Unable to get normal RTs when stitching RTs are present with the same RT value using netconf/yang

- /native/vrf/definition/address-family/ipv4/route-target/export-stitching
- /native/vrf/definition/address-family/ipv4/route-target/export-stitching/asn-ip
- /native/vrf/definition/address-family/ipv4/route-target/export-stitching/stitching
- /native/vrf/definition/address-family/ipv4/route-target/import-stitching
- /native/vrf/definition/address-family/ipv4/route-target/import-stitching/asn-ip
- /native/vrf/definition/address-family/ipv4/route-target/import-stitching/stitching
- /native/vrf/definition/address-family/ipv6/route-target/export-stitching
- /native/vrf/definition/address-family/ipv6/route-target/export-stitching/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/export-stitching/stitching
- /native/vrf/definition/address-family/ipv6/route-target/import-stitching
- /native/vrf/definition/address-family/ipv6/route-target/import-stitching/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/import-stitching/stitching


### Description
route-target import/export is not seen in yang get-config under af-ipv4 under vrf

### Reason
Fixed the model so that configure from ioscli/confd and netconf is reflected correctly

- /native/vrf/definition/address-family/ipv4/route-target/export-route-target
- /native/vrf/definition/address-family/ipv4/route-target/export-route-target/without-stitching
- /native/vrf/definition/address-family/ipv4/route-target/export-route-target/without-stitching/asn-ip
- /native/vrf/definition/address-family/ipv4/route-target/export-route-target/with-stitching
- /native/vrf/definition/address-family/ipv4/route-target/export-route-target/with-stitching/asn-ip
- /native/vrf/definition/address-family/ipv4/route-target/export-route-target/with-stitching/stitching
- /native/vrf/definition/address-family/ipv4/route-target/import-route-target
- /native/vrf/definition/address-family/ipv4/route-target/import-route-target/without-stitching
- /native/vrf/definition/address-family/ipv4/route-target/import-route-target/without-stitching/asn-ip
- /native/vrf/definition/address-family/ipv4/route-target/import-route-target/with-stitching
- /native/vrf/definition/address-family/ipv4/route-target/import-route-target/with-stitching/asn-ip
- /native/vrf/definition/address-family/ipv4/route-target/import-route-target/with-stitching/stitching
- /native/vrf/definition/address-family/ipv6/route-target/export-route-target
- /native/vrf/definition/address-family/ipv6/route-target/export-route-target/without-stitching
- /native/vrf/definition/address-family/ipv6/route-target/export-route-target/without-stitching/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/export-route-target/with-stitching
- /native/vrf/definition/address-family/ipv6/route-target/export-route-target/with-stitching/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/export-route-target/with-stitching/stitching
- /native/vrf/definition/address-family/ipv6/route-target/import-route-target
- /native/vrf/definition/address-family/ipv6/route-target/import-route-target/without-stitching
- /native/vrf/definition/address-family/ipv6/route-target/import-route-target/without-stitching/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/import-route-target/with-stitching
- /native/vrf/definition/address-family/ipv6/route-target/import-route-target/with-stitching/asn-ip
- /native/vrf/definition/address-family/ipv6/route-target/import-route-target/with-stitching/stitching
