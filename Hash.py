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
		for key in self.keys:
			n = self.find(key)
			if n == None:
				self.insert(key, 1)
			else:
				self.increase(key)

	def insert(self, key, value):
		index = self.hash_function(key)
		if self.hash[index] == None:
			node = Node(key, value)
			self.hash[index] = LinkedList(node)
		else:
			cur = self.hash[index].search(key)
			if cur == None:
				self.hash[index].insert(key, value)
			else:
				cur.set_value(value)

	def delete(self, key):
		index = self.hash_function(key)
		if self.hash[index] != None:
			self.hash[index].delete(key)

	def increase(self, key):
		n = self.find(key)
		v = n.get_value()
		n.set_value(v + 1)


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
		for i in range(self.maxHash):
			if self.hash[i]:
				self.hash[i].printkv()