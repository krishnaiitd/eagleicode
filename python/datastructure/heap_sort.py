## Heap Sort
def heapsort(alist):
	# Convert the list into heap:
		# each node is lower than each of its parent i.e max-heap
		# the tree is pertectly balanced
		# all leaves are in the leftmost position available.
	length = len(alist) - 1
	leastParent = length / 2
	for i in range(leastParent, -1, -1):
		moveDown(alist, i, length)

	print 'heap array ', alist
	
	# flatten heap into sorted array
	for i in range(length, 0, -1):
		if alist[0] > alist[i]:
			swap(alist, 0, i)
			moveDown(alist, 0, i - 1)

def moveDown(alist, first, last):
	largest = 2 * first + 1
	while largest <= last:
		# right child exist and it larger than left child
		if largest < last and alist[largest] < alist[largest + 1]:
			largest = largest + 1

		# right child is larger than parent
		if alist[largest] > alist[first]:
			swap(alist, largest, first)
			first = largest
			largest = 2*first + 1
		else:
			return;

def swap(alist, x, y):
	alist[x], alist[y] = alist[y], alist[x]

a = [5, 15, 10, 2]
print 'input array', a
heapsort(a)
print 'sorted array', a




