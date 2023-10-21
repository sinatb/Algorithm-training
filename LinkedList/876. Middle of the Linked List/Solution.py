# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        ctr = 0
        ptr = head
        while (ptr.next):
            ctr += 1
            ptr = ptr.next
        if (ctr%2 == 1):
            ctr/=2
            ctr+=1
        else:
            ctr+=1
            ctr/=2
        ptr = head
        for i in range(ctr):
            ptr = ptr.next
        return ptr
        