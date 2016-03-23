class Node(object):
	def __init__(self, key=None):
		self.key = key
		self.degree = 0
		self.parent = None
		self.child = None
		self.sibling = None