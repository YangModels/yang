Juniper YANG modules
====================

This package contains the configuration and operational YANG modules for
various JUNOS families. Each family has its own directory and contains the
family specific files. The 'common' directory contains the family independent
files and as the name suggests, is common across all families.

Each JUNOS family is a grouping of similar platforms :

junos           : M/MX, T/TX, Some EX platforms, ACX
junos-es        : SRX, Jseries, LN-*
junos-ex        : EX series
junos-qfx       : QFX series

The command "show system information" can be used to find what 'family' a
device belongs to. This command is supported from Junos 17.2 onwards.

Ex:

user@test> show system information
Model: mx240
Family: junos   <-----This is the device family
Junos: 17.2R1.1
Hostname: test

