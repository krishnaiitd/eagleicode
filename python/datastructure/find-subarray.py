def subArray(a, sumvalue):

	for i in range(len(a)):
		current_sum = a[i]
		for j in range(i+1, len(a)):
			if current_sum == sumvalue:
				print "found sub array starting from", i ," and ended at ", j-1
				return 1
			if current_sum > sumvalue or j == len(a):
				break;

			current_sum = current_sum + a[j]
			print current_sum
	print "No sub array found"
	return 0

subArray([1, 4, 0, 0, 3, 10,5], 7)


def subArray2(a, sumvalue):

	current_sum = a[0]
	start = 0
	for i in range(len(a)):
		
		while current_sum > sumvalue and start < i-1:
			current_sum  = current_sum - a[start]
			start = start + 1

		# If found then return	
		if current_sum == sumvalue:
			print "found sub array starting from", start ," and ended at ", i-1
			return 1
	
		if i < len(a):
			current_sum = current_sum + a[i]

		print current_sum
	print "No sub array found"
	return 0

subArray([1, 4, 0, 0, 3, 10,5], 7)