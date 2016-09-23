a = [1,4,20, 3, 10, 5]
sum = 33


def GetSubArray(a, sum):
	for i in range(len(a)):
		current_sum = a[i]
		for j in range(i+1, len(a)):
			current_sum += a[j]
			if current_sum == sum:
				print('Found subarray index start from ', i, ' to ', j)
				return 1
			if current_sum > sum:
				break
	print("No subarray founnd")



GetSubArray(a, sum)
# Complexity is o(n^2)
	

def  GetSubArray2(a, sum):
	start = 0
	current_sum = a[start]
	for i in range(1, len(a)):
		while current_sum > sum and start < i:
			current_sum -= a[start]
			start += 1
		if current_sum == sum:
			print("found subarray starting index ", start, ' to index ', i - 1)
			return 1
		if i < len(a):
			current_sum += a[i]
	print("No subarray found")		
