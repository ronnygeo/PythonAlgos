#Nil = Node("BLACK", None, None)

class Nil(object):
	def __init__(self):
		self.color = "BLACK"

class Node(object):
	def __init__(self, value, color="RED", left=Nil(), right=Nil(), parent=Nil()):
		self.value = value
		self.color = color
		self.left = left
		self.right = right
		self.parent = parent
