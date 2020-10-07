# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(list1,list2):

    # Check if both lists are not empty, if they are return the other one
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    # We want to make a copy of the lists to initialize variables
    l1 = list1
    l2 = list2
    prev = None
    # Loop through the lists to traverse them
    while l1 is not None and l2 is not None:
        #Input: 1->2->4, 1->3->4
        #Output: 1->1->2->3->4->4
        # We want to check for the values and compare to start building up the combined array
        if l1.value <= l2.value:
            prev = l1 
            l1 = l1.next  
        else: #l2 < l1
            #check if there is an item in variable prev
            if prev:
                prev.next = l2
            #if there is no prev
            prev = l2
            l2 = l2.next 
            prev.next = l1
    #if it's the end of l1
    if not l1:
        prev.next = l2
    #check original list for edge cases
    if list1 <= list2:
        return list1
    else:
        return list2

