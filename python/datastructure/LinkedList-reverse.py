 # Node class
class Node:
	def __init__(self, item):
		self.item = item
		self.next = None
	def __str__(self):
		return str(self.item) 


class LinkList:
	def __init__(self):
		self.head = None

	
	def InsertAtFirst(self, item):
		node = Node(item)
		node.next = self.head
		self.head = node


	def printList(self):
		temp = self.head
		while(temp):
			print temp.item, '->' ,
			temp = temp.next
		print 'None'
	
	def Reverse(self):
		list_reverse = None
		current = self.head
		while current is not None:
			next = current.next
			current.next = list_reverse
			list_reverse = current
			current = next

		self.head = list_reverse

	def GetFirstHalf(self):
		count = self.GetCount()
		temp = self.head
		
		firstHalf = self.head
		secondHalf = self.head

		temp1 = firstHalf
		index = 0
		while index < count /2:
			temp1 = temp1.next
			index = index + 1

		temp1.next = None

		# After above while loop firsthalf become actually first half of the list
		# Let's check the firsthalf is actual first half or not
		print 'first half list'
		tt = firstHalf
		while tt:
			print tt.item, '->',
			tt = tt.next

		print 'end of first half list'

		return firstHalf


	def GetSecondHalf(self):
		count = self.GetCount()
		temp = self.head
		index = 0
		while index <= count/2:
			index = index + 1
			temp = temp.next

		print temp.next.item
				
		secondHalf = temp.next
		# After this operation secondhald actual become second half
		print 'second half list'
		tt = secondHalf
		while tt:
			print tt.item, '->',
			tt = tt.next

		print 'end of second half list'

		return secondHalf

	def GetCount(self):
		count = 0
		temp = self.head
		while temp:
			count = count + 1
			temp = temp.next

		return count

	def ReverseHalf(self):
		firstList = self.GetFirstHalf()
		secondList = self.GetSecondHalf()



llist = LinkList()
llist.InsertAtFirst('krishna')
llist.InsertAtFirst(34)
llist.InsertAtFirst('prasad')
llist.InsertAtFirst(4)
llist.InsertAtFirst('prasad1')
llist.InsertAtFirst(42)
llist.printList()


llist.ReverseHalf()
#llist.printList()
