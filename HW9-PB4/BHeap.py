from Node import Node

class BHeap(object):
	def __init__(self):
		self.head = None
		self.n = None

	def makeHeap(self):
		bh = BHeap()
		return bh

	def minimum(self):
		head = self.head
		min = 99999
		current = None
		while head:
			if head.key < min:
				min = head.key
				current = head
			head = head.sibling
		return current

	def merge(self, n):
		p = None
		headx = self.head
		heady = n.head
		if headx.degree < heady.degree:
			p = headx
			headx = headx.sibling
		else:
			p = heady
			heady = heady.sibling
		self.head = p
		while headx != None and heady != None:
			if headx.degree <= heady.degree:
				p.sibling = headx
				headx = headx.sibling
			else:
				p.sibling = heady
				heady = heady.sibling
			p = p.sibling
		if headx != None:
			p.sibling = headx
		if heady != None:
			p.sibling = heady
		return self

	def link(self, n1, n2):
		n2.parent = n1
		n2.sibling = n1.child
		n1.child = n2
		n1.degree += 1

	def union(self, n):
		self.merge(n)
		n = None
		if self.head == None:
			return self
		prevNode = None
		currNode = self.head
		nextNode = currNode.sibling
		while nextNode != None:
			if (currNode.degree != nextNode.degree or (nextNode.sibling != None and currNode.degree == nextNode.sibling.degree)):
				prevNode = currNode
				currNode = nextNode
			elif currNode.key < nextNode.key:
				currNode.sibling = nextNode.sibling
				self.link(currNode, nextNode)
			else:
				if prevNode == None:
					self.head = nextNode
				else:
					prevNode.sibling = nextNode
				self.link(nextNode, currNode)
				currNode = nextNode
			nextNode = currNode.sibling
		return self

	def insert(self, key):
		n = Node(key)
		if (self.head == None):
			self.head = n
		else:
			temp = self.makeHeap()
			temp.head = n
			self.union(temp)

	def extractMin(self):
		n = self.head
		p, y, z = None, None, None
		min = 99999
		while n != None:
			if n.key < min:
				min = n.key
				y = n
				z = p
			p = n
			n = n.sibling
		z.sibling = y.sibling
		temp = self.makeHeap()
		currNode = y.child
		if currNode == None:
			return y
		prevNode = None
		nextNode = currNode.sibling
		while nextNode != None:
			currNode.sibling = prevNode
			currNode.parent = None
			prevNode = currNode
			currNode = nextNode
			nextNode = currNode.sibling
		currNode.sibling = prevNode
		currNode.parent = None
		temp.head = currNode
		self.union(temp)
		return y

	def decreaseKey(self, n, k):
		if k >= n.key:
			return None
		n.key = k
		y = n.parent
		while y != None and y.key > n.key:
			self.swap(n, y)
			n = y
			y = n.parent

	def swap(self, n, y):
		n.key = n.key ^ y.key
		y.key ^= y.key ^ n.key
		n.key = n.key ^ y.key

	def deleteNode(self, n):
		self.decreaseKey(n, -99999)
		self.extractMin()

	def deleteNodeByKey(self, key):
		n = self.find(key, self.head)
		if n == None:
			return None
		self.decreaseKey(n, -99999)
		self.extractMin()

	def find(self, key, n):
		if n == None:
			return None
		if key == n.key:
			return n
		n1 = self.find(key, n.sibling)
		n2 = self.find(key, n.child)

		if n1 != None or n2 != None:
			if n1 != None:
				return n1
			else:
				return n2
		else:
			return None

	def traversal(self, n):
		if n == None:
			return None
		print self.traversal(n.child),
		print self.traversal(n.sibling),
		print n.key


