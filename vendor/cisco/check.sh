#!/bin/sh
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
to_check="xr/530 xr/531 xr/532"

checkDir () {
    echo Checking yang files in $1
    cwd=`pwd`
    cd $1
    for f in *.yang; do
	pyang $f
	if [ -z $? ]; then
	    exit 1
	fi
    done
    cd $cwd
}

for d in $to_check; do
    checkDir $d
done

