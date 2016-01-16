#!/usr/bin/env python
"""This script copies figures from the RM2 tow tank experiment directory."""

import os
import sys
import shutil

figdir = os.path.join("RM2-tow-tank", "Figures")

figlist = ["cp_curves.eps",
           "cd_curves.eps",
           "perf_re_dep.eps",
    	   "meancontquiv.eps",
           "k_contours.eps",
    	   "K_trans_bar_graph.eps",
    	   "no_blades_all.eps",
    	   "perf_covers.eps"]

for fig in figlist:
    shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fig))
