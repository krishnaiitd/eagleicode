class Factorial:

	def RecursiveMethod(self, n):
		if n <= 1:
			return 1
		return n * self.RecursiveMethod(n-1)

	def InterativeMethod(self):
		if n <= 1:
			return 1
		#f =  i * (i-1) for i in range(self.n)
		#return f 
	

#f = Factorial()

#print f.RecursiveMethod(4)

p = [1,2,3,4,5,5]

def InterativeMethod(n):
	if n <= 1:
		return 1
	
	f =  [p[i]*p[i] for i in range(0,n+1)]
	return f 

print p
print InterativeMethod(4)


