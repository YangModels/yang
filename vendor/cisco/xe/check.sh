#!/usr/bin/env bash
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#

platform_dir="vendor/cisco/xe"
to_check="1631 1631/MIBS 1632 1632/MIBS 1641 1641/MIBS"
inc_path="../../../../standard/ietf/RFC"
pyang_flags=".:$inc_path"

checkDir () {
    echo Checking yang files in $platform_dir/$1
    cwd=`pwd`
    cd $1
    exit_status=""
    pyang_flags=".:$inc_path"
    if [ `basename $PWD` == "MIBS" ]; then
        pyang_flags="..:../$inc_path"
    fi

    for f in *.yang; do
        errors=`pyang -p $pyang_flags $f 2>&1 | grep "error:"`
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

echo Checking modules with pyang command:
printf "\n    pyang $pyang_flags MODULE\n\n"

if [ -e "$platform_dir" ]; then
    cd $platform_dir
fi

for d in $to_check; do
    checkDir $d
done
