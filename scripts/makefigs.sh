#!/usr/bin/env bash

cd RM2-tow-tank
python plot.py --all --save --noshow
cd ..
python scripts/getfigs.py
