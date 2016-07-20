def merge_sort(a):
	if len(a) <= 1:
		return a

	left = [];
	right = [];
	
	mid = len(a)/2

	left = a[0:mid]
	right = a[mid:(len(a))]

	print left
	print right
	#exit()

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):
	result = []
	while len(left) > 0 and len(right) > 0:
		lv = left[0]
		rv = right[0]
		if lv <= rv:
			result.append(lv)
			left.pop(0)
		else:
			result.append(rv)
			right.pop(0)
	while len(left) > 0:
		result.append(left.pop(0))

	while len(right) > 0:
		result.append(right.pop(0))

	return result
	
A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]

print A
print merge_sort(A)	




