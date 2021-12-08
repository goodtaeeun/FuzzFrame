#!/bin/bash
cd AFLGOPT
make clean all && cd llvm_mode && make clean all && cd ../distance_calculator && cmake -GNinja ./ && cmake --build ./
cd /
