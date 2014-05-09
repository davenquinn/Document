import os
import re
import json
import pystache

def replace_figures(filename, options, strip=False):

	def get_templates():
		dn = os.path.join("themes",options["theme"],"templates","figures")
		for fn in os.listdir(dn):
			path = os.path.join(dn,fn)
			with open(path) as f:
				string = f.read()
			id = os.path.splitext(fn)[0]
			yield id,string


	def generate_replacements():
		with open("document/figures.json") as f:
			figures = json.loads(f.read())

		templates = {k:v for k,v in get_templates()}
		create = lambda x,template: pystache.render("{{=<< >>=}}\n"+template, x)
		for d in figures:
			if "pos" not in d:
				d["pos"] = "r"
			kind = d.pop("type","basic")
			if not strip:
				replacement = create(d,templates[kind])
			else:
				replacement = ""
			s = "fig:{0}".format(d["id"]).replace("_","\_")
			yield r"{[}{[}"+s+r"{]}{]}", replacement

	with open(filename,"r") as f:
		string = f.read().decode('utf-8')

	for i in generate_replacements():
		print i
		string = string.replace(*i)

	return string