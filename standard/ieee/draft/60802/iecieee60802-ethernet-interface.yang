module iecieee60802-ethernet-interface {
  yang-version 1.1;
  namespace "urn:ieee:std:60802:yang:iecieee60802-ethernet-interface";
  prefix ia-eth-if;

  import ieee802-ethernet-interface {
    prefix eth-if;
  }
  import ietf-interfaces {
    prefix if;
  }

  organization
    "IEEE 802.1 Working Group";
  contact
    "WG-URL: http://ieee802.org/1/
     WG-EMail: stds-802-1-l@ieee.org

     Contact: IEEE 802.1 Working Group Chair
              Postal: C/O IEEE 802.1 Working Group
              IEEE Standards Association
              445 Hoes Lane
              Piscataway, NJ 08854
              USA

     E-mail: stds-802-1-chairs@ieee.org";
  description
    "Management objects that provide information about IEC/IEEE 60802 IA-Stations as specified in IEC/IEEE 60802.

     Copyright (C) IEC/IEEE (2023).
     This version of this YANG module is part of IEC/IEEE Std 60802;
     see the standard itself for full legal notices.";

  revision 2023-09-08 {
    description
      "Initial version.";
    reference
      "IEC/IEEE 60802 - YANG Data Model";
  }

  augment "/if:interfaces/if:interface/eth-if:ethernet" {
    description
      "Augment IEEE Std 802.3 ethernet.";
    list supported-mau-types {
      description
        "Contains a list of supported mau parameters.";
      key "mau-type";
      config false;
      leaf mau-type {
        type uint32;
        // the type of this leaf should be a type defined by IEEE P802.3 in future
        config false;
        description
          "The value is the supported Mau Type derived from the list position of the corresponding dot3MauType as listed in IETF RFC 4836, Clause 5.";
        reference
          "IEC/IEEE 60802 6.4.10.2.2.1 a)";
      }
      leaf preemption-supported {
        type boolean;
        // the type of this leaf should be a type defined by IEEE P802.3 in future
        config false;
        description
          "The Boolean value indicates if preemption is supported by the MAU Type.";
        reference
          "IEC/IEEE 60802 6.4.10.2.2.1 b)";
      }
    }
  }
}
