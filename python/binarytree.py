import sys


class Node :
	def __init__( self, key ):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None

	# def __str__(self):
		# retstr = ""
		# retstr += "key: "
		# retstr += str(self.key)
		# return retstr

class BinaryTree :
	def __init__( self ):
		self.root = None

	def searchTree( self, node, k):
		if node.key == -1:
			return node
		if node.key == k:
			return node
		elif k < node.key:
			return self.searchTree(node.left, k)
		elif k > node.key:
			return self.searchTree(node.right, k)

	def insert(self, node, k):
		if (self.root == None):
			self.root = Node(k)
			self.root.left = Node(-1)
			self.root.right = Node(-1)
			self.root.right.parent = self.root
			self.root.left.parent = self.root
			return
			# self.root.left 
		w = self.searchTree(self.root, k)
		# print "ugh" + str(w.key)
		# while w is internal
		while w.key != -1:
			# print("z")
			w = self.searchTree(w.left, k)
		w.key = k
		w.right = Node(-1)
		w.left = Node(-1)

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


# example code
t = BinaryTree()

t.insert(t.root, 7)
t.insert(t.root, 3)
t.insert(t.root, 2)
t.insert(t.root, 6)
t.insert(t.root, 5)

# print (t.root)
# print (t.root.right)

t.inOrder(t.root, 0)


