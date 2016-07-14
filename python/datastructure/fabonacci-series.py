class FabonacciSeries:
	def __init__(self, n):
		self.totalLen = n
		self.series = []
	def FabonacciNumberGenerator(self, totalLen):
		if totalLen == 0:
			return 0
		if totalLen == 1:
			return 1
		
		return self.FabonacciNumberGenerator(totalLen - 1) + self.FabonacciNumberGenerator(totalLen - 2) 

	def FabonacciSeriesGenerator(self):
		for i in range(self.totalLen):
			self.series.append(self.FabonacciNumberGenerator(i))

	def PrintSeries(self):
		print self.series



o = FabonacciSeries(8)
o.FabonacciSeriesGenerator()
o.PrintSeries()