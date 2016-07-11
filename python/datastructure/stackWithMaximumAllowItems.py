# Stack where we have given maximum allowed length of the stack i.e allowed size of the stack
class Stack:
	def __init__(self, allowed_size):
		self.stack = []
		self.allowed_size = allowed_size

	def Insert(self, item):
		if len(self.stack) > self.allowed_size:
			print('Stack is full, first delete some item then try to add on it')
			raise
		self.stack.append(item)

	def Remove(self):
		if self.stack > 0:
			return self.stack.pop()
		else:
			print('Stack is empty')

	def IsEmpty(self):
		self.stack == []

	def Size(self):
		return len(self.stack)

	def PrintAsString(self):
		return str("|") . join(str(item) for item in self.stack)



#s = Stack(5);

#s.Insert(34)
#print s.PrintAsString()

