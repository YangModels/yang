#!/bin/bash
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
platform_dir="vendor/cisco/xr"
to_check="5.3.0 5.3.1 5.3.2 5.3.3 5.3.4 6.0.0 6.0.1 6.0.2 6.1.1 6.1.2 6.1.3 6.2.1 6.2.2"
pyang_flags=""
debug=0

checkDir () {
    if [ "$debug" -eq "1" ]; then
	echo Checking yang files in $platform_dir/$1
    fi
    exit_status=""
    cwd=`pwd`
    cd $1
    for f in Cisco-IOS-XR-*-cfg.yang; do
        errors=`pyang $pyang_flags $f 2>&1 | grep "error:"`
        if [ ! -z "$errors" ]; then
            echo Errors in $f
            echo $errors
            exit_status="failed!"
        fi
    done
    for f in Cisco-IOS-XR-*-oper.yang; do
        errors=`pyang $pyang_flags $f 2>&1 | grep "error:"`
        if [ ! -z "$errors" ]; then
            echo Errors in $f
            echo $errors
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
