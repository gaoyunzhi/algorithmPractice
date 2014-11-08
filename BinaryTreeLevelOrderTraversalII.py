# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def preOrderTraverse(self, root, level ,res):
		if root:
			if len(res) < level + 1:
				res.append([])
			res[level].append(root.val)
			self.preOrderTraverse(root.left, level + 1, res)
			self.preOrderTraverse(root.right, level + 1, res)

	def levelOrderBottom(self, root):
		res = []
		level = 0
		self.preOrderTraverse(root, level, res)
		res.reverse()
		"""
		Careful: cannot do this: return res.reverse(), this will return None!!!!!
		"""
		return res