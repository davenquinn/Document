import pystache

def replace_data(filename, options):
	with open(filename,"r") as f:
		string = f.read()
	return pystache.render("{{=<< >>=}}\n"+string, options)