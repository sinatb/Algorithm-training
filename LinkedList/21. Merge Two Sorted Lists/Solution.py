# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        help = start = ListNode()
        while list1 and list2:
            print(list1.val)
            print(list2.val)
            if list1.val < list2.val:
                help.next = list1
                help = list1
                list1 = list1.next
            else:
                help.next = list2
                help = list2
                list2 = list2.next
        if list1:
            help.next = list1
        elif list2:
            help.next = list2
        return start.next
