#!/bin/bash

FUZZER_NAME='AFLGo'
. $(dirname $0)/common-setup.sh

exploit_time=`expr $3 \* 3 / 4`

timeout $3 /fuzzer/AFLGo/afl-fuzz -d -m none -z exp -c ${exploit_time}s -i seed -o output ./$1 $CMDLINE_OPT

. $(dirname $0)/common-postproc.sh
