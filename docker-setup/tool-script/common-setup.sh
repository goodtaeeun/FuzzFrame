#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Usage: $0 <target> <source> <timeout>"
    exit 1
fi

if [ $2 = "stdin" ]; then
    CMDLINE_OPT=""
elif [ $2 = "file" ]; then
    CMDLINE_OPT="@@"
else
    echo "Should provide 'stdin' or 'file' as input source"
    exit 1
fi

# Prepare a fresh working directory.
mkdir /box
cd /box
rm -rf ./*

# Prepare target program, seed, and runtime environment.
cp /benchmark/bin/$FUZZER_NAME/$1 ./$1
if [ -d "/benchmark/seed/$1" ]; then
    cp -r /benchmark/seed/$1 ./seed
else
    mkdir seed
    cp /benchmark/seed/empty ./seed/
fi
if [ -d "/benchmark/runtime/$1" ]; then
    cp -r /benchmark/runtime/$1 ./runtime
fi

export AFL_NO_AFFINITY=1
