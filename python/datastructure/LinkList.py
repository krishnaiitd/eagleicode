
# Link List implementation
class Node:
	def __init__(self, item = ''):
		self.data = item
		self.next = None;

	def __str__(self):
		return str(self.data)

	def SetData(self, item):
		self.data = item;

	def GetData(self):
		return self.data

	def SetNext(self, Next):
		self.next = Next

	def GetNext(self):
		return self.next



class LinkList:
	def __init__(self):
		self.head = None

	def InsertAtFirst(self, item):
		node = Node(item)
		
		node.SetNext(self.head)

		self.head = node

		return self.head

	def InsertAtLast(self, item):
		node = Node(item)

		if self.head is None:
			self.head = node
			return self.head

		StartNode = self.head

		while StartNode.GetNext() is not None:
			StartNode = StartNode.GetNext()

		
		StartNode.SetNext(node)

		return self.head

	def RemovedAtFirst(self):
		if self.head is None:
			print('Empty Link List')
			raise

		start = self.head
		
		self.head =  start.GetNext()

		return start.GetData()

	def RemovedAtLast(self):
		if self.head is None:
			print('LinkList is empty')
			raise

		previousNode = self.head
		start = previousNode.GetNext()

		if start is None:
			item = previousNode.GetData()
			previousNode.SetNext(None)
			return item

		while start.GetNext() is not None:
			previousNode = start
			start = start.GetNext()

		item = start.GetData()
		previousNode.SetNext(None)
		return item

	def Size(self):
		counter = 0
		start = self.head
		while start.GetNext() is not None:
			counter = counter + 1
			start = start.GetNext()

		return counter + 1

	def PrintAsString(self):
		s =  ''
		start = self.head;
		while start.GetNext() is not None:
			item = start.GetData()
			s = s + str(item) + "->"
			start = start.GetNext()

		s = s + str(start.GetData()) + "-> None"
		return s


head = LinkList()

head.InsertAtLast(21)
head.InsertAtLast(11)
head.InsertAtLast(121)
head.InsertAtLast(122)
head.InsertAtFirst(66)

head.InsertAtFirst(660)
head.InsertAtFirst('krishna')

head.InsertAtLast('Prasad')

head.InsertAtLast('Veena')
print head.PrintAsString()
print head.Size()
print 'Removed from Frist'
head.RemovedAtFirst()

print head.PrintAsString()
print head.Size()
print 'Removed from last'
head.RemovedAtLast()

print head.PrintAsString()
print head.Size()
print 'Removed from Frist'
head.RemovedAtFirst()

print head.PrintAsString()
print head.Size()

head.InsertAtFirst('afdsf')

print head.PrintAsString()
print head.Size()
