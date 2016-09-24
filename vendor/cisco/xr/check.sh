#!/bin/sh
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#

platform_dir="vendor/cisco/xr"
to_check="530 531 532 533 600 601 611"
pyang_flags="../../../standard/ietf/RFC"

checkDir () {
    echo Checking yang files in $platform_dir/$1
    exit_status=""
    for f in $1/*.yang; do
        errors=`pyang $pyang_flags $f 2>&1 | grep "error:"`
        if [ ! -z "$errors" ]; then
            echo Errors in $f
            echo $errors
            exit_status="failed!"
        fi
    done
    
    if [ ! -z "$exit_status" ]; then
       exit 1
    fi
}

echo Checking modules with pyang command:
printf "\n    pyang $pyang_flags MODULE\n\n"

if [ -e "$platform_dir" ]; then
    cd $platform_dir
fi

for d in $to_check; do
    checkDir $d
done
