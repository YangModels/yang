#!/bin/sh
#
# check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
# Also assumes that the script is run from the root of the yang master.
#
cwd=$(pwd)
ietf_dir="standard/ietf"
ieee_dir="standard/ieee"

to_check="draft/60802 draft/802.3 draft/802.1/qrev draft/802.1/ASrev draft/802.1/ASds draft/802.1/ASed draft/802.1/AXdz draft/CB-2017-cor1 draft/802.1/DD draft/1588 published/802 published/802.1 published/1588"

# relax constraint for now
# add --ietf if you want to do strict IETF checking
ietf_dir_flag="$cwd/$ietf_dir/RFC/"

checkDir() {
    local dir="$ieee_dir/$1"
    echo "\nChecking yang files in $dir"
    exit_status=""
    pyang_flags="--verbose --path $ietf_dir_flag --path $cwd/$ieee_dir/published"
    cd $dir

    if [ -f "./check_pyang_extra_flags" ]; then
        check_pyang_extra_flags=$(cat ./check_pyang_extra_flags)
        #pyang_flags="$pyang_flags $check_pyang_extra_flags"
        pyang_flags="$check_pyang_extra_flags $pyang_flags"
    fi
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
for d in $to_check; do
    checkDir $d
done
