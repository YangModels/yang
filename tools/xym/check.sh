#!/bin/sh
#
xym_dir="tools/xym"
echo Running xym self-test
cwd=`pwd`
cd $xym_dir
python -m unittest xym
if [ $? -ne 0 ]; then
    echo xym self-test failed
    exit 1
fi
