#!/usr/bin/env bash

cd RVAT-Re-dep
python plot.py all_meancontquiv all_kcont --save --savetype .eps --no-show
cd ..
python scripts/getfigs.py
