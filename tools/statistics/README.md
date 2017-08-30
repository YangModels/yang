Statistics
=====

This package contains a python script to create statistics.html file:

  * template directory containing jinja template for html file
  * statistics.py containing script to get all statistics

Statistics script goes through all the files in githup repo and also through all the
 modules populated in confd catalog using api search. It counts all the modules for 
 each sdo and vendor and it calculates percentage that pass the compilations.
 
This script will create statistics.html file which will be automatically added to yc.o
at [https://www.yangcatalog.org/statistics.html](https://www.yangcatalog.org/statistics.html)

This html file is divided to four categories:
1. SDO and Opensource statistics
    - IETF
    - BBF
    - IEEE
    - MEF
    - Openconfig
    
1. Vendor statistics
    - Cisco
    - Ciena
    - Juniper
    - Huawei

1. Cisco version-platform compatibility
    - IOS-XR
    - IOS-XE
    - NX-OS

1. General statistics
    - Number of yang files in vendor directory with duplicates
    - Number of yang files in vendor directory without duplicates
    - Number of yang files in standard directory with duplicates
    - Number of yang files in standard directory without duplicates
    - Number of files parsed into yangcatalog
    - Number of unique files parsed into yangcatalog