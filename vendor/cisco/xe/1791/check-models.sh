#!/bin/sh
#
# Simple run of pyang with the "--lint" flag over all yang files in
# this directory, ignoring some warnings. Prior to pushing to git, the
# validation was run with pyang 1.5. This script should be run with
# the working doirectory set to a directory containing the yang files
# to run "pyang --lint" over.
#
# The modules as uploaded exhibit a number of RFC 6087 amd RFC 6020
# errors and warnings that are judged to be cosmetic at this time and
# which do not impact the ability of a client to interact with a
# device supporting the module. The exact content ignored may be
# identified by reviewing the "grep -v" commands below.
#
GREP=`command -v grep`
PYANG=`command -v pyang`
PYANG_FLAGS="-p . -p ./MIBS --ignore-error LEAFREF_IDENTIFIER_NOT_FOUND --lax-quote-checks"

trap ctrl_c INT

ctrl_c() {
  echo 'User interruption, exiting ..' 
  exit -1
}
#
# simple function to check for existence of a binary on the current
# path
#
checkExists() {
    bin=`command -v $1`
    if [ -z "$bin" ]
    then
	echo this script requires $1 to be on your path
	exit 1
    fi
}

#
# check we have the utilties we need
#
checkExists pyang
checkExists egrep
checkExists grep

#
# brief help for the options we support
#
show_help () {
    echo Options for check-models.sh:
    printf "\n"
    printf "  -h       Show this help\n"
    printf "\n"
}

OPTIND=1
while getopts "hc:" opt; do
    case "$opt" in
    h|\?)
        show_help
	exit 0
	;;
    esac
done

#
# Run pyang over all the yang modules, ignoring certain errors and
# warnings. Only if we haven't been asked to do the BC check
#
#echo Checking all models with "--lint" flag

check_yang_set() {
    #echo "pyang $FLAGS" 
    YANG_INSTALL="/tmp" pyang $FLAGS 2>&1 | \
	grep -v "warning:"

}

for m in *.xml
    do
       FLAGS="--hello $m $PYANG_FLAGS"
       echo "pyang $FLAGS"
       check_yang_set
   done

# for m in *.yang
#   do
#    YANG_INSTALL="/tmp" pyang $PYANG_FLAGS $m 2>&1 | \
#        grep -v "warning:"
#  done

# YANG_INSTALL="/tmp" pyang $PYANG_FLAGS *.yang 2>&1 | \
# 	grep -v "warning:"

