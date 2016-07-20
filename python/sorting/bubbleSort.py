import sys
import random

class BubleSort:
	def __init__(self, count):
		self.totalElements = count

	def IntGenerator(self):
		a =[]
		for i in range(self.totalElements):
			a.append(random.randint(1, self.totalElements))
		return a

	def Sort(self):
		
		a = self.IntGenerator()
		print a
		print len(a)
		
		for passnum in range(len(a) - 1, 0, -1):
			print 'passnum = ' , passnum
			print a
			for i in range(passnum):
				if a[i] < a[i+1]:
					a[i], a[i+1] = a[i+1], a[i]
				print "i = ", i
				print a
			

		print a


b = BubleSort(10)

b.Sort()
#print b



