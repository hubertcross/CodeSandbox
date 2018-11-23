import sys


def shiftLeft(l, n):
	return l[n:] + l[:n]

def shiftRight(l, n):
	return l[-n:] + l[:-n]

class OrderedList :
	def __init__(self):
		self.keys = [] # empty array or 'sequence'

	def insert(self, key):
		# insert key into 'keys' sequence in order
		i = 0
		inserted = 0
		while i < len(self.keys):
			if (key < self.keys[i]):
				self.keys.insert(i, key)
				inserted = 1
				break
			i += 1
		if (inserted != 1):
			self.keys.insert(i, key)
		return i

	# def pop(self, i):
	# 	return self.keys.pop(i)

	def remove(self, key):
		self.keys.remove(key)

	def __str__(self):
		i = 0
		retstring = ""
		while i < len(self.keys):
			# print("balls" + str(i))
			retstring += " "
			retstring += str(self.keys[i])
			retstring += " "
			i += 1
		return retstring

	def __getitem__(self, element):
		return self.keys[element]


class Node :

	def __init__( self ):
		self.list = OrderedList()
		self.children = [None, None, None, None] # will be sequence of Node
		self.parent = None

	def addKey(self, key):
		# either here or in the inner method, we should also relocate the children according to the new
		# placement of the keys
		return self.list.insert(key)

	def reorderChildren(self, offset):
		print("reordering children")
		# if offset == 0:
		# 	self.children = shiftRight(self.children, 1)
		# after an insert, ensure sure the children's locations make sense
		# a node with keys  |2| and children[1] with |4| which has 1 key added becomes |1 2|
		# that |4| child should reside in children[2]
		# for i in range(len(self.children)):
		# 	if self.children[i] != None:
		# 		for key in self.list:
		# 			if hasattr(self.children[i], 'list'):
		# 				print("comparing node's key %i with child's rightmost key %i" % (key, self.children[i].list[len(self.children[i].list.keys) -1]) )
		# 				if self.children[i].list[len(self.children[i].list.keys) -1] > key:
		# 					print("Shift child with right-most key %i to the right" % self.children[i].list[len(self.children[i].list.keys) -1])
		# 					self.children = shiftRight(self.children, 1)

		for child in self.children:
			print(child)
			if child != None:
				# for key in self.list:
				for i in range(self.children.index(child), len(self.list.keys)):
					# print("bleh %i %i", (child.list[len(child.list.keys) - 1], key ) )
					print("bleh %i %i", (child.list[len(child.list.keys) - 1], self.list[i] ) )
					if child.list[len(child.list.keys) - 1] > self.list[i]:
						print("shifting right")
						self.children = shiftRight(self.children, 1)


	def __str__(self):
		retstr = ""
		retstr += "node: "
		retstr += str(self.list)
		return retstr

