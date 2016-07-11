class Queue:
	def __init__(self):
		self.queue = []

	def InQueue(self, item):
		self.queue.append(item)

	def DeQueue(self):
		if len(self.queue) <= 0:
			print('Queue is empty')
			raise

		return self.queue.pop(0)

	def Size(self):
		return len(self.queue)

	def IsEmpty(self):
		return self.queue == []

	def PrintAsString(self):
		return str("|") . join(str(item) for item in self.queue)


Q = Queue()
Q.InQueue(45)
print Q.PrintAsString()
print Q.Size()
Q.InQueue(11)
print Q.Size()
print Q.PrintAsString()

Q.InQueue(13)
print Q.Size()
print Q.PrintAsString()
print Q.Size()
print Q.DeQueue()
print Q.Size()
print Q.PrintAsString()
print Q.DeQueue()
print Q.Size()
print Q.PrintAsString()
print Q.DeQueue()
print Q.Size()
print Q.PrintAsString()
print Q.DeQueue()
print Q.Size()
print Q.PrintAsString()
