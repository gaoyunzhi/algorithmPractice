# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	"""
	解题思路：在这道题里，平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于1。
	这实际上是AVL树的定义。首先要写一个计算二叉树高度的函数，二叉树的高度定义为：树为空时，高度为0。
	然后递归求解：树的高度 = max(左子树高度，右子树高度)+1(根节点要算上)。
	高度计算函数实现后，递归求解每个节点的左右子树的高度差，如果有大于1的，则return False。
	如果高度差小于等于1，则继续递归求解。
	"""
	# @param root, a tree node
	# @return a boolean

###---------------------------------------Third version: the best way to do this problem ------------------------------------
	def height(self, root):
		"""
		Return the height of a tree
		"""
		if root:
			return max(self.height(root.left), self.height(root.right)) + 1
		else:
			return 0

	def isBalanced3(self, root):
		if root == None:
			return True
		elif abs(self.height(root.left) - self.height(root.right)) < 2 \
			and self.isBalanced3(root.left) and self.isBalanced3(root.right):
			return True
		else:
			return False


###--------------------------------------- Second version: Accepted, my second try---------------------------------------
	def helpBalanced(self, node):
		"""
		This is faster than the thrid version as I compute the height and test isBalanced 
		in only one recursion.

		"""
		if node:
			if node.left == None and node.right == None:
				# exam leaf node
				is_balanced = True
				max_depth = 1
				return (is_balanced, max_depth)
			else:
				# not leaf node
				is_balanced_left, max_depth_left = self.helpBalanced(node.left)
				is_balanced_right, max_depth_right = self.helpBalanced(node.right)
				if is_balanced_left and is_balanced_right\
					and abs(max_depth_left - max_depth_right) < 2 :
					return (True, max(max_depth_right, max_depth_left)+1)
				else:
					return (False, max(max_depth_left, max_depth_right) + 1)

		else:
			return (True, 0)

	def isBalanced2(self, root):
		return self.helpBalanced(root)[0]

###---------------------------------------First version: hit the recursion limit ---------------------------------------

	# def search(self, node, curr_level, max_level):
	# 	if node:
	# 		if node.left == None and node.right == None:
	# 			if curr_level > max_level[0]:
	# 				max_level[0] = curr_level
	# 		else:
	# 			self.search(node.left, curr_level + 1, max_level)
	# 			self.search(node.right, curr_level + 1, max_level)

	# def maxDepth(self, root):
	# 	if root == None:
	# 		return 0
	# 	max_level = [1]
	# 	self.search(root, 1, max_level)
	# 	return max_level[0]

	# def minDepth(self, root):
	# 	queue = [(root, 1)]

	# 	if root == None:
	# 		return 0

	# 	while queue:
	# 		node, level = queue.pop(0)
	# 		if node:
	# 			if node.left == None and node.right == None:
	# 				return level
	# 			else:
	# 				queue.append((node.left, level + 1))
	# 				queue.append((node.right, level + 1))


	# def isBalanced(self, root):
	# 	if root:
	# 		if abs(self.maxDepth(root.right) - self.maxDepth(root.left)) >= 2 \
	# 				or abs(self.minDepth(root.right) - self.minDepth(root.left)) >= 2:
	# 				return False
	# 		elif self.isBalanced(root.right) and self.isBalanced(root.left):
	# 				return True
	# 	return True

root = TreeNode(5)
a =  TreeNode(4)
root.left = a 
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


sol = Solution()
print sol.isBalanced3(root)
 
				