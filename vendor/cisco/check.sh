#!/bin/sh
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
vendor_dir="vendor/cisco"
to_check="xr/530 xr/531 xr/532 xr/600"
pyang_flags=""

checkDir () {
    echo Checking yang files in $vendor_dir/$1
    exit_status=""
    cwd=`pwd`
    cd $1
    for f in Cisco-IOS-XR-*.yang; do
	errors=`pyang $pyang_flags $f 2>&1 | grep "error:"`
	if [ ! -z "$errors" ]; then
	    echo Errors in $f
	    exit_status="failed!"
	fi
    done
    if [ ! -z "$exit_status" ]; then
	exit 1
    fi
    cd $cwd
}

echo Checking modules with pyang command:
printf "\n    pyang $pyang_flags MODULE\n\n"

cd $vendor_dir
for d in $to_check; do
    checkDir $d
done

