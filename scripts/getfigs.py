#!/usr/bin/env python
"""This script copies figures into the figures directory."""

import os
import sys
import shutil


def fix_eps(fpath):
    """Fix carriage returns in EPS files caused by Arial font."""
    txt = b""
    with open(fpath, "rb") as f:
        for line in f:
            if b"\r\rHebrew" in line:
                line = line.replace(b"\r\rHebrew", b"Hebrew")
            txt += line
    with open(fpath, "wb") as f:
        f.write(txt)


if __name__ == "__main__":
    # Get RM2 figs
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

    # Get RVAT-Re-dep figs
    figdir = os.path.join("RVAT-Re-dep", "Figures")
    figlist = ["meancontquiv_10.eps", "k_contours_10.eps"]

    for fig in figlist:
        fix_eps(os.path.join(figdir, fig))
        fign = "RVAT-Re-dep-" + fig
        shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fign))
