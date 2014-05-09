import os

def extend_options(options):
	options["title"] = options["title"].upper()
	return options

def post_make_bibliography(options):
	#!/usr/bin/env python
	fname = ".build/skeleton.bbl"

	def wrap(s):
		return "\\field{journaltitle}{"+s+"}"

	def get_replacements():
		fn = os.path.join(options["theme_dir"],"journal_abbreviations.txt")
		with open(fn,"r") as f:
			for line in f:
				yield line.strip().split("\t")

	with open(fname, "r") as f:
		s = f.read()
	for r in get_replacements():
		r = [wrap(i) for i in r]
		print r
		s = s.replace(*r)
	with open(fname, "w") as f:
		f.write(s)


hooks = {
	"extend_options": extend_options,
	"post_make_bibliography": post_make_bibliography
}