#!/bin/sh
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#

platform_dir="vendor/cisco/xr"
to_check="530 531 532 533 534 600 601 602 611 612 613"
#pyang_flags="-p ../../../standard/ietf/RFC"
pyang_flags=""

checkDir () {
    echo Checking yang files in $platform_dir/$1
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

printf "\nChecking modules with pyang command:\n"
printf "\n    pyang $pyang_flags MODULE\n\n"

if [ -e "$platform_dir" ]; then
    cd $platform_dir
fi

for d in $to_check; do
    checkDir $d
done
