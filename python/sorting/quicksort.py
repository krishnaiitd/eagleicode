import sys
import timeit
import random 

class QuickSort():
	def __init__(self, n):
		self.totalElements = n
		self.inputArray = []
		self.GenerateInt()

	def GenerateInt(self):
		for i in range(self.totalElements):
			self.inputArray.append(random.randint(1, self.totalElements))

		print 'input Array: ', self.inputArray
		return self.inputArray

	def SortArray(self):
		self.QSort(sefl.inputArray, 0, len(self.inputArray) - 1)

	def QSort(self, a, lo, hi):

		if lo - li < 2:
			return self.inputArray

		if lo < hi:
			p = self.Partition(lo, hi)
			self.Sort(lo, p-1)
			self.Sort(p+1, hi)

	def Partition(self, lo, hi):
		print '====Partition==== called'
		print self.inputArray
		i = lo # pivot place
		pivot = self.inputArray[hi]
		print 'pivot = ' , pivot
		for j in range(0, hi-1):
			if self.inputArray[j] <= pivot:
				self.inputArray[j], self.inputArray[i] = self.inputArray[i],  self.inputArray[j]
				i = i + 1

			print 'i = ' , i, 'array value ', self.inputArray	
			# swap the pivot with li
		self.inputArray[i], self.inputArray[hi] = self.inputArray[hi], self.inputArray[i]
		return i

	def PrintSortArray(self):
		print self.inputArray


q = QuickSort(5)
q.SortArray()
q.PrintSortArray()




def Qsort(a):
	if len(a) == 0:
		return a
	pivot = a[0]
	pivots = filter(lambda x: x == pivot, a)
	left = Qsort(filter(lambda x: x < pivot, a))
	right = Qsort(filter(lambda x: x> pivot, a))
	return left + pivots + right







