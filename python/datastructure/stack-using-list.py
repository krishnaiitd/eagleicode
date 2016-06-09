#import String
class Stack:
	def __init__(self):
		self.stack = []

	def Insert(self, data):
		self.stack.append(data)

	def Remove(self):
		data = self.stack.pop()
		return data

	def IsEmpty(self):
		return self.stack == []
	
	def Size(self):
		return len(self.stack)

	def PrintAsString(self):
		return str("|") . join(str(item) for item in self.stack)

		#string =  ''
		#for item in self.stack:
		#	string = string + str(item) + str("|")
		#return string

ss = Stack();

ss.Insert(23)
print ss.PrintAsString()
ss.Insert(2)
ss.Insert(11)
print ss.PrintAsString()
print 'adding 200 in stack'
ss.Insert(200) 
print ss.stack
print 'adding 300 in stack'
ss.Insert(300) 
print ss.stack
print 'Delete an element in stack'
print ss.Remove()
print ss.stack
print ss.PrintAsString()






		
