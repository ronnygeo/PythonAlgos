from fileOperation import *
from Hash import *

f = split_lines(read_file('PB1/alice.txt'))

h = Hash(f)

print h.list_all_keys()

#search for string
print h.find("Alice").get_value()

#writing to file
write_file(h.list_all_keys())

