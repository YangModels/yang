#!/bin/sh
#
# check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
test_dir="experimental/ieee"
to_check_1="802.1"
to_check_2="802.3"

# relax constraint for now
# add --ietf if you want to do strict IETF checking
pyang_flags="--verbose -p ../../../standard/ietf/RFC/"

checkDir () {
    echo Checking yang files in $1
    exit_status=""
    cwd=`pwd`
    cd "$test_dir/$1"
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


#check 802.1 modules
printf "\n Checking modules with pyang in directory $test_dir/$to_check_1 : \n"

for d in $to_check_1; do
    checkDir $d
done


#check 802.3 modules
printf "\n Checking modules with pyang in directory $test_dir/$to_check_1: \n"
for d in $to_check_2; do
    checkDir $d
done


