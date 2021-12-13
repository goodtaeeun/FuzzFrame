#!/bin/bash

FUZZER_NAME='AFLGOPT'
. $(dirname $0)/common-setup.sh

timeout $3 /fuzzer/AFLGOPT/afl-fuzz -d -m none -z exp -i seed -o output ./$1 $CMDLINE_OPT

. /tool-script/common-postproc.sh
