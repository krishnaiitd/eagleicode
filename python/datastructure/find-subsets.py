# Given a target sum, populate all subsets, whose sum is equal to the target sum, from an int array

class FindSubset:
	def __init__(self):
		self.sumInStack = 0
		self.stack = []

	def populateSubset(self, data, startIndex, endIndex, target):
		if self.sumInStack == target:
			st = "+" . join(stack)
			result = str(target) +  ' = ' + st
			print(st)
		for i in range(startIndex, endIndex, 1):
			if self.sumInstack + data[i] <= target:
				self.stack.append(data[i])
				self.sumInstack = self.sumInstack + data[i]
				self.populateSubset(data, startIndex + 1, endIndex)
				self.sumInStack = self.sumInstack - stack.pop()

aa = [1,3,4,5,6,15]
target = 15
sumInStack = 0

s =  FindSubset()
s.populateSubset(aa, 0, len(aa), target)




