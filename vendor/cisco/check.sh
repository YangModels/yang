#!/bin/sh
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#

# Check NX-OS Model Repository
./vendor/cisco/nx/check.sh

# Check IOS XR Model Repository
./vendor/cisco/xr/check.sh

# Check IOS XE Model Repository
./vendor/cisco/xe/check.sh

