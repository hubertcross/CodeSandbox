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

	def searchTree( self, node, k):
		if len(node.list.keys) == 0: # external node (list of keys is empty)
			return "external node"
		if k in node.list:
			return "key found"
		# else:
		# 	return "key not found"
		elif k < node.list[0]:
			print("search key is less than first stored key in current node. going left")
			return self.searchTree(node.children[0], k)
		# elif k < node.key:
		# 	return self.searchTree(node.left, k)
		# elif k > node.key:
		# 	return self.searchTree(node.right, k)

	# def insert(self, node, k):

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

t = TwoThreeFourTree()

t.root = Node()
t.root.children.append(Node())
t.root.children.append(Node())

t.root.addKey(5)

print(t.searchTree(t.root, 4))

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

