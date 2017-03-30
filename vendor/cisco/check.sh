#!/bin/sh
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
pids=""

# Check IOS-XR Model Repository
(./vendor/cisco/xr/check.sh) &
pids+=" $!"

# Check IOS-XE Model Repository
(./vendor/cisco/xe/check.sh) &
pids+=" $!"

# Check NX-OS Model Repository
(./vendor/cisco/nx/check.sh) &
pids+=" $!"

echo Waiting for jobs to finish...
for p in $pids; do
    wait $p || exit 1
done
