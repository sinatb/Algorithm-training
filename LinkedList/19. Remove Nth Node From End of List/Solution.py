# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start, delstart = head , head
        for i in range(n):
            start = start.next
        if not start:
            return head.next
        while start.next:
            start = start.next
            delstart = delstart.next
        delstart.next = delstart.next.next 
        return(head)