
def FindVar(x):
	mean = sum(x)/len(x)
	x_mean = [i-mean for i in x]
	x_mean_2 = [i*i for i in x_mean]
	return sum(x_mean_2)/len(x)



print FindVar([1,2,3,4])
