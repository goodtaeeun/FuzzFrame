#!/bin/bash

FUZZER_NAME='AFLGo'
. $(dirname $0)/common-setup.sh

if [$3 -lt 43200]
    then
    exploit_time=`expr $3 \* 7 / 8`
    else
    exploit_time=`expr $3 \* 5 / 6`
fi

timeout $3 /fuzzer/AFLGo/afl-fuzz \
  $DETER_OPT $DICT_OPT -m none -z exp -c ${exploit_time}s -i seed -o output -- \
  ./$1 $CMDLINE_OPT

. $(dirname $0)/common-postproc.sh
