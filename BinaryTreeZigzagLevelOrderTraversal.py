# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def traverse(self, root, level, res):
		if root:
			if len(res) < level + 1:
				res.append([])

			if level % 2 == 0:
				res[level].append(root.val)
			else:
				res[level].insert(0, root.val)
						
			self.traverse(root.left, level + 1, res)
			self.traverse(root.right, level + 1, res)

	def zigzagLevelOrder(self, root):
		level = 0 
		res = []
		self.traverse(root, level, res)
		return res



				