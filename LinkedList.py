class Node(object):

	def __init__(self, key, value=None, positions=None,next_element=None):
		self.key = key
		self.value = value
		self.positions = positions
		self.next_element = next_element

	def get_key(self):
		return self.key

	def get_value(self):
		return self.value

	def get_position(self):
		return self.positions

	def get_next_element(self):
		return self.next_element

	def set_value(self, value):
		self.value = value

	def set_next_element(self, next_element):
		self.next_element = next_element

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	def insert(self, k, v):
		newNode = Node(k, v)
		newNode.next_element = self.head
		self.head = newNode

	def search(self, k):
		cur = self.head
		while cur:
			if cur.get_key() == k:
				break
			cur = cur.get_next_element()
		return cur

	def count(self):
		cur = self.head
		count = 0
		while cur:
			count += 1
			cur = cur.get_next_element()
		return count

	def delete(self, k):
		cur = self.head
		prev = None
		while cur:
			if cur.get_key() == k:
				if prev != None:
					prev.set_next_element(cur.get_next_element())
					break
				else:
					self.head = cur.get_next_element()
					break
			prev = cur
			cur = cur.get_next_element()
		return cur

	def printkv(self):
		cur = self.head
		while cur:
			print cur.get_key(), cur.get_value()
			cur = cur.get_next_element()
