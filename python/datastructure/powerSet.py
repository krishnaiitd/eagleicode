def powersets(a):
	plist = []
	for i in range(1<<len(a)):
		tempList = []
		for j in range(len(a)):
			if i & (1<<j):
				tempList.append(a[j])
		plist.append(tempList)
	return plist


a = [1,2,5]

""" Test that all subsets are present are not """
#pw = powersets(a)
#print(pw)


"""
Find the subsets from a set whose sum equal to given particular number
"""

sum1 = 3

def findSubArray(a, sum1):
	subSets = []
	pwSets = powersets(a)
	for i in range(len(pwSets)):
		subSet = pwSets[i]
		if sum(subSet) == sum1:
			subSets.append(subSet)

	if len(subSets) == 0:
		print("No subset found")

	return subSets


a = [3, 34, 4, 12, 5, 2]
subsets = findSubArray(a, 9)

print(subsets)





