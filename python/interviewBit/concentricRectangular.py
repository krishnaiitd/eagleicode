A = 4
size = 2*A - 1

def getValue(i, j, A):
	for a in range(A):
		if i == a or i == 2*A - (a + 2) or j == a or j == 2*A - (a + 2):
			return A - a


mlist = []
for i in range(size):
	tlist = []
	for j in range(size):
		values = getValue(i, j, A)
		tlist.append(values)
	mlist.append(tlist)	
return mlist



		