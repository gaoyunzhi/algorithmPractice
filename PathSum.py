# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @param sum, an integer
	# @return a boolean

	def hasPathSum(self, root, sum):
		"""
		Careful: do not write 'while', it's 'if'
		"""
		if root:
			if root.left == None and root.right == None:
				# leaf node
				if root.val == sum:
					return True
			else:
				return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
		return False


