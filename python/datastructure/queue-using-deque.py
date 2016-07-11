from collections import deque
class Queue:
	def __init__(self):
		self.queue = deque()

	def InQueue(self, item):
		self.queue.append(item)
	def DeQueue(self):
		if len(self.queue) <= 0:
			print('Queue is empty')
			raise

		return self.queue.popleft()
	def Size(self):
		return len(self.queue)

	def IsEmpty(self):
		return len(self.queue) == 0

	def PrintAsString(self):
		print str("|") . join(str(item) for item in self.queue)


Q = Queue();

Q.InQueue(34)
Q.PrintAsString()

print 'size = ' +  str(Q.Size())


Q.InQueue(314)
Q.PrintAsString()
			
print 'size = ' +  str(Q.Size())

Q.InQueue(3234)
Q.PrintAsString()

print 'size = ' +  str(Q.Size())

item = Q.DeQueue()
print item
Q.PrintAsString()
print 'size = ' +  str(Q.Size())


item = Q.DeQueue()
print item
Q.PrintAsString()
print 'size = ' +  str(Q.Size())


item = Q.DeQueue()
print item
Q.PrintAsString()


print 'size = ' +  str(Q.Size())

item = Q.DeQueue()
print item
Q.PrintAsString()

