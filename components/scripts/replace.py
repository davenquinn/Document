#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
Replaces instances of [[fig:id]] with {id: ...,} from figures.json

Usage:
  replace.py <filename>

Options:
  -h --help     Show this screen.
"""

import json
import docopt
import pystache

args = docopt.docopt(__doc__)

with open("document/config.json") as f:
	config = json.loads(f.read())

with open(args["<filename>"],"r") as f:
	string = f.read()

print pystache.render("{{=<< >>=}}\n"+string, config)