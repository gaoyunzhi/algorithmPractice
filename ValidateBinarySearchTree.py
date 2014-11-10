# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	"""
	This seems similar to BalancedBinaryTree.py
	left subtree is BST and right subtree and left_root_val < root_val < right_root_val is not sufficient!!!!

	"""

###---------------------------------------Second version:  Accepted, consider the min and max value of both left and right subtrees--------------------------
	# def helpBST(self, root):
	def helpBST(self, root):
		# @return (root value, whether the current sub tree is a BST)
		if root:
			if root.left == None and root.right == None:
				min_val = max_val = root.val
				return (root.val, min_val, max_val, True)

			elif root.left == None:
				right_root_val, right_min_val, right_max_val, is_BST_right = self.helpBST(root.right)

				if is_BST_right and root.val < right_min_val :
					return (root.val, root.val, right_max_val, True)
				else: return (root.val, right_min_val, max(root.val, right_max_val), False)

			elif root.right == None:
				left_root_val, left_min_val, left_max_val, is_BST_left = self.helpBST(root.left)
				if is_BST_left and root.val > left_max_val:
					return (root.val, left_min_val, root.val, True)
				else: return (root.val,  min(left_min_val, root.val), left_max_val, False)
			else:
				left_root_val, left_min_val, left_max_val, is_BST_left = self.helpBST(root.left)
				right_root_val, right_min_val, right_max_val, is_BST_right = self.helpBST(root.right)

				if is_BST_left and is_BST_right and left_max_val < root.val and right_min_val > root.val:
					return (root.val, left_min_val, right_max_val,  True)
				else: return (root.val, min(left_min_val,right_min_val, root.val ), \
								max(left_max_val, right_max_val, root.val), False)

		else: return(None, None, None, True)

	def isValidBST(self, root):
		return self.helpBST(root)[-1]

###---------------------------------------First version: wrong algorithm, see the comment below the definition of class Solution ------------------------------------
	# def helpBST(self, root):
	# 	# @return (root value, whether the current sub tree is a BST)
	# 	if root:
	# 		if root.left == None and root.right == None:
	# 			return (root.val, True)

	# 		elif root.left == None:
	# 			right_root_val, is_BST_right = self.helpBST(root.right)
	# 			if is_BST_right and root.val < right_root_val:
	# 				return (root.val, True)
	# 			else: return (root.val, False)

	# 		elif root.right == None:
	# 			left_root_val, is_BST_left = self.helpBST(root.left)
	# 			if is_BST_left and root.val > left_root_val:
	# 				return (root.val, True)
	# 			else: return (root.val, False)
	# 		else:
	# 			left_root_val, is_BST_left = self.helpBST(root.left)
	# 			right_root_val, is_BST_right = self.helpBST(root.right)
	# 			if is_BST_left and is_BST_right and left_root_val < root.val and right_root_val > root.val:
	# 				return (root.val, True)
	# 			else: return (root.val, False)

	# 	else: return(None, True)

	# def isValidBST(self, root):
	# 	return self.helpBST(root)[1]



root = TreeNode(4)
a =  TreeNode(3)
root.left = a 
b = TreeNode(8)
root.right = b
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
print sol.isValidBST(root)

				