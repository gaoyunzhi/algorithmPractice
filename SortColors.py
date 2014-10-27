class Solution:
	# @param A a list of integers
	# @return nothing, sort in place
	# @should learn another algorithm
	def sortColors(self, A):
		"""
		sort in place
		用类似QuickSort 的思想
		http://www.cnblogs.com/zuoyuan/p/3775832.html
		"""
		if A:
			rightPointer = len(A) -1
			leftPointer = 0
			i = 0
			while i <= rightPointer:
				if A[i] == 1:
					i += 1
				elif A[i] == 0:
					A[leftPointer], A[i] = A[i], A[leftPointer]
					leftPointer += 1
					i += 1
				else:
					A[rightPointer], A[i] = A[i], A[rightPointer]
					rightPointer -= 1

A = [0,2,1,2,1,1,2,0,2]
sol = Solution()
sol.sortColors(A)
print(A)