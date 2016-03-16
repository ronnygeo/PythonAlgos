from LinkedList import *

class Hash(object):
	maxHash = 10000
	hash = []

	def __init__(self, keys = None):
		self.keys = keys
		#print keys
		for i in range(self.maxHash):
			self.hash = [None for i in range(self.maxHash)]
		self.insert_all_keys()

	def hash_function(self, str):
		#print str
		sum = 0
		i = len(str) - 1
		while i >= 0:
			sum += ord(str[i]) * i
			i -= 1
		return sum % self.maxHash


	def insert_all_keys(self):
		for k in range(len(self.keys)):
			key = self.keys[k]
			n = self.find(key)
			if n == None:
				self.insert(key, 1, k)
			else:
				self.increase(key, k)

	def insert(self, key, value, pos):
		index = self.hash_function(key)
		if self.hash[index] == None:
			node = Node(key, value)
			newNode = Node(key, pos)
			l = LinkedList(newNode)
			node.set_positions(l)
			self.hash[index] = LinkedList(node)
		else:
			cur = self.hash[index].search(key)
			if cur == None:
				self.hash[index].insert(key, value)
				posNode = Node(key, pos)
				l = LinkedList(posNode)
				self.hash[index].search(key).set_positions(l)
			else:
				cur.set_value(value)
				p = cur.get_positions()
				cur.set_positions(p.insert(key, pos))

	def delete(self, key):
		index = self.hash_function(key)
		if self.hash[index] != None:
			self.hash[index].delete(key)

	def increase(self, key, pos):
		n = self.find(key)
		v = n.get_value()
		n.set_value(v + 1)
		p = n.get_positions()
		newNode = Node(key, pos)
		if p == None:
			l = LinkedList(newNode)
			n.set_positions(l)
		else:
			p.insert(key, pos)

	def find(self, key):
		index = self.hash_function(key)
		#print index
		if self.hash[index] != None:
			cur = self.hash[index].search(key)
			if cur == None:
				return None
			else:
				return cur

	def list_all_keys(self):
		output = ""
		for i in range(self.maxHash):
			if self.hash[i]:
				output += self.hash[i].printkv()
				output += "\n"
		return output


