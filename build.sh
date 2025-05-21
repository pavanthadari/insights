#!/usr/bin/env bash

# Install core build dependencies first
pip install cython numpy

# Then pystan and prophet
pip install pystan==2.19.1.1
pip install prophet

# Then install the rest
pip install -r requirements.txt
