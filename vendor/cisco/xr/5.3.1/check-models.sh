#!/bin/sh
#
# Simple run of pyang with the "--ietf" flag over all yang files in
# this directory, ignoring some warnings. Prior to pushing to git, the
# validation was run with pyang 1.5. This script should be run with the working doirectory set to a directory containing the yang files to run "pyang --ietf" over.
#
# The modules as uploaded exhibit a number of the following errors and
# warnings which are assessed to be non-critical:
#
# IETF rule (RFC 6087: 4.7): statement "revision" must have a "reference" substatement
# IETF rule (RFC 6087: 4.8): namespace value should be "..."
# IETF rule (RFC 6087: 4.9): too many top-level data nodes
# imported module <module-name> not used
#
EGREP=`command -v egrep`
GREP=`command -v grep`
PYANG=`command -v pyang`

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
# check we have the utulitiues we need
#
checkExists pyang
checkExists egrep
checkExists grep

#
# Run pyang over all the yang modules, ignoring ceryain errors and
# warnings.
#
echo Checking all models with "--ietf" flag
for m in *.yang
do
    pyang --ietf $m 2>&1 | \
	grep -v "RFC 6087: 4.7" | \
	grep -v "RFC 6087: 4.8" | \
	grep -v "RFC 6087: 4.9" | \
	egrep "imported module [.]+ not used"
done

#
# Run pyang over all the models in the 531 directory that also exist
# in the 530 peer directory, using the --check-update-from option.
# This requires pyang 1.5 or better, so we check this first.
#
version=`pyang --version | awk '{print $NF}'`
if ! awk -v ver="$version" 'BEGIN { if (ver < 1.5) exit 1; }'; then
    printf 'ERROR: pyang version 1.5 or higher required\n'
    exit 1
fi
UPDATE_FROM_PATH=../../../../standard/ietf/RFC
echo Comparing all models that also exist in ../530 with "--check-update-from" flag
for m in *.yang
do
    VER_530="../530/$m"
    if [ -e "$VER_530" ]
    then
	pyang \
	    --check-update-from $VER_530 \
	    --check-update-from-path $UPDATE_FROM_PATH \
	    $m
    fi
done
