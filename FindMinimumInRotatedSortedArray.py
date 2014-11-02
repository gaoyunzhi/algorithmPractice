class Solution:
	# @param num, a list of integer
	# @return an integer
	"""
	Can deal with duplicates
	"""
	def findMin(self, num):
		if num == [ ]:
			return num

		leftMin = num[0]
		for i in range(1, len(num)):
			if num[i] < leftMin:
				return num[i]		
		return num[0]


sol = Solution()
print(sol.findMin([4, 4, 5, 6, 7, 0, 1, 2]))