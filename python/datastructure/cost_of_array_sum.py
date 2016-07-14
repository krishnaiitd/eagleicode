costArray = []

def ReduceArray(a):
	a.sort(reverse=True)
	x = a.pop()
	y = a.pop()
	s = x + y
	costArray.append(s)
	a.append(s)
	return a

def FindSum(a):
	if len(a) < 2:
		return a.pop()
	a = ReduceArray(a)
	return FindSum(a)

def FindCost(a):
	totalSum = FindSum(a)
	print('array sum is %d', totalSum)
	cost =  sum(costArray)
	print('Cost of array sum is %d', cost)

B = [2, 3, 4]
FindCost(B)


