# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	# """
	# Need to keep track of the sum of each path from leaf to node as the tree may be unbalanced
	# say 
	#    1
	#  /    \
	# 2    3
	# 	     \ 
	#          4
	# Also note that for a tree, there is only one path from root to each node,
	# thus, we don't need to keep track of each node along a particular path, but to keep the ' sum val' of each node

	def leafValues(self, node, father_val, leaves):
		# return current_node_value
		if node:
			if node.left == None and node.right == None:
				leaves.append(node.val + 10 * father_val)
			else:
				curr_val = 10 * father_val + node.val 
				self. leafValues(node.left, curr_val, leaves)
				self.leafValues(node.right, curr_val, leaves)

	def sumNumbers(self, root):
		leaves = []
		self.leafValues(root, 0, leaves)
		return sum(leaves)

root = TreeNode(4)
a =  TreeNode(3)
root.left = a 
b = TreeNode(8)
root.right = b
sol = Solution()
print sol.sumNumbers(root)