#!/bin/sh
#
# Possible IETF check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
cwd=$(pwd)
ietf_dir="standard/ietf"
ieee_dir="standard/ieee"
to_check="RFC"

# relax constraint for now
# add --ietf if you want to do strict IETF checking
ieee_dir_flag="--path $cwd/$ieee_dir/published/"
pyang_flags="--verbose $ieee_dir_flag"

checkDir() {
    local dir="$ietf_dir/$1"
    echo "\nChecking yang files in $dir"
    exit_status=""
    cd $dir
    printf "\n"
    for f in *.yang; do
        printf "pyang $pyang_flags $f\n"
        errors=$(pyang $pyang_flags $f 2>&1 | grep "error:")
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
printf "\n    pyang $pyang_flags MODULE\n"

for d in $to_check; do
    checkDir $d
done
