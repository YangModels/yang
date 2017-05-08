#!/bin/sh
#
# Possible IETF check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
ietf_dir="standard/ietf"
to_check="RFC"

# relax constraint for now
# add --ietf if you want to do strict IETF checking
pyang_flags="--verbose"

checkDir () {
    local dir="$ietf_dir/$1"
    echo Checking yang files in $dir
    exit_status=""
    cwd=`pwd`
    cd $dir
    printf "\n"
    for f in *.yang; do
        printf "pyang $pyang_flags $f\n"
	errors=`pyang $pyang_flags $f 2>&1 | grep "error:"`
	if [ ! -z "$errors" ]; then
	    echo Errors in $f
            printf "\n  $errors \n"
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

for d in $to_check; do
    checkDir $d
done

