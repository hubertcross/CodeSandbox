import sys

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
		self.children = [] # will be sequence of Node
		self.parent = None

	def addKey(self, key):
		self.list.insert(key)

	def __str__(self):
		retstr = ""
		retstr += "node: "
		retstr += str(self.list)
		return retstr

class TwoThreeFourTree :
	def __init__( self ):
		self.root = None

	def searchTree( self, node, k, depth, inserting):
		# if inserting is set to 1, we have to kick middle-keys in 3-key-nodes up to parent ...
		print("depth: %i searchkey: %i # keys in this node: %i. |keys: %s" % ( (depth + 1), k, (len(node.list.keys) ), node.list ))
		# if len(node.list.keys) == 0: # external node (list of keys is empty)
			# return "reached an external (keyless) node. key not found"
	
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
				return self.searchTree(node.children[i], k, depth + 1, inserting)
			# // check the right side of the last key
		print("Check if searchkey %i > %i" % (k, (node.list[len(node.list.keys) - 1] ) ))
		if (k > node.list[len(node.list.keys) - 1] ):
			print("The search key is greater than right-most element of the current node. Search right of final %ith element" % (len(node.list.keys)) )
			return self.searchTree(node.children[len(node.list.keys)], k, depth + 1, inserting)


	def insert(self, k):
		# search for they k in the tree
		# if you find k, keep going 'left' until you reach a leaf node (node with no children)
		myNode = self.searchTree(self.root, k, 0, 1)

		if k in myNode.list:
			# go all the way to the left
			print("K is in the returned node, going left until we hit a leaf node")
		elif k not in myNode.list:
			print("K is not in the tree, we can insert it at the current node: ")
			print(myNode)
			myNode.addKey(k)
			print(myNode)

# for i in range(2):
# 	print('balls %i' % i)

t = TwoThreeFourTree()

t.root = Node()
t.root.children.append(Node())
t.root.children.append(Node())

t.root.addKey(5)
t.root.addKey(10)
t.root.children.append(Node())

t.root.children[0].addKey(4)
t.root.children[1].addKey(7)

t.root.children[2].addKey(17)

# t.root.children[0].children.append(Node())
# t.root.children[0].children.append(Node())


print("new search for key %i" % 3)
print(t.searchTree(t.root, 3, 0, 0))

print("")
print("new search for key %i" %  4)
print(t.searchTree(t.root, 4, 0, 0))


print("")
print("new search for key %i" %  15)
print(t.searchTree(t.root, 15, 0, 0))

t.insert(3)

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

