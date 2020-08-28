'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Check if list are not empty
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        #copy lists
        list1 = l1
        prev = None
        list2 = l2
        while list1 and list2:
            if list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            else:
                if prev:
                    prev.next = list2
                prev = list2
                list2 = list2.next
                prev.next = list1
        if not list1:
            prev.next = list2
        if l1.val <= l2.val:
            return l1
        else:
            return l2
l1 = [1,2,4]
l2 = [1,3,4]
l = Solution()

print(l.mergeTwoLists(l1,l2))
