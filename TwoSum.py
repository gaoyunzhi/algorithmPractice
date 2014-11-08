class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		"""
		O(n) runtime, O(n) space – Hash table:
		We could reduce the runtime complexity of looking up a value 
		to O(1) using a hash map that maps a value to its index.
		"""
		dic = {}
		result = []
		for index, val in enumerate(num):
			if val in dic:
				dic[val].append(index + 1)
			else:
				dic[val] = []
				dic[val].append(index + 1)
		for val in dic:
			val2 = target - val
			if val2 in dic:
				if val == val2:
					return (dic[val][0], dic[val][1]) if dic[val][0] <= dic[val][1] else (dic[val][1], dic[val][0])
				else:
					return (dic[val][0], dic[val2][0]) if dic[val][0] <= dic[val2][0] else (dic[val2][0], dic[val][0])

		return None


sol = Solution()
print sol.twoSum([3,2,4], 6)
				# """
		# Careful: remember to use sorting algorithm
		# 要注意的一点是：在原来数组中找下标时，需要一个从头找，一个从尾找，要不无法通过。
		# 如这个例子：numbers=[0,1,2,0]; target=0。如果都从头开始找，就会有问题。
		# """
		# numToSort = num[:] # make a deep copy of the original list
		# numToSort.sort()
		# index = []

		# i = 0; j = len(numToSort) -1
		# while i < j:
		# 	if numToSort[i] + numToSort[j] == target:
		# 		for k in range(len(num)):
		# 			if num[k] == numToSort[i]:
		# 				index.append(k)
		# 				break
		# 		for k in range(len(num), -1, -1):
		# 			if num[k] == numToSort[j]:
		# 				index.append(k)
		# 				break
		# 		index.sort()
		# 		break
		# 	elif numToSort[i] + numToSort[j] < target:
		# 		i = i +1

		# 	elif numToSort[i] + numToSort[j] > target:
		# 		j = j-1

		# return (index[0] + 1, index[1] + 1)





