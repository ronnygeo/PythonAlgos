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


def rb_transplant(T, u, v):
	if u.p == NIL:
		T.root = v
	elif u == u.p.left:
		u.p.left = v
	else:
		u.p.right = v
	v.p = u.p

def rb_delete(T, z):
	y = z
	y_org_color = y.color
	if z.left == NIL:
		x = z.right
		rb_transplant(T, z, z.right)
	elif z.right == NIL:
		x = z.left
		rb_transplant(T, z, z.left)
	else:
		y = rbt_minimum(z.right)
		y_org_color = y.color
		x = y.right
		if y.p == z:
			x.p = y
		else:
			rb_transplant(T, y, y.right)
			y.right = z.right
			y.right.p = y
		rb_transplant(T, z, y)
		y.left = z.left
		y.left.p = y
		y.color = z.color
	if y_org_color == "BLACK":
		rb_delete_fixup(T, x)

def rb_delete_fixup(T, x):
	while x != T.root and x.color == "BLACK":
		if x == x.p.left:
			w = x.p.right
			if w.color == "RED":
				w.color = "BLACK"
				x.p.color = "RED"
				left_rotate(T, x.p)
				w = x.p.right
			if w.left.color == "BLACK" and w.right.color == "BLACK":
				w.color = "RED"
				x = x.p
			elif w.right.color == "BLACK":
				w.left.color = "BLACK"
				w.color = "RED"
				right_rotate(T, w)
				w = x.p.right
			w.color = x.p.color
			x.p.color = "BLACK"
			w.right.color = "BLACK"
			left_rotate(T, x.p)
			x = T.root
		else:
			w = x.p.left
			if w.color == "RED":
				w.color = "BLACK"
				x.p.color = "RED"
				right_rotate(T, x.p)
				w = x.p.left
			if w.right.color == "BLACK" and w.left.color == "BLACK":
				w.color = "RED"
				x = x.p
			elif w.left.color == "BLACK":
				w.right.color = "BLACK"
				w.color = "RED"
				left_rotate(T, w)
				w = x.p.left
			w.color = x.p.color
			x.p.color = "BLACK"
			w.left.color = "BLACK"
			right_rotate(T, x.p)
			x = T.root
	x.color = "BLACK"

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
