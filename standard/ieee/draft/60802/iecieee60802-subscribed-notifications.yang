module iecieee60802-subscribed-notifications {
  yang-version 1.1;
  namespace "urn:ieee:std:60802:yang:iecieee60802-subscribed-notifications";
  prefix ia-sn;

  import ietf-subscribed-notifications {
    prefix sn;
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

  augment "/sn:subscriptions" {
    description
      "Augment subscriptions in ietf-subscribed-notifications.";
    leaf max-subscriptions {
      type uint16;
      config false;
      description
        "The value is the maximum number of supported NETCONF Server subscriptions.";
      reference
        "6.4.10.2.8.1 of IEC/IEEE 60802";
    }
    leaf max-on-change-subscription-leaves {
      type uint16;
      config false;
      description
        "The value is the maximum number of supported leaves for NETCONF Server on-change subscriptions according to IETF RFC 8641.";
      reference
        "6.4.10.2.8.2 of IEC/IEEE 60802";
    }
    leaf max-periodic-subscription-leaves {
      type uint16;
      config false;
      description
        "The value is the maximum number of supported leaves for NETCONF Server periodic subscriptions according to IETF RFC 8641.";
      reference
        "6.4.10.2.8.3 of IEC/IEEE 60802";
    }
    leaf max-periodic-subscription-interval {
      type uint16;
      config false;
      description
        "The value is the minimum periodic subscription interval in centiseconds (0.01 seconds) for NETCONF Server periodic subscriptions according to IETF RFC 8641.";
      reference
        "6.4.10.2.8.4 of IEC/IEEE 60802";
    }
  }
}
