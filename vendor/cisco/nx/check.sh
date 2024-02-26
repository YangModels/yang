#!/bin/bash
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
platform_dir="vendor/cisco/nx"

# NOTE: please just have the directories you are checking here
to_check='10.2-7'

inc_path="."
pyang_flags="--lax-quote-checks"
debug="0"

checkDir () {
    if [ "$debug" -eq "1" ]; then
	echo Checking yang files in $platform_dir/$1
    fi
    exit_status=""
    cwd=`pwd`
    cd $1
    for f in *.yang; do
        if test "${f#*"openconfig-"}" != "$f"; then
            continue
        fi
    	errors=`YANG_INSTALL="." pyang $pyang_flags $f 2>&1 | grep -v "syntax error in pattern" | grep "error:"`
        if [ ! -z "$errors" ]; then
            echo Errors in $f
            echo "$errors"
            exit_status="failed!"
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
