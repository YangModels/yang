#!/bin/sh
#
# Use this script to compile the entire repository
# when doing local development
#

# submodule; don't assume it will be available
# ./vendor/fujitsu/yang-validate.sh

./vendor/cisco/nx/check.sh
./vendor/cisco/xr/check.sh
./vendor/cisco/xe/check.sh
./vendor/cisco/svo/check.sh
./standard/ietf/check.sh

# submodule; don't assume it will be available
# ./standard/bbf/check.sh

./experimental/ieee/check.sh
./standard/ieee/check.sh
./standard/iana/check.sh
