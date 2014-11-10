# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param p, a tree node
	# @param q, a tree node
	# @return a boolean
	def isSameTree(self, p, q):
		# basic case
		if (not p) and (not q):
			return True
		elif p and (not q):
			return False
		elif (not p) and q:
			return False
		else:
			if p.right and q.right and p.right.val == q.right.val:
				isSameTree(p.right, q.right)
				isSameTree(p.left, q.left)
			elif p.right and q.left and p.right.val == q.left.val:
				isSameTree(p.right, q.left)
				isSameTree(p.left, q.right)
			else:
				return False
		return True

