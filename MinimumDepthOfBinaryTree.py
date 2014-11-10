# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def minDepth(self, root):
		queue = [(root, 1)]

		if root == None:
			return 0

		while queue:
			node, level = queue.pop(0)
			if node:
				if node.left == None and node.right == None:
					return level
				else:
					queue.append((node.left, level + 1))
					queue.append((node.right, level + 1))



# root = TreeNode(5)
# a =  TreeNode(4)
# root.left = a 
# b = TreeNode(8)
# root.right = b
# c = TreeNode(11)
# a.left = c

# d = TreeNode(2)
# c.right = d
# d = TreeNode(7)
# c.left = d

# c = TreeNode(13)
# b.left = c
# c = TreeNode(4)
# b.right = c
# c.left = TreeNode(5)
# c.right = TreeNode(1)

root = TreeNode(0)
sol = Solution()
print sol.minDepth(root)
