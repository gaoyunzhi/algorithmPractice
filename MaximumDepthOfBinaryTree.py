# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def search(self, node, curr_level, max_level):
		if node:
			if node.left == None and node.right == None:
				if curr_level > max_level[0]:
					max_level[0] = curr_level
			else:
				self.search(node.left, curr_level + 1, max_level)
				self.search(node.right, curr_level + 1, max_level)



	def maxDepth(self, root):
		if root == None:
			return 0
		max_level = [1]
		self.search(root, 1, max_level)
		return max_level[0]

root = TreeNode(5)
a =  TreeNode(4)
root.left = a 
b = TreeNode(8)
root.right = b
c = TreeNode(11)
a.left = c

d = TreeNode(2)
c.right = d
d = TreeNode(7)
c.left = d

c = TreeNode(13)
b.left = c
c = TreeNode(4)
b.right = c
c.left = TreeNode(5)
c.right = TreeNode(1)


sol = Solution()
print sol.maxDepth(root)