#!/bin/bash
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
declare -a scripts=(
    "./vendor/cisco/nx/check.sh"
    "./vendor/cisco/xe/check.sh"
    "./vendor/cisco/xr/check.sh"
    "./vendor/cisco/svo/check.sh"
)

declare -a pids
for s in "${scripts[@]}"; do
    ($s) &
    pids+=('$!')
done

npids=${#pids[@]}
for (( i=0; i<${npids}; i++ )); do
    wait $p || exit 1
    echo ${scripts[$i]} is done!
done
