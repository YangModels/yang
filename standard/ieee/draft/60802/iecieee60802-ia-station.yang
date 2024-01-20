module iecieee60802-ia-station {
  yang-version 1.1;
  namespace "urn:ieee:std:60802:yang:iecieee60802-ia-station";
  prefix ias;

  import ietf-datastores {
    prefix ds;
    reference
      "RFC 8342: Network Management Datastore Architecture
       (NMDA)";
  }
  import ietf-netconf-acm {
    prefix nacm;
    reference
      "RFC 8341: Network Configuration Access Control Model";
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
    "Capability information and reset to factory defaults functionality for IEC/IEEE 60802 IA-Stations as specified in IEC/IEEE 60802 IEC/IEEE 60802.

     Copyright (C) IEC/IEEE (2023).
     This version of this YANG module is part of IEC/IEEE Std 60802;
     see the standard itself for full legal notices.";

  revision 2023-09-08 {
    description
      "Initial version.";
    reference
      "IEC/IEEE 60802 - YANG Data Model";
  }

  feature ia-factory-default-datastore {
    description
      "Indicates that the factory default configuration is
       available as a datastore.";
  }

  identity ia-factory-default {
    if-feature "ia-factory-default-datastore";
    base ds:datastore;
    description
      "This read-only datastore contains the factory default
       configuration for the device that will be used to replace
       the contents of the read-write conventional configuration
       datastores during a 'ia-factory-reset' RPC operation.";
  }

  container ia-station-capabilities {
    description
      "This container provides read only information about an ia-station's capabilities.";
    reference
      "IEC/IEEE 60802 - YANG Data Model";
    config false;
    leaf capability-lldp {
      type boolean;
      config false;
      description
        "The value is true if the device supports LLDP.";
      reference
        "6.4.10.2.8.5 of IEC/IEEE 60802";
    }
    leaf capability-timesync {
      type boolean;
      config false;
      description
        "The value is true if the device supports Timesync.";
      reference
        "6.4.10.2.8.6 of IEC/IEEE 60802";
    }
    leaf capability-keystore {
      type boolean;
      config false;
      description
        "The value is true if the device supports Keystore.";
      reference
        "6.4.10.2.8.7 of IEC/IEEE 60802";
    }
    leaf capability-truststore {
      type boolean;
      config false;
      description
        "The value is true if the device supports Truststore.";
      reference
        "6.4.10.2.8.9 of IEC/IEEE 60802";
    }
    leaf capability-nacm {
      type boolean;
      config false;
      description
        "The value is true if the device supports NACM.";
      reference
        "6.4.10.2.8.8 of IEC/IEEE 60802";
    }
    leaf capability-yang-library {
      type boolean;
      config false;
      description
        "The value is true if the device supports YANG library.";
      reference
        "6.4.10.2.8.10 of IEC/IEEE 60802";
    }
    leaf capability-yang-push {
      type boolean;
      config false;
      description
        "The value is true if the device supports YANG push.";
      reference
        "6.4.10.2.8.11 of IEC/IEEE 60802";
    }
    leaf capability-yang-notifications {
      type boolean;
      config false;
      description
        "The value is true if the device supports YANG notifications.";
      reference
        "6.4.10.2.8.12 of IEC/IEEE 60802";
    }
    leaf capability-netconf-monitoring {
      type boolean;
      config false;
      description
        "The value is true if the device supports NETCONF monitoring.";
      reference
        "6.4.10.2.8.13 of IEC/IEEE 60802";
    }
    leaf capability-netconf-client {
      type boolean;
      config false;
      description
        "The value is true if the device supports NETCONF client.";
      reference
        "6.4.10.2.8.14 of IEC/IEEE 60802";
    }
    leaf capability-tsn-uni {
      type boolean;
      config false;
      description
        "The value is true if the device supports TSN uni.";
      reference
        "6.4.10.2.8.15 of IEC/IEEE 60802";
    }
    leaf capability-sched-traffic {
      type boolean;
      config false;
      description
        "The value is true if the device supports scheduled traffic.";
      reference
        "6.4.10.2.8.16 of IEC/IEEE 60802";
    }
    leaf capability-frame-preemption {
      type boolean;
      config false;
      description
        "The value is true if the device supports frame preemption.";
      reference
        "6.4.10.2.8.17 of IEC/IEEE 60802";
    }
  }

  rpc ia-factory-reset {
    nacm:default-deny-all;
    description
      "The server resets all datastores to their factory
       default contents and any nonvolatile storage back to
       factory condition, deleting all dynamically
       generated files, including those containing keys,
       certificates, logs, and other temporary files.

       Depending on the factory default configuration, after
       being reset, the device may become unreachable on the
       network.

       In contrast to the original factory-reset RPC in RFC 8808,
       this RPC puts the device into a state where a subsequent
       configuration by a CNC component results in a funcioning
       60802 IA-station";
  }
}
