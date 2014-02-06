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
import pystache

args = docopt.docopt(__doc__)

def generate_replacements():
	with open("document/figures.json") as f:
		data = json.loads(f.read())

	with open("components/lib/proposition/tpl/figure.stache") as f:
		string = f.read()
		template = lambda x: pystache.render("{{=< >=}}\n"+string, x)

	for d in data:
		if "pos" not in d:
			d["pos"] = "r"
		if not args["--strip"]:
			replacement = template(d)
		else:
			replacement = ""
		yield "[[fig:"+d["id"]+"]]", replacement

with open(args["<filename>"],"r") as f:
	string = f.read().decode('utf-8')

for i in generate_replacements():
	string = string.replace(*i)

print string