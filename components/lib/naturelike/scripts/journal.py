#!/usr/bin/env python
import re


fname = "build/skeleton.bbl"

replacements = [
	#("\begin{thebibliography}{1}","\begin{thebibliography}{1}\small"),
	("\n\n"," "),
	("Geophys. Res. Lett.","GRL"),
	("Lunar Planet. Inst. Sci. Conf. Abstr.", "LPSC"),
	#("Geol. Soc. Am. Bull.","GSAB"),
	("J. Geophys. Res.","JGR"),
	("Proc. Natl. Acad. Sci. U. S. A.","PNAS")
]

with open(fname, "r") as f:
	s = f.read()

for i in replacements:
	s = s.replace(i[0],i[1])

s = re.sub(r"\\urlprefix\\url\{[^\}]+\}. ","",s)

with open(fname, "w") as f:
	f.write(s)

