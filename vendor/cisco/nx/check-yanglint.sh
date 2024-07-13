#!/bin/bash
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
# This script will only be run for the last release of a version branch.
# When a new set of models is committed for a version, the previous
# should be removed.
#
platform_dir="vendor/cisco/nx"

to_check='10.2-8'
debug=1

checkDir () {
    if [ "$debug" -eq "1" ]; then
	echo Checking yang files in $platform_dir/$1
    fi
    exit_status=""
    cwd=`pwd`
    cd $1
    to_process=`grep -L submodule *.yang`
    for f in $to_process; do
        if test "${f#*"openconfig-"}" != "$f"; then
            continue
        fi
	if [ "$debug" -eq "1" ]; then
	    echo Checking $f...
	fi
        errors=`yanglint $f 2>&1`
        if [ "$?" -eq 1 ]; then
	    realerrors=`echo $error | \
		perl -ne 'if (!/^err : Invalid keyword \"[^(\"\"\.)]/){print;}' | \
		perl -ne 'if (!/^err : Module \"[^(\")]+\" parsing failed\./){print;}'`
	    if [ ! -z "$realerrors" ]; then
		echo Errors in $f
		echo $realerrors
		exit_status="failed!"
	    fi
        fi
    done
    cd $cwd
    
    if [ ! -z "$exit_status" ]; then
       exit 1
    fi
}

if [ "$debug" -eq "1" ]; then
    printf "\nChecking modules with yanglint, using 'lax quote checks' via perlre filtering\n"
fi

if [ -e "$platform_dir" ]; then
    cd $platform_dir
fi

#declare -a pids
for d in $to_check; do
    checkDir $d
    # (checkDir $d) &
    # pids+=("$!")
done

#for p in $pids; do
#    wait $p || exit 1
#done
