# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def help(root,minimum,maximum):
            if not root:
                return True
            isvalidr = False
            isvalidl = False
            if minimum < root.val < maximum:
                isvalidr = help(root.right,root.val,maximum) 
                isvalidl = help(root.left,minimum,root.val)
            return isvalidr and isvalidl
        return help(root,float('-inf'),float('inf'))