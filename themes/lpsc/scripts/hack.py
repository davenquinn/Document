#!/usr/bin/env python

with open("components/skeleton.tex", "r") as f:
	s = f.read()

with open("_build/skeleton.tex", "w+") as f:
	f.write(s.replace(r"\renewcommand{\bibitem}[1]{\item}",""))

