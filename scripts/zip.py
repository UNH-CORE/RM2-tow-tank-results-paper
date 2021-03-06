#!/usr/bin/env python
"""This script zips up all the necessary source files to compile the paper."""

from zipfile import ZipFile
from subprocess import check_output
import os

# Describe version via git
version = check_output(["git", "describe"]).strip().decode()

figures = ["figures/" + f for f in os.listdir("figures") \
           if f.endswith(".eps") or f.endswith(".tif")]

files = ["paper.pdf", "paper.tex", "PLOS-Submission.eps", "plos2015.bst"]

with ZipFile("archive/paper-{}.zip".format(version), "w") as f:
    for fig in figures:
        f.write(fig)
    for file in files:
        f.write(file)
