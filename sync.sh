#!/bin/bash

# TODO create sub-directories per opendaylight branch

if [ -z "$1" ]; then
  echo "USAGE: sync.sh <PATH-TO-YOUR-opendaylight.git/releng/autorelease>"
  exit
fi
set -ex

pushd .
cd $1
git pull
git submodule init
git submodule update
git submodule foreach git reset --hard
git submodule foreach git checkout origin/master
git submodule foreach git pull --ff-only origin master
popd

git rm experimental/odp/*
mkdir experimental/odp

# There is a probably a better way to do this, but this works... ;-)
find /home/vorburger/dev/ODL/git/releng/autorelease -name "*.yang" -path "*src/main/yang*" ! -path "*test*" -printf 'cp %p experimental/odp/%f\n' >/tmp/copy-yang.sh
source /tmp/copy-yang.sh

git add experimental/odp/*
