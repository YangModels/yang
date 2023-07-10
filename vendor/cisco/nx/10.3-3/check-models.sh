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
EGREP=`command -v egrep`
GREP=`command -v grep`
PYANG=`command -v pyang`
CHECK_BC=""
PYANG_FLAGS="-p ../../../../standard/ietf/RFC"

trap ctrl_c INT

function ctrl_c() {
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
while getopts "h" opt; do
    case "$opt" in
    h|\?)
        show_help
	exit 0
	;;
    esac
done

#
# Run pyang over all the yang modules, ignoring certain errors and
# warnings.
#
echo Checking all models with "--lint" flag
compile_yang() {
    m=$1
    pyang_flags=${FLAGS}
    if test "${m#*"openconfig-"}" != "$m"; then
       pyang_flags=""
    fi

    echo "pyang $pyang_flags $m" 
    pyang $pyang_flags $m 2>&1 | \
	grep -v "warning: RFC 6087" | \
	grep -v "error: RFC 6087: 4.2" | \
	grep -v "error: RFC 6087: 4.7" | \
	grep -v "error: RFC 6087: 4.11,4.12" | \
	grep -v "error: RFC 6087: 4.12" | \
	grep -v "not in canonical order" | \
	grep -v "warning: locally scoped grouping" | \
	egrep -v "warning: imported module\s[a-zA-Z0-9\-]+\snot used"
}

FLAGS="$PYANG_FLAGS "
for m in *.yang
do
    if test "${m#*"openconfig-"}" != "$m"; then
        continue
    fi
    compile_yang $m
done

if [ -d "extensions" ]; then
   temp_dir="temp"
   for m in extensions/*.yang
   do  
       compile_yang $m
   done	
fi	
