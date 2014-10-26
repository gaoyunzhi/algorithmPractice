# http://www.cnblogs.com/zuoyuan/p/3747174.html
# 解题思路：这题也不难。需要用一个help函数，当然也是递归的。
# 当存在左右子树时，判断左右子树的根节点值是否相等，如果想
# 等继续递归判断左子树根的右子树根节点和右子树根的左子树根
# 节点以及左子树根的左子树根节点和右子树根的右子树根节点的
# 值是否相等。然后一直递归判断下去就可以了。
#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    # p is the left node and q is the right node
    def help(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            # Careful: not 'help(self, p.left, q.right)'. help here is defined as the method of an instance
            return self.help(p.left, q.right) and self.help(p.right, q.left)
        return False
        
    def isSymmetric(self, root):
        if root:
            return self.help(root.left, root.right)
        return True