#!/bin/sh
#
# Simple run of pyang with the "--lint" flag over all yang files in
# this directory, ignoring some warnings. Prior to pushing to git, the
# validation was run with pyang 1.7.4. This script should be run with
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
PYANG_FLAGS="-p ../../../../standard/ietf/DRAFT"

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
    printf "  -b <ver> Check backwards compatibility\n"
    printf "\n"
}

OPTIND=1
while getopts "hb:" opt; do
    case "$opt" in
    h|\?)
        show_help
	exit 0
	;;
    b)  CHECK_BC="$OPTARG"
	    ;;
    esac
done

#
# Run pyang over all the yang modules, ignoring certain errors and
# warnings.
#
echo Checking all models with "--lint" flag
for m in *.yang
do
    pyang $PYANG_FLAGS --lint $m 2>&1 | \
	grep -v "warning: RFC 8407" | \
	grep -v "error: RFC 8407: 4.3" | \
	grep -v "error: RFC 8407: 4.8" | \
	grep -v "error: RFC 8407: 4.13,4.14" | \
	grep -v "error: RFC 8407: 4.14" | \
	grep -v "not in canonical order" | \
	grep -v "warning: locally scoped grouping" | \
	egrep -v "warning: imported module\s[a-zA-Z0-9\-]+\snot used"
done

#
# Check if we're doing a BC check, if not, exit status 0
#
if [ -z "$CHECK_BC" ]; then
    exit 0
fi

#
# Run pyang over all the models in the 711 directory that also exist
# in the 721 peer directory, using the --check-update-from option.
# This requires pyang 1.7.4 or better, so we check this first.
#
version=`pyang --version | awk '{print $NF}'`
if ! awk -v ver="$version" 'BEGIN { if (ver < 1.7.4) exit 1; }'; then
    printf 'ERROR: pyang version 1.7.4 or higher required\n'
    exit 1
fi
UPDATE_FROM_PATH=../../../../standard/ietf/RFC
echo Comparing all models that also exist in ../$CHECK_BC AND that have
echo changed since version that version with "--check-update-from" flag:
echo
for m in *.yang
do
    VER_FROM="../$CHECK_BC/$m"
    if [ -e "$VER_FROM" ]
    then
	DIFF=`diff $VER_FROM $m`
	if [ ! -z "$DIFF" ]
	then
	    pyang \
		--check-update-from $VER_FROM \
		--check-update-from-path $UPDATE_FROM_PATH \
		$m
	fi
    fi
done
