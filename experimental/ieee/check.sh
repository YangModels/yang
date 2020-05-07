#!/bin/sh
#
# check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
base_dir="`pwd`/experimental/ieee/"
#to_check="802.1 802.3 1588"
to_check="802.1 1588 1906.1"

# relax constraint for now
# add --ietf if you want to do strict IETF checking
pyang_flags="--verbose -p ../../../standard/ietf/RFC/ -p ../../../standard/ieee/published/802 -p ../../../standard/ieee/published/802.1/ -p ../../../standard/ieee/published/802.3/ -p ../../../experimental/ieee/1588/ -p ../../../experimental/ieee/1588/ -p ../../../standard/ieee/draft/802.1/Qcw -p ../../../standard/ieee/draft/802.1/Qcr "

checkDir () {
    echo Checking yang files in $1
    exit_status=""
    cwd=`pwd`
    cd "$base_dir/$1"
    printf "\n"
    for f in *.yang; do
        printf "pyang $pyang_flags $f\n"
#        `pyang $pyang_flags $f`
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


# check modules in IEEE 802.X subdirectories
printf "\n Checking IEEE modules in $base_dir \n" 

echo cd "./$base_dir"

for d in $to_check; do
    printf "\n Checking modules with pyang in $to_check : \n"
    checkDir $d
done


