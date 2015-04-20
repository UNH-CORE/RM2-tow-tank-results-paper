#!/usr/bin/env python
"""
This script copies figures from the RM2 tow tank
experiment directory.
"""

import os
import sys
import shutil

figdir = os.path.join(os.path.expanduser("~"), "Research",
        "Experiments", "RM2 tow tank", "Figures")

figlist = ["perf_curves.tiff",
           "perf_re_dep.tiff"]

for fig in figlist:
    shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fig))
