#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
Replaces instances of [[fig:id]] with {id: ...,} from figures.json

Usage:
  figures.py [--strip] <filename>

Options:
  -h --help     Show this screen.
  -s --strip    Strip all figure tags without replacement.
"""

import re
import json
import docopt

args = docopt.docopt(__doc__)

def generate_replacements():
	with open("document/figures.json") as f:
		data = json.loads(f.read())

	for d in data:
		if "pos" not in d:
			d["pos"] = "r"
		if not args["--strip"]:
			graphics = "\\includegraphics[width="+d["width"]+"]{figures/"+d["images"][0]+"}"
			replacement = ("\\begin{figure*}"+
							"\\noindent"+graphics+
							"\\vspace{-5pt}\\caption{"+d["caption"]+"}"+
							"\\label{fig:"+d["id"]+"}"+
							"\\end{figure*}\\paragraph{}\\vspace*{-\\parskip}\\vspace*{-\\parsep}")
		else:
			replacement = ""
		yield "[[fig:"+d["id"]+"]]", replacement

with open(args["<filename>"],"r") as f:
	string = f.read().decode('utf-8')

for i in generate_replacements():
	string = string.replace(*i)

print string