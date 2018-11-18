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
		retstring = "retstring:"
		while i < len(self.keys):
			print("balls" + str(i))
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
		retstr += "key: "
		retstr += str(self.key)
		return retstr

class TwoThreeFourTree :
	def __init__( self ):
		self.root = None

	def searchTree( self, node, k, depth):
		print("depth: %i searchkey: %i # keys in this node: %i. |keys: %s" % ( (depth + 1), k, (len(node.list.keys) ), node.list ))
		if len(node.list.keys) == 0: # external node (list of keys is empty)
			return "external node. has no keys"
		if k in node.list:
			return "key found"

		for i in range(len(node.list.keys)):
			# print("ugh")
			print("Check if searchkey %i < %i" % (k, node.list[i]) )
			if (k < node.list[i]):
				print("The search key is less than the %ith element. Searching left of %ith element " % (i, i))
				return self.searchTree(node.children[i], k, depth + 1)
			# // check the right side of the last key
		print("Check if searchkey %i > %i" % (k, (node.list[len(node.list.keys) - 1] ) ))
		if (k > node.list[len(node.list.keys) - 1] ):
			print("The search key is greater than right-most element of the current node. Search right of final %ith element" % (len(node.list.keys)) )
			return self.searchTree(node.children[len(node.list.keys)], k, depth + 1)

		# return "key not found"

	def inOrder(self, node, depth):
		if (node.key == -1):
			return
		self.inOrder(node.left, depth + 1)
		#visit
		for i in range(1, depth+ 1):
			# print("  ", end=' ')
			sys.stdout.write('   ')

		print("key: " + str(node.key))
		self.inOrder(node.right, depth + 1)


for i in range(2):
	print('balls %i' % i)

t = TwoThreeFourTree()

t.root = Node()
t.root.children.append(Node())
t.root.children.append(Node())

t.root.addKey(5)
t.root.addKey(10)
t.root.children.append(Node())

t.root.children[0].addKey(4)

t.root.children[0].children.append(Node())
t.root.children[0].children.append(Node())


print("new search for key %i" % 3)
print(t.searchTree(t.root, 3, 0))

print("")
print("new search for key %i" %  4)
print(t.searchTree(t.root, 4, 0))


print("")
print("new search for key %i" %  15)
print(t.searchTree(t.root, 15, 0))


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

