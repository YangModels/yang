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
to_check="1651 1651/MIBS 1661 1661/MIBS 1662 1662/MIBS 1671 1671/MIBS 1681 1681/MIBS 1691 1691/MIBS 1693 1693/MIBS 16101 16101/MIBS"
inc_path="."
debug=0

checkDir () {
    if [ "$debug" -eq "1" ]; then
	printf "\n***\n"
	printf "*** Checking yang files in $platform_dir/$1\n"
	printf "***\n"
    fi
    cwd=`pwd`
    cd $1
    exit_status=""
    yanglint_flags=""
    if [ `basename $PWD` == "MIBS" ]; then
        yanglint_flags="-p . -p .."
    else
        yanglint_flags="-p ."	
    fi

    to_process=`grep -L submodule *.yang`
    for f in $to_process; do
	if [ "$debug" -eq "1" ]; then
	    echo Checking $f...
	fi
        errors=`yanglint $yanglint_flags $f 2>&1`
        if [ "$?" -eq 1 ]; then
	    if [ "$debug" -eq "1" ]; then
		printf "YANGLINT: found errors in $f, secondary pyang check running...\n"
	    fi
	    errors=`pyang --lax-quote-checks $yanglint_flags $f 2>&1 | grep -v "warning:"`
	    if [ ! -z "$errors" ]; then
		printf "PYANG: Errors in $f\n"
		printf "$errors\n"
		exit_status="failed!"
		if [ "$debug" -eq "1" ]; then
		    printf "\n\n*** EARLY EXIT DUE TO ERROR ***\n\n"
		    exit 1
		fi
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

# for d in $to_check; do
#     checkDir $d
# done

declare -a pids
for d in $to_check; do
    (checkDir $d) &
    pids+=("$!")
done

for p in $pids; do
    wait $p || exit 1
done
