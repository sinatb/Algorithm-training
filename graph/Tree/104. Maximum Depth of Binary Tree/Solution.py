# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findMax(root,d):
            if not root.left and not root.right:
                return d
            rd = 0
            ld = 0
            if root.left:
                rd = findMax(root.left,d+1)
            if root.right:
                ld = findMax(root.right,d+1)
            return max(rd,ld)
        if not root:
            return 0
        return findMax(root,1)