#!/usr/bin/env bash

cd RM2-tow-tank
python plot.py --all --save --no-show
cd ..
python scripts/getfigs.py