class TwoThreeFourTree :
	def __init__( self ):
		self.root = None

	def searchTree( self, node, k, depth, inserting, parentNode):
		# print("hubert")
		# print(parentNode)
		# print(node)
		root3node = 0
		if not hasattr(node, 'list'):
			print("External node reached")
			return parentNode
		# sys.stdout.write('Parent: ')
		# print(parentNode)
		# if inserting is set to 1, we have to kick middle-keys in 3-key-nodes up to parent ...
		if hasattr(node, 'list'):
			print("depth: %i searchkey: %i # keys in this node: %i. |keys: %s" % ( (depth + 1), k, (len(node.list.keys) ), node.list ))
		# if len(node.list.keys) == 0: # external node (list of keys is empty)
			# return "reached an external (keyless) node. key not found"

		if inserting == 1:
			# check if we've reached a 3-key-node
			if len(node.list.keys) == 3:
				print("Node has three keys, since we're doing an insert we're gonna restructure")
				print("debug0 %s" % node.list)

				
				# if parent is None, we're dealing with the root node and a new node must be created
				if parentNode == None:
					root3node = 1
					parentNode = Node()
					self.root = parentNode
					node.parent = parentNode
					self.root.children[0] = node
				# move the middle key to the parent
				parentNode.addKey(node.list.keys.pop(1))
				print("debug1 %s" % node.list)

				# create a sibling for current node that will hold current's THIRD key
				newSibling = Node()
				newSibling.parent = parentNode # sib has same parent of course
				print("debug2 %s" % node.list)
				#### IT'S NOT ALWAYS THE THIRD KEY
				#### IF THE 3NODE IS ITS PARENTS 
				if node == node.parent.children[0]:
					print("bleh0")
					newSibling.addKey(node.list.keys.pop(1)) # move current's third key to sibling
				elif node == node.parent.children[1]:
					if len(node.list.keys) == 2:
						print("BLEH1")
						newSibling.addKey(node.list.keys.pop(0)) # test if same case as above works
						parentNode.children[2] = node
				elif node == parentNode.children[2]:
					print("3node is parent's rightmost child")
					newSibling.addKey(node.list.keys.pop(0)) # move current's first key into new sibling
				print("debug3 %s" % node.list)
				print("root: %s" % self.root)
				# print(newSibling)
				# print(newSibling.parent)
				# if len(node.children) == 3:
				if (node.children[2] != None):
					print("Node's right key has left child, moving to sibling")
					newSibling.children[0] = (node.children[2]) # move the left and right children
					newSibling.children[0].parent = newSibling
					node.children[2] = None
				# if len(node.children) == 3:
				if (node.children[3] != None):
					print("node's right key has a right child, moving to sibling")
					newSibling.children[1] = (node.children[2]) # of current node's THIRD key
					newSibling.children[1].parent = newSibling
					node.children[3] = None
				print("linking new sibling to node's parent")
				# parentNode.children.insert(1, newSibling) # establish link from parent
				parentNode.children[1] = newSibling

				print("New node created: %s and with children:" % newSibling )
				for child in newSibling.children:
					print("child: %s" % child)

		if root3node: # if the root node a 3node, let's start over from new root
			node = self.root
		if k in node.list:
			# return "key found"
			sys.stdout.write('Found key ->')
			return node
		if len(node.children) == 0:
			print("reached a leaf (childless) node that doesn't contain k, so k is not in the tree")
			return node

		for i in range(len(node.list.keys)):
			# print("ugh")
			print("Check if searchkey %i < %i" % (k, node.list[i]) )
			if (k < node.list[i]):
				print("The search key is less than the %ith element. Searching left of %ith element " % (i, i))
				print("ugh. %s" % node)
				if node.children[i] == None:
					print("This node is external. Insert key here")
					return node
				return self.searchTree(node.children[i], k, depth + 1, inserting, node)
			# // check the right side of the last key
		print("Check if searchkey %i > %i" % (k, (node.list[len(node.list.keys) - 1] ) ))
		if (k > node.list[len(node.list.keys) - 1] ):
			print("The search key is greater than right-most element of the current node. Search right of final %ith element" % (len(node.list.keys)) )
			return self.searchTree(node.children[len(node.list.keys)], k, depth + 1, inserting, node)

	def insert(self, k):
		# root node
		if self.root == None:
			self.root = Node()
			self.root.addKey(k)
		# search for they k in the tree
		# if you find k, keep going 'left' until you reach a leaf node (node with no children)
		myNode = self.searchTree(self.root, k, 0, 1, None)

		if k in myNode.list:
			# go all the way to the left
			print("K is in the returned node, going left until we hit a leaf node")
		elif k not in myNode.list:
			print("K is not in the tree, we can insert it at the current node: ")
			print(myNode)
			x = myNode.addKey(k)
			print("insert %i returned %i | %s" % (k, x, myNode))
			# this is not necessarily always a shift right by 1 !!! it depends how the new key lines up
			# myNode.children = shiftRight(myNode.children, 1)
			myNode.reorderChildren(x)
			print(myNode)
		# elif myNode == None:
		# 	myNode = Node()
		# 	myNode.addKey(k)
		# 	print("created new node with key %i" % k)

# for i in range(2):
# 	print('balls %i' % i)

t = TwoThreeFourTree()

# t.root = Node()

# t.root.addKey(8)
# t.root.addKey(10)

# t.root.children[0] = Node()
# t.root.children[0].parent = t.root
# t.root.children[0].addKey(2)

# t.root.children[0].addKey(5)

# t.root.children[0].addKey(7)

# newNode = Node()
# newNode.addKey(4)
# newNode.parent = t.root.children[0]
# t.root.children[0].children[1] = newNode


# bleh = Node()
# bleh.addKey(6)
# bleh.parent = t.root.children[0]
# t.root.children[0].children[2] = bleh


# t.root.children[1] = Node()
# t.root.children[1].parent = t.root
# t.root.children[1].addKey(9)

# t.root.children[2] = Node()
# t.root.children[2].parent = t.root
# t.root.children[2].addKey(17)


# print("new search for key %i" % 3)
# print(t.searchTree(t.root, 3, 0, 0, None))

# print("")
# print("new search for key %i" %  4)
# print(t.searchTree(t.root, 4, 0, 0, None))


# print("")
# print("new search for key %i" %  1)
# print(t.searchTree(t.root, 1, 0, 0, None))

t.insert(4)
t.insert(3)
t.insert(10)
t.insert(15)
t.insert(5)
t.insert(1)
t.insert(17)
t.insert(19)
t.insert(2)
t.insert(6)

print("root:")
print(t.root)
print("root's first child")
print(t.root.children[0])
print(t.root.children[1])
print(t.root.children[2])
print(t.root.children[3])
# print("root's first grandchild")
print(t.root.children[0].children[0])
print(t.root.children[0].children[1])
print(t.root.children[0].children[2])
print(t.root.children[0].children[3])
print(t.root.children[1].children[0])
print(t.root.children[1].children[1])
print(t.root.children[1].children[2])
print(t.root.children[1].children[3])
# print(t.root.children[3].children[0])
# print(t.root.children[3].children[1])
# print(t.root.children[3].children[2])
# print(t.root.children[3].children[3])
# print("root's second grandchild")
# print(t.root.children[0].children[3])

# print("root's second child")
# print(t.root.children[1])
# print(t.root.children[1].children[0])


# print(t.searchTree(t.root, 15, 0))

# o = OrderedList()
# o.insert(5)
# o.insert(1)
# o.insert(3)
# o.insert(2)
# o.insert(7)
# o.insert(8)

# print(str(len(o.keys)))
# print(o)

# n = Node()
# n.addKey(1)
# print("hubert: " + str(n.list[0]))

# x = Node()
# x.addKey(8)

# n.children.insert(0, x)
# print("burgers: " + str(n.children[0].list[0]))

