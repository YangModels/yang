#!/bin/sh
#
# BBF check script (loosely) based on the IETF one.
#
# Currently checks out the latest version of pyang from GitHub because
# pyang 1.7 has a bug that affects "bits" defaults:
# * https://github.com/mbj4668/pyang/issues/232
# * https://github.com/mbj4668/pyang/commit/77fdee4

ietf_dir="standard/ietf"
bbf_dir="standard/bbf"
to_check="common interface"

cwd=`pwd`

pyang_flags="--strict --max-line-length=70 --lint --lint-modulename-prefix=bbf --lint-namespace-prefix=urn:bbf:yang: --verbose --path=$cwd/$ietf_dir --path=$cwd/$bbf_dir"

setupPyang () {
    local cwd=`pwd`
    cd $bbf_dir
    if [ -d pyang-temp ]; then
        (cd pyang-temp; git checkout master; git pull)
    else
        git clone https://github.com/mbj4668/pyang.git pyang-temp
    fi

    cd pyang-temp
    . ./env.sh
    cd $cwd
}

checkDir () {
    local dir="$bbf_dir/$1"
    echo Checking yang files in $dir
    exit_status=""
    printf "\n"
    for f in `find $dir -name '*.yang'`; do
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
}

echo Cloning/updating pyang
setupPyang

echo Checking modules with pyang command:
printf "\n    pyang $pyang_flags MODULE\n\n"

for d in $to_check; do
    checkDir $d
done

# if tidied up pyang would need to save and restore the exit status

