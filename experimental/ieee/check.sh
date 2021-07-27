#!/bin/sh
#
# check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
cwd=$(pwd)
ietf_dir="standard/ietf"
ieee_dir="standard/ieee"
ieee_experimental_dir="experimental/ieee"
#to_check="802.1 802.3 1588"
to_check="802.1 1588 1906.1"

# relax constraint for now
# add --ietf if you want to do strict IETF checking
ietf_dir_flag="--path $cwd/$ietf_dir/RFC/"
pyang_flags="--verbose --path $ietf_dir_flag --path $cwd/$ieee_dir/published/802 --path $cwd/$ieee_dir/published/802.1/ --path $cwd/$ieee_dir/published/802.3/ --path $cwd/$ieee_experimental_dir/1588/ --path $cwd/$ieee_experimental_dir/1588/ --path $cwd/$ieee_dir/draft/802.1/Qcw --path $cwd/$ieee_dir/draft/802.1/Qcr "

checkDir() {
    local dir="$ieee_experimental_dir/$1"
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

# check modules in IEEE 802.X subdirectories
printf "\nChecking IEEE experimental modules in $cwd/$ieee_experimental_dir\n"
echo Checking modules with pyang command:
printf "\n    pyang $pyang_flags MODULE\n"

for d in $to_check; do
    checkDir $d
done
