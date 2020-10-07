'''
remove_kth_from_end
(
SandraCoburn
)
Codewriting

Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

For example, if we have the following linked list: 
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

After the function executes, the state of the linked list should be:
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

If k is longer than the length of the linked list, the linked list should not be changed.

Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?

Note: When reading the tests, the linked list contents are enumerated in between square brackets; this does NOT mean the inputs are arrays.

For example, a test input of head: [2, 4 ,6] indicates that the input is a singly-linked list
(2) -> (4) -> (6) -> null whose head is the first element in the linked list.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

[input] integer k

[output] linkedlist.integer
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeFromEnd(head, k):
    # remove the kth node from the end
    #return the head of the node
    # if k is longer than list, list shouldn't be changed
    ## traverse throught he linked list to get the lenght
    count = 0
    curr = head 

    while curr is not None: ## O(n)
        count += 1
        curr = curr.next
    # Check if k is equal to lenght of array
    if k == count:
        return curr.next
    prev = count - k -1
    remove = count - k
    curr = head
    previous_node = None
    for i in range(count): ## O(n) 2n
        print("index", previous)
        print("remove", remove)
        if i == prev:
            previous_node = current
        if i == remove:
            previous_node.next = current.next
            return head 
        current = current.next
    return head 



    # count = 0
    # curr = head
    # while curr is not None:
    #     count +=1
    #     curr = curr.next

    # if k == count:
    #     return curr.next
    
    # curr = head
    # remove = count - k
    # prev = count -k -1
    # previous_node = None
    # for i in range(count):
    #     if i == prev:
    #         previous_node = curr
    #     if i == remove:
    #         previous_node.next = curr.next
    #         return head
    #     curr = curr.next
    # return head
