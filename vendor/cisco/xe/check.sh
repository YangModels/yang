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
# 2020-08-01 einarnn:
#
# Deprecating use of yanglint at least until Focal Fossa Ubuntu release
# is out.
#
# Added note to maintainers to just have the release being checked in
# in `to_check`.
#
# 2017-09-21 einarnn:
#
# 16.4.1 currently excluded because this release does not include all
# "RFC" models required and pyang cannot be configured to pick correct
# ietf-routing draft without versioned imports.
#
platform_dir="vendor/cisco/xe"

# NOTE: please just have the directories you are checking here
to_check="17141 17141/MIBS"

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
    pyang_flags="--ignore-error=LEAFREF_IDENTIFIER_NOT_FOUND --ignore-error=STRICT_XPATH_FUNCTION"
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
	errors=`YANG_INSTALL="." pyang --lax-quote-checks $yanglint_flags $pyang_flags $f 2>&1 | \
	    grep -v "warning:" | \
	    grep -v "takes 1-2 arguments but called with 0" | \
            grep -v "takes 3-4 arguments but called with 2"`
	if [ ! -z "$errors" ]; then
	    printf "PYANG: Errors in $f\n"
	    printf "$errors\n"
	    exit_status="failed!"
	    # if [ "$debug" -eq "1" ]; then
	    # 	printf "\n\n*** EARLY EXIT DUE TO ERROR ***\n\n"
	    # 	exit 1
	    # fi
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
