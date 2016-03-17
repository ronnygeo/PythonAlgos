#Nil = Node("BLACK", None, None)

class Nil(object):
	def __init__(self):
		self.color = "BLACK"

NIL = Nil()

class Node(object):
	def __init__(self, key, color="RED", left=NIL, right=NIL, parent=NIL):
		self.key = key
		self.color = color
		self.left = left
		self.right = right
		self.parent = parent
