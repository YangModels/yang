#!/usr/bin/python
import argparse
import os
import HTML
import time
import re


__author__ = 'Benoit Claise'
__copyright__ = "Copyright(c) 2017, Cisco Systems, Inc."
__license__ = "New-style BSD"
__email__ = "bclaise@cisco.com"


# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------


def list_of_yang_modules_in_subdir(srcdir, debug_level):
    """
    Returns the list of YANG Modules (.yang) in all sub-directories   
    :param srcdir: root directory to search for yang files
    :param debug_level: If > 0 print some debug statements to the console
    :return: list of YANG files
    """
    ll = []
    for root, dirs, files in os.walk(srcdir):
        for f in files:
            if f.endswith(".yang"):
                if debug_level > 0:
                    print(os.path.join(root, f))
                ll.append(os.path.join(root, f))
    return ll

    
# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count all YANG modules + related stats for a directory and its subdirectories')
    parser.add_argument("--rootdir", default = None,
                        help="The root directory where to find the source YANG models. "
                             "Default is '.'")
    parser.add_argument("--excludedir", 
                        help="The root directory from which to exclude YANG models. "
                             "This directory should be under rootdir. ")
    parser.add_argument("--excludekeyword", default = None,
                        help="Exclude some keywords from the YANG module name. Example: show")
    parser.add_argument("--removedup", type=bool, default=True, help="Remove duplicate YANG module. Default True.")
    parser.add_argument("--debug", type=int, default=0, help="Debug level; the default is 0")
    args = parser.parse_args()
    
    # equivalent shell commands (without the de-duplication
    # rootdir:
    # find /home/bclaise/yanggithub/ -name "*.yang" -print | wc -l
    # excludedir
    # find /home/bclaise/yanggithub/ -name "*.yang" -print | grep -v "vendor/cisco" | wc -l
    # excludekeyword
    # find /home/bclaise/yanggithub/ -name "*.yang" -print | grep -v "vendor/cisco" | grep -i show | wc -l
    # find /home/bclaise/yanggithub/ -name "*.yang" -print | grep -v "vendor/cisco" | grep -iv show | wc -l
    
    # runYANGallstats.py --rootdir /home/bclaise/yanggithub/ --excludekeyword "show" --excludedir "vendor"
    # --------------------------
    # Number of YANG data models in /home/bclaise/yanggithub/ : 672
    # Number of YANG data models in /home/bclaise/yanggithub/ (duplicates removed): 518
    # Number of YANG data models in /home/bclaise/yanggithub/ (duplicates removed) and without the keyword show :518

    yang_list = list_of_yang_modules_in_subdir(args.rootdir, args.debug)

    if args.debug > 0:
        print("yang_list content: ")
        print yang_list

    # Remove the entries corresponding to exludedir option
    temp_list = []
    if args.excludedir:
        for yang_file in yang_list:
            if args.excludedir not in yang_file:
                temp_list.append(yang_file)
        yang_list = temp_list            
          
    # Remove duplicates and count the YANG modules
    YANG_module_count = 0
    YANG_module_count_removed_dup = 0
    yang_list_removed_dup = []
    for yang_file in yang_list:
        yang_file_without_path = yang_file.split("/")[-1]
        if args.debug > 0:
            print("yang_list_removed_dup content: ") + yang_file_without_path
        YANG_module_count += 1
        if yang_file_without_path not in yang_list_removed_dup:
            yang_list_removed_dup.append(yang_file_without_path)
            YANG_module_count_removed_dup += 1
    
    if args.debug > 0:
        print("yang_list_removed_dup content: ")
        print yang_list_removed_dup
        
    print "--------------------------"
    print "Number of YANG data models in " + args.rootdir + " : " + str(YANG_module_count)
    print "Number of YANG data models in " + args.rootdir + " (duplicates removed): " + str(YANG_module_count_removed_dup)
    
    # Remove the excludekeyword
    YANG_module_count_removed_dup_removed_keyword = 0
    yang_list_removed_dup_removed_keyword = []
    if args.excludekeyword:
        for yang_file_without_path in yang_list_removed_dup:
            if args.excludekeyword not in yang_file_without_path:
                yang_list_removed_dup_removed_keyword.append(yang_file_without_path)
                YANG_module_count_removed_dup_removed_keyword += 1
        print "Number of YANG data models in " + args.rootdir + " (duplicates removed) and without the keyword " + args.excludekeyword + " :" + str(YANG_module_count_removed_dup_removed_keyword)

                
    
        
        