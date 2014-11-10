# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @param sum, an integer
	# @return a list of lists of integers
	def search(self, node, path, sum, results):
		"""
		Careful: how to record path
		"""
		if node:
			newPath = path[:]
			newPath.append(node.val)
			if node.left == None and node.right == None:
				if node.val == sum:
					results.append(newPath)
			else:
				self.search(node.left, newPath, sum - node.val, results)
				self.search(node.right, newPath, sum - node.val, results)


	def pathSum(self, root, sum):
		results = []
		self.search(root, [], sum, results)
		return results


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
print sol.pathSum(root, 22)


		









