# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        it1 = l1
        it2 = l2
        carry = 0
        head = ListNode()
        it3 = head
        while it1 and it2:
            s = it1.val + it2.val + carry
            if (s>=10):
                s-=10
                carry=1
            else:
                carry = 0
            it3.next = ListNode(val=s,next=None)
            it3 = it3.next
            it1 = it1.next
            it2 = it2.next
        it4 = it1 if it1 else it2
        while it4:
            s = it4.val + carry
            if (s>=10):
                s-=10
                carry=1
            else:
                carry = 0
            it3.next = ListNode(val=s,next=None)
            it3 = it3.next
            it4 = it4.next
        if carry==1:
            it3.next = ListNode(val=1,next=None)
        return head.next