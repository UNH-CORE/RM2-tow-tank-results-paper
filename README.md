# RM2 tow tank results paper

This repository is for the first paper describing the results from the 1:6
scale RM2 tow tank experiment at UNH. The paper has been published in PLOS ONE,
and is available open-access from http://dx.doi.org/10.1371/journal.pone.0163799.

The current plan is to write only about the experimental results, describing
them in a very matter-of-fact way, and submit to PLOS ONE. Note that according
to their [guidelines](http://www.plosone.org/static/latexGuidelines), figures
should be in EPS or TIFF format, and should not be included as part of the
submitted PDF. References also need to be contained in `paper.tex` rather than
as a separate *.bib or *.bbl file.


## TIFF figure sizing

* Maximum: 7.5 in (19.05 cm) W x 8.75 in (22.23 cm) H
* Minimum: 2.63 in (6.68 cm) W


## Converting PDF to EPS

Open in [Inkscape](http://inkscape.org) and save as EPS.


## Cover letter

Uses https://github.com/aaronwolen/pandoc-letter template. To build:

   pandoc --template=template-letter.tex cover-letter.md -o cover-letter.pdf
