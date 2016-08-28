#!/usr/bin/env bash

cd RVAT-Re-dep
python plot.py perf_re_dep all_meancontquiv all_kcont --save --savetype .eps --no-show --no-subplot-labels
cd ..
python scripts/getfigs.py
