
# About

A set of YANG modules describing nanoscale communication systems and their associated physical quantities in conformance with IEEE Std 1906.1-2015—a common framework for all nanoscale communication technologies—are comprised by this data model. Physics unique to the nanoscale are represented by the model.

1. IEEE 1906.1.1 (https://standards.ieee.org/project/1906_1_1.html) defines a common YANG [RFC 6020/7950] data model for IEEE 1906.1-2015 nanoscale communication systems.

2. IEEE 1906.1-2015 (https://standards.ieee.org/standard/1906_1-2015.html) defines nanoscale communication. It also specifies a framework for describing all nanoscale communication systems in terms of fulfilling the definition of a nanoscale network, universal framework components, and metrics.

This folder implements a definition, terminology, conceptual model, and standard metrics for ad hoc network communication at the nanoscale are provided. Human-engineered networking is extended by the physical properties of nanoscale communication in ways beyond that defined in existing communication standards. These include in vivo, sub-cellular medical communication, smart materials and sensing at the molecular level, and the ability to operate in environments that would be too harsh for macroscale communication mechanisms to operate. 


# How to start?

1. A good place to begin understanding the model is to review ieee1906-dot1-system.yang and note that it defines the main aspects of IEEE Standard 1906.1-2015.
2. See the ieee1906-dot1-system files in the Examples folder to corresponding JSON and XML instance data as well as a ieee1906-dot1-system UML diagram.
3. The IANA ieee19061nanocom identity in iana-if-type.yang (revision 2020-01-10) defines interfaces for Nanoscale and Molecular Communication.
4. A complementary module, ieee1906-dot1-si-units.yang, defines the International System of Units. This is meant to be useful in scientific network applications such as nanoscale and quantum networks.
5. Finally, ieee1906-dot1-math.yang and ieee1906-dot1-function.yang are YANG extensions to make real-time mathematics more amenable on network devices.

See the Examples folder for additional XML and JSON example instance data.

The XML instance data examples contain comments describing the motivation for the model structure.
