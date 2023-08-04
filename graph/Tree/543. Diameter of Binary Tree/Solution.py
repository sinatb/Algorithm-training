# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0 
            lclp2l, rclp2l = dfs(node.left), dfs(node.right) 
            d = lclp2l + rclp2l
            self.diameter = max(d, self.diameter)
            return max(lclp2l, rclp2l) + 1     
        dfs(root)
        return self.diameter