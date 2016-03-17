def read_file(filename):
	input_file = open(filename, "r")
	return input_file.read()


def split_lines(txt):
	import re
	return re.findall(r"\w+", txt)
	#return txt.split(' ')

def write_file(text):
	out_file = open('data.txt', 'w')
	out_file.write(text)
	out_file.close()