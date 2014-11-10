# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing

###------------Second version:  use DFS--------------------------
	def connect(self, root):
		if root and root.left:
			if root.left.left == None:
				root.left.next = root.right
			else:
				self.connect(root.left)
				self.connect(root.right)
				root.left.next = root.right
				left_node = root.left.right
				right_node = root.right.left
				while left_node:
					left_node.next = right_node
					left_node = left_node.right
					right_node = right_node.left
					


###------------First version:  Not using constant extra space--------------------------
	# def connect(self, root):
	# 	"""
	# 	Use BFS
	# 	"""
	# 	if root:
	# 		past_level_set = [root]
	# 		while past_level_set:
	# 			curr_level_set = past_level_set
	# 			past_level_set = []
	# 			for i in xrange(len(curr_level_set) -1):
	# 				curr_level_set[i].next = curr_level_set[i + 1]
	# 				past_level_set.append(curr_level_set[i].left)
	# 				past_level_set.append(curr_level_set[i].right)
	# 			past_level_set.append(curr_level_set[-1].left)
	# 			past_level_set.append(curr_level_set[-1].right)

	# 			if curr_level_set[0].left == None:
	# 				break



root = TreeNode(1)
a = TreeNode(2)
root.left = a
b= TreeNode(3)
root.right = b
a.left = TreeNode(4)
a.right = TreeNode(5)
b.right = TreeNode(7)
b.left = TreeNode(6)
sol = Solution( )
sol.connect(root)

print root.next
print root.left.next.val
print root.right.next

print root.left.left.next.val
print root.left.right.next.val
print root.left.right.next.next.val
print root.right.right.next


