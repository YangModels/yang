#!/bin/sh
#
# Use this script to compile the entire repository
# when doing local development
#

./vendor/fujitsu/yang-validate.sh
./vendor/cisco/nx/check.sh
./vendor/cisco/xr/check.sh
./vendor/cisco/xe/check.sh
./standard/ietf/check.sh
./standard/bbf/check.sh
./experimental/ieee/check.sh
./standard/ieee/check.sh

