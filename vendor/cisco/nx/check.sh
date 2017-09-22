#!/bin/bash
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
platform_dir="vendor/cisco/nx"
to_check="7.0-3-F1-1 7.0-3-F2-1 7.0-3-F2-2 7.0-3-F3-1 7.0-3-I5-1 7.0-3-I5-2 7.0-3-I6-1 7.0-3-I7-1"
inc_path=".:../../../../standard/ietf/RFC"
pyang_flags=""
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
    	errors=`pyang $pyang_flags $f 2>&1 | grep -v "syntax error in pattern" | grep "error:"`
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
    printf "\nChecking modules with pyang command:\n"
    printf "\n    pyang $pyang_flags MODULE\n\n"
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
