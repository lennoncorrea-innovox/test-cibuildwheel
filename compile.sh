#!/bin/bash

mkdir -p build

# Compile the main.cpp
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) src/main.cpp -o build/addpy_pckg$(python3-config --extension-suffix)
