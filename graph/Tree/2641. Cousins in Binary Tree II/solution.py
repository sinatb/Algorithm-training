# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        stack = []
        stack.append([root,None])

        while stack:
            child_sum = defaultdict(int)
            p = {}
            curr = 0
            for _ in range(len(stack)):
                node , parent = stack.pop(0)
                child_sum[parent] += node.val
                p[node] = parent
                curr += node.val
                if (node.left):
                    stack.append([node.left,node])
                if (node.right):
                    stack.append([node.right,node])     
            for node in p:
                node.val = curr - child_sum[p[node]]
        return root