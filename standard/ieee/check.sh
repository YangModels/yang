#!/bin/sh
#
# check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
base_dir="`pwd`"
to_check="802.1 802.3"

# relax constraint for now
# add --ietf if you want to do strict IETF checking
#pyang_flags="--verbose --canonical --max-identifier-length 70 ../../../ietf/RFC/ -p ../../draft/"
pyang_flags="--verbose ../ietf/RFC/ -p draft/"

checkDir () 
{
    #echo Checking yang files in $1
    exit_status=""
    cwd=`pwd`
    cd "$base_dir/draft/$1"
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

# check modules in IEEE 802.* subdirectories
printf "\n Checking IEEE modules in directory $base_dir \n" 

#echo cd "./$base_dir"
echo cd "$base_dir"

for d in $to_check; do
    #printf "\n Checking modules with pyang in $to_check : \n"
    printf "\n Checking modules with pyang in $d : \n"
    checkDir $d
done


