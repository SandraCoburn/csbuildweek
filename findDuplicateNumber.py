'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
'''
def findDuplicate(nums):
        
    duplicate = {}
    for num in nums:
        if num in duplicate:
            print("duplicates", duplicate)
            return duplicate[num]
        else: 
            duplicate[num] = num
dup = [1,3,4,5,2,2]
dup2 = [3,1,3,4,2]
print(findDuplicate(dup))