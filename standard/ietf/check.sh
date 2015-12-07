#!/bin/sh
#
# Possible IETF check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
ietf_dir="standard/ietf"
to_check="RFC"

# relax constraint for now
#pyang_flags="--ietf"

checkDir () {
    echo Checking yang files in $1
    exit_status=""
    cwd=`pwd`
    cd $1
    for f in *.yang; do
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

cd $ietf_dir
for d in $to_check; do
    checkDir $d
done

