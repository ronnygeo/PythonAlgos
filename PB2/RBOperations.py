from Node import *
from RBTree import *


def left_rotate(T, x):
	y = x.right
	x.right = y.left
	if y.left != NIL:
		y.left.p = x
	y.p = x.p
	if x.p == NIL:
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
	if y.right != NIL:
		y.right.p = x
	y.p = x.p
	if x.p == NIL:
		T.root = y
	elif x == x.p.right:
		x.p.right = y
	else:
		x.p.left = y
	y.right = x
	x.p = y

def rb_insert(T, z):
	y = NIL
	x = T.root
	while x != NIL:
		y = x
		if z.key < x.key:
			x = x.left
		else:
			x = x.right
	z.p = y
	if y == NIL:
		T.root = z
	elif z.key < y.key:
		y.left = z
	else:
		y.right = z
	z.left = NIL
	z.right = NIL
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
	while x.left != NIL:
		x = x.left
	return x


def rbt_maximum(x):
	while x.right != NIL:
		x = x.right
	return x


def rbt_successor(x):
	if x.right != NIL:
		return rbt_minimum(x.right)
	y = x.p
	while y != NIL and x == y.right:
		x = y
		y = y.p
	return y


def rbt_predecessor(x):
	if x.left != NIL:
		return rbt_maximum(x.left)
	y = x.p
	while y != NIL and x == y.left:
		x =y
		y = y.p
	return y


def rbt_height(n):
	if n == NIL:
		return 0
	return max(1 + rbt_height(n.left), 1 + rbt_height(n.right))


def sort(node):
	l = []
	if node != NIL:
		l += sort(node.left)
		l.append(node.key)
		l += sort(node.right)
	return l


def search(T, key):
	x = T.root
	while x != NIL and key != x.key:
		if key < x.key:
			x = x.left
		else:
			x = x.right
	return x
