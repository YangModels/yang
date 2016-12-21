#!/bin/sh
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#

platform_dir="vendor/cisco/nx"
to_check="7.0-3-F1-1 7.0-3-I5-1"
inc_path="../../../../standard/ietf/RFC"

checkDir () {
    echo Checking yang files in $platform_dir/$1
    exit_status=""
    cwd=`pwd`
    cd $1
    for f in *.yang; do
        if test "${f#*"openconfig-"}" != "$f"; then
            continue
        fi
        echo File $f being checked...
    	errors=`pyang -p ..:$1:$inc_path $f 2>&1 | grep -v "syntax error in pattern" | grep "error:"`
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

echo Checking modules with pyang command:
printf "\n    pyang -p ..:$1:$inc_path MODULE\n\n"

if [ -e "$platform_dir" ]; then
    cd $platform_dir
fi

for d in $to_check; do
    checkDir $d
done
