#!/usr/bin/env bash
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
# This script will only be run for the last three releases. When a new
# release is added, the current first release (left to right) should
# be removed.
#
# 2017-09-21 einarnn:
#
# 16.4.1 currently excluded because this release does not include all
# "RFC" models required and pyang cannot be configured to pick correct
# ietf-routing draft without versioned imports.
#
platform_dir="vendor/cisco/xe"
to_check="1651 1651/MIBS 1661 1661/MIBS"
inc_path="."
debug=0

checkDir () {
    if [ "$debug" -eq "1" ]; then
	echo Checking yang files in $platform_dir/$1
    fi
    cwd=`pwd`
    cd $1
    exit_status=""
    yanglint_flags=""
    if [ `basename $PWD` == "MIBS" ]; then
        yanglint_flags="-p .."
    fi

    to_process=`grep -L submodule *.yang`
    for f in $to_process; do
        errors=`yanglint $yanglint_flags $f 2>&1`
        if [ "$?" -eq 1 ]; then
	    realerrors=`echo $error | \
		perl -ne 'if (!/^err : Invalid keyword \"[^(\"\"\.)]/){print;}' | \
		perl -ne 'if (!/^err : Module \"[^(\")]+\" parsing failed\./){print;}'`
	    if [ ! -z "$realerrors" ]; then
		echo Errors in $f
		echo $realerrors
		exit_status="failed!"
	    fi
        fi
    done
    cd $cwd
    
    if [ ! -z "$exit_status" ]; then
	   exit 1
    fi
}

if [ "$debug" -eq "1" ]; then
    printf "\nChecking modules with yanglint, using 'lax quote checks' via perlre filtering\n"
fi

if [ -e "$platform_dir" ]; then
    cd $platform_dir
fi

declare -a pids
for d in $to_check; do
    (checkDir $d) &
    pids+=("$!")
done

for p in $pids; do
    wait $p || exit 1
done
