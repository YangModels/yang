module iecieee60802-sched-bridge {
  yang-version 1.1;
  namespace "urn:ieee:std:60802:yang:iecieee60802-sched-bridge";
  prefix ia-sched-bridge;

  import ieee802-types {
    prefix ieee802;
  }
  import ieee802-dot1q-bridge {
    prefix bridge;
  }
  import ieee802-dot1q-sched-bridge {
    prefix sched-bridge;
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

  augment "/if:interfaces/if:interface/bridge:bridge-port/sched-bridge:gate-parameter-table" {
    description
      "Augment IEEE Std 802.1 bridge/gate-parameter-table.";
    list min-gating-times {
      description
        "The list of minimum gating times per supported line speed.";
      reference
        "6.4.10.2.4.3 of IEC/IEEE 60802";
      key "speed";
      config false;
      leaf speed {
        type uint32;
        config false;
        description
          "This value is the line speed in Mbps.";
      }
      container min-cycle-time {
        uses ieee802:rational-grouping;
        description
          "The value is the minimum value supported by this port of the AdminCycleTime and OperCycleTime parameters given as rational number of seconds.";
        reference
          "6.4.10.2.4.3 a) of IEC/IEEE 60802";
      }
      leaf min-interval-time {
        type uint32;
        description
          "The value is the minimum value supported by this port of the TimeIntervalValue parameter in nanoseconds.";
        reference
          "6.4.10.2.4.3 b) of IEC/IEEE 60802";
      }
    }
  }
}
