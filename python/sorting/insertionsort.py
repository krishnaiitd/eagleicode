import sys
import timeit
import random 

class InsertionSort:
	def __init__(self, n):
		self.totalLen = n

	def GenerateIntergers(self):
		a = []
		for i in range(self.totalLen):
			a.append(random.randint(1, self.totalLen))
		return a

	def Sort(self):
		a = self.GenerateIntergers()
		for passnum in range(len(a) - 1):
			#print 'passnum = ', passnum, a

			start = passnum + 1
			while start > 0 and a[start] > a[start -1]:
				a[start], a[start - 1] = a[start - 1], a[start]
				start = start - 1

			#print 'after ', passnum , ' iteration', a

	def GetTime(self):
		start_time = timeit.default_timer()
		self.Sort()
		elapsed = timeit.default_timer() - start_time
		print "Elapsed time: " + str(round(elapsed, 2)) + ' seconds'

insertion = InsertionSort(1000)
insertion.GetTime()







