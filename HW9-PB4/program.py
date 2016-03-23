from BHeap import BHeap
from fileOperation import *

input_filename = 'number2.txt'
bheap1 = BHeap()
bheap2 = BHeap()

a_temp = read_file(input_filename)
a_temp2 = a_temp.split(',')
a1 = [int(x) for x in a_temp2]

a_temp = read_file("number.txt")
a_temp2 = a_temp.split(',')
a2 = [int(x) for x in a_temp2]

for i in range(len(a1)):
	bheap1.insert(a1[i])

for i in range(len(a2)):
	bheap2.insert(a2[i])

bheap1.extractMin()
print "Min Before Merge: ", bheap1.minimum().key
#bheap1.traversal(bheap1.head)
bheap1.union(bheap2)
bheap1.deleteNodeByKey(1)
print "Min After Merge:", bheap1.minimum().key
