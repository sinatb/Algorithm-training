# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (not root):
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)    
        root.right , root.left = root.left , root.right
        return root