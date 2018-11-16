class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None
		self.tail = None		

	def add( self, data ) :
		node = Node( data )
		if self.head == None :	
			self.head = node
			self.tail = node
		else :
			node.next = self.head
			node.next.prev = node						
			self.head = node

	def append(self, data) :
		node = Node(data)
		if self.head == None and self.tail == None:
			self.head = node
			self.tail = node
		else :
			self.tail.next = node
			node.prev = self.tail
			self.tail = node

	def printAllForward(self):
		p = self.head
		# print "sauce %s" % p.data
		while p != None:
			print p.data
			p = p.next

	def printAllReverse(self):
		p = self.tail
		# print "sauce %s" % p.data
		while p != None:
			print p.data
			p = p.prev			


	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p				
				p = p.next
			if ( p.data == k ) :
				return p
		return None

	def remove( self, p ) :
		p.prev.next = p.next

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s

# example code
l = LinkedList()

l.add( 'a' )
l.add( 'b' )
l.add( 'x' )
l.add( 'c' )
l.append( 'd')

# print l
l.remove( l.search( 'a' ) )
# print
# print l

# print
# l.remove(l.search('b'))
# print l

print "ugh"
l.printAllForward()
print "nuts"
l.printAllReverse()
