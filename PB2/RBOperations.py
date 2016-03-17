from Node import *
from RBTree import *


def left_rotate(T, x):
	y = x.right
	x.right = y.left
	if y.left != Nil():
		y.left.p = x
	y.p = x.p
	if x.p == Nil():
		T.root = y
	elif x == x.p.left:
		x.p.left = y
	else:
		x.p.right = y
	y.left = x
	x.p = y


def right_rotate(T, x):
	y = x.left
	x.left = y.right
	if y.right != Nil():
		y.right.p = x
	y.p = x.p
	if x.p == Nil():
		T.root = y
	elif x == x.p.right:
		x.p.right = y
	else:
		x.p.left = y
	y.right = x
	x.p = y

def rb_insert(T, z):
	y = Nil()
	x = T.root
	while x != Nil():
		y = x
		if z.key < x.key:
			x = x.left
		else:
			x = x.right
	z.p = y
	if y == Nil():
		T.root = z
	elif z.key < y.key:
		y.left = z
	else:
		y.right = z
	z.left = Nil()
	z.right = Nil()
	z.color = "RED"
	rb_insert_fixup(T, z)

def rb_insert_fixup(T, z):
	while z != T.root and z.p.color == "RED":
		if z.p == z.p.p.left:
			y = z.p.p.right
			if y.color == "RED":
				z.p.color = "BLACK"
				y.color = "BLACK"
				z.p.p.color = "RED"
				z = z.p.p
			else:
				if z == z.p.right:
					z = z.p
					left_rotate(T, z)
				z.p.color = "BLACK"
				z.p.p.color = "RED"
				right_rotate(T, z.p.p)
		else:
			y = z.p.p.left
			if y.color == "RED":
				z.p.color = "BLACK"
				y.color = "BLACK"
				z.p.p.color = "RED"
				z = z.p.p
			else:
				if z == z.p.left:
					z = z.p
					right_rotate(T, z)
				z.p.color = "BLACK"
				z.p.p.color = "RED"
				left_rotate(T, z.p.p)
	T.root.color = "BLACK"


def rbt_minimum(x):
	while x.left != Nil():
		x = x.left
	return x


def rbt_maximum(x):
	while x.right != Nil():
		x = x.right
	return x


def rbt_successor(x):
	if x.right != Nil():
		return rbt_minimum(x.right)
	y = x.p
	while y != Nil() and x == y.right:
		x = y
		y = y.p
	return y


def rbt_predecessor(x):
	if x.left != Nil():
		return rbt_maximum(x.left)
	y = x.p
	while y != Nil() and x == y.left:
		x =y
		y = y.p
	return y


def rbt_height(n):
	if n == Nil():
		return 0
	return max(1 + rbt_height(n.left), 1 + rbt_height(n.right))


def sort(T):
	node = T.root
	sort_helper(node)

def sort_helper(node):
	l = []
	if node != Nil() and node != None:
		l += sort(node.left)
		l.append(node.key)
		l += sort(node.right)
	return l


def search(T, key):
	x = T.root
	while x != Nil() and key != x.key:
		if key < x.key:
			x = x.left
		else:
			x = x.right
	return x
