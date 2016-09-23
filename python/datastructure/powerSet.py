def powersets(a):
	plist = []
	for i in range(1<<len(a))
		tempList = []
		for j in range(len(a)):
			if i & (1<<j):
				tempList.append(a[j])
		plist.append(tempList)
	return plist


pw = powersets([1,2,5])

print(pw)

	