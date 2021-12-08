#!/bin/bash
git clone https://github.com/goodtaeeun/AFLGOPT.git
cd AFLGOPT
apt-get -y update
apt-get -y install python3 python3-dev python3-pip libboost-all-dev ninja-build --no-install-recommends
pip3 install --upgrade pip
pip3 install networkx==2.5 pydot pydotplus
make clean all && cd llvm_mode && make clean all && cd ../distance_calculator && cmake -GNinja ./ && cmake --build ./
