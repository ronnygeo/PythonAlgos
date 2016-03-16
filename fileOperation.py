def read_file(filename):
	input_file = open(filename, "r")
	return input_file.read()


def split_lines(txt):
	return txt.split(' ')