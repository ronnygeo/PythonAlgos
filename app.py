from fileOperation import *
from Hash import *

f = split_lines(read_file('alice.txt'))

h = Hash(f)

print h.find("Alice").get_value()

#h.list_all_keys()

#print len(f)
#print type(split_lines(f))
#print len(split_lines(f))