class Stack:
	def __init__(self):
		self.stack = []
	def Insert(self, item):
		self.stack.append(item)

	def Pop(self):
		if len(self.stack) <= 0:
			print('Stack is empty')
			raise

		return self.stack.pop()

	def Size(self):
		return len(self.stack)

	def IsEmpty(self):
		return self.stack == []


# Implement Queue using above Stack


class Queue:
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def InQueue(self, item):
		# In Queue in stack 1
		self.s1.Insert(item)

	def DeQueue(self):
		# Get all the element from S1 till last one, and placed into second Stack S2, return the last
		# element from S1 and again replaced back from S2 to S1.
		el = ''
		if self.s1.Size() <= 0:
			print('Queue is empty')
			return

		for i in range(self.s1.Size()):
			self.s2.Insert(self.s1.Pop())

		rel = self.s2.Pop()

		# Replace back all element to S1
		for item in range(self.s2.Size()):
			el = self.s2.Pop()
			self.s1.Insert(el)

		return rel



Q = Queue()
Q.InQueue(1)
Q.InQueue(2)
print Q.DeQueue()
print '---'
print Q.DeQueue()
print '---'
Q.InQueue(45)
Q.InQueue(52)
print Q.DeQueue()
print '---'
