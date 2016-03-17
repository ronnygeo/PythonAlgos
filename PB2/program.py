from fileOperation import *
from RBOperations import *
from RBTree import *
import re

input_filename = 'number.txt'
tree = RBTree()

a_temp = read_file(input_filename)
a_temp2 = a_temp.split(',')
a = [int(x) for x in a_temp2]


for i in range(len(a)):
	rb_insert(tree, Node(a[i]))
print "After the Initial import, height of the tree is " + str(rbt_height(tree.root))


inp = ''
while inp != 'q':
	input = raw_input("Enter your command (insert x, sort, search x, minimum, maximum, etc). q to exit.\n")
	inp = input.split(' ')
	if str(inp[0]) == "insert":
		rb_insert(tree, Node(int(inp[1])))
		print "New key inserted successfully."
	elif inp[0] == "search":
		if type(search(tree, int(inp[1]))) == Node:
			print "key exists."
		else:
			print "key not found."
	elif inp[0] == "sort":
		print "Sorted Order: ", sort(tree.root)
	elif inp[0] == "minimum":
		print "Minimum: ", rbt_minimum(tree.root).key
	elif inp[0] == "maximum":
		print "Maximum: ", rbt_maximum(tree.root).key
	elif inp[0] == "successor":
		print "Successor: ", rbt_successor(tree.root).key
	elif inp[0] == "predecessor":
		print "Predecessor: ", rbt_predecessor(tree.root).key
	else:
		print "Invalid Option."
	print "Height: ", rbt_height(tree.root)

